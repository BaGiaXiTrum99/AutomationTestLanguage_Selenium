import base64
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from io import BytesIO

def gen_report_to_excel(file_path : str = "reports/report.xml",report_name : str = "reports/test_report_openpyxl.xlsx"):
    with open(file_path, "r") as f:
        data=f.readlines()

    idx = 1
    rows=[]
    for line_idx in range(len(data)):
        if data[line_idx].startswith("Expected text:"):
            expected_text = data[line_idx].replace("Expected text: ","").strip()
            actual_text = data[line_idx+1].replace("Actual text: ","").strip()
            screenshot = data[line_idx+2].replace("[Screenshot](data:image/png;base64:","").strip()
            rows.append([idx, expected_text, actual_text,screenshot])
            idx += 1

    wb = Workbook()
    ws = wb.active
    ws.title = "Test Report"

    ws.append(["No.", "Expected result", "Actual result", "Image"])

    for row in rows:
        idx, expected, actual, base64_string = row

        ws.append([idx, expected, actual])

        img_data = base64.b64decode(base64_string)
        image = Image(BytesIO(img_data)) 

        img_cell = f"D{ws.max_row}"  
        ws.add_image(image, img_cell)

    ws.column_dimensions["B"].width = 30  
    ws.column_dimensions["C"].width = 30  
    ws.column_dimensions["D"].width = 20 

    excel_file_path = report_name
    wb.save(excel_file_path)

    print(f"Report with images saved: {excel_file_path}")