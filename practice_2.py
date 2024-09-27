# practice 2
#initialize value dictionary inside list
studend_list = [
    {"name": "Professor X", "roll_number": 101, "mark": 1.0},
    {"name": "Jean Grey", "roll_number": 102, "mark": 1.4},
    {"name": "Storm", "roll_number": 103, "mark": 1.5},
    {"name": "Gambit", "roll_number": 104, "mark": 2.6},
    {"name": "Cyclops", "roll_number": 105, "mark": 1.5},
]
#loop until the person input 8 or exit
while True:
    print("Student Record System!")
    print("[1].Add a Student")
    print("[2].Remove a Student")
    print("[3].Update student marks")
    print("[4].Display all students record")
    print("[5].Display the average of all students")
    print("[6].Display the number of students")
    print("[7].Search for a student by their roll")
    print("[8].Exit the system.")
    choi = int(input("Enter your choice: "))
    # add student
    if choi == 1:
        roll_number_list=[]  #list to store all roll number
        name = input("Enter name: ").title() #input name
        for i in studend_list: #storing all rollnumber exist
            roll_number_list.append(i["roll_number"]) 
        while True: #looping for input of roll number
            roll_number = int(input("Enter roll_number: "))
            if roll_number in roll_number_list: # loop if the roll number add already exisy
                print('Already Exist! Try Again!')
            else:
                break #if the rollnumber  not exist
        mark = float(input("Enter Mark: ")) #adding mark
        studend_list.append({"name": name, "roll_number": roll_number, "mark": mark}) #append add student records to student list
        print("Successfully Added!")
        print()
    elif choi == 2: #remove a student by roll number
        remove = 0 #setting remove to 0
        removed_stud = int(input("Enter student roll number to removed student: ")) #input roll number to remove
        for i in studend_list:#loop all dictionary in list
            if removed_stud == i["roll_number"]:# if input rollnumber equals to roll number exist in the list
                studend_list.remove(i) #this will remove student record with a roll number input
                print(f'Student {i["name"]} with roll number {removed_stud} Successfully Removed!') #display if successfully removed
                remove += 1 #setting remove to 1
        if remove == 0: #conditon if the roll number is not found or exist
            print(f"Student roll number {removed_stud} not found!") #display if not found
        print()
    elif choi == 3: # update students mark
        update = 0 #setting update to 0
        update_rollnum = int(input("Enter roll number to update student marks: ")) #input roll number
        for i in studend_list: #looping to find the roll number
            if update_rollnum == i["roll_number"]: #if the input roll number is equal to rollnumber in list
                i['mark'] = float(input(f'Enter update mark for student {i['name']}: ')) #it will overwrite the mark of a student with the input roll number
                print(f'Successfully Updated student {i["name"]} mark!')#display if successfully updated
                update+=1 #setting to 1
        if update ==0: #condition if the roll number exist
            print(f'roll number {i['roll_number']} is not found!')
        print()
    elif choi == 4: #Display all students record
        for i in studend_list:
            print(f'Student Name: {i['name']}, Roll Number: {i['roll_number']}, Mark: {i["mark"]}')#display
        print()
    elif choi == 5: #display the average of all students
        sum_all_studmark =0 #initialize the sum to 0
        for i in studend_list:
            sum_all_studmark+= i["mark"] #adding the marks of each students
        average = sum_all_studmark/len(studend_list) #calculating average
        print(f'The average of all student is {average:.1f}') #display average of all students
        print()
    elif choi == 6:#display number of student
        print(f'There are {len(studend_list)} students in total') #display
        print()
    elif choi == 7: #seach for student
        search=0 #initialize search to 0
        search_rollnum= int(input('Enter roll number of a student:')) #input roll num
        for i in studend_list:
            if search_rollnum == i["roll_number"]:#condition if rollnum exist
                print(f'Student Name: {i['name']}, Roll Number: {i['roll_number']}, Mark: {i["mark"]}')#display student record
                search+=1 #setting search to 1
        if search ==0:#condition if roll num does not exist or found
            print(f"Student roll number {removed_stud} not found!") #display
        print() 
    elif choi == 8: #exit
        print('Exiting, Thank you for using!')
        break
    else: #if the input is not in the choices
        print("Invalid Input!")#this will display
        print()
    # print() for spacing after each loop
