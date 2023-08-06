import uuid

from sqlalchemy import (Column, 
                        ForeignKey, 
                        BigInteger, 
                        String, 
                        Date, 
                        DateTime, 
                        Identity,
                        text)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.base_class import Base

def generate_uuid():
    return str(uuid.uuid4())

class SupplierSmartBoardModel(Base):
    __tablename__ = 'supplier_smart_board'
    __table_args__ = {'comment': '（含有电子元件的安全电路）SMART主板'}

    smartb_id = Column(String, primary_key=True, default=generate_uuid, index=True, 
                        comment='ID号')
    contract_no = Column(String, 
                         comment='合同号')
    dept_id = Column(BigInteger, 
                     comment='制造单位ID')
    smartb_model = Column(String(100), 
                          comment='产品型号')
    smartb_manufacture_batch_no = Column(String(100), 
                                         comment='制造批次号')
    smartb_type_testing_cert_no = Column(String(100), 
                                         comment='型式试验证书编号')
    smartb_manufacture_date = Column(Date, 
                                     comment='制造日期')
    # user_id = Column(BigInteger, 
    #                  comment='操作用户id')
    create_time = Column(DateTime(timezone=True), 
                         server_default=func.now(), 
                         comment='创建时间')
    update_time = Column(DateTime(timezone=True), 
                         onupdate=func.now(), 
                         comment='更新时间')
    remark = Column(String(100), nullable=True,
                    comment='备注')

