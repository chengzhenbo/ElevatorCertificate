# -*- coding: utf-8 -*-
from datetime import datetime,date

class ParseJson:
    def __init__(self, data_dict:dict):
        self.data = data_dict
        self.__report_data:dict = {}
        self.__supplier:dict = {}

        self.extract_product()
        self.extract_tech_para()
        self.extract_ropehead()
        self.extract_drivecontroller()


    
    def extract_product(self)->None:
        """提取产品基本信息"""
        product:dict = {}
        product["product_num"] = self.data['contract_no'][3:] #去除合同号前3位
        product["product_contract_no"] = self.data['contract_no']
        product["product_type"] = self.data['ReadinHetonginfo']['梯型'] 
        product["product_name"] = self.data['ModelReadinHgzCsZjb']['SysBasicInfoMachine']['产品名称']
        product["product_device_type"] = self.data['ModelReadinHgzCsZjb']['SysBasicInfoMachine']['设备类别']
        product["product_device_category"] = self.data['ModelReadinHgzCsZjb']['SysBasicInfoMachine']['设备品种']
        product["product_manufacturing_company"] = "西子电梯科技有限公司"
        product["product_device_num"] = self.data['ModelReadinHgzCsZjb']['SysBasicInfoMachine']['设备代码']
        product["product_customer_company"] = self.data['ModelReadinHgzCsZjb']['项目名称']
        product["product_license_num"] = self.data['cert_manufacturing_license_numbe']
        product["product_license_expiration_date"] = ParseJson.get_datestr(original_date=self.data['cert_valid_date'])
        
        self.__report_data["product"] = product

    def extract_tech_para(self)->None:
        """主要技术参数"""
        tech_para = {}
        tech_para['rated_load'] = self.data['ModelReadinHgzCsZjb']['载重']
        tech_para['rated_speed'] = self.data['ModelReadinHgzCsZjb']['速度']
        tech_para['control_method'] = '集选' # 集选/微处理器/群控制系统/直接梯/工程维护
        tech_para['elevator_control_mode'] = self.data['ModelReadinHgzCsZjb']['控制方式'] 
        tech_para['door_open_mode'] = self.data['ModelReadinHgzCsZjb']['开门方式']
        tech_para['floor_num'] = self.data['ModelReadinHgzCsZjb']['层数']
        tech_para['stop_num'] = self.data['ModelReadinHgzCsZjb']['站数']
        tech_para['floor_num'] = self.data['ModelReadinHgzCsZjb']['门数']
        tech_para['lifting_height'] = self.data['ModelReadinHgzCsZjb']['提升高度']
        carbine_area = int(self.data['ModelReadinHgzCsZjb']['轿厢净宽'])*int(self.data['ModelReadinHgzCsZjb']['轿厢净深'])/ 1000000
        tech_para['carbine_area'] = carbine_area
        tech_para['carbine_weight'] = self.data['ModelReadinHgzCsZjb']['轿厢自重']
        tech_para['coefficient_range'] = "0.4~0.5"
        tech_para['suspension_ratio'] = f"{self.data['ModelReadinHgzCsZjb']['曳引比']}:1"
        tech_para['carbine_size'] = f"净宽 {self.data['ModelReadinHgzCsZjb']['轿厢净宽']} mm x 净深 {self.data['ModelReadinHgzCsZjb']['轿厢净深']} mm"
        tech_para['product_standard'] = 'Q/HU 1102-2022《电梯制造与安装安全标准》'

        self.__report_data["tech_para"] = tech_para
    
    def extract_ropehead(self)->None:
        """绳头组合"""
        ropehead = {} 
        ropehead['product_name'] = self.data['SupplierRopeHead']['ropehc_name']
        ropehead['product_model'] = self.data['SupplierRopeHead']['ropehc_model']
        ropehead['batch_no'] = self.data['SupplierRopeHead']['ropehc_manufacture_batch_no']
        ropehead['manufacturing_company'] = self.data['SupplierRopeHead']['dept_name']
        ropehead['testing_cert_no'] = self.data['SupplierRopeHead']['ropehc_type_testing_cert_no']
        ropehead['manufacture_date'] = ParseJson.get_datestr(self.data['SupplierRopeHead']['ropehc_manufacture_date'],type=None)
        
        self.__supplier['ropehead'] = ropehead

    def extract_drivecontroller(self)->None:
        """驱动主机"""
        drivecontroller = {} 
        drivecontroller['product_name'] = self.data['SupplierDriveController']['product_type_name']
        drivecontroller['product_model'] = self.data['SupplierDriveController']['dc_model']
        drivecontroller['batch_no'] = self.data['SupplierDriveController']['dc_no']
        drivecontroller['manufacturing_company'] = self.data['SupplierDriveController']['dept_name']
        drivecontroller['testing_cert_no'] = self.data['SupplierDriveController']['dc_type_testing_cert_no']
        drivecontroller['manufacture_date'] = ParseJson.get_datestr(self.data['SupplierDriveController']['dc_manufacture_date'],type=None)
        
        self.__supplier['drivecontroller'] = drivecontroller      


    @property
    def report_data(self):
        self.__report_data["supplier"] = self.__supplier
        return self.__report_data
    
    @classmethod
    def get_datestr(cls, original_date:date,type="chinese")->str:
        """将日期类型转换为需要的输出格式"""
        dateobj = datetime.strptime(original_date, "%Y-%m-%d")
        if type=="chinese":
            return f"{dateobj.year}年{dateobj.month}月{dateobj.day}日"
        else:
            return f"{dateobj.year}.{dateobj.month}.{dateobj.day}"