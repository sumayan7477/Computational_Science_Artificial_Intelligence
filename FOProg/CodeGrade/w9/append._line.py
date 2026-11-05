def append_line(path, text):
    try:
        file = open(path , "a")
        file.write(text + "\n")
        file.close()
    except OSError:
        print("Could not write to the file.")
