from tkinter import *
# import tkMessageBox as mb
from tkinter import messagebox as mb

# pada python 3
# from tkinter import *
# import tkinter.messagebox as mb


class DemoDialog:
    def __init__(self, induk, judul):
        self.induk = induk

        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.tutup)
        self.induk.resizable(False, False)

        self.aturKomponen()

    def aturKomponen(self):
        # atur frame utama
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)

        ## box tombol dialog
        box = Frame(mainFrame, bd=20)
        box.pack(fill=BOTH, expand=YES)

        # pasang aneka tombol
        btnInfo = Button(box, text='Dialog showinfo',
                         command=self.onKlikInfo)
        btnInfo.pack(side=LEFT)

        btnWarning = Button(box, text='Dialog showwarning',
                            command=self.onKlikWarning)
        btnWarning.pack(side=LEFT, padx=5)

        btnError = Button(box, text='Dialog showerror',
                          command=self.onKlikError)
        btnError.pack(side=LEFT)

        # pasang tombol KELUAR
        btnKeluar = Button(box, text="KELUAR",
                           command=self.tutup)
        btnKeluar.pack(side=LEFT, padx=5)

        # atur statusbar
        Label(mainFrame, text='www.KlinikPython.wordpress.com',
              bd=1, relief=RIDGE, foreground='blue').pack(
            side=BOTTOM, fill=X)

    def onKlikInfo(self, event=None):
        mb.showinfo("Info Penting!", "Ini adalah DIALOG SHOW INFO")

    def onKlikError(self, event=None):
        mb.showerror("Kesalahan Fatal!", "Ini adalah DIALOG SHOW ERROR")

    def onKlikWarning(self, event=None):
        mb.showwarning("Peringatan!", "Ini adalah DIALOG SHOW WARNING")

    def tutup(self, event=None):
        self.induk.destroy()


if __name__ == '__main__':
    root = Tk()

    app = DemoDialog(root, ":: Demo Dialog ::")

    root.mainloop()