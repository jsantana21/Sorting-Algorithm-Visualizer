from tkinter import *
from tkinter import ttk
import random # To generate random data values


# Generates a black window; Background for GUI 
root = Tk() # Boots up the tkinter module 
root.title('Sorting Algorithm Visualizer')
root.maxsize(1500, 600)
root.config(bg='black')

#variables & functions
selectedAlgorithm = StringVar()

def drawDataArray(data):
    canvas.delete("all") # Delete data values from canvas from previous use of drawDataArray
    canvas_height = 380
    canvas_width = 1400
    bargraph_width = canvas_width / (len(data) + 1) # Width of each bar in array 
    offset = 5 # needed so that the bars don't start at the border of the screen 
    spacing_between_bars = 5 #in pxiels
    
    normalizedData = [ i / max(data) for i in data] #to make sure the height of the bars are relative and seeable in the GUI 
    
    for i, height in enumerate(normalizedData):
        # x1, y1 are coordinates of the top left  needed to create the rectangle for each data
        x1 = i * bargraph_width + offset + spacing_between_bars
        y1 = canvas_height - height * 340
        # x2, y2 are coordinates of the bottom right needed to create the rectangle for each data
        x2 = (i + 1) * bargraph_width + offset
        y2 = canvas_height

        canvas.create_rectangle(x1, y1, x2, y2, fill="red") #Creates the bar for each data value using the x1,y1 and x2,y2 coordinates
        canvas.create_text(x1, y1, anchor=SW, text=str(data[i])) # Writes the numbers over the bar representing the data


def GenerateNewArray():
    print('Sorting Algorithm Selected: ' + selectedAlgorithm.get())

    try:
        minValue = int(minValueEntry.get()) # Recieves the string that the user typed in the Min Value box and converts it to an int
    except:
        minValue = 1 # If no input is given, then minValue is 1 by default
    try:
        maxValue = int(maxValueEntry.get()) # Recieves the string that the user typed in the Max Value box and converts it to an int
    except:
        maxValue = 30 # If no input is given, then maxValue is 10 by default
    try:
        arraySize = int(arraySizeEntry.get()) # Recieves the string that the user typed in the Array Size box and converts it to an int
    except:
        arraySize = 25 # If no input is given, then arraySize is 10 by default

    # Conditional Statments to avoid any bugs
    if minValue < 0 : # To avoid negative value data values
        minValue = 0
    if maxValue > 100: # To avoid the bars going past the canvas and keep format clean as possible
        maxValue = 100
    if arraySize > 100 or arraySize < 3:# To avoid the array of bars being cut by the canvas 
        arraySize = 100
    if minValue > maxValue: # To avoid any bugs in generating the data values
        minValue, maxValue = maxValue, minValue # swap the values

    data = []
    # Fills in the data array with random values with the range of the minValue and maxValue
    for _ in range(arraySize):
        data.append(random.randrange(minValue, maxValue+1))

    
    drawDataArray(data)

# Generates the background User Interface area of the GUI
UserInterfaceFrame = Frame(root, width = 1400, height = 200, bg='snow4')
UserInterfaceFrame.grid(row=0, column=0, padx=10, pady=5)

# Generates the background / canvas where the bars of data will be drawn on 
canvas = Canvas(root, width = 1400, height = 380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface Area - Text Boxes, Buttons, etc.

# FIRST ROW
# (Top Left Corner); Algorithm Label (where you can choose which sorting algorithm you want to use)
Label(UserInterfaceFrame, text="Sorting Algorithm: ", bg='snow4').grid(row=0, column=0, padx=5, pady=5, sticky=W) # W for west aka left
algorithmList = ttk.Combobox(UserInterfaceFrame, textvariable = selectedAlgorithm, values=['Bubble Sort', 'Quick Sort','Merge Sort'])
algorithmList.grid(row=0, column=1, padx=5, pady=5)
algorithmList.current(0) #chooses Bubble Sort by default since it is in index 0

# Button to Generate New Random Array
Button(UserInterfaceFrame, text="Generate New Random Array", command=GenerateNewArray, bg='white').grid(row=0, column=2, padx=5, pady=5)

# SECOND ROW
# 'Array Size' Label where you can decide how many elements you want to have the array
Label(UserInterfaceFrame, text="Array Size ", bg='snow4').grid(row=1, column=0, padx=5, pady=5, sticky=W)
arraySizeEntry = Entry(UserInterfaceFrame)
arraySizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# 'Min Value' Label where you can decide what the smallest element in the array is 
Label(UserInterfaceFrame, text="Min Value ", bg='snow4').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minValueEntry = Entry(UserInterfaceFrame)
minValueEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# 'Max Value' Label where you can decide what the biggest element in the array is 
Label(UserInterfaceFrame, text="Max Value ", bg='snow4').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxValueEntry = Entry(UserInterfaceFrame)
maxValueEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

root.mainloop() # tkinter's equivalent of main()
