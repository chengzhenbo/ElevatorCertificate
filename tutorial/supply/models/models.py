from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, ForeignKey, Identity, Integer, SmallInteger, String, text
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class SysBasicInfoMachine客梯整机基本信息(Base):
    __tablename__ = 'Sys_BasicInfoMachine客梯整机基本信息'
    __table_args__ = {'comment': '客梯整机基本信息'}

    id = Column(BigInteger, primary_key=True, comment='电梯类型')
    elevatorType = Column(String(100), nullable=False, comment='电梯类型')
    elevatorCategory = Column(String(100), comment='设备类别')
    elevatorVariety = Column(String(100), comment='设备品种')
    elevatorModel = Column(String(100), comment='产品型号')
    elevatorName = Column(String(100), comment='产品名称')
    elevatorCode = Column(String(50), comment='设备代码')
    control_model = Column(String(100), comment='控制柜型号')
    move_protect_model = Column(String(100), comment='轿厢意外移动保护装置型号')
    move_protect_code = Column(String(100), comment='轿厢意外移动保护装置编号')
    safety_circuits_model = Column(String(100), comment='含有电子元件的安全电路型号（提前开门及再平层模块）')


class SysFileManage(Base):
    __tablename__ = 'Sys_FileManage'
    __table_args__ = {'comment': '证书文件管理'}

    file_id = Column(BigInteger, primary_key=True)
    filename = Column(String(100), comment='文件名')
    filelabel = Column(String(100), comment='文件别称')
    fileurl = Column(String(100), comment='保存路径')
    uploadtime = Column(DateTime(True), server_default=text('now()'), comment='上传时间')
    user_id = Column(BigInteger, comment='用户id')
    file_type = Column(String(100), comment='文件类型 （型式试验证书，合格证书等）')


class SysGateTypeCompare门系统对照表(Base):
    __tablename__ = 'Sys_GateTypeCompare门系统对照表'
    __table_args__ = {'comment': '门系统对照表'}

    id = Column(BigInteger, primary_key=True)
    sysType = Column(String(100))
    toDoorType = Column(String(100))
    toLockType = Column(String(100))


class SysTypeTestCert(Base):
    __tablename__ = 'Sys_TypeTestCert'
    __table_args__ = {'comment': '型试式验报告证书录入登记表'}

    id = Column(BigInteger, primary_key=True)
    supplier = Column(String(100))
    lang = Column(String(100))
    report_category = Column(String(100))
    product_name = Column(String(100))
    product_model = Column(String(100))
    report_no = Column(String(100))
    cert_no = Column(String(100))
    cert_expire_time = Column(Date)
    remark = Column(String(100))
    cert_auth = Column(String(100))
    status = Column(String(100))


class ReadinOcpLablejgEcode(Base):
    __tablename__ = 'readin_ocp_lablejg_ecode'
    __table_args__ = {'comment': '同步过来的ocp_lablejg_ecode表'}

    id = Column(BigInteger, primary_key=True)
    contract_no = Column(String(255), nullable=False, unique=True)
    device_ecode = Column(String(255))
    status = Column(SmallInteger)
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))


class ReadinVFocus发货通知单视图(Base):
    __tablename__ = 'readin_v_focus_发货通知单视图'
    __table_args__ = {'comment': '同步过来的 v_focus_发货通知单视图表'}

    id = Column(BigInteger, primary_key=True)
    合同编号 = Column(String(255), nullable=False, unique=True)
    发货工厂 = Column(String(255))
    订单单据类型 = Column(String(255))
    梯型 = Column(String(255))
    梯型分类 = Column(String(255))
    项目名称 = Column(String(255))
    预计发货时间 = Column(TIMESTAMP(True, 6))
    制单人 = Column(String(255))
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))


