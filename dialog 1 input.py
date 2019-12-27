from tkinter import *
import tkinter.messagebox as tm


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_nim = Label(self, text="Nim   :")
        self.entry_nim = Entry(self)

        self.label_nim.grid(row=1, sticky=E)
        self.entry_nim.grid(row=1, column=1)


        self.logbtn = Button(self, text="Kirim Data Baru", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        nim = self.entry_nim.get()

        print(nim)

        if nim == "3260":
            tm.showinfo("Login info", "Data telah terkirim")
        else:
            tm.showerror("Login error", "Incorrect username")


root = Tk()
lf = LoginFrame(root)
root.mainloop()