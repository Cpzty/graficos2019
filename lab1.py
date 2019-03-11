#cristian perez
#carnet 16011
####
import gl
import sys
sys.setrecursionlimit(4000)
print(sys.getrecursionlimit())
####
gl.glCreateWindow(500,500)
x1 = y1 = x2 = y2 = 0
def estandarizar():
    global x1,y1,x2,y2
    x1 = round(x1/250-1,2)
    print("x1:{}".format(x1))
    x2 = round(x2/250-1,2)
    print("x2:{}".format(x2))
    y1 = round(y1/250-1,2)
    print("y1:{}".format(y1))
    y2 = round(y2/250-1,2)
    print("y2:{}".format(y2))
#poligono1
x1 = 165
x2 = 185
y1 = 380
y2 = 360
#estandarizar()
#250 + 250x = valor
#x = valor + 250/250... = valor/250 -1
gl.glLineBresenham(x1,y1,x2,y2)
#azul a verde (me estoy guiando por desmos)
x1 = 185
y1 = 360
x2 = 180
y2 = 330
#estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
gl.glLineBresenham(x1,y1,x2,y2)
#verde a morado
x2 = 207
y2 = 345
x1 = 180
y1 = 330
#estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
gl.glLineBresenham(x1,y1,x2,y2)
#morado a negro
x1 = 207
y1 = 345
x2 = 233
y2 = 330
#estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
gl.glLineBresenham(x1,y1,x2,y2)
#negro a rojo suave
x2 = 230
y2 = 360
x1 = 233
y1 = 330
#print("mal")
#estandarizar()
#gl.glLine(x2,y2,x1,y1,0.004)
gl.glLineBresenham(x1,y1,x2,y2)
#rojo suave a azul suave
x1 = 230
y1 = 360
x2 = 250
y2 = 380
#estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
gl.glLineBresenham(x1,y1,x2,y2)
#azul suave a verde suave
x1 = 250
y1 = 380
x2 = 220
y2 = 385
#estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
gl.glLineBresenham(x1,y1,x2,y2)
#verde suave a morado cima
x1 = 220
y1 = 385
x2 = 205
y2 = 410
#estandarizar()
#gl.glLine(x2,y2,x1,y1,0.004)
gl.glLineBresenham(x1,y1,x2,y2)
#morado a negro
x2 = 193
y2 = 383
x1 = 205
y1 = 410
#estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
gl.glLineBresenham(x1,y1,x2,y2)
#negro a rojo
x1 = 193
y1 = 383
x2 = 165
y2 = 380
#estandarizar()
gl.glLineBresenham(x1,y1,x2,y2)
#gl.glLine(x1,y1,x2,y2,0.004)
#gl.glVertex(-0.2,0.5)
#gl.flood_fill(-0.2,0.5,0,0.64, b'\x00\x00\x00',-0.34,0.32)
#gl.bucketfill(-0.34,0.32,0,0.64)

#poligono2
x1 = 321
y1 = 335
x2 = 288
y2 = 286
estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
#2
x1 = 288
y1 = 286
x2 = 339
y2 = 251
estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
#3
x1 = 339
y1 = 251
x2 = 374
y2 = 302
estandarizar()
#gl.glLine(x2,y2,x1,y1,0.004)
#4
x1 = 374
y1 = 302
x2 = 321
y2 = 335
estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
#figura3
x1 = 377
y1 = 249
x2 = 411
y2 = 197
estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
#2
x1 = 411
y1 = 197
x2 = 436
y2 = 249
estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)
#3
x1 = 436
y1 = 249
x2 = 377
y2 = 249
estandarizar()
#gl.glLine(x1,y1,x2,y2,0.004)


gl.glFinish("Lab1")
