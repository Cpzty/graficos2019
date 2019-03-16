# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:45:21 2019

@author: Cristian
"""

import gl

gl.glCreateWindow(1000,1000)
gl.glLoad('./cube.obj',translate=(0,0,0))
gl.glFinish('sr4light2')