class ReadinVFocus销售订单合格证(Base):
    __tablename__ = 'readin_v_focus_销售订单_合格证'
    __table_args__ = {'comment': '同步过来的v_focus_销售订单_合格证'}

    id = Column(BigInteger, primary_key=True)
    合同编号 = Column(String(255), unique=True)
    大区 = Column(String(255))
    小区 = Column(String(255))
    办事处 = Column(String(255))
    设备性质 = Column(String(255))
    实际客户 = Column(String(255))
    是否跨区 = Column(String(255))
    被跨大区 = Column(String(255))
    被跨分公司 = Column(String(255))
    被跨办事处 = Column(String(255))
    被跨区销售员 = Column(String(255))
    市场细分 = Column(String(255))
    品牌 = Column(String(255))
    FENTRYID = Column(String(255))
    最后修改日期 = Column(DateTime(True))
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))


class Readin合格证参数中间表(Base):
    __tablename__ = 'readin_合格证参数中间表'
    __table_args__ = {'comment': '同步过来的合格证参数中间表'}

    id = Column(BigInteger, primary_key=True)
    合同号 = Column(String(255), nullable=False)
    合同编号 = Column(String(255), unique=True)
    项目名称 = Column(String(255))
    到站港 = Column(String(255))
    电梯型号 = Column(String(255))
    载重 = Column(String(255))
    速度 = Column(String(255))
    层数 = Column(String(255))
    站数 = Column(String(255))
    门数 = Column(String(255))
    单双通 = Column(String(255))
    控制方式 = Column(String(255))
    提升高度 = Column(String(255))
    轿厢净高 = Column(String(255))
    轿厢净宽 = Column(String(255))
    轿厢净深 = Column(String(255))
    轿厢外宽 = Column(String(255))
    轿厢外深 = Column(String(255))
    净开门高 = Column(String(255))
    净开门宽 = Column(String(255))
    开门方式 = Column(String(255))
    门机型号 = Column(String(255))
    门系统类型 = Column(String(255))
    轿厢导轨型号 = Column(String(255))
    对重导轨型号 = Column(String(255))
    对重安全钳 = Column(String(255))
    停电应急疏散装置 = Column(String(255))
    厅外IC卡装置类型 = Column(String(255))
    安全钳型号 = Column(String(255))
    轿厢自重 = Column(String(255))
    控制板 = Column(String(255))
    曳引比 = Column(String(255))
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))


class SysDept(Base):
    __tablename__ = 'sys_dept'
    __table_args__ = {'comment': '单位表 '}

    dept_id = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    parent_role_id = Column(BigInteger, nullable=False)
    dept_name = Column(String(100))
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))
    remark = Column(String(100))
    product_type_ids = Column(String(100), server_default=text('0'))
    is_enable = Column(Boolean, server_default=text('true'))


class SysDeptPtypeMapping(Base):
    __tablename__ = 'sys_dept_ptype_mapping'
    __table_args__ = {'comment': '单位 与 生产部件类型 关系表'}

    id = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    dept_id = Column(BigInteger)
    ptype_id = Column(BigInteger)


