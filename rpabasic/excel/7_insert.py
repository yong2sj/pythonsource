from openpyxl import load_workbook

wb = load_workbook("./rpabasic/excel/range.xlsx")
ws = wb.active

# 행 삽입
# ws.insert_rows(8, 5)  # 8번행부터 5행 추가

# 열 삽입
# ws.insert_cols(2)
ws.insert_cols(2, 3)


wb.save("./rpabasic/excel/range.xlsx")
