from core.excel_reader import read_supplier_data, SupplierType
import pandas as pd
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

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
def test_xianshuqi():
    products = read_supplier_data(supplier_type=SupplierType.XIANSUQI, 
                                           path = "tests/supplier_excel_data/限速器缓冲器数据表.xlsx")
    print(products)
def test_zhuji():
    products_1 = read_supplier_data(supplier_type=SupplierType.ZHUJI_QUDONG, 
                                           path = "tests/supplier_excel_data/主机数据表.xlsx")
    products_2 = read_supplier_data(supplier_type=SupplierType.ZHUJI_YIDONGBAOHU, 
                                           path = "tests/supplier_excel_data/主机数据表.xlsx")
    products_3 = read_supplier_data(supplier_type=SupplierType.ZHUJI_ZHIDONG, 
                                           path = "tests/supplier_excel_data/主机数据表.xlsx")
    print(products_1)
    print(products_2)
    print(products_3)

class ItemsModel(BaseModel):
    col1:list[int]
    col2:list[float]
    col3:list[str] = Field(default_factory='2')
    def __init__(self, **data):
        super().__init__(**data)
        self.col3 = [str(i) for i in self.col1]

class ItemModel(BaseModel):
    col1:int 
    col2:float 
    col3:Optional[date] = date.today()

def test_dic_model_1():
    """pydantic 模型可以设置初始值，且可以直接接受dict"""
    df = pd.DataFrame({'col1': [1, 2], 'col2': [0.5, 0.75]},index=['row1', 'row2'])
    items = df.to_dict('list')
    ism = ItemsModel(**items)
    print(ism)

def test_dic_model_2():
    """pydantic 模型可以设置初始值，且可以直接接受dict"""
    df = pd.DataFrame({'col1': [1, 2], 'col2': [0.5, 0.75]},index=['row1', 'row2'])
    items:list[ItemModel] = []
    for _, row in df.iterrows():
        items.append(ItemModel(col1 = row['col1'], col2 = row['col2']))
    print(items)

def test_dic_model_3():
    """pydantic 模型可以设置初始值，且可以直接接受dict"""
    df = pd.DataFrame({'col1': [1, 2], 'col2': [0.5, 0.75]},index=['row1', 'row2'])
    records = df.to_dict('records')
    items:list[ItemModel] = [ItemModel(**r) for r in records]
    
    print(items)

def test_gangshisheng():
    products_1 = read_supplier_data(supplier_type=SupplierType.GANGSHISHENG, 
                                           path = "tests/supplier_excel_data/钢丝绳数据表.xlsx")
    print(products_1.valid_dataframe)
if __name__ == '__main__':
    test_gangshisheng()