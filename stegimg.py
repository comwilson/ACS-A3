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
		for n in sys.argv[3]:
			message += bin(ord(n))[2:].zfill(8)
			print bin(ord(n))[2:].zfill(8)
		message += '00000000'
		message_index = 0
		print "binary message: " + message
	print im.size
	pic = im.load()

	for x in range(im.size[0]):
		for y in range(im.size[1]):
			c = pic[x, y]
			#pic[x, y] = (255, c[1], 255)
			#print c
			if mode == "encode":
				if (message_index < len(message)):
					#print message[message_index]
					encoded_value = bin(c[2])[:-1] + message[message_index]
					pic[x, y] = (c[0], c[1], int(encoded_value, 2))
					message_index += 1
			else:
				#print chr(pic[x,y][2])
				message += bin(c[2])[-1]
	if mode == "encode":
		extension_index = file_name.find(".")
		if extension_index > 1:
			output_file = file_name[:extension_index]
		else:
			output_file = file_name
		im.save(output_file + ".png")
	else:
		output_message = ""
		for i in range(0, len(message), 8):
			binary_value = '0b' + message[i:i+8]
			if binary_value == '0b00000000':
				break
			output_message += chr(int(binary_value, 2))
		print "message: " + output_message
		with open("output.txt", "w") as f:
			f.write(output_message)

main()

