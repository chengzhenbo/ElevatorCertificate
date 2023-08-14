
from pathlib import Path
from enum import StrEnum
from dataclasses import dataclass
import re
import json
import configparser
from typing import NamedTuple

import pandas as pd
import pypinyin
from pandera.typing import DataFrame

HERE = Path(__file__).resolve().parent

CONFIG = configparser.ConfigParser()
CONFIG.read(HERE/'exceltemplate.ini', encoding='utf-8')

class SecName(NamedTuple):
    sec_name_colunms:str
    sec_name_hidx:str
    sec_name_bianhao:str

class SupplierData(NamedTuple):
    valid_dataframe: DataFrame
    invalid_dataframe: DataFrame

class SupplierType(StrEnum):
    ZHUBAN_SMART = 'ZHUBAN_SMART'
    ZHUBAN_LVCT = 'ZHUBAN_LVCT'
    ZHUJI_QUDONG = 'ZHUJI_QUDONG'
    ZHUJI_ZHIDONG = 'ZHUJI_ZHIDONG'
    ZHUJI_YIDONGBAOHU = 'ZHUJI_YIDONGBAOHU'
    ZHIDONGJIUYUAN = 'ZHIDONGJIUYUAN'
    IC_CARD = 'IC_CARD'
    SHENGTOUZHUHE = 'SHENGTOUZHUHE'
    ANQUANQIAN = 'ANQUANQIAN'
    XIANSUQI = 'XIANSUQI'
    HUANCHONGQI = 'HUANCHONGQI'
    GANGSHISHENG = 'GANGSHISHENG'

@dataclass
class ParasParserExcel():
    origin_columns:list[str]
    new_columns:list[str]
    bianhao_idxs:list[list[str]]
    header_idx:int = 0
    usecols:str = None 

@dataclass
class ColumnHeaderError(Exception):
    header:str 
    def __str__(self) -> str:
        return f"Excel模板文件的列名'{self.header}'不存在，请使用正确的模板文件上传数据."

@dataclass
class SupplierTypeError(Exception):
    supplier_type:str 
    def __str__(self) -> str:
        return f"供应商类型'{self.supplier_type}'不存在."
    
class ExcelReader:
    def __init__(self, file_path:Path, 
                 header_idx:int, 
                 usecols:str,
                 columns:list[str],
                 new_columns:list[str] = None)->None:
        self.file_path = file_path
        self.header_idx = header_idx
        self.usecols = usecols
        self.columns = columns
        self.new_columns = new_columns

    def __call__(self)->DataFrame:
        self.df = pd.read_excel(io = self.file_path, 
                                header=self.header_idx,
                                usecols=self.usecols,
                                dtype=str)
        # 检查excel文件列名
        self.check_header()
        # # 合同号为空的数据条目滤去
        # if '合同号' in self.df.columns:
        #     self.df = self.df[self.df[['合同号']].notnull().all(1)]

        # 制造日期列的数据格式转换
        if '制造日期' in self.df.columns:
            self.df['制造日期'] = self.df['制造日期'].astype('datetime64[ns]')
        
        if self.new_columns is not None:
            # 将中文列名转换更新为新的列名，方便导入到数据库
            self.df.columns = self.new_columns
            # TODO 列可能重名，现在用穷举的办法，后面应该设计更好的方法进行转换
            if 'ZhiZhaoRiQi' in self.df.columns:
                self.df['ZhiZhaoRiQi'] = self.df['ZhiZhaoRiQi'].astype('datetime64[ns]')
            if 'ZhiZhaoRiQi1' in self.df.columns:
                self.df['ZhiZhaoRiQi1'] = self.df['ZhiZhaoRiQi1'].astype('datetime64[ns]')
            if 'ZhiZhaoRiQi2' in self.df.columns:
                self.df['ZhiZhaoRiQi2'] = self.df['ZhiZhaoRiQi2'].astype('datetime64[ns]')    
        return self.df

    def check_header(self):
        """检查Excel文件的header是否与模板一致"""
        for i, col in enumerate(self.columns):
            if self.df.columns.values[i].split('.')[0] != col:
                raise ColumnHeaderError(col)

