import numpy as np
import pandas as pd
import openpyxl

# Excel 파일 읽기
condition = pd.read_excel('input.xlsx')
history = pd.read_excel('history.xlsx')
reactor = pd.read_excel('reactor.xlsx')

# rod worth 데이터 처리
rod_positions = np.arange(0, 24000, 1)
FR_experiment = reactor[['FR_position', 'FR_worth']].dropna().values
CR_experiment = reactor[['CR_position', 'CR_worth']].dropna().values


# 선형 보간을 위한 함수
def interpolate_rod_worth(positions, experiment_data):
    return np.interp(positions, 
                    experiment_data[:, 0],  # x: positions
                    experiment_data[:, 1])  # y: worth values

# rod worth 배열 생성
rod_FR_worth = interpolate_rod_worth(rod_positions, FR_experiment)
rod_CR_worth = interpolate_rod_worth(rod_positions, CR_experiment)

# 기타 조건
FR_position = float(condition['i_rod(FR)'][0])
CR_position = float(condition['i_rod(CR)'][0])
plife = float(reactor['pn_life'][0])
t_interval = float(reactor['t_interval'][0])
power = float(condition['power'][0])

# rod worth 찾기 위한 함수
def get_rod_worth(position, worth_array):
    pos_idx = round(position * 1000)
    return worth_array[pos_idx] if pos_idx < len(worth_array) else worth_array[-1]

# 초기 반응도 계산
cur_rho = float(condition['rho'][0] / 1e5)
insert_rho = (get_rod_worth(FR_position, rod_FR_worth) + 
              get_rod_worth(CR_position, rod_CR_worth)) / 1e5

# precursor 데이터
beta = reactor['beta'].dropna().values
decay = reactor['decay'].dropna().values
beta_eff = np.sum(beta)


c = np.zeros(6)
c = beta * power / (plife * decay)

# 운전 데이터 처리 
def prepare_operation_data():
    # NaN 값을 제거한 데이터프레임 생성
    clean_history = history[['Time', 'rod(FR)', 'rod(CR)', 'Power']].dropna()
    history_array = clean_history.values

    # 시간 배열 생성
    operation_t = np.arange(0.0, len(clean_history), t_interval)
    operation_t = np.round(np.trunc(operation_t/t_interval)*t_interval, 4)
    operation_t = np.unique(operation_t)

    # 운전 데이터 보간
    operation_FR = np.interp(operation_t, history_array[:, 0], history_array[:, 1])
    operation_CR = np.interp(operation_t, history_array[:, 0], history_array[:, 2])
    operation_Power = np.interp(operation_t, history_array[:, 0], history_array[:, 3])

    # 빠른 검색을 위한 해시 테이블 생성
    time_indices = {t: i for i, t in enumerate(operation_t)}
    
    return operation_t, operation_FR, operation_CR, operation_Power, time_indices

# 데이터 준비
operation_t, operation_FR, operation_CR, operation_Power, time_indices = prepare_operation_data()
end_t = float(operation_t[-1])

# 최적화된 rod position 검색 함수
def get_rod_positions(time):
    # 가장 가까운 시간 찾기
    rounded_time = round(time / t_interval) * t_interval
    rounded_time = round(rounded_time, 4)  # 부동소수점 오차 방지
    
    # 해시 테이블에서 직접 검색
    try:
        idx = time_indices[rounded_time]
        return operation_FR[idx], operation_CR[idx], operation_Power[idx]
    except KeyError:
        # 범위를 벗어난 경우 가장 가까운 값 반환
        if rounded_time < operation_t[0]:
            return operation_FR[0], operation_CR[0], operation_Power[0]
        elif rounded_time > operation_t[-1]:
            return operation_FR[-1], operation_CR[-1], operation_Power[-1]
        else:
            # 필요한 경우에만 argmin 사용
            idx = np.abs(operation_t - rounded_time).argmin()
            return operation_FR[idx], operation_CR[idx], operation_Power[idx]

# 배열을 텍스트 파일로 저장
def save_operation_data_to_text(filename, operation_t, operation_FR, operation_CR):
    with open(filename, 'w') as file:
        file.write(f"{'Time':<10}\t{'FR':<10}\t{'CR':<10}\n")
        for t, fr, cr in zip(operation_t, operation_FR, operation_CR):
            file.write(f"{t:<10.4f}\t{fr:<10.4f}\t{cr:<10.4f}\n")

def save_rod_worth_to_text(filename, rod_positions, rod_FR_worth, rod_CR_worth):
    with open(filename, 'w') as file:
        file.write(f"{'Position':<15}\t{'Rod_FR_Worth':<15}\t{'Rod_CR_Worth':<15}\n")
        for position, FR, CR in zip(rod_positions, rod_FR_worth, rod_CR_worth):
            file.write(f"{position/1e3:<15.4f}\t{FR:<15.4f}\t{CR:<15.4f}\n")

# 배열 저장 함수 호출
save_operation_data_to_text('operation_data.txt', operation_t, operation_FR, operation_CR)
save_rod_worth_to_text('rod_worth_data.txt', rod_positions, rod_FR_worth, rod_CR_worth)