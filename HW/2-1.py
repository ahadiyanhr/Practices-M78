# A function for converting celcius temp. to farenheit
def tConvertor(Temperature):
    intTemp = float(Temperature)    # Temperature can be a float
    return (intTemp*9/5+32)

celciusList = [0,   # Water melting point
            12.5,
            18.3,    # The best bedroom temp. for sleep
            25,     # Room temp.
            34.2,   # Sunny weather temp. for Tehran :)
            37    # Body Temp.
            ]

farenheitList = list(map(tConvertor, celciusList))
print(farenheitList)