temp1 = 50
while True:
        if temp1 > 70:
            light.set_all(light.rgb(255, 0, 0 ))
        elif temp1 > 40:
            light.set_all(light.rgb(0, 255, 0 ))
        else: 
            light.set_all(light.rgb(0, 0, 255 ))



