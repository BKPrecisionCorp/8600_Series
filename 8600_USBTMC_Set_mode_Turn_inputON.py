import visa
    
try:
    manager = visa.ResourceManager()
    manager.list_resources()
      
    dcload = manager.open_resource("USB0::0xFFFF::0x8800::602197010697010001::INSTR")

    #Set Timeout - 5 seconds
    dcload.timeout =  5000
    
    dcload.write("*IDN?")    #*IDN? - Query Instrument ID
    print dcload.read()#Read the result of the query and prints it to the console

    dcload.write("FUNC CURR")   # Set the input function to Constant Current Mode
    dcload.write("FUNC?") #Queries the input function of the unit  (CC, CV, CR, CW)	
    print dcload.read() #Reads the result of the query and prints it to the console

    dcload.write("CURR 5") # Set current that the load will regulate when in constant current mode
    dcload.write("CURR?") #Queries the status of the input
    print dcload.read() #Reads the result of the query and prints it to the console

    #Source Input
    dcload.write('INP 1') #Turns input of the  unit on
    dcload.write("INP?") #Queries the status of the input
    print dcload.read() #Reads the result of the query and prints it to the console

    
    #Close Connection
    dcload.close()
    print 'close instrument connection'

finally:
    #perform clean up operations
    print 'complete'
