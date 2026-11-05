def load_file(path):
    try :
       file = open(path,"r")
       lines = file.readlines()
       file.close()
       
       result =[]
       for line in lines:
           result.append(line.rstrip("\n"))
       return result
    except OSError:
        print("Could not open the file.")
        return[]
