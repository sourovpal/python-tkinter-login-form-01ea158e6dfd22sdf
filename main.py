from tkinter import *
from tkinter import messagebox

root=Tk()
root.title()
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)


def singin():
    username = user.get()
    pass_word = password.get()
    if username == 'admin' and pass_word == 'admin':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+300+200")
        screen.config(bg='white')
        Label(screen, text="Hello Everyone!", bg="#fff", fg="#57a1f8", font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
        screen.mainloop()
    elif username != 'admin' and pass_word != 'admin':
        messagebox.showerror("Invalid", "Invalid username and password!")        

img = PhotoImage(file="login.png")
Label(root, image=img, bg="white").place(x=50,  y=50)


frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

header = Label(frame, text="Sign In", fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light', 23, 'bold'))
header.place(x=100, y=5)
#########---------------------------------------------###########
def on_enter(e):
    user.delete(0, 'end');
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")

user = Entry(frame, width=25, fg='#666', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=1, bg="#e6e6e6").place(x=25, y=107)

#########--------------------------------------------#############
def on_enter(e):
    password.delete(0, 'end');
def on_leave(e):
    name = password.get()
    if name == '':
        password.config(show="")
        password.insert(0, "Password")
    else:
        password.config(show="*")

password = Entry(frame, width=25, fg='#666', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, "Password")
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=1, bg="#e6e6e6").place(x=25, y=177)


Button(frame, width=41, pady=7, text="Sign In", bg="#57a1f8", fg="white", border=0, command=singin).place(x=25, y=204)

lbl_not_account = Label(frame, text="Don't have an account?", fg="#666", bg="white", font=('Microsoft YaHei UI Light', 9))
lbl_not_account.place(x=75, y=270)

sign_up_btn = Button(frame, width=6, text="Sign up", border=0, bg='white', cursor='hand2', fg="#57a1f8")
sign_up_btn.place(x=215, y=270)

root.mainloop()
