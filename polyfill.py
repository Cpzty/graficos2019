import gl

gl.glCreateWindow(500,500)
gl.glClear()
print(gl.my_bitmap.pixels[499][499])

if(b'\x00\x00\x00' == gl.my_bitmap.pixels[499][499]):
    print("ahoy maties yes")
#gl.glColor(1,0,0)
gl.glVertex(1,1)
if(b'\x00\x00\x00' == gl.my_bitmap.pixels[499][499]):
    print("ahoy maties")
else:
    print(gl.my_bitmap.pixels[499][499])
    print("my invention works")

