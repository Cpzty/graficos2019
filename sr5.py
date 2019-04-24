import gl
from obj import Texture
gl.glCreateWindow(400,400)
textur = Texture('./modelos/sky.bmp')
gl.glLoad('./cube.obj',(3.5,-1.5,0),(60,60,1),texture=textur)

gl.glFinish('sr5')
