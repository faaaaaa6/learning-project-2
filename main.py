students=[]

while True:
    print("\n---Student Management Sytstem---")
    print("1.add student")
    print("2.View Students")
    print("3.search student")
    print("4:delete student")
    print("5:Update student")
    print("6.Exit")

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
         print("SEARCH STUDENT SELECTED")

         search_name = input("Enter student name to search: ")

         found = False

         for student in students:

             if student["name"].lower() == search_name.lower():

                 print("\nStudent is active")
                 print("Name:",student["name"])
                 print("Age:",student["age"])

                 found =True

         if not found:
             print("Student is not active")

    elif choice == 4:
         print("SELECTED DELETING OPTION")

         delete_name = input("Enter the student name to delete :")

         found=False

         for student in students:
             if student["name"].lower() == delete_name.lower():

                 students.remove(student)
                 print("student deleted successfully")
                 found = True
                 break

         if not found:

             print("there is no data") 

    elif choice == 5:
         print("UPDATE STUDENT SELECTED")

         update_name = input("Enter student name to update :")

         found = False

         for student in students:

             if student["name"].lower() == update_name.lower():

              new_name = input("Enter new name:")
              new_age = int(input("Enter new age:"))


              student["name"] = new_name
              student["age"] = new_age

              print("student updated successfully")

              found = True

              break

         if not found:
             print("student not found")
    elif choice == 6:

         print("PROGRAME EXIT")

         break   
    else:
         print("invalid operation")    


                

