# 이미지 삽입
from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("./rpabasic/excel/dog.jpg")

ws.add_image(img, "C3")

wb.save("./rpabasic/excel/image.xlsx")

# ImportError: You must install Pillow to fetch image objects
# pip install Pillow
