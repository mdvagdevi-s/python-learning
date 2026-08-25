students = [
    {"id": 1, "name": "Priya", "branch": "CSE", "marks": 91},
    {"id": 2, "name": "Rahul", "branch": "ISE", "marks": 85}
]
def add_students():
    found=False
    ID=int(input("Enter ID:"))
    for n in students:
        if ID==n["id"]:
            found=True
            break
    if found:
        print("Already exist")

    else:
        print("You can add this student")

        user_profile={}
        user_profile["id"]=ID
        user_profile["name"]=input("Enter name:")
        user_profile["branch"]=input("Enter branch:")
        user_profile["marks"]=int(input("Enter marks:"))
        students.append(user_profile)
        print("Student added successfully",user_profile)


def view_students():
    for n in students:
         print("ID:",n["id"],"| Name:",n["name"],"| Branch:",n["branch"],"| Marks:",n["marks"])


def search_student():
    found=False
    ID=int(input("Enter ID:"))
    for n in students:
        if ID==n["id"]:
            found=True
            print("ID:",n["id"],"|| Name:",n["name"],"|| Branch:",n["branch"],"|| Marks:",n["marks"])
            break
    if not found:
        print("Student not found!")


def update_student():
    found=False
    ID=int(input("Enter ID:"))
    for n in students:
        if ID==n["id"]:
            print("Current student:")
            found=True
            print("ID:",n["id"])
            print(" Name:",n["name"]) 
            print(" Branch:",n["branch"])
            print(" Marks:",n["marks"])
           
            n["name"]=input("Enter new name:")
            n["branch"]=input("Enter new branch:")
            n["marks"]=int(input("Enter new marks:"))
            print("Student updated successfully!")
            break
    if not found:
        print("Student not found!")




def delete_student():
    found=False
    ID=int(input("Enter ID:"))
    for n in students:
        if ID==n["id"]:
            found=True
            students.remove(n)
            print("Student deleted successfully!")
            break
    if not found:
        print("Student not found!")

def calculate_average():
    total=0
    for n in students:
        total+=n["marks"]

    avg=total/len(students)
    print("Average marks:",avg)


def top_student():
    highest=students[0]["marks"]
    topper=students[0]
    for n in students:
        if n["marks"]>highest:
            highest=n["marks"]
            topper=n
    print("Top student is:",topper["name"])
    print("Toppers marks:",highest)


print("\n-----STUDENT MANAGEMENT SYSTEM------")
choice=1
while choice!=8:
    
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Calcualte average")
    print("7. Top student")
    print("8. Exit")

    choice=int(input("Enter Your choice:"))
    print("You selected:", choice)
    if choice==1:
        add_students()
        

    elif choice==2:
        view_students()
          

    elif choice==3:
        search_student()
        

    elif choice==4:
        update_student()
        

    elif choice==5:
        delete_student()
       

    elif choice==6:
        calculate_average()
        

    elif choice==7:
        top_student()
        

    else:
        print("Invalid choice!")