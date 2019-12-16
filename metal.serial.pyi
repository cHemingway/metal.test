

from enum import Enum
class endianess_t(Enum):
    big = "big"
    little = "little"

class session:
    def endianess(self) -> endianess_t: ...
    def get_str   (self) -> str: ...
    def get_raw   (self) -> bytearray: ...
    def get_int   (self) -> int: ...
    def get_uint  (self) -> int: ...
    def get_uint8 (self) -> int: ...
    def get_int8  (self) -> int: ...
    def get_char  (self) -> int: ...
    def get_uint16(self) -> int: ...
    def get_int16 (self) -> int: ...
    def get_uint32(self) -> int: ...
    def get_int32 (self) -> int: ...
    def get_uint64(self) -> int: ...
    def get_int64 (self) -> int: ...
    def get_bool  (self) -> bool: ...
    def get_ptr   (self) -> int: ...
    def set_exit  (self) -> None: ...

class argument_parser_t:
    def add_argument(self, key: str, **kwargs) -> None : ...

argument_parser: argument_parser_t

def metal_serial_plugin(object): ...
