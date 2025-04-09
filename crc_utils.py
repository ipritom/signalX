from crc import Calculator, Crc16
from protocol import Protocol

proto = Protocol()

# data = bytes([0xA5, 0x06, 0x01, 0x00])
calc = Calculator(Crc16.XMODEM, optimized=True)
# val = calc.checksum(data)
# print(data)
# temp = []
# temp.append(val >>8)
# temp.append(val & 0xFF)
# print(bytes(temp))
# data = data + bytes(temp)
# print(data)



def command_frame(header:int, command:int, reg:int, data:list[int]) -> bytes:
    print(reg)
    data_len = len(data)
    frame_len = data_len + 6
    frame  = bytes([header]) + bytes([frame_len])+ bytes([command]) + bytes([reg]) + bytes(data)
    crc16_val = calc.checksum(frame)
    crc_bytes = bytes([crc16_val >> 8, crc16_val & 0xFF])
    frame = frame + crc_bytes
    return frame

# frame = command_frame(header=proto.header_m2s, 
#                       command=proto.cmd_ReadReg, 
#                       reg=0x00, 
#                       data=[0x00])

# frame = command_frame(header=proto.header_m2s, 
#                       command=proto.cmd_WriteReg, 
#                       reg=proto.reg_FuncEn, 
#                       data=[0x03]) # displayEn, AutoBrightness

frame = command_frame(header=proto.header_m2s,
                        command=proto.cmd_WriteReg, 
                        reg=proto.reg_DigitSingle, 
                        data=[0x01, 0x00])

frame = command_frame(header=proto.header_m2s,
                        command=proto.cmd_WriteReg, 
                        reg=proto.reg_DecPointSingle, 
                        data=[0x0])

# frame = command_frame(header=proto.header_m2s,
#                         command=proto.cmd_WriteReg, 
#                         reg=proto.reg_DigitMultiple, 
#                         data=[0x01, 0x02, 0x03, 0x04]) # 1,

frame_str = " ".join([hex(byte).upper() for byte in frame])

print(frame_str)


# print(hex(proto.header_m2s))
