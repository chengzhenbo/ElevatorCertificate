# -*- coding: utf-8 -*-
from datetime import datetime,date
from collections import defaultdict

class ParseJson:
    def __init__(self, data_dict:dict):
        self.data = data_dict
        self.__report_data:dict = {}
        self.__supplier:dict = {}

        self.extract_product()
        self.extract_tech_para()
        self.extract_ropehead()
        self.extract_drivecontroller()
        self.extract_controlcabinet_doorsystem()
        self.extract_board()
        self.extract_another_parts()
        self.extract_steel_rope()
        self.extract_cabin_safety()
        self.extract_speed_limiter()
        self.extract_safebrake()
        self.extract_buffer()

    def extract_product(self)->None:
        """提取产品基本信息"""
        product:dict = defaultdict(str)
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
        product["product_license_expiration_date"] = ParseJson.get_datestr(original_date=self.data['cert_valid_date'],type="C")
        
        self.__report_data["product"] = product

    def extract_tech_para(self)->None:
        """主要技术参数"""
        tech_para = defaultdict(str)
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
        ropehead = defaultdict(str)
        ropehead['product_name'] = self.data['SupplierRopeHead']['ropehc_name']
        ropehead['product_model'] = self.data['SupplierRopeHead']['ropehc_model']
        ropehead['batch_no'] = self.data['SupplierRopeHead']['ropehc_manufacture_batch_no']
        ropehead['manufacturing_company'] = self.data['SupplierRopeHead']['dept_name']
        ropehead['testing_cert_no'] = self.data['SupplierRopeHead']['ropehc_type_testing_cert_no']
        ropehead['manufacture_date'] = ParseJson.get_datestr(self.data['SupplierRopeHead']['ropehc_manufacture_date'])
        
        self.__supplier['ropehead'] = ropehead

    def extract_drivecontroller(self)->None:
        """驱动主机"""
        drivecontroller = defaultdict(str) 
        drivecontroller['product_name'] = self.data['SupplierDriveController']['product_type_name']
        drivecontroller['product_model'] = self.data['SupplierDriveController']['dc_model']
        drivecontroller['batch_no'] = self.data['SupplierDriveController']['dc_no']
        drivecontroller['manufacturing_company'] = self.data['SupplierDriveController']['dept_name']
        drivecontroller['testing_cert_no'] = self.data['SupplierDriveController']['dc_type_testing_cert_no']
        drivecontroller['manufacture_date'] = ParseJson.get_datestr(self.data['SupplierDriveController']['dc_manufacture_date'])
        
        self.__supplier['drivecontroller'] = drivecontroller   

    def extract_controlcabinet_doorsystem(self)->None:
        """控制柜和门系统 
        TODO: 这里判断的类型变量应该从supply的schema中导入，以确保类型的一致""" 
        control_cabinet = defaultdict(str) # 控制柜
        landing_door = defaultdict(str)    # 层门
        fire_door = defaultdict(str)       # 防火门
        glass_door = defaultdict(str)      # 玻璃轿门
        glass_wall = defaultdict(str)      # 玻璃轿壁
        halldoor_lock = defaultdict(str)   # 厅门锁
        cardoor_lock = defaultdict(str)    # 轿门锁
        for data in self.data['SupplierKongZhiGuiMenXiTongs']:
            if data['remark'] == '控制柜':
                control_cabinet['product_name'] = data['type_name']
                control_cabinet['product_model'] = data['model']
                control_cabinet['batch_no'] = data['batch_no']
                control_cabinet['manufacturing_company'] = data['dept_name']
                control_cabinet['testing_cert_no'] = data['type_testing_cert_no']
                control_cabinet['manufacture_date'] = ParseJson.get_datestr(data['manufacture_date'])
            elif data['remark'] == '层门':
                landing_door['product_name'] = data['type_name']
                landing_door['product_model'] = data['model']
                landing_door['batch_no'] = data['batch_no']
                landing_door['manufacturing_company'] = data['dept_name']
                landing_door['testing_cert_no'] = data['type_testing_cert_no']
                landing_door['manufacture_date'] = ParseJson.get_datestr(data['manufacture_date'])
            elif data['remark'] == '防火门':
                fire_door['product_name'] = data['type_name']
                fire_door['product_model'] = data['model']
                fire_door['batch_no'] = data['batch_no']
                fire_door['manufacturing_company'] = data['dept_name']
                fire_door['testing_cert_no'] = data['type_testing_cert_no']
                fire_door['manufacture_date'] = ParseJson.get_datestr(data['manufacture_date'])
            elif data['remark'] == '玻璃轿门':
                glass_door['product_name'] = data['type_name']
                glass_door['product_model'] = data['model']
                glass_door['batch_no'] = data['batch_no']
                glass_door['manufacturing_company'] = data['dept_name']
                glass_door['testing_cert_no'] = data['type_testing_cert_no']
                glass_door['manufacture_date'] = ParseJson.get_datestr(data['manufacture_date'])
            elif data['remark'] == '玻璃轿壁':
                glass_wall['product_name'] = data['type_name']
                glass_wall['product_model'] = data['model']
                glass_wall['batch_no'] = data['batch_no']
                glass_wall['manufacturing_company'] = data['dept_name']
                glass_wall['testing_cert_no'] = data['type_testing_cert_no']
                glass_wall['manufacture_date'] = ParseJson.get_datestr(data['manufacture_date'])
            elif data['remark'] == '厅门锁':
                halldoor_lock['product_name'] = data['type_name']
                halldoor_lock['product_model'] = data['model']
                halldoor_lock['batch_no'] = data['batch_no']
                halldoor_lock['manufacturing_company'] = data['dept_name']
                halldoor_lock['testing_cert_no'] = data['type_testing_cert_no']
                halldoor_lock['manufacture_date'] = ParseJson.get_datestr(data['manufacture_date'])
            elif data['remark'] == '轿门锁':
                cardoor_lock['product_name'] = data['type_name']
                cardoor_lock['product_model'] = data['model']
                cardoor_lock['batch_no'] = data['batch_no']
                cardoor_lock['manufacturing_company'] = data['dept_name']
                cardoor_lock['testing_cert_no'] = data['type_testing_cert_no']
                cardoor_lock['manufacture_date'] = ParseJson.get_datestr(data['manufacture_date'])

        self.__supplier['control_cabinet'] = control_cabinet 
        self.__supplier['landing_door'] = landing_door 
        self.__supplier['fire_door'] = fire_door 
        self.__supplier['glass_door'] = glass_door 
        self.__supplier['glass_wall'] = glass_wall 
        self.__supplier['halldoor_lock'] = halldoor_lock 
        self.__supplier['cardoor_lock'] = cardoor_lock 
            
    def extract_board(self)->None:
        """两个安全电路配件：SMART和LVCT1"""
        smart_board = defaultdict(str)
        lvct1_board = defaultdict(str)

        smart_board['product_model'] = self.data['SupplierSmartBoard']['smartb_model']
        smart_board['batch_no'] = self.data['SupplierSmartBoard']['smartb_manufacture_batch_no']
        smart_board['manufacturing_company'] = self.data['SupplierSmartBoard']['dept_name']
        smart_board['testing_cert_no'] = self.data['SupplierSmartBoard']['smartb_type_testing_cert_no']
        smart_board['manufacture_date'] = ParseJson.get_datestr(self.data['SupplierSmartBoard']['smartb_manufacture_date'])

        lvct1_board['product_model'] = self.data['SupplierLvct1Board']['lvct_model']
        lvct1_board['batch_no'] = self.data['SupplierLvct1Board']['lvct_manufacture_batch_no']
        lvct1_board['manufacturing_company'] = self.data['SupplierLvct1Board']['dept_name']
        lvct1_board['testing_cert_no'] = self.data['SupplierLvct1Board']['lvct_type_testing_cert_no']
        lvct1_board['manufacture_date'] = ParseJson.get_datestr(self.data['SupplierLvct1Board']['lvct_manufacture_date'])

        self.__supplier['smart_board'] = smart_board 
        self.__supplier['lvct1_board'] = lvct1_board 

    def extract_another_parts(self)->None:
        """其它装置"""
        ic_card = defaultdict(str)
        auto_rescue = defaultdict(str)
        energy_feedback = defaultdict(str)
        for data in self.data['SupplierIcCard']: # IC-card可能存在连个编号
            ic_card['product_model'] = data['ic_model'] 
            if len(ic_card['batch_no']) == 0:
                ic_card['batch_no'] = data['ic_no'] 
            else:
                ic_card['batch_no'] = ic_card['batch_no'] + '/' + data['ic_no'] 

        auto_rescue['product_model'] = self.data['SupplierAred']['ared_model']
        auto_rescue['batch_no'] = self.data['SupplierAred']['ared_no']

        energy_feedback['product_model'] = self.data['EquipmentEnergyFeedback']['enfb_model']
        energy_feedback['batch_no'] = self.data['EquipmentEnergyFeedback']['enfb_no']
        
        self.__supplier['ic_card'] = ic_card 
        self.__supplier['auto_rescue'] = auto_rescue 
        self.__supplier['energy_feedback'] = energy_feedback 

    def extract_steel_rope(self)->None:
        """钢丝绳"""
        steel_rope = defaultdict(str)
        steel_rope['product_model'] = self.data['SupplierSteelRope']['steelr_specifications_model_value']
        steel_rope['diameter'] = self.data['SupplierSteelRope']['steelr_diameter_specifications_value']
        steel_rope['num'] = self.data['SupplierSteelRope']['steelr_num']

        self.__supplier['steel_rope'] = steel_rope 

    def extract_cabin_safety(self)->None:
        """轿厢意外保护装置"""
        braking_deceleration_device = defaultdict(str) # 制动减速装置
        movement_protection_device = defaultdict(str)  # 意外移动保护装置

        for data in self.data['SupplierCabinUpOPs']:
            braking_deceleration_device['product_name'] = data['cabinuop_product_type_name']
            braking_deceleration_device['product_model'] = data['cabinuop_model'] 
            if len(braking_deceleration_device['batch_no']) == 0:
                braking_deceleration_device['batch_no'] = data['cabinuop_no1'] 
            else:
                braking_deceleration_device['batch_no'] = braking_deceleration_device['batch_no'] + '/' + data['cabinuop_no1']
            braking_deceleration_device['manufacturing_company'] = data['dept_name'] 
            braking_deceleration_device['testing_cert_no'] = data['cabinuop_type_testing_cert_no']
            braking_deceleration_device['manufacture_date'] = ParseJson.get_datestr(data['cabinuop_manufacture_date'])

        for data in self.data['SupplierCabinUnMPs']:
            movement_protection_device['product_name'] = data['cabinump_product_type_name'] 
            movement_protection_device['product_model'] = data['cabinump_model'] 
            if len(movement_protection_device['batch_no']) == 0:
                movement_protection_device['batch_no'] = data['cabinump_no1'] 
            else:
                movement_protection_device['batch_no'] = movement_protection_device['batch_no'] + '/' + data['cabinump_no1']
            movement_protection_device['manufacturing_company'] = data['dept_name'] 
            movement_protection_device['testing_cert_no'] = data['cabinump_type_testing_cert_no']
            movement_protection_device['manufacture_date'] = ParseJson.get_datestr(data['cabinump_manufacture_date'])
        
        self.__supplier['braking_deceleration_device'] = braking_deceleration_device 
        self.__supplier['movement_protection_device'] = movement_protection_device

    def extract_speed_limiter(self)->None:
        """限速器"""
        speed_limiter_1 = defaultdict(str)
        speed_limiter_2 = defaultdict(str)

        speed_limiter_1['product_name'] = self.data['SupplierSpeedLimiters'][0]['sl_product_type_name']
        speed_limiter_1['product_model'] = self.data['SupplierSpeedLimiters'][0]['sl_model']
        speed_limiter_1['batch_no'] = self.data['SupplierSpeedLimiters'][0]['sl_no']
        speed_limiter_1['manufacturing_company'] = self.data['SupplierSpeedLimiters'][0]['dept_name']
        speed_limiter_1['testing_cert_no'] = self.data['SupplierSpeedLimiters'][0]['sl_type_testing_cert_no']
        speed_limiter_1['manufacture_date'] = ParseJson.get_datestr(self.data['SupplierSpeedLimiters'][0]['sl_manufacture_date'])

        if len(self.data['SupplierSpeedLimiters']) > 0:
            speed_limiter_2['product_name'] = self.data['SupplierSpeedLimiters'][1]['sl_product_type_name']
            speed_limiter_2['product_model'] = self.data['SupplierSpeedLimiters'][1]['sl_model']
            speed_limiter_2['batch_no'] = self.data['SupplierSpeedLimiters'][1]['sl_no']
            speed_limiter_2['manufacturing_company'] = self.data['SupplierSpeedLimiters'][1]['dept_name']
            speed_limiter_2['testing_cert_no'] = self.data['SupplierSpeedLimiters'][1]['sl_type_testing_cert_no']
            speed_limiter_2['manufacture_date'] = ParseJson.get_datestr(self.data['SupplierSpeedLimiters'][1]['sl_manufacture_date'])

        self.__supplier['speed_limiter_1'] = speed_limiter_1 
        self.__supplier['speed_limiter_2'] = speed_limiter_2 

    def extract_safebrake(self)->None:
        """安全钳：最多两个型号，每个型号最多两个编号"""
        safebrake_1 = defaultdict(str)
        safebrake_2 = defaultdict(str)
        product_model = defaultdict(list)

        for data in self.data['SupplierSafeBrakes']:
            safebrake_1['product_name'] = data['safeb_product_type_name']
            # 相同型号的编号、制造单位、证书编号和制造日期数据用list关联
            product_model[data['safeb_model']].append([data['safeb_no1'],
                                                       data['dept_name'],
                                                       data['safeb_type_testing_cert_no'],
                                                       ParseJson.get_datestr(data['safeb_manufacture_date'])])
        # 通过将字典转换为迭代器，可依次取字典中元素。
        iter_product_model = iter(product_model)
        if len(product_model) > 0:
            model_1 = next(iter_product_model)
            safebrake_1['product_model'] = model_1
            batch_no1 = ''
            for item in product_model[model_1]:
                batch_no1 += '/'+item[0]
            safebrake_1['batch_no'] = batch_no1[1:] # 去掉第一个/字符
            # product_model[model_1]list中包含list的个数与该类型下的编号数一致
            # manufacturing_company,testing_cert_no,manufacture_date相同类型数据一致
            # 可在list中的第一个list（也就是以下代码的[0]）中取
            safebrake_1['manufacturing_company'] = product_model[model_1][0][1]
            safebrake_1['testing_cert_no'] = product_model[model_1][0][2]
            safebrake_1['manufacture_date'] = product_model[model_1][0][3]

        if len(product_model) > 1: # 安全钳型号超过2个
            model_2 = next(iter_product_model)
            safebrake_2['product_model'] = model_2
            batch_no2 = ''
            for item in product_model[model_2]:
                batch_no2 += '/'+item[0]
            safebrake_2['batch_no'] = batch_no2[1:] # 去掉第一个/字符
            safebrake_2['manufacturing_company'] = product_model[model_2][0][1]
            safebrake_2['testing_cert_no'] = product_model[model_2][0][2]
            safebrake_2['manufacture_date'] = product_model[model_2][0][3]

        self.__supplier['safebrake_1'] = safebrake_1 
        self.__supplier['safebrake_2'] = safebrake_2 

    def extract_buffer(self)->None:
        """缓冲器：最多2个型号，对应有10个编号"""
        buffer = defaultdict(str)
        product_model = defaultdict(str)
        for data in self.data['SupplierBuffers']:
            buffer['product_name'] = data['buffer_product_type_name']
            # 将相同型号的编号字符串进行拼接
            product_model[data['buffer_model']] += '/'+ data['buffer_no']
            # 以下数据任意编号都相同，可在任意一个编号数据中取 
            buffer['manufacturing_company'] = data['dept_name']
            buffer['testing_cert_no'] = data['buffer_type_testing_cert_no']
            buffer['manufacture_date'] = ParseJson.get_datestr(data['buffer_manufacture_date'])
        
        iter_product_model = iter(product_model)
        if len(product_model) == 1: # 1个型号的缓冲期
            model = next(iter_product_model)
            buffer['product_model'] = model
            buffer['batch_no'] = product_model[model][1:]
        elif len(product_model) == 2: # 2个型号的缓冲期，用括号区分
            model_1 = next(iter_product_model)
            model_2 = next(iter_product_model)
            buffer['product_model'] = f"{model_1} ({model_2})"
            buffer['batch_no'] = f"{product_model[model_1][1:]} ({product_model[model_2][1:]})"
        else:
            pass
        self.__supplier['buffer'] = buffer 

    @property
    def report_data(self):
        self.__report_data["supplier"] = self.__supplier
        return self.__report_data
    
    @classmethod
    def get_datestr(cls, original_date:date,type:str="")->str:
        """将日期类型转换为需要的输出格式"""
        dateobj = datetime.strptime(original_date, "%Y-%m-%d")
        if type=="C":
            return f"{dateobj.year}年{dateobj.month}月{dateobj.day}日"
        else:
            return f"{dateobj.year}.{dateobj.month}.{dateobj.day}"