class SysElevatorCert合格证排班表(Base):
    __tablename__ = 'sys_elevator_cert_合格证排班表'

    id = Column(BigInteger, primary_key=True)
    contract_no = Column(String(255), unique=True)
    w_check_opeartor_id = Column(BigInteger)
    w_is_checked = Column(Boolean)
    w_affiliates_printer_id = Column(BigInteger)
    w_number_copies = Column(String(255))
    w_is_printed = Column(Boolean)
    w_is_mailed = Column(Boolean)
    w_mail_staff = Column(String(255))
    w_mail_date = Column(Date)
    w_mail_no = Column(String(255))
    w_mail_address = Column(String(255))
    w_special_remark = Column(String(255))
    w_control_mode = Column(String(255))
    w_serial_no = Column(String(255))
    w_sfactory_no = Column(String(255))
    w_sequipment_code = Column(String(255))
    install_special_equip_license_no = Column(String(255))
    install_unit = Column(String(255))
    install_address = Column(String(255))
    install_date = Column(Date)
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))

    readin_hetonginfo = relationship('ReadinHetonginfo', uselist=False, back_populates='sys_elevator_cert_合格证排班表')
    supplier_ared自动救援操作装置 = relationship('SupplierAred自动救援操作装置', back_populates='sys_elevator_cert_合格证排班表')
    supplier_buffer缓冲器 = relationship('SupplierBuffer缓冲器', back_populates='sys_elevator_cert_合格证排班表')
    supplier_ic_card = relationship('SupplierIcCard', back_populates='sys_elevator_cert_合格证排班表')
    supplier_lvct1_board = relationship('SupplierLvct1Board', back_populates='sys_elevator_cert_合格证排班表')
    supplier_smart_board = relationship('SupplierSmartBoard', back_populates='sys_elevator_cert_合格证排班表')
    supplier_主机 = relationship('Supplier主机', back_populates='sys_elevator_cert_合格证排班表')
    supplier_厅门锁 = relationship('Supplier厅门锁', back_populates='sys_elevator_cert_合格证排班表')
    supplier_安全钳 = relationship('Supplier安全钳', back_populates='sys_elevator_cert_合格证排班表')
    supplier_层门装置 = relationship('Supplier层门装置', back_populates='sys_elevator_cert_合格证排班表')
    supplier_控制柜 = relationship('Supplier控制柜', back_populates='sys_elevator_cert_合格证排班表')
    supplier_玻璃轿壁 = relationship('Supplier玻璃轿壁', back_populates='sys_elevator_cert_合格证排班表')
    supplier_玻璃轿门 = relationship('Supplier玻璃轿门', back_populates='sys_elevator_cert_合格证排班表')
    supplier_绳头组合 = relationship('Supplier绳头组合', back_populates='sys_elevator_cert_合格证排班表')
    supplier_能量回馈装置 = relationship('Supplier能量回馈装置', back_populates='sys_elevator_cert_合格证排班表')
    supplier_轿厢上行超速保护装置 = relationship('Supplier轿厢上行超速保护装置', back_populates='sys_elevator_cert_合格证排班表')
    supplier_轿厢意外移动保护装置 = relationship('Supplier轿厢意外移动保护装置', back_populates='sys_elevator_cert_合格证排班表')
    supplier_轿门锁 = relationship('Supplier轿门锁', back_populates='sys_elevator_cert_合格证排班表')
    supplier_钢丝绳 = relationship('Supplier钢丝绳', back_populates='sys_elevator_cert_合格证排班表')
    supplier_防火门装置 = relationship('Supplier防火门装置', back_populates='sys_elevator_cert_合格证排班表')
    supplier_限速器 = relationship('Supplier限速器', back_populates='sys_elevator_cert_合格证排班表')


class SysProductType(Base):
    __tablename__ = 'sys_product_type'
    __table_args__ = {'comment': '生产部件类型表'}

    pt_id = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    pt_name = Column(String(100), comment='产品类型名称 IC卡 安全钳等')
    pt_code = Column(String(100), comment='产品类型代码 IC卡=iccard  安全钳=safegear等')


class SysRole(Base):
    __tablename__ = 'sys_role'
    __table_args__ = {'comment': '角色表'}

    role_id = Column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    role_name = Column(String(50))
    role_code = Column(String(50))
    is_enable = Column(Boolean, server_default=text('true'))
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))
    sort = Column(Integer)
    remark = Column(String(100))


class SysUser(Base):
    __tablename__ = 'sys_user'
    __table_args__ = {'comment': '用户表'}

    user_id = Column(BigInteger, primary_key=True)
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    is_delete = Column(Boolean, server_default=text('false'), comment='是否删除')
    username = Column(String(100))
    password = Column(String(100))
    remark = Column(String(100), comment='备注')
    department_id = Column(BigInteger, server_default=text('0'), comment='部门')
    phone = Column(String(11), comment='手机')
    is_active = Column(Boolean, server_default=text('true'), comment='是否启用')
    true_name = Column(String(100))
    role_id = Column(BigInteger)


