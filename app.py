import time
import flet as ft
from fletFlow import fletFlowApp, fletFlowView

from views.main_view import MainView # import all of your views

s = time.time()
print(f"App started {time.time()-s}")
class App(fletFlowApp):
    def __init__(self, title=None, debug=False):
        print(f"App Initiated {time.time()-s}")
        super().__init__(title, debug)

    def config_page_setting(self):
        self.page.theme_mode = ft.ThemeMode.DARK
        theme = ft.Theme()
        theme.page_transitions.windows = ft.PageTransitionTheme.NONE
        theme.page_transitions.linux = ft.PageTransitionTheme.NONE
        self.page.theme = theme
    
    def views(self, page:ft.Page):
        # register views here with route 
        self.register_view("/", MainView)
    
    def app_presentaion(self):
        print(f"App presentation {time.time()-s}")
        self.page.go("/")

        
# creating app object and running the app
app = App(title="SignalX")
app.run()
