import time
import visa
rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])

print(vi.query("*idn?"))
vi.write("FUNC CURR")
vi.write("trace:clear")
vi.write("trace:feed two")
vi.write("trace:feed:control next")
#vi.write("trace:points 100")
vi.write("TRACE:TIMER 0.005")
#vi.write("TRAN ON")
#vi.write("CURR:TRAN:MODE TOGG")
#vi.write("CURR:SLEW MIN")
#vi.write("CURR:TRAN:ALEV 0")
#vi.write("CURR:TRAN:BLEV 1") #my power supply is small...

vi.write("source:input:state ON")
input("set the transient rate to slow, from fast: [enter] to continue")

vi.write("trig:imm")
time.sleep(3) # The trace data is a live buffer now
                # so we need to wait till the transient is finished.
print(vi.query("TRACE:DATA?"))

vi.write("source:input:state off") # turn off the output