class ReadinHetonginfo(Base):
    __tablename__ = 'readin_hetonginfo'
    __table_args__ = {'comment': '同步过来的hetonginfo表'}

    id = Column(BigInteger, primary_key=True)
    合同编号 = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), unique=True)
    销售员 = Column(String(255))
    大区 = Column(String(255))
    分公司 = Column(String(255))
    合同总号 = Column(String(255))
    梯型 = Column(String(255))
    代理商 = Column(String(255))
    合同类别 = Column(String(255))
    项目地 = Column(String(255))
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='readin_hetonginfo')


class SupplierAred自动救援操作装置(Base):
    __tablename__ = 'supplier_ared自动救援操作装置'
    __table_args__ = {'comment': 'ARED 自动救援操作装置'}

    ared_id = Column(BigInteger, primary_key=True, comment='id号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    ared_model = Column(String(100), comment='型号')
    ared_no = Column(String(100), comment='编号')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_ared自动救援操作装置')


class SupplierBuffer缓冲器(Base):
    __tablename__ = 'supplier_buffer缓冲器'
    __table_args__ = {'comment': '缓冲器'}

    buffer_id = Column(BigInteger, primary_key=True, comment='id号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    buffer_product_type_name = Column(String(100), comment='设备品种名称')
    buffer_model = Column(String(100), comment='型号')
    buffer_no = Column(String(100), comment='编号')
    buffer_speed = Column(String(100), comment='速度')
    buffer_manufacture_batch_no = Column(String(100), comment='制造批次号')
    buffer_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    buffer_manufacture_date = Column(Date, comment='制造日期')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_buffer缓冲器')


class SupplierIcCard(Base):
    __tablename__ = 'supplier_ic_card'
    __table_args__ = {'comment': 'IC卡'}

    ic_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户ID')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    ic_model = Column(String(100), comment='IC卡型号')
    ic_no = Column(String(100), comment='IC卡编号')
    hegezs_id = Column(BigInteger, comment='合格证证书文件id')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_ic_card')


class SupplierLvct1Board(Base):
    __tablename__ = 'supplier_lvct1_board'
    __table_args__ = {'comment': '(含有电子元件的安全电路)LVCT1板'}

    lvct_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    lvct_model = Column(String(100), comment='产品型号')
    lvct_manufacture_batch_no = Column(String(100), comment='制造批次号')
    lvct_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    lvct_manufacture_date = Column(String(100), comment='制造日期')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_lvct1_board')


class SupplierSmartBoard(Base):
    __tablename__ = 'supplier_smart_board'
    __table_args__ = {'comment': '（含有电子元件的安全电路）SMART主板'}

    smartb_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    smartb_model = Column(String(100), comment='产品型号')
    smartb_manufacture_batch_no = Column(String(100), comment='制造批次号')
    smartb_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    smartb_manufacture_date = Column(Date, comment='制造日期')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_smart_board')


class Supplier主机(Base):
    __tablename__ = 'supplier_主机'
    __table_args__ = {'comment': '主机'}

    dc_id = Column(BigInteger, primary_key=True, comment='ID号')
    dept_name = Column(String(100), comment='制造单位')
    product_type_name = Column(String(100), comment='设备品种名称')
    dc_model = Column(String(100), comment='型号')
    dc_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    dc_manufacture_date = Column(Date, comment='制造日期')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    user_id = Column(BigInteger, comment='操作用户ID')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    dc_no = Column(String(100), comment='编号')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_主机')


class Supplier厅门锁(Base):
    __tablename__ = 'supplier_厅门锁'
    __table_args__ = {'comment': '厅门锁'}

    hdl_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    hdl_product_type_name = Column(String(100), comment='产品名称 ')
    hdl_model = Column(String(100), comment='产品型号')
    hdl_manufacture_batch_no = Column(String(100), comment='制造批次号')
    hdl_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    hdl_manufacture_date = Column(Date, comment='制造日期')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_厅门锁')


class Supplier安全钳(Base):
    __tablename__ = 'supplier_安全钳'
    __table_args__ = {'comment': '安全钳'}

    safec_id = Column(BigInteger, primary_key=True, comment='ID')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='用户ID')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    safec_product_type_name = Column(String(100), comment='设备品种名称')
    safec_model = Column(String(100), comment='型号')
    safec_speed = Column(String(100), comment='速度m/s')
    safec_no1 = Column(String(100), comment='编号1')
    safec_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    safec_manufacture_date = Column(Date, comment='制造日期')
    safec_no2 = Column(String(100), comment='编号2')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_安全钳')


class Supplier层门装置(Base):
    __tablename__ = 'supplier_层门装置'
    __table_args__ = {'comment': '层门装置'}

    floord_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='添加时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    floord_product_type_name = Column(String(100), comment='产品类型名称')
    floord_model = Column(String(100), comment='型号')
    floord_manufacture_batch_no = Column(String(100), comment='制造批次号')
    floord_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    floord_manufacture_date = Column(Date, comment='制造日期')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_层门装置')


class Supplier控制柜(Base):
    __tablename__ = 'supplier_控制柜'
    __table_args__ = {'comment': '控制柜'}

    cb_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    cb_model = Column(String(100), comment='型号')
    cb_manufacture_batch_no = Column(String(100), comment='制造批次号')
    cb_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    cb_manufacture_date = Column(Date, comment='制造日期')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_控制柜')


class Supplier玻璃轿壁(Base):
    __tablename__ = 'supplier_玻璃轿壁'
    __table_args__ = {'comment': '玻璃轿壁'}

    glassw_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户ID号')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    glassw_product_type_name = Column(String(100), comment='产品名称 ')
    glassw_model = Column(String(100), comment='产品型号')
    glassw_manufacture_batch_no = Column(String(100), comment='制造批次号')
    glassw_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    glassw_manufacture_date = Column(Date, comment='制造日期')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_玻璃轿壁')


class Supplier玻璃轿门(Base):
    __tablename__ = 'supplier_玻璃轿门'
    __table_args__ = {'comment': '玻璃轿门'}

    glassd_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    glassd_product_type_name = Column(String(100), comment='产品类型名称')
    glassd_model = Column(String(100), comment='产品型号')
    glassd_manufacture_batch_no = Column(String(100), comment='制造批次号')
    glassd_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    glassd_manufacture_date = Column(Date, comment='制造日期')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_玻璃轿门')


class Supplier绳头组合(Base):
    __tablename__ = 'supplier_绳头组合'
    __table_args__ = {'comment': '绳头组合'}

    ropehc_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    ropehc_model = Column(String(100), comment='产品型号')
    ropehc_manufacture_batch_no = Column(String(100), comment='制造批次号')
    ropehc_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    ropehc_manufacture_date = Column(Date, comment='制造日期')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_绳头组合')


class Supplier能量回馈装置(Base):
    __tablename__ = 'supplier_能量回馈装置'
    __table_args__ = {'comment': '能量回馈装置'}

    enfb_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    enfb_model = Column(String(100), comment='型号')
    enfb_no = Column(String(100), comment='编号')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_能量回馈装置')


class Supplier轿厢上行超速保护装置(Base):
    __tablename__ = 'supplier_轿厢上行超速保护装置'
    __table_args__ = {'comment': '轿厢上行超速保护装置cabin_upward_overspeed_protection'}

    cabinuop_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位名称')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    cabinuop_product_type_name = Column(String(100), comment='设备品种名称')
    cabinuop_model = Column(String(100), comment='型号')
    cabinuop_no1 = Column(String(100), comment='编号1')
    cabinuop_no2 = Column(String(100), comment='编号2')
    cabinuop_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    cabinuop_manufacture_date = Column(Date, comment='制造日期')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_轿厢上行超速保护装置')


class Supplier轿厢意外移动保护装置(Base):
    __tablename__ = 'supplier_轿厢意外移动保护装置'
    __table_args__ = {'comment': '轿厢意外移动保护装置cabin_unintended_movement_protection'}

    cabinump_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    cabinump_product_type_name = Column(String(100), comment='设备品种名称')
    cabinump_model = Column(String(100), comment='型号')
    cabinump_no1 = Column(String(100), comment='编号1')
    cabinump_no2 = Column(String(100), comment='编号2')
    cabinump_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    cabinump_manufacture_date = Column(Date, comment='制造日期')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    user_id_ = Column('user_id ', BigInteger, comment='操作用户id')
    remark = Column(String(100), comment='备注')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_轿厢意外移动保护装置')


class Supplier轿门锁(Base):
    __tablename__ = 'supplier_轿门锁'
    __table_args__ = {'comment': '轿门锁'}

    cdl_id = Column(BigInteger, primary_key=True)
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'))
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger)
    create_time = Column(DateTime(True), server_default=text('now()'))
    update_time = Column(DateTime(True), server_default=text('now()'))
    remark = Column(String(100))
    cdl_product_type_name = Column(String(100))
    cdl_model = Column(String(100))
    cdl_manufacture_batch_no = Column(String(100))
    cdl_type_testing_cert_no = Column(String(100))
    cdl_manufacture_date = Column(Date)

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_轿门锁')


