import flet as ft
from fletFlow import fletFlowView

from mqtt.pub import mqtt_publish_msg
from utils.crc_utils import command_frame
from utils.protocol import Protocol

proto = Protocol()
MQTT_BASE_TOPIC = "esp32/wifi_sta/listen"

class MainView(fletFlowView):
    def __init__(self, page: ft.Page):
        super().__init__(page)
    
    def controls(self):
        
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.command_btn1 = ft.ElevatedButton("CMD1", on_click=self.on_click_command_btn, data="CMD1")
        self.command_text1 = ft.TextField(label="Command", width=512, data="CMD1")


        self.command_btn2 = ft.ElevatedButton("CMD2", on_click=self.on_click_command_btn, data="CMD2")
        self.command_text2 = ft.TextField(label="Command", width=512, data="CMD2")

        self.command_btn3 = ft.ElevatedButton("CMD3", on_click=self.on_click_command_btn, data="CMD3")
        self.command_text3 = ft.TextField(label="Command", width=512, data="CMD3")

        self.frame_header = ft.Dropdown(label="Header", 
                                        options=[ft.dropdown.Option(text='header_m2s', key=proto.header_m2s),
                                                 ft.dropdown.Option(text='header_m2s', key=proto.header_s2m)
                                                 ], 
                                        data="Header",
                                        width=200, height=40, text_size=10)
        
        self.frame_cmd = ft.Dropdown(label="Command",
                                     options=[ft.dropdown.Option(text='cmd_WriteReg', key=proto.cmd_WriteReg),
                                              ft.dropdown.Option(text='cmd_ReadReg', key=proto.cmd_ReadReg)
                                              ],
                                              width=200, height=40, text_size=10)
        
        self.frame_reg = ft.Dropdown(label="Register",
                                     options=[ft.dropdown.Option(key=proto.reg_DisplaySts, text='reg_DisplaySts'),
                                              ft.dropdown.Option(text='reg_FuncEn', key=proto.reg_FuncEn),
                                                ft.dropdown.Option(text='reg_DigitSingle', key=proto.reg_DigitSingle),
                                                ft.dropdown.Option(text='reg_DigitMultiple', key=proto.reg_DigitMultiple),
                                                ft.dropdown.Option(text='reg_DecPointSingle', key=proto.reg_DecPointSingle),
                                                ft.dropdown.Option(text='reg_DecPointMultiple', key=proto.reg_DecPointMultiple),
                                                ft.dropdown.Option(text='reg_ManualBrightness', key=proto.reg_ManualBrightness),
                                                ft.dropdown.Option(text='reg_AutoBrightnessADCVal', key=proto.reg_AutoBrightnessADCVal),
                                                ft.dropdown.Option(text='reg_AutoBrightnessSlopeADCH', key=proto.reg_AutoBrightnessSlopeADCH),
                                                ft.dropdown.Option(text='reg_AutoBrightnessSlopeADCL', key=proto.reg_AutoBrightnessSlopeADCL),
                                                ft.dropdown.Option(text='reg_AutoBrightnessSlopeValH', key=proto.reg_AutoBrightnessSlopeValH),
                                                ft.dropdown.Option(text='reg_AutoBrightnessSlopeValL', key=proto.reg_AutoBrightnessSlopeValL),
                                                ],
                                                width=200, height=40, text_size=10)
        
        
        self.frame_data = ft.TextField(label="Data", data="Data", width=200, height=40, text_size=10)
        self.frame_send = ft.ElevatedButton("Send", on_click=self.on_click_command_btn, data="CMD_SEND")
        self.frame_text = ft.Text()
        self.frame_box = ft.Column([self.frame_header, self.frame_cmd, self.frame_reg, self.frame_data, self.frame_send],width=500, alignment=ft.MainAxisAlignment.CENTER, expand=True)

        # command_frame()
        
        # self.test_btn = ft.CupertinoFilledButton("Test Button")

    # page.add(container)

    def layout(self):
        lout = ft.Row([
            ft.Container(content=ft.Column(
                            [   ft.Row([ft.Text("SignalX", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER)]),
                                ft.Row([self.command_btn1, self.command_text1]),
                                ft.Row([self.command_btn2, self.command_text2]),
                                ft.Row([self.command_btn3, self.command_text3]),
                                self.frame_box,
                            ],
                        width=500),
                        padding=10,
                        alignment=ft.alignment.top_center,
                        expand=True

          
            )])
        return lout
    

    def on_click_command_btn(self, e:ft.ControlEvent):
        data = e.control.data
        print(f"Button clicked: {data}")

        if data=="CMD1":
            mqtt_publish_msg(MQTT_BASE_TOPIC, self.command_text1.value)
        
        elif data=="CMD2":
            mqtt_publish_msg(MQTT_BASE_TOPIC, self.command_text2.value)
        
        elif data=="CMD3":
            mqtt_publish_msg(MQTT_BASE_TOPIC, self.command_text3.value)

        elif data== "CMD_SEND":
            # retrieve values from dropdowns and textfields
            header = int(self.frame_header.value)
            cmd = int(self.frame_cmd.value)
            reg = int(self.frame_reg.value)
            data = [int(h,16) for h in self.frame_data.value.split(" ")]

            print(header, cmd, reg, data)
            # create command frame
            frame = command_frame(header, cmd, reg, data)
            frame_str = " ".join([hex(byte).upper() for byte in frame])
            # publish to mqtt
            mqtt_publish_msg(MQTT_BASE_TOPIC, frame_str)
            self.frame_text.value = f"Command Frame: {frame_str}"
            
        self.page.add(ft.Text("Button Clicked!"))
        self.page.update()