def get_sec_name(supplier_type:SupplierType)->SecName:
    """根据供应商类型，得到解析配置文件所需的section名"""
    if supplier_type == SupplierType.ZHUBAN_SMART:
        sec_name_colunms = SupplierType.ZHUBAN_SMART.value + "_COLUMNS"
        sec_name_hidx = SupplierType.ZHUBAN_SMART.value + "_IND"
        sec_name_bianhao = SupplierType.ZHUBAN_SMART.value + "_BIANHAO"
    elif supplier_type == SupplierType.ZHUBAN_LVCT:
        sec_name_colunms = SupplierType.ZHUBAN_LVCT.value + "_COLUMNS"
        sec_name_hidx = SupplierType.ZHUBAN_LVCT.value + "_IND"
        sec_name_bianhao = SupplierType.ZHUBAN_LVCT.value + "_BIANHAO"
    elif supplier_type == SupplierType.ZHUJI_QUDONG:
        sec_name_colunms = SupplierType.ZHUJI_QUDONG.value + "_COLUMNS"
        sec_name_hidx = SupplierType.ZHUJI_QUDONG.value + "_IND"
        sec_name_bianhao = SupplierType.ZHUJI_QUDONG.value + "_BIANHAO"
    elif supplier_type == SupplierType.ZHUJI_ZHIDONG:
        sec_name_colunms = SupplierType.ZHUJI_ZHIDONG.value + "_COLUMNS"
        sec_name_hidx = SupplierType.ZHUJI_ZHIDONG.value + "_IND"
        sec_name_bianhao = SupplierType.ZHUJI_ZHIDONG.value + "_BIANHAO"
    elif supplier_type == SupplierType.ZHUJI_YIDONGBAOHU:
        sec_name_colunms = SupplierType.ZHUJI_YIDONGBAOHU.value + "_COLUMNS"
        sec_name_hidx = SupplierType.ZHUJI_YIDONGBAOHU.value + "_IND"
        sec_name_bianhao = SupplierType.ZHUJI_YIDONGBAOHU.value + "_BIANHAO"
    elif supplier_type == SupplierType.ZHIDONGJIUYUAN:
        sec_name_colunms = SupplierType.ZHIDONGJIUYUAN.value + "_COLUMNS"
        sec_name_hidx = SupplierType.ZHIDONGJIUYUAN.value + "_IND"
        sec_name_bianhao = SupplierType.ZHIDONGJIUYUAN.value + "_BIANHAO"
    elif supplier_type == SupplierType.IC_CARD:
        sec_name_colunms = SupplierType.IC_CARD.value + "_COLUMNS"
        sec_name_hidx = SupplierType.IC_CARD.value + "_IND"
        sec_name_bianhao = SupplierType.IC_CARD.value + "_BIANHAO"
    elif supplier_type == SupplierType.SHENGTOUZHUHE:
        sec_name_colunms = SupplierType.SHENGTOUZHUHE.value + "_COLUMNS"
        sec_name_hidx = SupplierType.SHENGTOUZHUHE.value + "_IND"
        sec_name_bianhao = SupplierType.SHENGTOUZHUHE.value + "_BIANHAO"
    elif supplier_type == SupplierType.ANQUANQIAN:
        sec_name_colunms = SupplierType.ANQUANQIAN.value + "_COLUMNS"
        sec_name_hidx = SupplierType.ANQUANQIAN.value + "_IND"
        sec_name_bianhao = SupplierType.ANQUANQIAN.value + "_BIANHAO"
    elif supplier_type == SupplierType.XIANSUQI:
        sec_name_colunms = SupplierType.XIANSUQI.value + "_COLUMNS"
        sec_name_hidx = SupplierType.XIANSUQI.value + "_IND"
        sec_name_bianhao = SupplierType.XIANSUQI.value + "_BIANHAO"
    elif supplier_type == SupplierType.HUANCHONGQI:
        sec_name_colunms = SupplierType.HUANCHONGQI.value + "_COLUMNS"
        sec_name_hidx = SupplierType.HUANCHONGQI.value + "_IND"
        sec_name_bianhao = SupplierType.HUANCHONGQI.value + "_BIANHAO"
    elif supplier_type == SupplierType.GANGSHISHENG:
        sec_name_colunms = SupplierType.GANGSHISHENG.value + "_COLUMNS"
        sec_name_hidx = SupplierType.GANGSHISHENG.value + "_IND"
        sec_name_bianhao = SupplierType.GANGSHISHENG.value + "_BIANHAO"
    else:
        raise SupplierTypeError(supplier_type)
    
    return SecName(sec_name_colunms = sec_name_colunms, 
                     sec_name_hidx = sec_name_hidx,
                     sec_name_bianhao = sec_name_bianhao)
     
