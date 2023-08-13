# Import all the models, so that Base has them before being
# imported by Alembic
from db.base_class import Base  # noqa
from models.supplier import SupplierSmartBoard  # noqa
from models.supplier import SupplierLvctBoard  # noqa
from models.supplier import SupplierRopeHead  # noqa
from models.supplier import SupplierAutoRescue
from models.supplier import SupplierIcCard
from models.supplier import SupplierSafeBrake
from models.supplier import SupplierSpeedLimiter
from models.supplier import SupplierBuffer