import uuid

from sqlalchemy import (Column, 
                        ForeignKey, 
                        BigInteger, 
                        String, 
                        Date, 
                        DateTime, 
                        Integer,
                        Float,
                        text)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.base_class import Base

def generate_uuid():
    return str(uuid.uuid4())



class SupplierSmartBoard(Base):
    __tablename__ = 'supplier_smart_board'
    __table_args__ = {'comment': '（含有电子元件的安全电路）SMART主板'}

    smartb_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String, 
                         comment='合同号')
    dept_name = Column(String(100), 
                     comment='制造单位名称')
    smartb_model = Column(String(100), 
                          comment='产品型号')
    smartb_manufacture_batch_no = Column(String(100), 
                                         comment='制造批次号')
    smartb_type_testing_cert_no = Column(String(100), 
                                         comment='型式试验证书编号')
    smartb_manufacture_date = Column(Date, 
                                     comment='制造日期')
    user_id = Column(BigInteger, 
                     comment='操作用户id')
    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    remark = Column(String(100), nullable=True,
                    comment='备注')
    
class SupplierLvctBoard(Base):
    __tablename__ = 'supplier_lvct_board'
    __table_args__ = {'comment': '(含有电子元件的安全电路)LVCT1板'}

    lvctb_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String, 
                         comment='合同号')
    dept_name = Column(String(100), 
                     comment='制造单位名称')
    lvct_model = Column(String(100), 
                          comment='产品型号')
    lvct_manufacture_batch_no = Column(String(100), 
                                       comment='制造批次号')
    lvct_type_testing_cert_no = Column(String(100), 
                                       comment='型式试验证书编号')
    lvct_manufacture_date = Column(Date, 
                                     comment='制造日期')
    user_id = Column(BigInteger, 
                     comment='操作用户id')
    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    remark = Column(String(100), 
                    comment='备注')

class SupplierRopeHead(Base):
    __tablename__ = 'supplier_rope_head'
    __table_args__ = {'comment': '绳头组合'}

    rope_head_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String, 
                         comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    ropehc_name = Column(String(100), comment='设备品种')
    ropehc_model = Column(String(100), comment='产品型号')
    ropehc_manufacture_batch_no = Column(String(100), comment='制造批次号')
    ropehc_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    ropehc_manufacture_date = Column(Date, comment='制造日期')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    remark = Column(String(100), comment='备注')

class SupplierAutoRescue(Base):
    __tablename__ = 'supplier_auto_rescue'
    __table_args__ = {'comment': 'ARED 自动救援操作装置'}

    auto_rescue_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String, 
                         comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    auto_rescue_model = Column(String(100), comment='型号')
    auto_rescue_no = Column(String(100), comment='编号')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    remark = Column(String(100), comment='备注')

class SupplierIcCard(Base):
    __tablename__ = 'supplier_ic_card'
    __table_args__ = {'comment': 'IC卡'}

    icard_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String, 
                         comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    icard_model = Column(String(100), comment='IC卡型号')
    icard_no = Column(String(100), comment='IC卡编号')
    user_id = Column(BigInteger, comment='操作用户ID')
    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    remark = Column(String(100), comment='备注')

class SupplierSafeBrake(Base):
    __tablename__ = 'supplier_safe_brake'
    __table_args__ = {'comment': '安全钳'}

    safe_brake_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String, 
                         comment='合同号')
    user_name = Column(String(100), comment='用户名称') 
    dept_name = Column(String(100), comment='制造单位')
    product_type_name = Column(String(100), comment='设备品种名称')
    product_model = Column(String(100), comment='型号')
    product_speed = Column(Float, comment='速度m/s')
    product_no = Column(String(100), comment='编号')
    product_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    manufacture_date = Column(Date, comment='制造日期')
    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    user_id = Column(BigInteger, comment='操作用户ID')
    remark = Column(String(100), comment='备注')

class SupplierSpeedLimiter(Base):
    __tablename__ = 'supplier_speed_limiter'
    __table_args__ = {'comment': '限速器'}

    speed_limiter_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    
    contract_no = Column(String, 
                         comment='合同号')
    project_name = Column(String(100), comment='项目名称') 
    dept_name = Column(String(100), comment='制造单位')
    product_type_name = Column(String(100), comment='设备品种名称')
    product_model = Column(String(100), comment='型号')
    product_speed = Column(Float, comment='速度m/s')
    product_no = Column(String(100), comment='编号')
    product_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    manufacture_date = Column(Date, comment='制造日期')

    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    user_id = Column(BigInteger, comment='操作用户ID')
    data_state = Column(String(10), comment='数据的状态') 
    remark = Column(String(100), comment='备注')

