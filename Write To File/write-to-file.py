print("-----Write To A File-----")
data = input("Please input that data you want written to a file:\n")
f = open("Info_Output.txt","w")
f.write(" " +data)
f.close()
print("Printing Input")
r = open("Info_Output.txt","r")
print(r.read())
r.close()