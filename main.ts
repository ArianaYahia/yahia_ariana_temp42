while (true) {
    console.log("temperature" + input.temperature(TemperatureUnit.Fahrenheit))
    if (input.temperature(TemperatureUnit.Fahrenheit) > 75) {
        light.setAll(light.rgb(255, 255, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) > 40) {
        light.setAll(light.rgb(255, 0, 255))
    } else {
        light.setAll(light.rgb(0, 0, 255))
    }
    
}
