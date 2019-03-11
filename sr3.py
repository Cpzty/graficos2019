import gl
import time as t
gl.glCreateWindow(400,400)
start = t.time()
gl.glLoad("./cube.obj",(0.4,0.3,0.3),(100,100,0.5))
gl.glFinish('cube')
finish = t.time()
print("took: {}".format(finish-start))
