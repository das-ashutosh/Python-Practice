filename = input("Enter a file name: ")
if "." in filename:
    extension = filename.split(".")[-1]
    print("File extension:", extension)

    if extension == "py":
        print("This is a Python file.")
    elif extension == "java":
        print("This is a Java file.")
    elif extension == "jpg" or extension == "png":
        print("This is an image file.")
    elif extension == "pdf":
        print("This is a PDF file.")
    else:
        print("Unknown file type.")
else:
    print("The file has no extension.")
