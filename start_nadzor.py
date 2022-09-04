from nadzor_base import CONFIG_NADZOR, login_gui

class StartProgramm:
    def __init__(self):
        self.result = None
        self.login_window = login_gui.LoginGui()
        self.login_window.create_login_window()

    def login_gui(self):
        pass


if __name__ == '__main__':
    MainClass = StartProgramm()
