# -*- coding: utf-8 -*-
import configparser
from pathlib import Path
import json
import uuid

from PyPDF2 import PdfReader, PdfMerger
from z3c.rml import rml2pdf
import preppy 

from parse_json import ParseJson

HERE = Path(__file__).resolve().parent

config = configparser.ConfigParser()
config.read(HERE / 'congfig_printed_file.ini')

TEMPLATE_CERTFILE = Path(HERE / 
                     config.get('paths', 'template_directory') / 
                     config.get('filenames', 'cert_template_file'))

def merge_pdfs(pdf_files:list[Path], output_path:Path)->Path:
    """将多个pdf文件合并为一个pdf文件"""
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()
    # for pdf_file in pdf_files:
    #     pdf_reader = PdfReader(pdf_file, strict=False)
    #     for page in range(len(pdf_reader.pages)):
    #         pdf_page = pdf_reader.pages[page]
    #         pdf_writer.add_page(pdf_page)

    # # 将合并后的PDF写入文件
    # with open(output_path, "wb") as output_file:
    #     pdf_writer.write(output_file)
    
    if output_path.exists():
        return output_path
    else:
        return None

def generate_report(report_data:dict)->Path:
    output_path = Path(HERE / 
                       config.get('paths', 'output_directory'))
    file_name = str(uuid.uuid4()) + '.pdf'
    out_pdf = Path(output_path / file_name)

    mymodule = preppy.getModule(TEMPLATE_CERTFILE)
    rmlText = mymodule.get(report_data)
    pdf = rml2pdf.parseString(rmlText)
    with open(out_pdf, 'wb') as file:
        file.write(pdf.read())

    if out_pdf.exists():
        return out_pdf
    else:
        return None
    
def generate_reports(data_list:list)->Path:
    """如果传入的是一个list，则将输出的pdf合并后输出"""
    pdf_files = []
    for data in data_list:
        parser = ParseJson(data_dict = data)
        report_data = parser.report_data

        pdf_file = generate_report(report_data)
        pdf_files.append(pdf_file)
    
    if len(pdf_files):
        output_fn = merge_pdfs(pdf_files, Path("output.pdf"))

    return output_fn

        





