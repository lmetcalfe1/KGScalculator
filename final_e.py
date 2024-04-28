#Logan Metcalfe
#Main file for the Extruder calculator
#v.1
from tkinter import *
import math
import subprocess
subprocess.call(["python" , "kgspermin.py"])
root = Tk()
header = Label(root, text="Volume calculator for the colorant dosers on Plastic extruders", font= ('bold', 20))
header.grid(row=0, column=8, columnspan=3)
note = Label(root, text = "Note: currently there is no 'line 5' on this plant. The machine designation remains "
             "reserved for simplicity.")

def kgCalc():
    #Used to determine the volume of the plastic extruders
    pe = .0345
    pp = .0325
    lbsPerMin = 0
    counter = 1
    machine = input("enter the machine name ")
    ipm = int(input("enter the rate from the shear counter (inches per minute) "))
    width = int(input("enter the width of the sheet, after the steel rolls, but before the slitters "))
    gauge = int(input("Enter the guage of the sheet, in the format commonly spoken, '35' for 35 gauge. "))
    gauge = float(gauge) / 1000
    lbsPerMin = lbsPerMin + ((ipm * width) * gauge)
    material = input("enter the material being uesed. (PP or PE)")
    material = material.lower()
    if material == "pe" or "pp":
        if material == "pe":
            lbsPerMin *= pe
        if material == "pp":
            lbsPerMin *= pp
    else:
        print("invalid input")
        material = input("enter the material being uesed. (PP or PE) ")
    counter += 1
    #calculating min to hrs and lbs to kg
    lbsPerhr = lbsPerMin * 60
    kgsPerhr = lbsPerhr / 2.2046
    kgsPerhr = round(kgsPerhr , 2)
    print('Line ', machine, '\'s kgs per hour is: ', kgsPerhr, sep='')


def checker():
    if kgsperhour == 0:
        print("No prior data on file! Would you like to run a new calculation?")


note.grid(row = 1, column=8, columnspan=3)
machine1 = Button(root, text = "Line 1")
machine2 = Button(root, text = "Line 2")
machine3 = Button(root, text = "Line 3")
machine4 = Button(root, text = "Line 4")
machine6 = Button(root, text = "Line 6")
machine7 = Button(root, text = "Line 7")
machine8 = Button(root, text = "Line 8")
machine9 = Button(root, text = "Line 9")
machine10 = Button(root, text = "Line 10")
machine11 = Button(root, text = "Line 11")
machine12 = Button(root, text = "Line 12")

machine1.grid(row=2, column=0)
machine2.grid(row=3, column=0)
machine3.grid(row=4, column=0)
machine4.grid(row=5, column=0)
machine6.grid(row=6, column=0)
machine7.grid(row=7, column=0)
machine8.grid(row=8, column=0)
machine9.grid(row=9, column=0)
machine10.grid(row=10, column=0)
machine11.grid(row=11, column=0)
machine12.grid(row=12, column=0)

root.mainloop()