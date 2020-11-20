let temp1 = 50
while (true) {
    if (temp1 > 60) {
        light.setPixelColor(4, light.rgb(255, 0, 0))
    } else if (temp1 > 40) {
        light.setPixelColor(4, light.rgb(0, 255, 0))
    } else {
        light.setPixelColor(4, light.rgb(0, 0, 255))
    }
    
}
