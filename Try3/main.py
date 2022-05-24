from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


def retrieveValues():
    global age, weight, height, handSize, footSize, forearmSize, faceSize, femurSize
    age = assign(ageEntry.get())
    weight = assign(weightEntry.get())
    height = assign(heightEntry.get())
    handSize = assign(handSizeEntry.get())
    footSize = assign(footSizeEntry.get())
    forearmSize = assign(forearmSizeEntry.get())
    faceSize = assign(faceSizeEntry.get())
    femurSize = assign(femurSizeEntry.get())

    Calculate()
    Calculate()
    Calculate()
    Draw()


def assign(value):
    if bool(value):
        return float(value)
    else:
        return 0


def BMI():
    global height, weight, age
    if 0 not in (height, weight) and age > 19:
        bmi = (weight/2.205) / ((height/39.37) ** 2) #kg/m^2
        return round(bmi , 2)
    else:
        return "N/A"


def FaceAndHand():
    global handSize, faceSize
    if 0 not in (faceSize, handSize):
        return
    # Face is Equal to Hand
    if faceSize != 0:
        handSize = faceSize
    elif handSize != 0:
        faceSize = handSize
    else:
        return "NA"


def FootAndForearm():
    global footSize, forearmSize
    if 0 not in (footSize, forearmSize):
        return
    #foot equals Forearm
    if footSize != 0:
        forearmSize = footSize
    elif forearmSize != 0:
        footSize = forearmSize
    else:
        return "NA"


def ForearmAndHand():
    global forearmSize, handSize
    if 0 not in (forearmSize, handSize):
        return
    #forearm is 1.39 times longer than hand
    if handSize != 0:
        forearmSize = handSize * 1.39
    elif forearmSize != 0:
        handSize = forearmSize / 1.39
    else:
        return "NA"


def FemurAndHeight():
    global femurSize, height
    if 0 not in (femurSize, height):
        return
    # 1:4
    if femurSize != 0:
        height = femurSize * 4
    elif height != 0:
        femurSize = height / 4
    else:
        return "NA"


def FaceAndHeight():
    global faceSize, height
    if 0 not in (faceSize, height):
        return
    if faceSize != 0:
        if age <6:
            height = faceSize * 6
        if age <13:
            height = faceSize * 6.5
        else:
            height = faceSize * 8
    elif height != 0:
        if age <6:
            faceSize = height / 6
        if age <13:
            faceSize = height / 6.5
        else:
            faceSize = height / 8
    else:
        return "NA"


def Calculate():
    FaceAndHand()
    FootAndForearm()
    ForearmAndHand()
    FemurAndHeight()
    FaceAndHeight()
    BMI()


def Draw():
    decimalsWanted = 2
    ageLabel = tk.Label(text="Age: {}".format(round(age,decimalsWanted)), bg="white")
    weightLabel = tk.Label(text="Weight: {}".format(weight), bg="white")
    heightLabel = tk.Label(text="Height\n{}\"".format(round(height, decimalsWanted)), bg="white")
    handsizeLabel = tk.Label(text="Hand Size\n {}\"".format(round(handSize, decimalsWanted)), bg="white")
    footSizeLabel = tk.Label(text="Foot Size\n {}\"".format(round(footSize, decimalsWanted)), bg="white")
    forearmSizeLabel = tk.Label(text="Forearm Size\n {}\"".format(round(forearmSize, decimalsWanted)), bg="white")
    faceSizeLabel = tk.Label(text="Face Size\n{}\"".format(round(faceSize, decimalsWanted)), bg="white")
    femurSizeLabel = tk.Label(text="Femur Size\n{}\"".format(round(femurSize, decimalsWanted)), bg="white")
    BMILabel = tk.Label(text="Body to Mass Index: {}".format(BMI()), bg="white")

    ageLabel.place(x=535, y=10)
    weightLabel.place(x=535, y=30)
    BMILabel.place(x=535, y=50)

    heightLabel.place(x=575, y=350)
    handsizeLabel.place(x=65, y=245)
    footSizeLabel.place(x=125, y=430)
    forearmSizeLabel.place(x=90, y=180)
    faceSizeLabel.place(x=375, y=40)
    femurSizeLabel.place(x=445, y=275)

# GLOBAL VARIABLES
age = 0
weight = 0
height = 0
handSize = 0
footSize = 0
forearmSize = 0
faceSize = 0
femurSize = 0

# WINDOW SETUP
window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("700x800+800+20")  # WxH+Horizontal+Vertical
frame = tk.Frame()

# QUESTION AND ENTRY  SETUP
ageEntry = Entry(window)
weightEntry = Entry(window)
heightEntry = Entry(window)
handSizeEntry = Entry(window)
footSizeEntry = Entry(window)
forearmSizeEntry = Entry(window)
faceSizeEntry = Entry(window)
femurSizeEntry = Entry(window)
ageQL = tk.Label(text="Enter Age(Required)")
weightQL = tk.Label(text="Enter Weight (Pounds)")
heightQL = tk.Label(text="Enter Height (Inches)")
handSizeQL = tk.Label(text="Enter Hand Size (Inches)")
footSizeQL = tk.Label(text="Enter Foot Size (Inches)")
forearmSizeQL = tk.Label(text="Enter Forearm Size (Inches)")
faceSizeQL = tk.Label(text="Enter Face Size (Inches)")
femurSizeQL = tk.Label(text="Enter Femur Size (Inches)")

# Setting up Skeleton Image
image = Image.open('Human with Distances2.png')
    # height, width
image = image.resize((640, 469), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_imgLabel = Label(window, image=my_img)
my_imgLabel.pack()

calculateBtn = tk.Button(text="Calculate!", command=retrieveValues)

# PACKING
ageQL.pack(side=LEFT)
ageEntry.pack(side=LEFT)
weightQL.pack(side=LEFT)
weightEntry.pack(side=LEFT)
heightQL.pack()
heightEntry.pack()
handSizeQL.pack()
handSizeEntry.pack()
footSizeQL.pack()
footSizeEntry.pack()
forearmSizeQL.pack()
forearmSizeEntry.pack()
faceSizeQL.pack()
faceSizeEntry.pack()
femurSizeQL.pack()
femurSizeEntry.pack()
calculateBtn.pack(pady=5)

window.mainloop()

'''greeting = tk.Label(
    text="Hello, Tkinter",
)
greeting.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
# debug statement
    print(
        "Age {} weight {} , height {}, handSize {} , footSize{} , forearmSize{}, faceSize{}, femurSize{}".format(age,
                                                                                                                 weight,
                                                                                                                 height,
                                                                                                                 handSize,
                                                                                                                 footSize,
                                                                                                                 forearmSize,
                                                                                                                 faceSize,
                                                                                                                 femurSize))
    print("BMI is | ", BMI())
    print("FaceNHand | ", FaceNHand())
    print("footNForearm | ", FootNForearm())
    print("forearmNhand | ", ForearmNHand())
    print("femurNheight | ", FemurNHeight())
    print("face N height | ", FaceNHeight())
    print(
        "Age {} weight {} , height {}, handSize {} , footSize{} , forearmSize{}, faceSize{}, femurSize{}, BMI{}".format(age,
                                                                                                                 weight,
                                                                                                                 height,
                                                                                                                 handSize,
                                                                                                                 footSize,
                                                                                                                 forearmSize,
                                                                                                                 faceSize,
                                                                                                                 femurSize, BMI()))

'''
