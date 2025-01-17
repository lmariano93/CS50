file = input("File name: ").lower().strip()

_, _, example = file.rpartition(".")

if file.endswith((".gif",".png")):
    print(f"image/{example}")
elif file.endswith((".pdf",".zip")):
    print(f"application/{example}")
elif file.endswith((".jpg",".jpeg",)):
    print(f"image/jpeg")
elif file.endswith(("txt")):
    print("text/plain")
else:
    print("application/octet-stream")


