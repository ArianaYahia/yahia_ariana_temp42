temp1 = 30
while True:
        if temp1 > 60:
            light.set_pixel_color(4, light.rgb(255, 0, 0 ))
        elif temp1 > 40:
            light.set_pixel_color(4, light.rgb(0, 255, 0 ))
        else: 
            light.set_pixel_color(4, light.rgb(0, 0, 255 ))



