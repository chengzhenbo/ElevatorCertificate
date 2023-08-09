from core.excel_reader import read_supplier_data, SupplierType

def test_lvpt_board():
    products = read_supplier_data(supplier_type=SupplierType.ZHUBAN_LVCT, 
                                           path = "tests/supplier_excel_data/主板数据表.xlsx")
    print(products.valid_dataframe)
    print(products.invalid_dataframe)

def test_smart_board():
    products = read_supplier_data(supplier_type=SupplierType.ZHUBAN_SMART, 
                                           path = "tests/supplier_excel_data/主板数据表.xlsx")
    print(products)

def test_sheng_tou():
    products = read_supplier_data(supplier_type=SupplierType.SHENGTOUZHUHE, 
                                           path = "tests/supplier_excel_data/绳头组合.xlsx")
    print(products)

def test_zhidongjiuyuan():
    products = read_supplier_data(supplier_type=SupplierType.ZHIDONGJIUYUAN, 
                                           path = "tests/supplier_excel_data/自动救援操作装置数据表.xlsx")
    print(products)
if __name__ == '__main__':
    test_zhidongjiuyuan()