# -*- coding: utf-8 -*-
import configparser
from pathlib import Path
import uuid
import io

from PIL import Image
from PyPDF2 import PdfMerger
from z3c.rml import rml2pdf
import preppy 

from parse_json import ParseJson

HERE = Path(__file__).resolve().parent

config = configparser.ConfigParser()
config.read(HERE / 'congfig_printed_file.ini')

TEMPLATE_CERTFILE = Path(HERE / 
                     config.get('paths', 'template_directory') / 
                     config.get('filenames', 'cert_template_file'))
OUTPUT_PATH = Path(HERE / 
                       config.get('paths', 'output_directory'))

def merge_pdfs(pdf_files:list[Path], merged_pdf:Path)->Path:
    """将多个pdf文件合并为一个pdf文件"""
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(merged_pdf)
    merger.close()
 
    if merged_pdf.exists():
        return merged_pdf
    else:
        return None

def generate_qrimg()->Path:
    """将二维码数据流生成png文件"""
    qrcode_img_stream = b"your_image_stream_data_here" # 添加生成二维码函数调用
    input_stream = io.BytesIO(qrcode_img_stream)
    image = Image.open(input_stream)
    qrimg_tem_path = Path(OUTPUT_PATH / 'qrimg_tem_path')
    if not qrimg_tem_path.exists():
        qrimg_tem_path.mkdir(parents=True, exist_ok=True)
    qrimg_file = Path(qrimg_tem_path / f"{uuid.uuid4()}.png")
    image.save(qrimg_file, "PNG")
    # 返回相对路径
    return qrimg_file.relative_to(HERE) 

def generate_report(data:dict)->Path:
    """传入字典数据，按合同号生成打印的pdf文件"""
    parser = ParseJson(data_dict = data)
    report_data = parser.report_data

    # # 得到二维码图像，并将文件名传入到report_data里面 TODO 二维码文件在使用后需要删除
    # qrimg_file = generate_qrimg()
    # if qrimg_file.exists():
    #     report_data["product"]["qrimg_file"] = qrimg_file
    ### 替换以上，即可生成动态二维码
    report_data["product"]["qrimg_file"] = "templatefile/qrimg_tem_path/xizhi_qr.png"

    # 将合同号与产品型号作为PDF文件的文件名
    file_name = report_data["product"]["product_contract_no"]+\
                                "_"+report_data["product"]["product_type"] + '.pdf'
    out_pdf = Path(OUTPUT_PATH / file_name)

    mymodule = preppy.getModule(TEMPLATE_CERTFILE)
    rmlText = mymodule.get(report_data)
    pdf = rml2pdf.parseString(rmlText)
    with open(out_pdf, 'wb') as file:
        file.write(pdf.read())

    if out_pdf.exists():
        return out_pdf
    else:
        return None
    
def generate_reports(data_list:list[dict])->Path:
    """如果传入的是一个list，则将输出的pdf合并后输出"""
    pdf_files = []
    for data in data_list:
        pdf_file = generate_report(data)
        pdf_files.append(pdf_file)
    # 合并后的pdf文件存放，该文件生成唯一的文件名
    merged_pdf = Path(OUTPUT_PATH / f"{uuid.uuid4()}.pdf")
    if len(pdf_files):
        output_fn = merge_pdfs(pdf_files, merged_pdf)

    return output_fn

        





