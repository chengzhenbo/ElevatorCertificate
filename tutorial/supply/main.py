
from excel_reader import read_supplier_data, SupplierType


def main():

    product_parts = read_supplier_data(supplier_type=SupplierType.ZHUBAN_SMART, 
                                       file = "供应商数据表/主机数据表.xlsx")
    ind_columns = product_parts.columns.values
    # 显示索引名
    print('ind_columns = ', ind_columns)
    # 遍历行
    for _, row in product_parts.iterrows():
        # 第0列和最后一列的所有数据
        print(row[0], row[-1])


if __name__ == '__main__':
    main()
