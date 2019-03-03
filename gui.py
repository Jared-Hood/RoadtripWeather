from tkinter import *
import googleImages
import roadMap
import getWeather
from PIL import Image, ImageTk
import glob

def gui():

    def enter():

        start = e1.get()
        end = e2.get()
        days = int(e3.get())
        master.destroy()

        window = Tk()
        window.title("Your Roadtrip Weather Slideshow")

        directions = roadMap.getDirections(start, end)
        parsed_directions = roadMap.parseWaypoints(directions, days)
        city_state, full_address = roadMap.reverseGeo(parsed_directions[1])

        print(parsed_directions)

        places = []
        im_list = []

        iter = 1
        for i in range(len(parsed_directions)):
            lat = str(parsed_directions[i][0])
            long = str(parsed_directions[i][1])
            currentWeather = getWeather.getWeather(lat, long)[iter][2]

            city_state, full_address = roadMap.reverseGeo(parsed_directions[i])
            googleImages.getPics(city_state + " " + currentWeather + " day")
            iter += 1

            print(currentWeather + ": " + city_state)

            d = iter - 1
            w = currentWeather
            i_p = city_state + " " + currentWeather + " day"
            l = city_state
            places.append((d,w,i_p,l))
            size = 250,250

            for filename in glob.glob('/Users/jaredhood/Documents/RoadtripWeather/downloads/' + i_p +'/*.jpg'):
                im=Image.open(filename)
                im.thumbnail(size, Image.ANTIALIAS)
                im_list.append(im)

            for filename in glob.glob('/Users/jaredhood/Documents/RoadtripWeather/downloads/' + i_p +'/*.png'):
                im=Image.open(filename)
                im.thumbnail(size, Image.ANTIALIAS)
                im_list.append(im)

            for filename in glob.glob('/Users/jaredhood/Documents/RoadtripWeather/downloads/' + i_p +'/*.jpeg'):
                im=Image.open(filename)
                im.thumbnail(size, Image.ANTIALIAS)
                im_list.append(im)


        dayL = Label(window, text="Day: ")
        dayL.grid(row=1, column=0)
        LocationL = Label(window, text="Location: ")
        LocationL.grid(row=2, column=0)
        weatherL = Label(window, text="Weather: ")
        weatherL.grid(row=3, column=0)
        picL = Label(window, text="Live Look: ")
        picL.grid(row=4, column=0)


        z = 1
        x = 0
        for i in places:
            day = Label(window,text=i[0])
            day.grid(row = 1, column=z)

            location = Label(window, text=i[3])
            location.grid(row=2, column=z)

            weather = Label(window, text=i[1])
            weather.grid(row=3, column=z)

            img = im_list[x]
            photo = ImageTk.PhotoImage(img)
            label = Label(image=photo)
            label.image = photo
            label.grid(row=4, column=z)

            z += 1
            x += 1

        Button(window, text='Quit', command=window.quit).grid(row=5, column=1, sticky=W, pady=10)

        window.mainloop()


    master = Tk()

    master.title("Roadtrip Weather Planner")

    Label(master, text='Start').grid(row=0)
    Label(master, text='Destination').grid(row=1)
    Label(master, text='Number of Days').grid(row=2)

    e1 = Entry(master)
    e1.grid(row=0, column=1)

    e2 = Entry(master)
    e2.grid(row=1, column=1)

    e3 = Entry(master)
    e3.grid(row=2, column=1)

    Button(master, text='Enter',command=enter).grid(row=3, column=0, sticky=W,pady=10)
    Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=W, pady=10)

    master.mainloop()

    #start of slideshow pane

gui()