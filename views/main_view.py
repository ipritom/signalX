import flet as ft
from fletFlow import fletFlowView

from mqtt.pub import mqtt_publish_msg

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
        # self.test_btn = ft.CupertinoFilledButton("Test Button")

    # page.add(container)

    def layout(self):
        lout = ft.Row([
            ft.Container(content=ft.Column(
                            [   
                                ft.Row([self.command_btn1, self.command_text1]),
                                ft.Row([self.command_btn2, self.command_text2])
                            ],
                        width=500),
                        padding=200,
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

        self.page.add(ft.Text("Button Clicked!"))
        self.page.update()