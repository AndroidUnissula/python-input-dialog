from tkinter import *
from tkinter import simpledialog
import playsound
from gtts import gTTS

root=Tk()
root.withdraw()

nama = simpledialog.askstring(title="Test", prompt="Masukkan nama Anda")

bahasa = 'id'
suara = gTTS(text = nama,lang=bahasa, slow = False)
suara.save("suara.mp3")

playsound.playsound("suara.mp3", True)