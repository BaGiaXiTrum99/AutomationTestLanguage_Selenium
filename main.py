import pytest
from gen_report.gen_report import gen_report_to_excel
from datetime import datetime

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

TEST_FOLDER = "./tests/questions/questions_page.py"
REPORT_XML_FILE = f"./reports/report_xml_{current_time}.xml"
REPORT_EXCEL_FILE = f"./reports/report_excel_{current_time}.xlsx"

if __name__ == "__main__":
    pytest.main([
        "-v", 
        TEST_FOLDER,     
        "--junitxml="+REPORT_XML_FILE,
        "-s"  
        ])
    gen_report_to_excel(REPORT_XML_FILE,REPORT_EXCEL_FILE)
    