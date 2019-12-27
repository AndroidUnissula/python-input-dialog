from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_nama = Label(self, text="Nama  :")
        self.label_nim = Label(self, text="Nim   :")

        self.entry_nama = Entry(self)
        self.entry_nim = Entry(self)

        self.label_nama.grid(row=0, sticky=E)
        self.label_nim.grid(row=1, sticky=E)
        self.entry_nama.grid(row=0, column=1)
        self.entry_nim.grid(row=1, column=1)


        self.logbtn = Button(self, text="Kirim Data Baru", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_nama.get()
        password = self.entry_nim.get()

        print(username, password)

        if username == "niam" and password == "password":
            tm.showinfo("Login info", "Data telah terkirim")
        else:
            tm.showerror("Login error", "Incorrect username")


root = Tk()
lf = LoginFrame(root)
root.mainloop()