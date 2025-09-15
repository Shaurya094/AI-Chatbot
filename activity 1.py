n = input("What is your name?\n")
x = input(f"Hello, {n}! How is your day?\n")
x = x.lower()
x = str(x)
if x == "good":
    print(f"That's great, {n}!")
elif x == "bad":
    print (f"Sorry to hear that, {n}, hope it gets better!")
else:
    print ("I'm not smart enough for that!")