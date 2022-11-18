# Name: Pratham Garg
# ID: 2110994808

import smbus				# library to access I2C devices
from time import sleep		# import sleep(delay) function from time library

Address = 0x23				# variable to store the address of the I2C device. This is the default address
bus = smbus.SMBus(1)		# create object of SMBus class to access I2C based Python function

try:
	while True:
		data = bus.read_i2c_block_data(Address, 0x23, 2) # This function is used to read a block of 32 bytes. here it reads 2 bytes of data
		
		intesity = int.from_bytes(data, "big", signed=False) # this fuction converts the array of 2 bytes to integer value
		
		# set the parameters to print the brightness according to sensor value
		if intesity >= 1000:
			level = 'too bright'
		elif intesity < 1000 and intesity >= 750:
			level = 'bright'
		elif intesity < 750 and intesity >= 500:
			level = 'medium'
		elif intesity <500 and intesity >= 250:
			level = 'dark'
		else:
			level = 'too dark'
		
		print('Light is', level, ':', intesity, 'lx')	# print the light brightness with the intesity
		sleep(0.5) 			# delay of half second
    
except KeyboardInterrupt:			#code stops id ctrl+c is pressed on keyboard
    GPIO.cleanup()
