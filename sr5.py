# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:45:21 2019

@author: Cristian
"""

import gl
from obj import Texture
gl.glCreateWindow(1000,1000)
tex = Texture('./sky.bmp')
gl.glLoad('./earth.obj',(1000,800,0),(0.5,0.5,1),texture=tex)
gl.glFinish('sr5')
