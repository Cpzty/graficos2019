from gl import *
from obj import Texture, NormalMap
from random import random, randint, choice
def gourad(bitmap, bar, **kwargs):
    w, v, u = bar
    #primer color es rojo, luego naranja 
    list_of_colors = [b'\x00\x00\xff', b'\x00\x00\xff',b'\x00\x00\xff', b'\x00E\xff']
    #tA, tB, tC = kwargs['texture_coords']
    #tx = tA.x * w + tB.x * v + tC.x * u
    #tx = random()
    #ty = tA.y * w + tB.y * v + tC.y * u
    #color = bitmap.texture.get_color(tx,ty)
    color = choice(list_of_colors)
    
    iA, iB, iC = [dot(n, V3(random(),random(),random())) for n in kwargs['varying_normals']]
    intensity = w * iA + v *iB + u * iC
    if intensity > 1:
        intensity = 1
    return bytes(map(lambda b : round(b * intensity) if b * intensity > 0 else 0, color))

glCreateWindow(1000,1000)
glLoad('./MarsPlanet.obj', (100, 100, 1), (4, 4, 1), shader=gourad)

glFinish('lab3')
