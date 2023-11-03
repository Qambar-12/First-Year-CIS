""" Program : Slicing statements """
#Slicing statements
string = "COMPUTERPROGRAMMING"
print(string[3:8]) #PUTER
print(string[-8:-3]) #GRAMM
print(string[8:15]) #PROGRAM
print(string[:8]) #COMPUTER
#Extended Slicing statements
print(string[7:2:-1]) #RETUP
print(string[-4:-9:-1]) #MMARG
print(string[-5:-12:-1]) #MARGORP
print(string[-12:-20:-1]) #RETUPMOC
#Pattern
string = "COMPUTERS"
for count in range(len(string)):
    print(string[count:len(string)])
