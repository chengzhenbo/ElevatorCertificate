# -*- coding: utf-8 -*-
from z3c.rml import rml2pdf
from pathlib import Path
HERE = Path(__file__).resolve().parent
import configparser

import preppy 

HERE = Path(__file__).resolve().parent

config = configparser.ConfigParser()
config.read(HERE / 'congfig_printed_file.ini')

template_file = Path(HERE / 
                     config.get('paths', 'template_directory') / 
                     config.get('filenames', 'certi_file'))

def generate_report(output_pdf, report_data):
    mymodule = preppy.getModule(template_file)

    rmlText = mymodule.get(report_data)
    pdf = rml2pdf.parseString(rmlText)
    with open(output_pdf, 'wb') as file:
        file.write(pdf.read())

if __name__ == "__main__":
    output_pdf = Path(HERE / 
                     config.get('paths', 'output_directory') / 
                     config.get('filenames', 'output_certi_file'))
    report_data = {
        "title": "Ad9u9231",
        "description": "This is a summary of the product sales.",
        "products": [
            {"name": "Product A", "quantity": 100, "price": 15},
            {"name": "Product B", "quantity": 50, "price": 20},
            {"name": "Product C", "quantity": 75, "price": 12},
        ],
    }
    generate_report(output_pdf, report_data)


