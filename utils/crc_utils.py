from crc import Calculator, Crc16
from dump.protocol import Protocol

proto = Protocol()


calc = Calculator(Crc16.XMODEM, optimized=True)


def command_frame(header:int, command:int, reg:int, data:list[int]) -> bytes:
    print(reg)
    data_len = len(data)
    frame_len = data_len + 6
    frame  = bytes([header]) + bytes([frame_len])+ bytes([command]) + bytes([reg]) + bytes(data)
    crc16_val = calc.checksum(frame)
    crc_bytes = bytes([crc16_val >> 8, crc16_val & 0xFF])
    frame = frame + crc_bytes
    return frame