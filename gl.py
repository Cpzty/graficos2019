import struct
import math
import sys
import random
from obj import Obj
#uso numpy para la funcion sign y los steps de float en la linea

def char(c):
    return struct.pack("=c",c)

def word(w):
    return struct.pack("=h",w)

def dword(d):
    return struct.pack("=l",d)

def color(r,g,b):
    return bytes([b,g,r])

#color para clear
bmp_color = color(0,0,0)

class Bitmap(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.pixelf = []
        self.clear()
    def clear(self):
        self.pixels = [
            [
                bmp_color for x in range(self.width)
                ] for y in range(self.height)
            ]
    def write(self, filename):
        f = open(filename, "bw")
        #header
        f.write(b'B')
        f.write(b'M')
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        #imageheader
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.pixels[x][y])
        
        f.close()
        
    def point(self,x,y,color):
        self.pixels[y][x] = color

#variables globales
my_bitmap = Bitmap(0,0)
offsetx = 0
offsety = 0

port_width = 0
port_height = 0

bmp_width = 0
bmp_height = 0
vertex_color = color(255,255,255)

#agregados en ejercicio de linea
deltax = 0
deltay = 0
m = 0


#funciones gl
def glInit():
 return   

def glCreateWindow(width,height):
    global my_bitmap, bmp_width, bmp_height
    
    my_bitmap = Bitmap(width,height) 
    bmp_width = width
    bmp_height = height

def glViewPort(x,y,width,height):
    global offestx, offsety, port_width, port_height
    
    offsetx = x
    offsety = y
    port_width = width
    port_height = height

def glClear():
    global my_bitmap
    
    my_bitmap.clear()

def glClearColor(r,g,b):
    global bmp_color
    
    bmp_color = color(round(255*r), round(255*g), round(255*b))

def glVertex(x,y):
    global my_bitmap, bmp_width, bmp_height
    half_width = math.floor(bmp_width/2)
    half_height = math.floor(bmp_height/2)
    if(x<1 and y<1):
        my_bitmap.point(half_width + round(((half_width)*x)),half_height + round(((half_height)*y)),vertex_color)
    elif(x==1 and y==1):
        my_bitmap.point(half_width-1 + round(((half_width)*x)),half_height-1 + round(((half_height)*y)),vertex_color)
    elif(x==1 and y!=1):
        my_bitmap.point(half_width-1 + round(((half_width)*x)),half_height + round(((half_height)*y)),vertex_color)
    elif(x!=1 and y==1):
        my_bitmap.point(half_width + round(((half_width)*x)),half_height-1 + round(((half_height)*y)),vertex_color)
    else:
        print("valores fuera del rango")

def glColor(r,g,b):
    global vertex_color
    
    vertex_color = color(round(255*r), round(255*g), round(255*b))

#linea
#frange
def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i += step
        
def glLine(x0,y0,x1,y1,step):
    #step = diferencia en decimales/diferencia de enteros
    global deltax,deltay,m
    
    deltax = abs(x1 - x0)
    deltay = abs(y1 - y0)
    #m = abs(deltay/deltax)
    error = 0
    threshold = deltax
    y = y0
    #step = 1/(my_bitmap.width/2)
    if(deltay > deltax):
        x0,y0 = y0,x0
        x1,y1 = y1,x1
    if(x0>x1):
        x0,x1 = x1,x0
        y0,y1 = y1,y0
        #step = 1/(my_bitmap.height/2)
        y = y0
    for x in frange(x0,x1,step):
        #print(x,y)
        if(deltay > deltax):
            glVertex(float(y),float(x))
        else:
            glVertex(float(x),float(y))
        error += deltay * 2
        if error >= threshold:
            y += 1/my_bitmap.width/2 if y0 < y1 else -1/my_bitmap.width/2
            threshold += deltax * 2

#obj
def glLoad(filename,translate=(0,0),scale=(1,1)):
    global my_bitmap
    model = Obj(filename)
    for face in model.vfaces:
        vcount = len(face)
        #print(vcount)
        for j in range(vcount):
            f1 = face[j][0]
            f2 = face[(j+1)%vcount][0]

            v1 = model.vertices[f1-1]
            v2 = model.vertices[f2-1]
            scaleX,scaleY = scale
            translateX,translateY = translate

            x1 = round((v1[0] + translateX) * scaleX)
            x1 = round(x1/(my_bitmap.width/2),2)
            y1 = round((v1[1] + translateY) * scaleY)
            y1 = round(y1/(my_bitmap.height/2),2)
            x2 = round((v2[0] + translateX) * scaleX)
            x2 = round(x2/(my_bitmap.width/2),2)
            y2 = round((v2[1] + translateY) * scaleY)
            y2 = round(y2/(my_bitmap.height/2),2)
            #print(x1,x2,y1,y2)

            glLine(x1,y1,x2,y2,0.004)
def glFinish(name):
    global my_bitmap
    my_bitmap.write(str(name)+".bmp")
