while True:
        print("temperature" + input.temperature(TemperatureUnit.FAHRENHEIT))
        if input.temperature(TemperatureUnit.FAHRENHEIT) > 75:
            light.set_all(light.rgb(255, 255, 0 ))
        elif input.temperature(TemperatureUnit.FAHRENHEIT) > 40:
            light.set_all(light.rgb(255, 0, 255 ))
        else: 
            light.set_all(light.rgb(0, 0, 255 ))

