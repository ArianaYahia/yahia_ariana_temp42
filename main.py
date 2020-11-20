temp1 = 75
while True:
        if temp1 > 60:
            light.set_pixel_color(4, light.rgb(255, 0, 0 ))
        else:
            light.clear()

