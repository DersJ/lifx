import lifxlan
import keyboard
import time, random

colors = 

class Color:
	def __init__(self, h, s, l):
		self.hue = h
		self.saturation = s
		self.luminance = l



def msc(light, h, s, l):
	adjusted_hue = (int)(h/360 * 65535)
	adjusted_sat = (int)(s/100 * 65535)
	adjusted_lum = (int)(l/100 * 65535)
	print(adjusted_hue +" "+ adjusted_sat +" "+adjusted_lum)
	light.set_color([adjusted_hue, adjusted_sat, adjusted_lum, 5750])

def asdf():
	print('hello world')


def main():
	lan = lifxlan.LifxLAN()
	bulb = lan.get_lights()[0]
	colors = random_colors()
	if(bulb):
		while(True):
			if(keyboard.is_pressed('a')):
				print("a is pressed")
				time.sleep(.05)
			elif (keyboard.is_pressed('e')):
				print("e pressed, exiting")
				break
	print("loop finished")


main()				

def random_colors():
	colors = []
	for i in range(3):
		h = random.random * 360
		s = random.random
		l = random.random
		colors.append((h,s,l))
	return colors

	
