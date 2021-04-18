################################
# Michael D. McKinney          #
# QR Encoding                  #
# December 31, 2020            #
################################

# A simple utility to take user's input and encode it into QR code 
# and save it as a PNG or a SVG (or both), as well as outputting it to terminal.  

#Requires pyqrcode and pypng modules.  
import pyqrcode
import png

from pyqrcode import QRCode

#Opening
print("\n\n\n\t\tQR CODE GENERATOR\n\n\n")

qr_string = ''
qr_version = ''
qr_error = ''

while True:

	if qr_string == '':
		qr_string = input("Enter the string you want to encode into QR code: ")

	if qr_version == '':
		qr_version = input("\nEnter the version you would like to use."
			"\n(1-40, 1 is smallest and 40 is largest): ")
		try:
			qr_version = int(qr_version)
		except ValueError:
				print("That wasn't a valid version input.")
				qr_version = ''
				continue
	
	if qr_version < 1 or qr_version > 40:
		print("That wasn't a valid version input.")
		qr_version = ''
		continue

	if qr_error == '':
		qr_error = input("\nEnter the error level you would like to use."
			"\n(L (7%), M (15%), Q (25%), H (30%)): ")
		qr_error = qr_error.lower()
		if qr_error != 'l' and qr_error != 'm' and qr_error != 'q' and qr_error != 'h':
			print("Not a valid error level.")
			qr_error = ''
			continue 	

	output = input("\nSave the output as PNG? " )
	if output == 'yes' or output == 'ye' or output == 'y':
		qr_output = pyqrcode.create(qr_string, error=qr_error, version=qr_version, mode='binary')
		qr_output.png('qr-output.png', scale=6, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xff])
		output = ''
		print("\nSaved the output to qr-output.png.")

	output = input("\nSave the output as SVG? " )
	if output == 'yes' or output == 'ye' or output == 'y':
		qr_output = pyqrcode.create(qr_string, error=qr_error, version=qr_version, mode='binary')
		qr_output.svg('qr-output.svg', scale=6)
		output = ''
		print("\nSaved the output to qr-output.svg.")

	output = input("\nDo you want to print QR code out in terminal? " )
	if output == 'yes' or output == 'ye' or output == 'y':
		# Print QR code out in terminal.
		qr_output = pyqrcode.create(qr_string, error=qr_error, version=qr_version, mode='binary')		
		text = qr_output.terminal()
		print(text)

	break

	


	