def get_pingying_columns(columns:list[str])->list[str]:
    """将中文的列名转换为拼音，每个字拼音首字母大写"""
    pinying_columns = []
    for c_col in columns:
        result = pypinyin.pinyin(c_col, style=pypinyin.NORMAL)
        result_ = ''.join([i[0].capitalize() for i in result])
        p_col = re.split(r'\W+', result_) 
        pinying_columns.append(p_col[0])
    return pinying_columns

def paras_parser_file(sec_name:SecName)->ParasParserExcel:
    """根据配置文件，解析读取excel文件所需的参数"""
    sec_name_colunms = sec_name.sec_name_colunms
    sec_name_hidx = sec_name.sec_name_hidx
    sec_name_bianhao = sec_name.sec_name_bianhao
    
    origin_columns = []
    new_columns = []
    keys = [key for key, _ in CONFIG[sec_name_colunms].items()]
    for key in keys:
        item = json.loads(CONFIG.get(sec_name_colunms, key))
        origin_columns.append(item[0])
        new_columns.append(item[1])
    header_idx = CONFIG.getint(sec_name_hidx, 'header_idx'),
    usecols = ','.join(CONFIG.options(sec_name_colunms))
    bianhao_idxs = json.loads(CONFIG.get(sec_name_bianhao, 'bianhao_idx'))

    return ParasParserExcel(origin_columns = origin_columns,
                            new_columns = new_columns,
                            bianhao_idxs = bianhao_idxs,
                            header_idx = header_idx,
                            usecols = usecols)

def read_supplier_data(supplier_type:SupplierType, path:Path)->DataFrame:
    """根据供应商类型和文件路径，读入excel数据返回pandas的dataframe类型数据"""
    sec_name = get_sec_name(supplier_type=supplier_type)
    paras_parser = paras_parser_file(sec_name=sec_name)
    excel_reader = ExcelReader(file_path = path,
                                header_idx = paras_parser.header_idx,
                                usecols = paras_parser.usecols,
                                columns = paras_parser.origin_columns,
                                new_columns = paras_parser.new_columns)
    products = excel_reader()
    
    bianhao_idxs = paras_parser.bianhao_idxs
    if len(bianhao_idxs) > 0:  # 根据配置文件中编号设置，将产品按编号组织数据
        for i, bianhao in enumerate(bianhao_idxs):
            if i == 0:
                product_0 = products[bianhao]
            else:
                product_1 = products[bianhao]
                product_1.columns = product_0.columns
                product_0 = pd.concat([product_0, product_1],ignore_index=True)
                
        if 'manufacture_date' in product_0.columns:
            product_0['manufacture_date'] = product_0['manufacture_date'].astype('datetime64[ns]') 
        
        product_0_without_null = product_0.dropna()
        product_0_with_null = product_0[product_0.isnull().any(axis=1)]
        return SupplierData(valid_dataframe = product_0_without_null, 
                            invalid_dataframe = product_0_with_null)
    else: # 否则直接返回
        if 'manufacture_date' in products.columns:
            products['manufacture_date'] = products['manufacture_date'].astype('datetime64[ns]') 
        products_without_null = products.dropna()
        products_with_null = products[products.isnull().any(axis=1)]
        return SupplierData(valid_dataframe = products_without_null, 
                            invalid_dataframe = products_with_null)





