
from excel_reader import read_supplier_data, SupplierType


def main():

    product_parts = read_supplier_data(supplier_type=SupplierType.XIANSUQI, 
                                       path = "供应商数据表/限速器缓冲器数据表.xlsx")

    for _, row in product_parts.iterrows():
        print(row['HeTongHao'], row['BianHao1'])


if __name__ == '__main__':
    main()
