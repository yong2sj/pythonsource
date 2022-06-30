from openpyxl import load_workbook

wb = load_workbook("./rpabasic/excel/range.xlsx")
ws = wb.active

# 셀 이동
# rows=0 : 그대로 냅둠 / cols=1 : 오른쪽 옆으로 한칸
# - 를 주게 되면 왼쪽 / 위로
ws.move_range("B1:C11", rows=0, cols=1)


wb.save("./rpabasic/excel/range.xlsx")
