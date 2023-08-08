from core.excel_reader import read_supplier_data, SupplierType

def test_lvpt_board():
    lvpt_board = read_supplier_data(supplier_type=SupplierType.ZHUBAN_LVCT, 
                                           path = "tests/supplier_excel_data/主板数据表.xlsx")
    print(lvpt_board.valid_dataframe)
    print(lvpt_board.invalid_dataframe)

def test_smart_board():
    smart_board = read_supplier_data(supplier_type=SupplierType.ZHUBAN_SMART, 
                                           path = "tests/supplier_excel_data/主板数据表.xlsx")
    print(smart_board)

if __name__ == '__main__':
    test_lvpt_board()
    # test_smart_board()