temperature = int(input("What's it like today/temp in celcius:"))

if temperature < 15 :
    outfit = "jacket"
    print("It's cold today, you should wear a " + outfit)
else:
    outfit = "t-shirt"
    print("It's warm today, you should wear a " + outfit)

is_raining = input("Is it raining today? (yes/no): ")

if is_raining == "yes":
    print("Don't forget to take an umbrella!")


wind_speed = int(input("What's the wind speed today in km/h: "))
if wind_speed > 20:
    need_windbreaker = "yes"
    print("It's windy today, you might want to wear a windbreaker!")
else:
    need_windbreaker = "no"
    print("It's not very windy today, you don't need a windbreaker.")


has_puddliess = input("Are there puddles on the ground? (yes/no): ")
if has_puddliess == "yes":
    shoes = "waterproof shoes"
    print("There are puddles on the ground, you should wear " + shoes)
else:
    shoes = "regular shoes"
    print("There are no puddles on the ground, you can wear " + shoes)


print("")
print("Summary of today's weather and outfit recommendations:")



print("=======Outfit Recommendations=======")
print("Temperature: " + str(temperature) + "°C")
print("Outfit: " + outfit)
print("Raining: " + is_raining)
print("Wind Speed: " + str(wind_speed) + " km/h")
print("Need Windbreaker: " + need_windbreaker)
print("Puddles: " + has_puddliess)
print("Shoes: " + shoes)
print("=====================================")
