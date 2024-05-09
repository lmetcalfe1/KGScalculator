#Logan Metcalfe
#Main file for the Extruder calculator
#v.1
from tkinter import *
import math
import sys
import os
from PIL import ImageTk, Image
#import all the goodies
root = Tk()
root.title('KGS per hour calculator') #Title
root.iconbitmap('images/icon.ico') #Icon (Broken and I don't know why, I also got no reply for why.)

header = Label(root, text="Volume calculator for the colorant dosers on Plastic extruders", font= ('bold', 20)) #Header
note = Label(root, text = "Note: This tool has been designed as a lite version for use on the site. ") #Note

def submit(): #Called when the button is pushed. 
    global kgsPerhr
    lbsPerMin = 0 #initializing the variable
    ipm = int(IPMentry.get()) #Getting the Variable from the first window
    width = int(widthentry.get()) #Getting the Variable from the first window
    gauge = int(gaugeentry.get()) #Getting the Variable from the first window
    material = int(materialentry.get()) #Getting the Variable from the first window
    gauge = gauge / 1000 #Converting common notation to actual notation, thousandths of an inch
    lbsPerMin += ((ipm * width) * gauge) #First part of the calculation
    if material == 2: #Determine which material is selected
        lbsPerMin *= .0345 #PE
    else:
        lbsPerMin *= .0325 #PP
    #calculating min to hrs and lbs to kg
    lbsPerhr = lbsPerMin * 60
    kgsPerhr = lbsPerhr / 2.2046
    kgsPerhr = round(kgsPerhr , 2) #Rounding to the second place, required by the machine.
    Answer = Toplevel() #Creating the second window
    Answer.title('KGS per hour calculator') #Title
    Answer.iconbitmap('images/icon.ico')#Icon (Broken and I don't know why, I also got no reply for why.)
    photo1 = ImageTk.PhotoImage(Image.open('images/Yorha_64x64.jpg')) #Glory, to mankind.
    img1 = Label(Answer, image=photo1) #Assigning photo to label
    header2 = Label(Answer, text="Volume calculator for the colorant dosers on Plastic extruders", font= ('bold', 20)) #Header, should be the same as on page 1
    header2.grid(row=0, column=1) #Alligning it
    photo2 = ImageTk.PhotoImage(Image.open('images/extruder.jpg'))#Photo of extruder
    solution = Label(Answer, text='Based on the input you provided, at a rate of ' + str(ipm) + ' inches per minute, at a width of '
                    + str(width) + ' inches,\n and a thickness of ' + str(gauge) + " inches, your final rate for KGS per hour is: " + str(kgsPerhr) + ' kilograms per hour.\n'
                    ' enter this directly into the screen for the colorant doser.', font=('bold', 10)) #Big words for making the final calculation and putting it to words
    img1.grid(row=0, column=0,) #aligning it
    img2 = Label(Answer, image=photo2) #Label for extruder photo
    img2.grid(row=1,column=0, columnspan=2) #putting it on the screen
    solution.grid(row=2,column=0, columnspan=2) #Oh yeah, align it.
    Answer.mainloop()



materialentry = IntVar() #Intvar for the radio buttons 
photo1 = ImageTk.PhotoImage(Image.open('images/Yorha_64x64.jpg')) #Image
img1 = Label(image=photo1)#image
submit = Button(root, text = 'calculate', width = 20, command=submit)#Button
promptIPM = Label(root, text='Enter the rate from the shear counter (inches per minute)') #Prompt text for the input
promptwidth = Label(root, text='Enter the width of the sheet, after the steel rolls, but before the slitters')#Prompt text for the input
promptgauge = Label(root, text='Enter the gauge of the sheet, in the format commonly spoken, ''"35"'' for 35 gauge.')#Prompt text for the input
promptmaterial = Label(root, text='Enter the material being used.')#Prompt text for the input
IPMentry = Entry(root, relief= SUNKEN) #Input field. Entry style
widthentry = Entry(root, relief= SUNKEN)#Input field. Entry style
gaugeentry = Entry(root, relief= SUNKEN)#Input field. Entry style

ppbutton = Radiobutton(root, text='Polypropylene', variable=materialentry, value= 1)#radio buttons. 
pebutton = Radiobutton(root, text='Polyethylene', variable=materialentry, value= 2)#Turn on the radio. TURN ON THE RADIO AYE SIR

#test = Label(root, text=materialentry.get()) Testing for the radio buttons. Comment back in to verify functionality.

promptIPM.grid(row=2, column=0, columnspan=3) #Prompt placement, all of these are the same. They alternate between the prompt, then the field. 
promptwidth.grid(row=4, column=0, columnspan=3)
promptgauge.grid(row=6, column=0, columnspan=3)
promptmaterial.grid(row=8, column=0, columnspan=3)
IPMentry.grid(row=3, column=1)
widthentry.grid(row=5, column=1)
gaugeentry.grid(row=7, column=1)
ppbutton.grid(row=9, column=1) #Radio
pebutton.grid(row=10, column=1)



header.grid(row=0, column=1)# aligning the header all the way down here
note.grid(row = 1, column=1) #I think technically there is a single frame where this allignment isn't loaded yet so it 
submit.grid(row=11, column=1)#shows a jumbled mess, then fixes itself. 

img1.grid(row=0, column=0, rowspan=2) #Alignment for the image

root.mainloop()
#DONE