class Supplier钢丝绳(Base):
    __tablename__ = 'supplier_钢丝绳'
    __table_args__ = {'comment': '钢丝绳'}

    steelwr_id = Column(BigInteger, primary_key=True, comment='钢丝绳id')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), nullable=False, comment='合同号')
    suspension_device_name = Column(String(100), comment='悬挂装置名称')
    dept_name = Column(String(100), comment='制造单位')
    steelwr_specifications_model_name = Column(String(100), comment='钢丝绳规格/钢带型号，名称 跟证书名称要一致')
    steelwr_specifications_model_value = Column(String(100), comment='规格型号值')
    steelwr_diameter_specifications_name = Column(String(100), comment='直径/产品规格名称')
    steelwr_diameter_specifications_value = Column(String(100), comment='钢丝绳直径/钢带规格值')
    steelwr_num = Column(Integer, comment='数量')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String, comment='备注')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_钢丝绳')


class Supplier防火门装置(Base):
    __tablename__ = 'supplier_防火门装置'
    __table_args__ = {'comment': '防火门装置'}

    fired_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户id')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    fired_product_type_name = Column(String(100), comment='设备品种名称')
    fired_model = Column(String(100), comment='产品型号')
    fired_manufacture_batch_no = Column(String(100), comment='制造批次号')
    fired_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    fired_manufacture_date = Column(Date, comment='制造日期')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_防火门装置')


class Supplier限速器(Base):
    __tablename__ = 'supplier_限速器'
    __table_args__ = {'comment': '限速器'}

    sl_id = Column(BigInteger, primary_key=True, comment='ID号')
    contract_no = Column(ForeignKey('sys_elevator_cert_合格证排班表.contract_no'), comment='合同号')
    dept_name = Column(String(100), comment='制造单位')
    user_id = Column(BigInteger, comment='操作用户ID')
    create_time = Column(DateTime(True), server_default=text('now()'), comment='创建时间')
    update_time = Column(DateTime(True), server_default=text('now()'), comment='更新时间')
    remark = Column(String(100), comment='备注')
    sl_product_type_name = Column(String(100), comment='产品品种名称')
    sl_model = Column(String(100), comment='型号')
    sl_no = Column(String(100), comment='编号')
    sl_speed = Column(String(100), comment='速度')
    sl_type_testing_cert_no = Column(String(100), comment='型式试验证书编号')
    sl_manufacture_date = Column(Date, comment='制造日期')

    sys_elevator_cert_合格证排班表 = relationship('SysElevatorCert合格证排班表', back_populates='supplier_限速器')
