# This is example code for the BK Precision 8600
# A programming manual for the BK Precision 8600 can be found at:
# https://bkpmedia.s3.amazonaws.com/downloads/programming_manuals/en-us/8600_Series_programming_manual.pdf
# This code has been updated for Python 3

import visa
    
manager = visa.ResourceManager()
print("This Script is made for the BK8600 DC Electronic Load")
manager = visa.ResourceManager()
li = manager.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which Device?: ")
dcload=manager.open_resource(li[int(choice)]) #creates an alias (variable) for the VISA resource name of a device
# we do this so we don't have to call that constantly. This is unique to a unit and changes depending on USB port used and serial number of a unit. 
# This will automatically detect connected devices and allows you to select the one you want to run the script on.


# Set Timeout - 5 seconds
dcload.timeout =  5000
    
dcload.write("*IDN?")   # *IDN? - Query Instrument ID
print(dcload.read())    # Read the result of the query and prints it to the console

dcload.write("FUNC CURR")   # Set the input function to Constant Current Mode
dcload.write("FUNC?")       # Queries the input function of the unit  (CC, CV, CR, CW)	
print(dcload.read())        # Reads the result of the query and prints it to the console

dcload.write("CURR 5")      # Set current that the load will regulate when in constant current mode
dcload.write("CURR?")       # Queries the status of the input
print(dcload.read())        # Reads the result of the query and prints it to the console

# Source Input
dcload.write('INP 1')       # Turns input of the  unit on
dcload.write("INP?")        # Queries the status of the input
print (dcload.read())       # Reads the result of the query and prints it to the console

    
# Close Connection
dcload.close()
print('close instrument connection')

# perform clean up operations
print('complete')
