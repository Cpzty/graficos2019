#cristian perez carnet 16011
#Ejercicio 1

import struct
import math
import sys
import random

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

def glFinish(name):
    global my_bitmap
    my_bitmap.write(str(name)+".bmp")

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    if action == "1":
        glCreateWindow(400,400)
        glVertex(round(random.random(),1),round(random.random(),1))
        glFinish("punto_random")
    elif action == "2":
        glCreateWindow(400,400)
        glVertex(-1,-1)
        glVertex(-1,1)
        glVertex(1,-1)
        glVertex(1,1)
        glFinish("puntos_esquinas")
    elif action == "3":
        glCreateWindow(400,400)
        x2 = -0.05
        y3 = -0.05
        y2 = -0.05
        x3 = -0.05
        for i in range(19):
            if(i == 0):
                x1 = -0.05
                y1 = 0.05
                glVertex(x1,y1-0.01)
                glVertex(x1,-y1)
            else:
                x2 = 0.005 + x2
                y2 = 0.005 + y2
                glVertex(x2,y1-0.01)
                glVertex(x3,y2)
                glVertex(-x3-0.01,y2)
                glVertex(x2,y3)
        glFinish("cubo")
    elif action == "4":
        glCreateWindow(400,400)
        #glColor(1,0,0)
        x1 = -1
        y1 = -1
        for i in range(399):
            glVertex(x1,1)
            glVertex(x1,-1)
            x1 = x1 + 0.005
            glVertex(1,y1)
            glVertex(-1,y1)
            y1 = y1 + 0.005
        glFinish("bordes")
    elif action == "5":
        glCreateWindow(400,400)
        x1_y1 = -1
        for i in range(399):
            glVertex(x1_y1,x1_y1)
            x1_y1 = x1_y1 + 0.005
        glFinish("linea_cruzada")
    elif action == "6":
        glCreateWindow(400,400)
        x1 =-1
        y1 =-1
        for j in range(399):
            for i in range(399):
                decide = random.randint(0,1)
                if(decide == 0):
                    glColor(0,0,0)
                    glVertex(x1,y1)
                else:
                    glColor(1,1,1)
                    glVertex(x1,y1)
                x1 = x1 + 0.005
                if(i == 398):
                    y1 = y1 + 0.005
                    x1 = -1
        glFinish("muchos_puntos_blancos")
    elif action =="7":
        glCreateWindow(400,400)
        x1 =-1
        y1 =-1
        for j in range(399):
            for i in range(399):                
                glColor(random.random(),random.random(),random.random())
                glVertex(x1,y1)    
                x1 = x1 + 0.005
                if(i == 398):
                    y1 = y1 + 0.005
                    x1 = -1
        glFinish("muchos_puntos_colores")
    elif action == "8":
        glCreateWindow(400,400)
        x1 =-1
        y1 =-1
        for j in range(399):
            for i in range(399):
                decide = random.randint(0,359)
                if(decide == 0):
                    glColor(1,1,1)
                    glVertex(x1,y1)
                else:
                    glColor(0,0,0)
                    glVertex(x1,y1)
                x1 = x1 + 0.005
                if(i == 398):
                    y1 = y1 + 0.005
                    x1 = -1
        glFinish("estrellas")
    elif action == "atari":
        glCreateWindow(160,192)
        glClearColor(0.66,0.53,0)
        glClear()
        glColor(0.95,0.82,0.10)
        x1 = -0.44 #70
        y1 = 0.36  #70
        x2 = x1
        y2 = -y1
        for i in range(139):
            glVertex(x1,y1-0.02)
            glVertex(x1,-y1)
            x1 = x1 + 0.006
            glVertex(x2,y2)
            glVertex(-x2-0.04,y2)
            y2 = y2 + 0.005
        #coloreo de la serpiente    
        glColor(0.16,0.57,0)
        x3 = -0.16
        y3 = 0.08
        y4 = 0.155
        x4 = x3
        x5 = 0
        y5 = 0.155
        for j in range(14):
            glVertex(x3,y3)
            glVertex(x3-0.008,y3)
            glVertex(x3-0.016,y3)
            y3 = y3 + 0.005
        for k in range(29):
            glVertex(x4-0.016,y4)
            glVertex(x4-0.016,y4-0.005)
            x4 = x4 + 0.006
        for l in range(49):
            glVertex(x5,y5)
            glVertex(x5-0.006,y5)
            glVertex(x5-0.012,y5)
            y5 = y5 - 0.005
        #cubo
        glVertex(-0.060,-0.22)
        glVertex(-0.054,-0.22)
        glVertex(-0.048,-0.22)
        glVertex(-0.042,-0.22)
        glVertex(-0.060,-0.215)
        glVertex(-0.054,-0.215)
        glVertex(-0.048,-0.215)
        glVertex(-0.042,-0.215)
        glVertex(-0.060,-0.21)
        glVertex(-0.054,-0.21)
        glVertex(-0.048,-0.21)
        glVertex(-0.042,-0.21)
        glVertex(-0.060,-0.205)
        glVertex(-0.054,-0.205)
        glVertex(-0.048,-0.205)
        glVertex(-0.042,-0.205)
        #contador
        glColor(0.01,0.23,0.84)
        glVertex(-0.18,-0.5)
        glVertex(-0.18,-0.5+0.005)
        glVertex(-0.18,-0.5+0.01)
        glVertex(-0.18,-0.5+0.015)
        glVertex(-0.18,-0.5+0.020)
        glVertex(-0.18,-0.5+0.025)
        glVertex(-0.18,-0.5+0.030)
        glVertex(-0.18,-0.5+0.035)
        glVertex(-0.18,-0.5+0.040)
        glVertex(-0.18,-0.5+0.045)
        glVertex(-0.18,-0.5+0.050)
        glVertex(-0.18,-0.5+0.055)
        glVertex(-0.18,-0.5+0.060)
        glVertex(-0.18+0.006,-0.5)
        glVertex(-0.18+0.012,-0.5)
        glVertex(-0.18+0.018,-0.5)
        glVertex(-0.18+0.024,-0.5)
        glVertex(-0.18+0.030,-0.5)
        glVertex(-0.18+0.036,-0.5)
        glVertex(-0.18+0.042,-0.5)
        glVertex(-0.18+0.048,-0.5)
        glVertex(-0.18+0.054,-0.5)
        glVertex(-0.18+0.060,-0.5)
        glVertex(-0.18+0.066,-0.5)
        glVertex(-0.18+0.072,-0.5)
        glVertex(-0.18+0.078,-0.5)
        glVertex(-0.18+0.084,-0.5)
        #
        glVertex(-0.096,-0.5)
        glVertex(-0.096,-0.5+0.005)
        glVertex(-0.096,-0.5+0.01)
        glVertex(-0.096,-0.5+0.015)
        glVertex(-0.096,-0.5+0.020)
        glVertex(-0.096,-0.5+0.025)
        glVertex(-0.096,-0.5+0.030)
        glVertex(-0.096,-0.5+0.035)
        glVertex(-0.096,-0.5+0.040)
        glVertex(-0.096,-0.5+0.045)
        glVertex(-0.096,-0.5+0.050)
        glVertex(-0.096,-0.5+0.055)
        glVertex(-0.096,-0.5+0.060)
        #
        glVertex(-0.096,-0.5)
        glVertex(-0.096,-0.5-0.005)
        glVertex(-0.096,-0.5-0.01)
        glVertex(-0.096,-0.5-0.015)
        glVertex(-0.096,-0.5-0.020)
        glVertex(-0.096,-0.5-0.025)
        glVertex(-0.096,-0.5-0.030)
        glVertex(-0.096,-0.5-0.035)
        glVertex(-0.096,-0.5-0.040)
        glVertex(-0.096,-0.5-0.045)
        glVertex(-0.096,-0.5-0.050)
        glVertex(-0.096,-0.5-0.055)
        glVertex(-0.096,-0.5-0.060)
        glFinish("snake")
        
        
        
        
if __name__ == '__main__':
    main()
    

#glColor(1,0,0)

#glVertex(-1,-1)
#glVertex(-1,1)
#glVertex(1,1)
#glVertex(1,-1)

        


        
