from dataclasses import dataclass

@dataclass
class Protocol:
    header_m2s : hex = 0xa5
    header_s2m : hex = 0x5a
    cmd_WriteReg : hex = 0x00
    cmd_ReadReg : hex = 0x01
    reg_DisplaySts : hex = 0x00
    reg_FuncEn: hex = 0x01
    reg_DigitSingle : hex = 0x02
    reg_DigitMultiple : hex = 0x03		
    reg_DecPointSingle : hex = 	0x04
    reg_DecPointMultiple : hex = 0x05	
    reg_ManualBrightness : hex = 0x06		
    reg_AutoBrightnessADCVal : hex = 0x07		
    reg_AutoBrightnessSlopeADCH : hex = 0x08		
    reg_AutoBrightnessSlopeADCL : hex = 0x09	
    reg_AutoBrightnessSlopeValH : hex = 0x0a	
    reg_AutoBrightnessSlopeValL : hex = 0x0b	

    