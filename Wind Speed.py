import math
wind_speed = float(input('enter the wind speed: '))
tempreture = float(input('enter the temprature in faranhite: '))

def wind_chill(speed, temp):
    a = 0.6215 * temp
    b = 0.4275 * temp
    w = 35.74  + a + (b - 35.75) * speed * 0.16
    return w

print(f'Wind Chill is: {wind_chill(wind_speed, tempreture)}')
print(f'wind speed: {wind_speed} MPH')
print(f'temprature: {tempreture / 33.8} C')
