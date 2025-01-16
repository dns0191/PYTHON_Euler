import Function as f
import Variable as v
import openpyxl
import numpy as np

cur_time = 0.0
p_0 = v.power

# 데이터 저장용 리스트
data_buffer = []

def save_data_to_excel(sheet, data_buffer):
    """엑셀 시트에 데이터를 저장하는 함수"""
    for row in data_buffer:
        sheet.append(row)
    data_buffer.clear()

if __name__ == '__main__':
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["Time", "Power", "Operation", "FR", "CR", "Rho", "Insert_Rho"])
    sheet.append([cur_time, p_0, v.operation_Power[0], v.FR_position, v.CR_position, v.cur_rho*1e5, v.insert_rho*1e5])

    while cur_time <= v.end_t:
        next_time = f.update_reactor_state(v, cur_time, data_buffer)
        
        # 엑셀에 데이터 추가
        if int(next_time) > int(cur_time):
            save_data_to_excel(sheet, data_buffer)

        cur_time = next_time

        if cur_time % 10 == 0:
            print(f"Progress: {cur_time} sec")
    
    # 엑셀 파일 저장
    wb.save('output.xlsx')