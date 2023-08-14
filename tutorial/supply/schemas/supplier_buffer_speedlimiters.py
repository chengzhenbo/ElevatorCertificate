from typing import List

from pydantic import BaseModel

from schemas.supplier_buffer import BufferInDBBase
from schemas.supplier_speed_limiter import SpeedLimiterInDBBase

class Buffer_Speedlimiters(BaseModel):
    buffers: List[BufferInDBBase]
    speed_limiters: List[SpeedLimiterInDBBase]