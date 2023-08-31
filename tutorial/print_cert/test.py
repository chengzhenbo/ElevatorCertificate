
from pathlib import Path
import json

from generate_pdf import generate_report,generate_reports

HERE = Path(__file__).resolve().parent

def test_json():
    with open(Path(HERE/"json1.txt")) as f:
        json_data = json.load(f)
    print(json_data)
    

def test_one_pdf():
    """测试生成一个打印PDF文件"""
    with open(Path(HERE/"jsondata"/"json3.txt")) as f:
        json_data = json.load(f)
    pdf_file = generate_report(json_data)
    print(pdf_file)

def test_many_pdf():
    """测试生成多个个打印PDF文件"""
    data_list = []
    with open(Path(HERE/"jsondata"/"json1.txt")) as f:
        json_data_1 = json.load(f)
    with open(Path(HERE/"jsondata"/"json2.txt")) as f:
        json_data_2 = json.load(f)
    with open(Path(HERE/"jsondata"/"json3.txt")) as f:
        json_data_3 = json.load(f)
    data_list = [json_data_1, json_data_2, json_data_3]

    pdf_file = generate_reports(data_list)
    print(pdf_file)


if __name__ == "__main__":
    test_many_pdf()