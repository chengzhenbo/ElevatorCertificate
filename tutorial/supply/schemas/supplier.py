from enum import Enum

class DataState(str,Enum):
    """数据在提交但未处理前可直接删除，在数据状态大于1之后的删除不再删除数据，
       而是将数据的状态修改为deleted
    """
    Submited = "submitted"    # 供应商提交数据，总公司还未打印数据
    Completed = "completed"  # 总公司已经打印了该数据
    Updated = "updated"      # 已经打印的数据，发生了修改（TODO：可以考虑记录修改痕迹）
    Deleted = "deleted"      # 删除已经打印的数据