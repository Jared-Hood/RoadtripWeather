from tkinter import *
from datetime import *

global place1
global place2
global daysBetween
global destinations

m = Tk()
frame = Frame(m)
frame.grid(row=0)
midFrame = Frame(m)
midFrame.grid(row=1)
botFrame = Frame(m)
botFrame.grid(row=2)

Label(frame, text = 'Road Tripper').grid(row=0, padx=200)
#Label(frame, text = '"Finding the Best Time to Vacation Made Easy"').grid(row=1)

Label(midFrame, text = 'Start Location').grid(row=0,column=0)
startPlace = Entry(midFrame)
startPlace.grid(row=1, column=0, padx = 10,pady=5)
place1 = startPlace.get()
endPlace = Entry(midFrame)
endPlace.grid(row=1, column=1, padx = 10)
place2 = endPlace.get()
Label(midFrame, text = 'Destination').grid(row=0, column=1)

Label(midFrame, text = 'Start Date').grid(row=2, column=0)
startDate = Entry(midFrame)
startDate.insert(0, 'ex. 1/12/2019')
startDate.grid(row=3, column=0, padx=10)


endDate = Entry(midFrame)
endDate.grid(row=3, column = 1,padx=10,pady=5)
Label(midFrame, text = 'End Date').grid(row=2, column = 1)

#Label(botFrame, text = 'Destinations along the way?').grid(row=0,column=0,pady=5)
#numPlaces = Spinbox(botFrame, from_ = 0, to =10,width=5).grid(row=0,column=1,padx=5)
#destinations = numPlaces.get()

def getDates():
    date1 = startDate.get()
    date_array = date1.split('/')
    date_date = date(int(date_array[2]), int(date_array[1]), int(date_array[0]))

    date2 = endDate.get()
    date_array1 = date2.split('/')
    date_date1 = date(int(date_array1[2]), int(date_array1[1]), int(date_array1[0]))

    global daysBetween
    daysBetween = date_date1 - date_date

    m.destroy()


Button(botFrame, text='Next', width=10, command=getDates).grid(row=1)

m.mainloop()

m1 = Tk()

m1.mainloop()



