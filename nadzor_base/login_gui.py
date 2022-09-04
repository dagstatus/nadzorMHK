import tkinter
from tkinter import *
from functools import partial
from nadzor_base import users, main_window

class LoginGui:
    def __init__(self):
        self.user_validate = users.UserAccess()
        self.main_window = main_window.MainWindow()

    def create_login_window(self):
        def validateLogin(username, password):
            login_flag = self.user_validate.check_user(user_name=username.get(), password=password.get())
            if login_flag:
                # тут надо вызвать основное окно
                pass
                tkAuthWindow.destroy()
                self.main_window.create_main_window()
            else:
                text.set('Неверный логин или пароль')
            # print("username entered :", username.get())
            # print("password entered :", password.get())
            return


        # window
        tkAuthWindow = Tk()
        tkAuthWindow.geometry('300x100')
        tkAuthWindow.title('Введите логи и пароль')
        tkAuthWindow.resizable(False, False)

        # username label and text entry box
        usernameLabel = Label(tkAuthWindow, text="Логин").grid(row=0, column=1)


        username = StringVar()
        usernameEntry = Entry(tkAuthWindow, textvariable=username)
        usernameEntry.grid(row=0, column=2)
        usernameEntry.focus_set()

        # password label and password entry box
        passwordLabel = Label(tkAuthWindow, text="Пароль").grid(row=1, column=1)
        password = StringVar()
        passwordEntry = Entry(tkAuthWindow, textvariable=password, show='*').grid(row=1, column=2)

        text = tkinter.StringVar()
        text.set('')
        login_label_rezult = Label(tkAuthWindow, textvariable=text).grid(row=5, column=2)

        validateLogin = partial(validateLogin, username, password)

        # login button
        loginButton = Button(tkAuthWindow, text="Вход", command=validateLogin, width=30).grid(row=4, column=2)

        tkAuthWindow.bind('<Return>', lambda event:validateLogin())


        tkAuthWindow.mainloop()



if __name__ == '__main__':
    Test = LoginGui()
    Test.create_login_window()
