# -*- coding: utf-8 -*-
import configparser
from pathlib import Path
import json
import uuid
from datetime import datetime

from PyPDF2 import PdfReader, PdfWriter
from z3c.rml import rml2pdf
import preppy 

HERE = Path(__file__).resolve().parent

config = configparser.ConfigParser()
config.read(HERE / 'congfig_printed_file.ini')


def extract_data(data_dict:dict)->dict:
    """从字典类型数据中解析出打印所需要的字段"""
    report_data:dict = {}
    product:dict = {}
    tech_para:dict = {}
    # 产品信息
    product["product_num"] = data_dict['w_equipment_code'] 
    product["product_contract_no"] = data_dict['contract_no']
    product["product_type"] = data_dict['ReadinHetonginfo']['梯型'] 
    product["product_name"] = data_dict['ModelReadinHgzCsZjb']['SysBasicInfoMachine']['产品名称']
    product["product_device_type"] = data_dict['ModelReadinHgzCsZjb']['SysBasicInfoMachine']['设备类别']
    product["product_device_category"] = data_dict['ModelReadinHgzCsZjb']['SysBasicInfoMachine']['设备品种']
    product["product_manufacturing_company"] = "西子电梯科技有限公司"
    product["product_device_num"] = data_dict['ModelReadinHgzCsZjb']['SysBasicInfoMachine']['设备代码']
    product["product_customer_company"] = data_dict['ModelReadinHgzCsZjb']['项目名称']
    product["product_license_num"] = data_dict['cert_manufacturing_license_numbe']
    expiration_date = datetime.strptime(data_dict['cert_valid_date'], "%Y-%m-%d")
    product["product_license_expiration_date"] = f"{expiration_date.year}年{expiration_date.month}月{expiration_date.day}日"

    # 主要技术参数
    tech_para['rated_load'] = data_dict['ModelReadinHgzCsZjb']['载重']
    tech_para['rated_speed'] = data_dict['ModelReadinHgzCsZjb']['速度']
    tech_para['control_method'] = "群控"
    tech_para['elevator_control_mode'] = data_dict['ModelReadinHgzCsZjb']['控制方式']
    tech_para['door_open_mode'] = data_dict['ModelReadinHgzCsZjb']['开门方式']
    tech_para['floor_num'] = data_dict['ModelReadinHgzCsZjb']['层数']
    tech_para['stop_num'] = data_dict['ModelReadinHgzCsZjb']['站数']
    tech_para['floor_num'] = data_dict['ModelReadinHgzCsZjb']['门数']
    tech_para['lifting_height'] = data_dict['']
    tech_para['carbine_area'] = data_dict['']
    tech_para['carbine_weight'] = data_dict['']
    tech_para['coefficient_range'] = data_dict['']
    tech_para['suspension_ratio'] = data_dict['']
    tech_para['carbine_size'] = data_dict['']


    report_data["product"] = product
    report_data["tech_para"] = tech_para

    return report_data

template_certfile = Path(HERE / 
                     config.get('paths', 'template_directory') / 
                     config.get('filenames', 'cert_template_file'))

def generate_report(report_data:dict)->Path:
    output_path = Path(HERE / 
                     config.get('paths', 'output_directory'))
    file_name = 'test' + '.pdf'
    # file_name = str(uuid.uuid4()) + '.pdf'
    out_pdf = Path(output_path / file_name)

    mymodule = preppy.getModule(template_certfile)
    rmlText = mymodule.get(report_data)
    pdf = rml2pdf.parseString(rmlText)
    with open(out_pdf, 'wb') as file:
        file.write(pdf.read())

    if out_pdf.exists():
        return out_pdf
    else:
        return None
    
def merge_pdfs(pdf_files:list[Path], output_path:Path)->Path:
    pdf_writer = PdfWriter()
    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file, strict=False)
        for page in range(len(pdf_reader.pages)):
            pdf_page = pdf_reader.pages[page]
            pdf_writer.add_page(pdf_page)

    # 将合并后的PDF写入文件
    with open(output_path, "wb") as output_file:
        pdf_writer.write(output_file)
    
    if output_path.exists():
        return output_path
    else:
        return None

def generate_reports(*json_args)->Path:
    pdf_files = []
    for json_str in json_args:
        json_data = json.loads(json_str)
        pdf_file = generate_report(json_data)
        pdf_files.append(pdf_file)
    
    if len(pdf_files):
        output_fn = merge_pdfs(pdf_files, Path("output.pdf"))
    
    return output_fn

        





