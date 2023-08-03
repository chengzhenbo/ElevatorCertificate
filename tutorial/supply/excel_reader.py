
from pathlib import Path
from enum import StrEnum
from dataclasses import dataclass
import re
import json
import configparser

import pandas as pd
import pypinyin
from pandera.typing import DataFrame

CONFIG = configparser.ConfigParser()
CONFIG.read('exceltemplate.ini')


class SupplierType(StrEnum):
    ZHUBAN_SMART = 'ZHUBAN_SMART'
    ZHUBAN_LVCT = 'ZHUBAN_LVCT'
    ZHUJI_QUDONG = 'ZHUJI_QUDONG'
    ZHUJI_ZHIDONG = 'ZHUJI_ZHIDONG'
    ZHUJI_YIDONGBAOHU = 'ZHUJI_YIDONGBAOHU'
    ZHIDONGJIUYUAN = 'ZHIDONGJIUYUAN'
    IC_CARD = 'IC_CARD'
    SHENGTOUZHUHE = 'SHENGTOUZHUHE'
    ANQUANQIAN_1 = 'ANQUANQIAN_1'
    ANQUANQIAN_2 = 'ANQUANQIAN_2'
    XIANSUQI = 'XIANSUQI'
    HUANCHONGQI = 'HUANCHONGQI'

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
                 pingying_columns:list[str] = None)->None:
        self.file_path = file_path
        self.header_idx = header_idx
        self.usecols = usecols
        self.columns = columns
        self.pingying_columns = pingying_columns

    def read_file_clean(self)->DataFrame:
        self.df = pd.read_excel(io = self.file_path, 
                                header=self.header_idx,
                                usecols=self.usecols,
                                dtype=str)
        # 检查excel文件列名
        self.check_header()
        
        if self.pingying_columns is not None:
            # 将中文列名转换为拼音列名，每字拼音首字母大写
            self.df.columns = self.pingying_columns
            # 合同号为空的数据条目滤去
            if 'HeTongHao' in self.df.columns:
                self.df = self.df[self.df[['HeTongHao']].notnull().all(1)]
            # 制造日期列的数据格式转换
            if 'ZhiZaoRiQi' in self.df.columns:
                self.df['ZhiZaoRiQi'] = self.df['ZhiZaoRiQi'].astype('datetime64[ns]')
        return self.df

    def check_header(self):
        """检查Excel文件的header是否与模板一致"""
        for i, col in enumerate(self.columns):
            if self.df.columns.values[i].split('.')[0] != col:
                raise ColumnHeaderError(col)

def get_pingying_columns(columns:list[str])->list[str]:
    """将中文的列名转换为拼音，每个字拼音首字母大写"""
    pinying_columns = []
    for c_col in columns:
        result = pypinyin.pinyin(c_col, style=pypinyin.NORMAL)
        result_ = ''.join([i[0].capitalize() for i in result])
        p_col = re.split(r'\W+', result_) 
        pinying_columns.append(p_col[0])
    return pinying_columns

def read_data(colunms_name:str, ind_name:str, path:Path)->DataFrame:
    colunms = [column for _, column in CONFIG[colunms_name].items()]
    pingying_columns = get_pingying_columns(colunms)
    excelreader_zhuban_SMART = ExcelReader(file_path = path,
                                header_idx = json.loads(CONFIG.get(ind_name, 'header_idx')),
                                usecols = ','.join(CONFIG.options(colunms_name)),
                                columns = colunms,
                                pingying_columns=pingying_columns)
    products = excelreader_zhuban_SMART.read_file_clean()

    return products

def read_supplier_data(supplier_type:SupplierType, file:Path)->DataFrame:
    """根据供应商类型和文件路径，读入excel数据返回pandas的dataframe类型数据"""
    if supplier_type == SupplierType.ZHUBAN_SMART:
        colunms_name = SupplierType.ZHUBAN_SMART.value + "_COLUMNS"
        ind_name = SupplierType.ZHUBAN_SMART.value + "_IND"
    elif supplier_type == SupplierType.ZHUBAN_LVCT:
        colunms_name = SupplierType.ZHUBAN_LVCT.value + "_COLUMNS"
        ind_name = SupplierType.ZHUBAN_LVCT.value + "_IND"
    elif supplier_type == SupplierType.ZHUJI_QUDONG:
        colunms_name = SupplierType.ZHUJI_QUDONG.value + "_COLUMNS"
        ind_name = SupplierType.ZHUJI_QUDONG.value + "_IND"
    elif supplier_type == SupplierType.ZHUJI_ZHIDONG:
        colunms_name = SupplierType.ZHUJI_ZHIDONG.value + "_COLUMNS"
        ind_name = SupplierType.ZHUJI_ZHIDONG.value + "_IND"
    elif supplier_type == SupplierType.ZHUJI_YIDONGBAOHU:
        colunms_name = SupplierType.ZHUJI_YIDONGBAOHU.value + "_COLUMNS"
        ind_name = SupplierType.ZHUJI_YIDONGBAOHU.value + "_IND"
    elif supplier_type == SupplierType.ZHIDONGJIUYUAN:
        colunms_name = SupplierType.ZHIDONGJIUYUAN.value + "_COLUMNS"
        ind_name = SupplierType.ZHIDONGJIUYUAN.value + "_IND"
    elif supplier_type == SupplierType.IC_CARD:
        colunms_name = SupplierType.IC_CARD.value + "_COLUMNS"
        ind_name = SupplierType.IC_CARD.value + "_IND"
    elif supplier_type == SupplierType.SHENGTOUZHUHE:
        colunms_name = SupplierType.SHENGTOUZHUHE.value + "_COLUMNS"
        ind_name = SupplierType.SHENGTOUZHUHE.value + "_IND"
    elif supplier_type == SupplierType.ANQUANQIAN_1:
        colunms_name = SupplierType.ANQUANQIAN_1.value + "_COLUMNS"
        ind_name = SupplierType.ANQUANQIAN_1.value + "_IND"
    elif supplier_type == SupplierType.ANQUANQIAN_2:
        colunms_name = SupplierType.ANQUANQIAN_2.value + "_COLUMNS"
        ind_name = SupplierType.ANQUANQIAN_2.value + "_IND"
    elif supplier_type == SupplierType.XIANSUQI:
        colunms_name = SupplierType.XIANSUQI.value + "_COLUMNS"
        ind_name = SupplierType.XIANSUQI.value + "_IND"
    elif supplier_type == SupplierType.HUANCHONGQI:
        colunms_name = SupplierType.HUANCHONGQI.value + "_COLUMNS"
        ind_name = SupplierType.HUANCHONGQI.value + "_IND"
    else:
        raise SupplierTypeError(supplier_type)
    
    return read_data(colunms_name =  colunms_name,
                     ind_name = ind_name, 
                     path = file)





