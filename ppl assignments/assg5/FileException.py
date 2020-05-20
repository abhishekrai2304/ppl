try:
    f = open("Demo.txt")
    f.write("Hello")
except:
    print("something went wrong") #this file is readonly
finally:
    f.close()

