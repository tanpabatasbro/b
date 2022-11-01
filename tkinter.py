from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

mainframe = Tk()
mainframe.withdraw()

kg = simpledialog.askfloat("berat", "masukkan berat badan (kg)")
m = simpledialog.askfloat("tinggi", "masukkan tinggi badan (m)")

bmi = kg/(m*m)
messagebox.showinfo("BMI", bmi)


if (bmi<17.0) :
     messagebox.showinfo("status", "kurus, kekurangan berat badan tingkat berat")
elif (bmi>= 17.0 and bmi<=18.4) :
     messagebox.showinfo("status", "kurus, kekurangan berat badan tingkat ringan")
elif (bmi>=18.5 and bmi<=25.0) :
     messagebox.showinfo("status", "normal")
elif (bmi>=25.1 and bmi<=27.0) :
     messagebox.showinfo("status", "gemuk, kelebihan berat badan tingkat ringan")
else:
    messagebox.showinfo("status", "obesitas")

