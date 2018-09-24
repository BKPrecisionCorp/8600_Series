import visa

rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])

print(vi.query("*idn?"))
# setup list
vi.write("list:range 30")
vi.write("list:slow 0")
vi.write("list:count 1")
vi.write("list:step 5")

# Set the values
vi.write("list:level 1, 1")
vi.write("list:width 1, 0.1")
vi.write("list:level 2, 2")
vi.write("list:width 2, 0.2")
vi.write("list:level 3, 3")
vi.write("list:width 3, 0.3")
vi.write("list:level 4, 4")
vi.write("list:width 4, 0.4")
vi.write("list:level 5, 5")
vi.write("list:width 5, 0.5")
# Save to slot 3
vi.write("list:save 3")
