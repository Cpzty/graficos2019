#cristian perez
#carnet 16011
####
import gl
####
gl.glCreateWindow(500,500)
x1 = y1 = x2 = y2 = 0
def estandarizar():
    global x1,y1,x2,y2
    x1 = round(x1/gl.my_bitmap.width,2)
    x2 = round(x2/gl.my_bitmap.width,2)
    y1 = round(y1/gl.my_bitmap.height,2)
    y2 = round(y2/gl.my_bitmap.height,2)
#poligono1
x1 = 165
x2 = 185
y1 = 380
y2 = 360
estandarizar()
gl.glLine(x1,y1,x2,y2,0.0015)
#2do par
x1 = 180
x2 = 207
y1 = 330
y2 = 345
estandarizar()
#gl.glLine(x1,y1,x2,y2)
#3er par
x1 = 233
x2 = 230
y1 = 330
y2 = 360
estandarizar()
#gl.glLine(x1,y1,x2,y2)
#4to par
x1 = 250
x2 = 220
y1 = 380
y2 = 385
estandarizar()
#gl.glLine(x1,y1,x2,y2)
#5to par
x1 = 205
x2 = 193
y1 = 410
y2 = 383
estandarizar()
#gl.glLine(x1,y1,x2,y2)
gl.glFinish("Lab1")
