import os
print(os.getcwd())
print(os.listdir())
print(os.listdir("Advance python"))
#os.mkdir("projects")--creates a folder named projects.
#import os.makedirs("projects/Python/practice")---makedirs() can create the entire folder path if the parent folders don't already exist.
print(os.path.exists("Advance python/math.py"))#checks whether the path exists
print(os.path.isdir("Advance python"))
print(os.path.isfile("Advance python/math.py"))
path=os.path.join("Advance python","math.py")
print(os.path.isfile(path))
#os.remove("data.txt")--os.remove() deletes a file.
#os.rmdir("projects")--for removing folder
