from .crud_supplier_board import (create_smart_board, 
                                 create_lvct_board, 
                                 delete_smart_board_on_days,
                                 delete_lvct_board_on_days,
                                 get_smart_boards,
                                 get_lvct_boards,
                                 delete_smart_board,
                                 delete_lvct_board)
from .crud_supplier_ropehead import (get_rope_head,
                                     create_rope_head,
                                     delete_rope_head,
                                     delete_rope_head_on_days)
from .crud_supplier_autorescue import (get_auto_rescue,
                                       create_auto_rescue,
                                       delete_auto_rescue,
                                       delete_auto_rescue_on_days)
from .crud_supplier_icard import (get_ic_card,
                                  create_ic_card,
                                  delete_ic_card,
                                  delete_ic_card_on_days)
from .crud_supplier_safe_brake import (get_safe_brake, 
                                       create_safe_brake, 
                                       delete_safe_brake, 
                                       delete_safe_brake_on_days)
from .crud_supplier_speedlimiter import (get_speed_limiters,
                                         create_speed_limiter,
                                         create_speed_limiters,
                                         delete_speed_limiter,
                                         delete_speed_limiter_on_days)
from .crud_supplier_buffer import (get_buffers,
                                    create_buffer,
                                    create_buffers,
                                    delete_buffer,
                                    delete_buffer_on_days)
from .crud_supplier_brake_machine import (get_brake_machines,
                                    create_brake_machine,
                                    create_brake_machines,
                                    delete_brake_machine,
                                    delete_brake_machine_on_days)
from .crud_supplier_traction_machine import (get_traction_machines,
                                    create_traction_machine,
                                    create_traction_machines,
                                    delete_traction_machine,
                                    delete_traction_machine_on_days)
from .crud_supplier_safety_machine import (get_safety_machines,
                                    create_safety_machine,
                                    create_safety_machines,
                                    delete_safety_machine,
                                    delete_safety_machine_on_days)
from .crud_supplier_wire_rope import (get_wire_ropes,
                                    create_wire_rope,
                                    create_wire_ropes,
                                    delete_wire_rope,
                                    delete_wire_rope_on_days)
from .crud_supplier_doorsystem import (get_door_systems,
                                    create_door_system,
                                    create_door_systems,
                                    delete_door_system,
                                    delete_door_system_on_days)
from .crud_supplier_controlcabinet import (get_control_cabinets,
                                    create_control_cabinet,
                                    create_control_cabinets,
                                    delete_control_cabinet,
                                    delete_control_cabinet_on_days)