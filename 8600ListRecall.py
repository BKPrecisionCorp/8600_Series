import visa

rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])

print(vi.query("*idn?"))

# Create a list
vi.write("list:rcl 3")

print("Number of steps: ", vi.query("list:step?"))
print("Slow slew?: ", vi.query("list:slow?"))
print("Repeat count: ", vi.query("list:count?"))
for i in range(1,6,1):
    step = "list:level? "+str(i)
    width = "list:width? "+str(i)
    print("Step ",str(i), " level: ",vi.query(step), "Width: ", vi.query(width))
