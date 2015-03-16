import struct
with open("control.img", "rb") as f:
	byte = f.read(2)
	image_num = 0
	while byte != "":
		if byte == '\xff\xd8':

			'''
				FIRST ALGORITHM
			'''
			'''string = byte
			while byte != '\xff\xd9':
				if byte == '\xff\xd8':
					string = byte
				else:
					string += byte
				byte = f.read(2)
			string += byte
			with open("image" + str(image_num) + ".jpg", "wb") as o:
				o.write(string)'''
			'''
				END
			'''
			'''
				SECOND ALGORITHM
			'''
			'''with open("image" + str(image_num) + ".jpg", "wb") as o:
				while byte != '\xff\xd9':
					o.write(byte)
					byte = f.read(2)
				o.write(byte)'''
			'''
				END
			'''
			'''
				THIRD ALGORITHM
			'''
			
			string = byte
			byte = f.read(2) #app1 tag
			string += byte
			byte = f.read(2) #size of exif data
			string += byte
			for x in range(struct.unpack("<H", byte)[0]):
				byte = f.read(2) #exif data
				string += byte

			while byte != '\xff\xd9':
				byte = f.read(2)
				string += byte
			with open("image" + str(image_num) + ".jpg", "wb") as o:
				o.write(string)
			
			'''
				END
			'''
			image_num += 1
		byte = f.read(2)