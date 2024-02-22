import login_gui
import login_system
from server_main_gui import Admin_Main
from client_main_gui import Client_Main
from tkinter import messagebox

login_instance = login_gui.login()

if(login_system.status.session_status == True and login_system.status.login_type == "admin"):
    print(login_system.status.session_status, login_system.status.login_type)
    admin_main = Admin_Main()
elif(login_system.status.session_status == True and login_system.status.login_type == "client"):
    print(login_system.status.session_status, login_system.status.login_type)
    client_main = Client_Main()
    pass
elif(login_system.status.session_status == False):
    pass
else:
    messagebox.showerror("There was some unknown error in the code")
print(login_system.status.session_status, login_system.status.login_type)
