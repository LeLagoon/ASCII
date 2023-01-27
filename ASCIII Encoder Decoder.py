x = input("Welcome to ASCII Decoder/Encoder. What would you like to do? ")
if x.lower == ("encode"):
    inpe = input("What do you want to encode? ")
    for i in inpe:
        print(ord(i), end=" ")
elif x.lower == ("decode"):
    inpd = input("What would you like to decode? ").split(" ")
    for j in inpd:
        print(chr(int(j)), end=" ")
else:
    print("You can only respond with Encode or Decode")