from sense_hat import SenseHat

sense = SenseHat()

o = [100,0,100]

img = [
o, o, o, o, o, o, o, o,
o, o, o, o, o, o, o, o,
o, o, o, o, o, o, o, o,
o, o, o, o, o, o, o, o,
o, o, o, o, o, o, o, o,
o, o, o, o, o, o, o, o,
o, o, o, o, o, o, o, o,
o, o, o, o, o, o, o, o,
]

sense.set_pixels(img)