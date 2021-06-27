#from tkinter import *
#
#master = Tk()
#
#w = Canvas(master, width=200, height=100)
#w.pack()
#
#w.create_line(0, 0, 200, 100)
#i = w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
#
#w.create_rectangle(50, 25, 150, 75, fill="blue")
#
##i = w.create_line(xy, fill="red")
#
#w.coords(i, (0,100,200,50)) # change coordinates
#w.itemconfig(i, fill="blue") # change color
#
##w.delete(i) # remove
#
##w.delete(ALL) # remove all items
#
#mainloop()

from tkinter import *

canvas_width = 700
canvas_height = 500

def paint( event ):
   python_green = "#000"
   
   x1, y1 = ( event.x - 2 ), ( event.y - 2 )
   x2, y2 = ( event.x + 2 ), ( event.y + 2 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

python_green = "#000"
points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
a = w.create_polygon(points, outline=python_green,fill='yellow', width=3)

b = w.create_text(canvas_width / 2,canvas_height / 2,width=300,justify=CENTER,text="Python lorem ipsum dolor sit amet cor mist dela cyi",fill= '#b00016',font=('Times new roman',30))

points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]

c = w.create_polygon(points, outline=python_green, 
            fill='yellow', width=3)

message = Label( master, text = "Press and Drag the mouse to draw" )
#message.pack( side = BOTTOM )

d =w.create_window((100,200),window=message,anchor='w')
print(w.find_below(c))
print(w.find_all())
print(w.find_closest())

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
nsteps = len(bitmaps)
step_x = int(canvas_width / nsteps)

for i in range(0, nsteps):
   w.create_bitmap((i+1)*step_x - step_x/2,50, bitmap=bitmaps[i])
   
mainloop()