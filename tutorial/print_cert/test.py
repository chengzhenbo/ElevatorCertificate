
from pathlib import Path
import json

from generate_pdf import generate_report,generate_reports
from parse_json import ParseJson

HERE = Path(__file__).resolve().parent

def test_json():
    with open(Path(HERE/"json1.txt")) as f:
        json_data = json.load(f)
    print(json_data)
    

def test_one_pdf():
    with open(Path(HERE/"json1.txt")) as f:
        json_data = json.load(f)

    parsejson = ParseJson(data_dict = json_data[0])
    report_data = parsejson.report_data

    pdf_file = generate_report(report_data)
    print(pdf_file)

def test_many_pdf():
    
    report_data1 = '{"title": "ERasdf394", "age": 30}'
    report_data2 = '{"title": "DDAlice23", "age": 30}'
   
    pdf_file = generate_reports(report_data1,report_data2)
    print(pdf_file)


if __name__ == "__main__":
    test_one_pdf()