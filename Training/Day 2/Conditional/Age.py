a=int(input())
if a<18 :
    print("Not allowed")
else:
    print("You're allowed")
    if a>75:
        print("Risk for life")
    elif a>40:
        print("Panic attack")
    elif a > 25:
        print("No nonsense things")
    elif a>18 and a<25:
        print("Dont scream")