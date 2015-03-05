__author__ = "Blackfry"

#***********************************************************************
# CODEWARS: Temperature converter
#***********************************************************************

#Description:
#
#Write a function convert_temp(temp, from_scale, to_scale) converting temperature from one scale to another. Return #converted temp value.
#
#Round converted temp value to an integer(!).
#
#Reading: http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature
#
#possible scale inputs:
#    "C"  for Celsius
#    "F"  for Fahrenheit
#    "K"  for Kelvin
#    "R"  for Rankine
#    "De" for Delisle
#    "N"  for Newton
#    "Re" for Réaumur
#    "Ro" for Rømer
#temp is a number, from_scale and to_scale are strings.
#
#convert_temp(   100, "C",  "F") # => 212
#convert_temp(    40, "Re", "C") # => 50
#convert_temp(    60, "De", "F") # => 140
#convert_temp(373.15, "K",  "N") # => 33
#convert_temp(   666, "K",  "K") # => 666


def convert_temp(temp, from_scale, to_scale):
    x = 0
    if from_scale == "C":
        x = temp
    elif from_scale == "F":
        x = ((temp - 32) * 5 / 9)
    elif from_scale == "K":
        x = (temp - 273.15)
    elif from_scale == "R":
        x = ((temp - 491.67) * 5 / 9)
    elif from_scale == "De":
        x = (100 - temp * 2 / 3)
    elif from_scale == "N":
        x = (temp * 100 / 44)
    elif from_scale == "Re":
        x = (temp * 5 / 4)
    elif from_scale == "Ro":
        x = ((temp - 7.5) * 40 / 21)

    if to_scale == "C":
        return x
    elif to_scale == "F":
        return int(x * 9 /5 + 32)
    elif to_scale == "K":
        return int(x + 273.15)
    elif to_scale == "R":
        return int((x + 273.15) * 9 / 5)
    elif to_scale == "De":
        return int((100 - x) * 3 / 2)
    elif to_scale == "N":
        return int(x * 33 / 100)
    elif to_scale == "Re":
        return int(x * 4 / 5)
    elif to_scale == "Ro":
        return int(x * 21 / 40 + 7.5)