class SupplierBuffer(Base):
    __tablename__ = 'supplier_buffer'
    __table_args__ = {'comment': '缓冲器'}

    buffer_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    
    contract_no = Column(String, 
                         comment='合同号')
    project_name = Column(String(100), comment='项目名称') 
    dept_name = Column(String(100), comment='制造单位')
    product_type_name = Column(String(100), comment='设备品种名称')
    product_model = Column(String(100), comment='型号')
    product_speed = Column(String(10), comment='速度m/s')
    product_no = Column(String(100), comment='编号')
    product_batch_no = Column(String(100), comment='产品批次号') 
    product_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    manufacture_date = Column(Date, comment='制造日期')

    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    user_id = Column(BigInteger, comment='操作用户ID')
    data_state = Column(String(10), comment='数据的状态') 
    remark = Column(String(100), comment='备注')

class SupplierTractionMachine(Base):
    __tablename__ = 'supplier_traction_machine'
    __table_args__ = {'comment': '驱动主机'}

    traction_machine_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    
    contract_no = Column(String,comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    product_type_name = Column(String(100), comment='设备品种名称')
    product_model = Column(String(100), comment='型号')
    product_no = Column(String(100), comment='编号')
    product_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    manufacture_date = Column(Date, comment='制造日期')

    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    user_id = Column(BigInteger, comment='操作用户ID')
    data_state = Column(String(10), comment='数据的状态') 
    remark = Column(String(100), comment='备注')    

class SupplierBrakeMachine(Base):
    __tablename__ = 'supplier_brake_machine'
    __table_args__ = {'comment': '制动器'}

    brake_machine_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    
    contract_no = Column(String,comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    product_type_name = Column(String(100), comment='设备品种名称')
    product_model = Column(String(100), comment='型号')
    product_no = Column(String(100), comment='编号')
    product_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    manufacture_date = Column(Date, comment='制造日期')

    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    user_id = Column(BigInteger, comment='操作用户ID')
    data_state = Column(String(10), comment='数据的状态') 
    remark = Column(String(100), comment='备注')  

class SupplierSafetyMachine(Base):
    __tablename__ = 'supplier_safety_machine'
    __table_args__ = {'comment': '轿厢保护装置'}

    safety_machine_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    
    contract_no = Column(String,comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    product_type_name = Column(String(100), comment='设备品种名称')
    product_model = Column(String(100), comment='型号')
    product_no = Column(String(100), comment='编号')
    product_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    manufacture_date = Column(Date, comment='制造日期')

    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    user_id = Column(BigInteger, comment='操作用户ID')
    data_state = Column(String(10), comment='数据的状态') 
    remark = Column(String(100), comment='备注')  

class SupplierWireRope(Base):
    __tablename__ = 'supplier_wire_rope'
    __table_args__ = {'comment': '钢丝绳'}

    wire_rope_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    
    wr_contract_no = Column(String,comment='合同号')
    wr_product_name = Column(String(50), comment='产品名称')
    wr_dept_name = Column(String(50), comment='制造单位')
    wr_product_testing_cert = Column(String(50), comment='检测报告')
    wr_product_model = Column(String(50), comment='规格')
    wr_product_matric = Column(String(10), comment='度量')
    wr_product_value = Column(Float, comment='数值')
    wr_product_num = Column(Integer, comment='根数')

    create_time = Column(DateTime, 
                         nullable=False, 
                         comment='创建时间')
    update_time = Column(DateTime, 
                         nullable=False, 
                         comment='更新时间')
    user_id = Column(BigInteger, comment='操作用户ID')
    data_state = Column(String(10), comment='数据的状态') 
    remark = Column(String(100), comment='备注') 


class ModelSupplierMenXiTong(Base):
    __tablename__ = 'supplier_门系统'
    __table_args__ = {'comment': '门系统'}

    door_system_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String(100), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    model = Column(String(100), comment='型号')
    batch_no = Column(String(100), comment='编号')
    type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    manufacture_date = Column(Date, comment='制造日期')
    user_id = Column(String(64), comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='层门,防火门,玻璃轿门,玻璃轿壁，厅门锁，轿门锁')
    status = Column(String(255))
    type_name = Column(String(255), comment='设备品种') 
    data_state = Column(String(10), comment='数据的状态') 

class ModelSupplierKongZhiGui(Base):
    __tablename__ = 'supplier_控制柜'
    __table_args__ = {'comment': '控制柜'}

    control_cabinet_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String(100), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    model = Column(String(100), comment='型号')
    batch_no = Column(String(100), comment='编号')
    type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    manufacture_date = Column(Date, comment='制造日期')
    user_id = Column(String(64), comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注') 
    status = Column(String(255))
    type_name = Column(String(255), comment='设备品种') 
    data_state = Column(String(10), comment='数据的状态') 