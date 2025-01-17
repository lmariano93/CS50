aswer = input ("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
if aswer.strip() == "42":
    print ("yes")
elif aswer.lower().strip() == "forty-two":
    print ("yes")
elif aswer.lower().strip() == "forty two":
    print ("yes")
else:
    print ("no")
