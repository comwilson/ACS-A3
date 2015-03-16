'''
stegimg.py
	author: Cameron Wilson
	description: 
'''
from PIL import Image
import sys
def main():
	if len(sys.argv) < 3:
		print "usage: stegimg.py <encode|decode> <file> [message]"
		return

	if sys.argv[1] == "encode":
		if len(sys.argv) != 4:
			print "encoding requires a filename and a message to encode"
			return


	elif sys.argv[1] == "decode":
		if len(sys.argv) != 3:
			print "decoding requires a file name only"
			return


	else:
		print "mode must be either 'encode' or 'decode'"
		return

	mode = sys.argv[1]
	file_name = sys.argv[2]

	print "mode: " + mode
	print "file: " + file_name
	im = Image.open(file_name)

	message = ""
	if mode == "encode":
		message = sys.argv[3]
		message_index = 0

	print im.size
	pic = im.load()

	for x in range(im.size[0]):
		for y in range(im.size[1]):
			c = pic[x, y]
			#pic[x, y] = (255, c[1], 255)
			#print c
			if mode == "encode":
				if (message_index < len(message)):
					print message[message_index]
					pic[x, y] = (c[0], c[1], ord(message[message_index]))
					message_index += 1
			else:
				#print chr(pic[x,y][2])
				message += chr(c[2])
	if mode == "encode":
		im.save(file_name)
	else:
		with open("output.txt", "w") as f:
			f.write(message)

main()

