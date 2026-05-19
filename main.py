students=[]

while True:
    print("\n---Student Management Sytstem---")
    print("1.add student")
    print("2.View Students")
    print("3.Exit")

    choice=int(input("Enter your choice :"))

    if choice == 1:
        print("ADD STUDENT SELECTED")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))

        student = {
             
             "name": name,
             "age": age
        }

        students.append(student)

        print("student added successfully") 
    elif choice == 2:
        print("VIEW STUDENT SELECTED")

        if len(students) ==0:
           print("no student data found")

        else:
            for student in students:
                print("\nStudent Details")
                print("Name:",student["name"])
                print("age",["age"])       

    elif choice == 3:
        print("PROGRAME EXIT")

        break   
    else:
        print("invalid operation")    


                

                