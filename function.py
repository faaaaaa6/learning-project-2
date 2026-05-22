students =[]

#--- add feature function---

def add_student():
    print("ADD STUDENT, SELECTED")

    name = input("Enter your name :")
    age = int(input("Enter your age :"))

    student = {

        "name": name,
        "age": age
    }

    students.append(student)

    print("successfully added student ")

#---view feature function---

def  view_student():
    print("VIEW STUDENT SELECTED")

    if len(students)==0:
        print("no data found")

    else:
        for student in students:
            print("\nstudent Details")
            print("name:",student["name"])
            print("age",student["age"]) 

#---search feature function---

def search_student():
    print("SEARCH STUDENT SELECTED")

    search_name = input("Enter student name to search:")

    found = False

    for student in students:
        
        if student["name"].lower() == search_name.lower():
            
            print("\nstudent is active")
            print("Name :", student["name"])
            print("Age :",student["age"])

            found =True

    if not found :
        print("student is not active")       

#--delete feature added---

def delete_student():
    print("DELETE STUDENT SELECTED")

    delete_name = input("Enter the name :")

    found=False

    for student in students:
        if student["name"].lower()==delete_name.lower(): 

            students.remove(student)
            print("student deleted successfully")
            found = True
            break                  

while True:
    print("\n---student Management System")
    print("1.add student")
    print("2.view student")
    print("3.search student")
    print("4.delete student")


    choice = int(input("Enter your choice :"))

    if choice == 1:
        add_student()

    elif choice ==2:
        view_student()
    
    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()    

            
        




