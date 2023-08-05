
from excel_reader import read_supplier_data, SupplierType

def main():

    product_parts = read_supplier_data(supplier_type=SupplierType.ZHUJI_QUDONG, 
                                       path = "供应商数据表/主机数据表.xlsx")
    ind_columns = product_parts.columns.values
    # 显示索引名
    print(product_parts)
    


if __name__ == '__main__':
    main()
