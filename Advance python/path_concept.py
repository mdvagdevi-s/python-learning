from pathlib import Path

path = Path("Advance python")
for item in path.iterdir():
    print(item)

for file in path.glob("*.py"):
    print(file)

a=Path("student.txt")
content=a.read_text()
print(content)

a.write_text("Hello Python")

#unlink() → deletes the file.

#path = Path("projects")
#path.mkdir()

#path = Path("A/B/C")
#path.mkdir(parents=True)