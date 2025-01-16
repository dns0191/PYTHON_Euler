import Variable as v
import numpy as np


def update_reactor_state(v, cur_time, data_buffer):
    """
    반응도 및 출력 데이터 업데이트
    """
    pre_insert_rho = v.insert_rho
    v.pre_rho = v.cur_rho  # 이전 반응도를 v 객체에 저장
    dt = v.t_interval
    next_time = round(cur_time + dt, 4)
    
    # 제어봉 위치 및 반응도 업데이트
    v.FR_position, v.CR_position, operation_power = v.get_rod_positions(cur_time)
    v.insert_rho = (v.get_rod_worth(v.FR_position, v.rod_FR_worth) +
                   v.get_rod_worth(v.CR_position, v.rod_CR_worth)) / 1e5

    delta_rho = v.insert_rho - pre_insert_rho
    v.cur_rho += delta_rho

    k = 1 / (1 - v.cur_rho)
    pgen = v.plife / k
    
    # 출력 변화율 계산
    delay = np.sum(v.c * v.decay)
    prompt = (v.cur_rho - v.beta_eff) * v.power / pgen
    dp_dt = prompt + delay
    
    # 지발중성자군 변화율 계산
    dc_dt = -v.decay * v.c + v.beta * v.power / pgen
    
    # 업데이트
    v.power += dp_dt * dt
    v.c += dc_dt * dt
    
    # 데이터 저장
    if int(next_time) > int(cur_time):
        data_buffer.append([next_time, v.power, operation_power, v.FR_position, v.CR_position, 
                            np.round(v.cur_rho * 1e5, 4), np.round(v.insert_rho * 1e5, 4)])
    
    return next_time
