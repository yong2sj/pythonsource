import re
from openpyxl import load_workbook

# 원본 문자 : python VS java
# VS 를 기준으로 문자열 분리 -> ['python','java']
pattern = re.compile(" VS ")
print(pattern.split("python VS java"))

# data_kr.xlsx의 주민번호 컬럼을 읽어서 화면 출력
# 단, 주민번호 뒷자리는 *로 변경해서 출력
wb = load_workbook("./rpabasic/crawl/download/data_kr.xlsx")
ws = wb.active

# 찾아야 하는 패턴 : 주민등록번호 뒷자리
pattern = re.compile("[0-9]{7}")

for each_row in ws.rows:
    print(re.sub(pattern, "*******", each_row[1].value))

wb.close()
