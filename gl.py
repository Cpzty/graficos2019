import struct
import math
from obj import Obj
from collections import namedtuple

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])


def sum(v0, v1):
  return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)

def sub(v0, v1):
  return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)

def mul(v0, k):
  return V3(v0.x * k, v0.y * k, v0.z *k)

def dot(v0, v1):
  return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def cross(v0, v1):
  return V3(
    v0.y * v1.z - v0.z * v1.y,
    v0.z * v1.x - v0.x * v1.z,
    v0.x * v1.y - v0.y * v1.x,
  )

def length(v0):
  return (v0.x**2 + v0.y**2 + v0.z**2)**0.5

def norm(v0):
  v0length = length(v0)

  if not v0length:
    return V3(0, 0, 0)

  return V3(v0.x/v0length, v0.y/v0length, v0.z/v0length)

def bbox(*vertices):
  xs = [ vertex.x for vertex in vertices ]
  ys = [ vertex.y for vertex in vertices ]
  xs.sort()
  ys.sort()

  return V2(xs[0], ys[0]), V2(xs[-1], ys[-1])

def barycentric(A, B, C, P):
  bary = cross(
    V3(C.x - A.x, B.x - A.x, A.x - P.x), 
    V3(C.y - A.y, B.y - A.y, A.y - P.y)
  )
  if abs(bary[2]) < 1:
    return -1, -1, -1   

  return (
    1 - (bary[0] + bary[1]) / bary[2], 
    bary[1] / bary[2], 
    bary[0] / bary[2]
  )


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
        self.zbuffer = [
            [-float('inf') for x in range(self.width)]
            for y in range(self.height)
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
        
    def point(self,x,y,color = None):
        self.pixels[y][x] = color or self.current_color

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

def estandarizarx(entrada):
    global my_bitmap
    entrada = round(entrada/(my_bitmap.width/2)-1,4)
    return entrada
def estandarizary(entrada):
    global my_bitmap
    entrada = round(entrada/(my_bitmap.height/2)-1,4)
    return entrada

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
        
##def glLine(x0,y0,x1,y1,step):
##    #step = diferencia en decimales/diferencia de enteros
##    global deltax,deltay,m
##    
##    deltax = round(abs(x1 - x0),2)
##    deltay = round(abs(y1 - y0),2)
##    #m = abs(deltay/deltax)
##    error = 0
##    threshold = deltax
##    y = y0
##    #step = 1/(my_bitmap.width/2)
##    if(deltay > deltax):
##        x0,y0 = y0,x0
##        x1,y1 = y1,x1
##    if(x0>x1):
##        x0,x1 = x1,x0
##        y0,y1 = y1,y0
##        #step = 1/(my_bitmap.height/2)
##        y = y0
##    for x in frange(x0,x1+(1/(my_bitmap.width/2)),step):
##        #print(x,y)
##        if(deltay > deltax):
##            #print(deltax)
##            #print(deltay)
##            glVertex(float(y),float(x))
##        else:
##            glVertex(float(x),float(y))
##        error += deltay * 2
##        if error >= threshold:
##            y += 2.5/my_bitmap.width/4 if y0 < y1 else -2.5/my_bitmap.width/4
##            threshold += deltax * 2

def glLineLow(x0,y0,x1,y1,step):
  dx = round(x1 - x0,2)
  dy = round(y1 - y0,2)
  yi = (1/my_bitmap.height/2)
  if dy < 0:
    yi = -(1/my_bitmap.height/2)
    dy = -dy
  threshold = (2*dy) - dx
  y = y0
  for x in frange(x0,x1+(1/(my_bitmap.width/2)),step):
    glVertex(float(x),float(y))
    if threshold > 0:
        y = y + yi
        threshold = threshold - (2 * dx)
    threshold = threshold + (2 * dy)

def glLineHigh(x0,y0,x1,y1,step):
    dx = round(x1 - x0,2)
    dy = round(y1 - y0,2)
    xi = (1/my_bitmap.width/2)
    if dx < 0:
        xi = -(1/my_bitmap.width/2)
        dx = -dx
    threshold = (2 *dx) - dy
    x = x0
    for y in frange(y0,y1+(1/(my_bitmap.height/2)),step):
        glVertex(x,y)
        if threshold > 0:
            x = x + xi
            threshold = threshold - (2*dy)
        threshold = threshold + (2 * dx)
    
#def glLineBresenham(x0,y0,x1,y1,step):
#    if abs(y1-y0) < abs(x1-x0):
#        if x0 > x1:
#            glLineLow(x1,y1,x0,y0,step)
#        else:
#            glLineLow(x0,y0,x1,y1,step)
#    else:
#        if y0 > y1:
#            glLineHigh(x1,y1,x0,y0,step)
#        else:
#            glLineHigh(x0,y0,x1,y1,step)

def glLineLow_norm(x0,y0,x1,y1):
  dx = round(x1 - x0,2)
  dy = round(y1 - y0,2)
  yi = 1
  if dy < 0:
    yi = -1
    dy = -dy
  threshold = (2*dy) - dx
  y = y0
  for x in range(x0,x1+1):
    xs = estandarizarx(x)
    ys = estandarizary(y)
    glVertex(xs,ys)
    if threshold > 0:
        y = y + yi
        threshold = threshold - (2 * dx)
    threshold = threshold + (2 * dy)

def glLineHigh_norm(x0,y0,x1,y1):
    dx = round(x1 - x0,2)
    dy = round(y1 - y0,2)
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    threshold = (2 *dx) - dy
    x = x0
    for y in range(y0,y1+1):
        xs = estandarizarx(x)
        ys = estandarizary(y)
        glVertex(xs,ys)
        if threshold > 0:
            x = x + xi
            threshold = threshold - (2*dy)
        threshold = threshold + (2 * dx)
    
def glLineBresenham(x0,y0,x1,y1):
    if abs(y1-y0) < abs(x1-x0):
        if x0 > x1:
            glLineLow_norm(x1,y1,x0,y0)
        else:
            glLineLow_norm(x0,y0,x1,y1)
    else:
        if y0 > y1:
            glLineHigh_norm(x1,y1,x0,y0)
        else:
            glLineHigh_norm(x0,y0,x1,y1)
            
            

#def triangle(A, B, C, color=None):
#    if A.y > B.y:
#      A, B = B, A
#    if A.y > C.y:
#      A, C = C, A
#    if B.y > C.y: 
#      B, C = C, B
#
#    dx_ac = C.x - A.x
#    dy_ac = C.y - A.y
#    if dy_ac == 0:
#        return
#    mi_ac = dx_ac/dy_ac
#
#    dx_ab = B.x - A.x
#    dy_ab = B.y - A.y
#    if dy_ab != 0:
#        mi_ab = dx_ab/dy_ab
#
#        for y in range(A.y, B.y + 1):
#            xi = round(A.x - mi_ac * (A.y - y))
#            xf = round(A.x - mi_ab * (A.y - y))
#
#            if xi > xf:
#                xi, xf = xf, xi
#            for x in range(xi, xf + 1):
#                #print(x)
#                #print(y)
#                x = estandarizarx(x)
#                y = estandarizary(y)
#                glColor(1,0,0)
#                glVertex(x, y)
#
#    dx_bc = C.x - B.x
#    dy_bc = C.y - B.y
#    if dy_bc:
#        mi_bc = dx_bc/dy_bc
#
#
#        for y in range(B.y, C.y + 1):
#            xi = round(A.x - mi_ac * (A.y - y))
#            xf = round(B.x - mi_bc * (B.y - y))
#
#            if xi > xf:
#                xi, xf = xf, xi
#            for x in range(xi, xf + 1):
#                x = estandarizarx(x)
#                y = estandarizary(y)
#                glColor(1,0,0)
#                glVertex(x, y)
      
def triangle(A, B, C, texture=None, texture_coords=(), color=None,intensity=1):
    global my_bitmap
    bbox_min, bbox_max = bbox(A, B, C)
    for x in range(bbox_min.x, bbox_max.x + 1):
      for y in range(bbox_min.y, bbox_max.y + 1):
        w, v, u = barycentric(A, B, C, V2(x, y))
        if w < 0 or v < 0 or u < 0: 
          continue

        if texture:
          tA,tB,tC = texture_coords
          tx = tA.x * w + tB.x * v + tC.x * u
          ty = tA.y * w + tB.y * v + tC.y * u
          color = texture.get_color(tx,ty,intensity)
        
        z = A.z * w + B.z * v + C.z * u
        if x< 0 or y < 0:
          continue
        if x < len(my_bitmap.zbuffer) and y < len(my_bitmap.zbuffer[x]) and z > my_bitmap.zbuffer[x][y]:
          glColor(1,0,0)
          xs = estandarizarx(x)
          ys = estandarizary(y)
          glVertex(xs, ys)
          my_bitmap.zbuffer[x][y] = z
        

def glTransform(vertex, translate=(0, 0, 0), scale=(1, 1, 1)):

    return V3(
      round((vertex[0] + translate[0]) * scale[0]),
      round((vertex[1] + translate[1]) * scale[1]),
      round((vertex[2] + translate[2]) * scale[2])
    )

#obj
def glLoad(filename,translate=(0,0,0),scale=(1,1,1), texture = None):
    global my_bitmap
    model = Obj(filename)
    light = V3(0.7,0.7,-0.7)
    for face in model.vfaces:
        vcount = len(face)
        if vcount == 3:
            f1 = face[0][0] - 1
            f2 = face[1][0] - 1
            f3 = face[2][0] - 1

            a = glTransform(model.vertices[f1], translate, scale)
            b = glTransform(model.vertices[f2], translate, scale)
            c = glTransform(model.vertices[f3], translate, scale)

            normal = norm(cross(sub(b, a), sub(c, a)))
            intensity = dot(normal, light)
            if not texture:
              grey = round(255 * intensity)
              if grey < 0:
                  continue  
              triangle(a, b, c, color=color(grey, grey, grey))
            else:
              t1 = face[0][1] - 1
              t2 = face[1][1] - 1
              t3 = face[2][1] - 1
              tA = V3(*model.tvertices[t1])
              tB = V3(*model.tvertices[t2])
              tC = V3(*model.tvertices[t3])
              triangle(a, b, c, texture=texture, texture_coords=(tA, tB, tC), intensity=intensity)

        else:
            f1 = face[0][0] - 1
            #print(f1)
            f2 = face[1][0] - 1
            #print(f2)
            f3 = face[2][0] - 1
            #print(f3)
            f4 = face[3][0] - 1   
            #print(f4)
            #print(model.vertices[f1])
            vertices = [
                glTransform(model.vertices[f1], translate, scale),
                glTransform(model.vertices[f2], translate, scale),
                glTransform(model.vertices[f3], translate, scale),
                glTransform(model.vertices[f4], translate, scale)
            ]

            normal = norm(cross(sub(vertices[0], vertices[1]), sub(vertices[1], vertices[2])))  
            intensity = dot(normal, light)
            grey = round(255 * intensity)
            A,B,C,D = vertices
            if not texture:
              grey = round(255 * intensity)
              if grey < 0:
                  continue  
              triangle(A, B, C, color(grey, grey, grey))
              triangle(A, C, D, color(grey, grey, grey))
            else:
              t1 = face[0][1] - 1
              t2 = face[1][1] - 1
              t3 = face[2][1] - 1
              t4 = face[3][1] - 1
              tA = V3(*model.tvertices[t1])
              tB = V3(*model.tvertices[t2])
              tC = V3(*model.tvertices[t3])
              tD = V3(*model.tvertices[t4])  
              triangle(A, B, C, texture=texture, texture_coords=(tA, tB, tC), intensity=intensity)
              triangle(A, C, D, texture=texture, texture_coords=(tA, tC, tD), intensity=intensity)

def glLoadOld(filename,translate=(0,0),scale=(1,1)):
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
            #x1 = round(x1/(my_bitmap.width/2),2)
            y1 = round((v1[1] + translateY) * scaleY)
            #y1 = round(y1/(my_bitmap.height/2),2)
            x2 = round((v2[0] + translateX) * scaleX)
            #x2 = round(x2/(my_bitmap.width/2),2)
            y2 = round((v2[1] + translateY) * scaleY)
            #y2 = round(y2/(my_bitmap.height/2),2)
            #print(x1,x2,y1,y2)

            glLineBresenham(x1,y1,x2,y2)

def glLoadZ(filename,translate=(0,0,0),scale=(1,1,1)):
    global my_bitmap
    model = Obj(filename)
    light = V3(0,1,0)
    for face in model.vfaces:
        vcount = len(face)
        if vcount == 3:
            f1 = face[0][0] - 1
            f2 = face[1][0] - 1
            f3 = face[2][0] - 1

            a = glTransform(model.vertices[f1], translate, scale)
            b = glTransform(model.vertices[f2], translate, scale)
            c = glTransform(model.vertices[f3], translate, scale)

            normal = norm(cross(sub(b, a), sub(c, a)))
            intensity = dot(normal, light)
            grey = round(255 * intensity)
            if grey < 0:
                continue  
            triangle(a, b, c, color(grey, grey, grey))
        else:
            f1 = face[0][0] - 1
            #print(f1)
            f2 = face[1][0] - 1
            #print(f2)
            f3 = face[2][0] - 1
            #print(f3)
            f4 = face[3][0] - 1   
            #print(f4)
            #print(model.vertices[f1])
            vertices = [
                glTransform(model.vertices[f1], translate, scale),
                glTransform(model.vertices[f2], translate, scale),
                glTransform(model.vertices[f3], translate, scale),
                glTransform(model.vertices[f4], translate, scale)
            ]

            normal = norm(cross(sub(vertices[0], vertices[1]), sub(vertices[1], vertices[2])))  
            intensity = dot(normal, light)
            grey = round(255 * intensity)
            if grey < 0:
                continue 
            A, B, C, D = vertices 
            triangle(A, B, C, color(grey, grey, grey))
            triangle(A, C, D, color(grey, grey, grey))

    
def glFinish(name):
    global my_bitmap
    my_bitmap.write(str(name)+".bmp")

def flood_fill(x,y,maxx,maxy,initial_color,minx,miny):
  global my_bitmap
  xs = estandarizarx(x)
  ys = estandarizary(y)
  print(x)
  if(x>=maxx or y >=maxy):
    return
  if(x<=minx or y <=miny):
    return
  elif(b'\xff\xff\xff' == my_bitmap.pixels[round(xs*250+1)][round(ys*250+1)]):
    return
  else:
    glVertex(xs,ys)
    flood_fill(x + 1, y,maxx,maxy,initial_color,minx,miny) 
    flood_fill(x - 1, y,maxx,maxy,initial_color,minx,miny) 
    flood_fill(x, y + 1,maxx,maxy,initial_color,minx,miny) 
    flood_fill(x, y - 1,maxx,maxy,initial_color,minx,miny) 

def bucketfill(x,y,maxx,maxy):
  x1 = x
  resetx = x
  y1 = y
  for i in frange(y,maxy,0.004):
    for j in frange(x,maxx,0.004):
      glVertex(x1,y1)
      if(x1<maxx):
        x1 += 0.004
      else:
        x1 = resetx
    y1 += 0.004
  
def fill(self, x, y, color):
        self.validate(x, y, color)

        self.max_depth = 0
        old_color = self.pixels[x][y]

        if old_color == color:
            return  # nothing to do

        stack = [(y, x)]
        w = len(self.pixels[0])
        h = len(self.pixels)

        while stack:
            self.max_depth = max(self.max_depth, len(stack))
            cur_point = stack.pop()
            x1, y1 = cur_point

            while x1 >= 0 and self.pixels[y1][x1] == old_color:
                x1 -= 1
            x1 += 1

            above = False
            below = False

            while x1 < w and self.pixels[y1][x1] == old_color:
                self.pixels[y1][x1] = color

                if not above and y1 > 0 and self.pixels[y1 - 1][x1] == old_color:
                    stack.append((x1, y1 - 1))
                    above = True
                elif above and y1 < h - 1 and self.pixels[y1 - 1][x1] != old_color:
                    above = False

                if not below and y1 < h - 1 and self.pixels[y1 + 1][x1] == old_color:
                    stack.append((x1, y1 + 1))
                    below = True
                elif below and y1 < h - 1 and self.pixels[y1 + 1][x1] != old_color:
                    below = False

                x1 += 1
    
