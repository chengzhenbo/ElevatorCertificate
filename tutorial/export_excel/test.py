from pathlib import Path

from generate_certificate import (read_json,
                                  copy_template_files,
                                  export_printed_files)

def test_read_json():
    data = read_json(path=Path('datafile/config1.json'))
    print(data)

def test_copy_files():
    data = read_json(path=Path('datafile/certificate1.json'))
    files_prefix = data['contact_num']+'_'+ data['product_num']
    fs = copy_template_files(prefix=files_prefix)
    print(fs)

def test_export_printed_files():
    cert_data = read_json(path=Path('testdata/certificate1.json'))
    config_data = read_json(path=Path('testdata/config1.json'))
    files = export_printed_files(cert_data=cert_data, config_data=config_data)
    print(files)
    
if __name__ == '__main__':
    
    test_export_printed_files()

