aswer = input("Greeting: ").lower().strip()

if aswer.startswith("hello"):
    print("$0")
elif aswer.startswith("h"):
    print("$20")
else:
    print("$100")
