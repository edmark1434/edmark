from statistics import mean #import mean from statistics library
record = [# initialize dictionary inside list
    ["Dan", {"Math": 90, "English": 90, "Science": 90}],
    ["Jayson", {"Math": 90, "English": 89, "Science": 87}],
    ["Jm", {"Math": 99, "English": 97, "Science": 85}],
]

#fuction in adding student
def add_stud(student, subject):
    record.append([student, subject])
    print(f"Student {student} successfully added in Record!".title())
#function in checking if student exist
def exist(student):
    exist=0
    for i in record:
        if student == i[0]:
            exist+=1
    if exist==0:
        print(f'Student {student} does not exist')
#function in removing and updating
def action_stud(student,action):
    #if action == remove
    if action.title() =="Remove":
        for i in record:
            if student == i[0]:#check if student exist
                record.remove(i)#if found it remove the record of the student
                print(f'Successfully Remove Student {student}')
    elif action.title() =="Update":#if update
        subj_exist = []
        for i in record:
            subj_exist.extend(i[1]) #getting the existing subject
            if student == i[0]:#check if student exist
                choice = input('Enter your choice of update subject (All/manual): ')#ask user if all grade to update or not
                if choice == 'All':
                    math, english, science = map(
                        int,
                        input(
                            "Enter grades for math, english and science(example : 90 89 90): "
                        ).split(), #input 3 grades in one prompt and using split and map to assigned it to the variable
                    )
                    i[1]['Math'],i[1]['English'],i[1]["Science"] = math,english,science #updating each grade
                    print(f'Student {student} successfully updated his Math, English, and Science grades!')
                elif choice.title() =='Manual':    #if manual it will ask for subject to update           
                    while True:#check if the subject exist
                        subject_name = input("Enter Subject: ").capitalize()
                        if subject_name not in list(set(subj_exist)):#if subject input is not in list it will ask again
                            #explanation for this, so i created list for getting the subject , if ever the subject of each dictionary is not same it will be the perfect way to store a subject without duplicat
                            #i write set to remove duplicate
                            print("Subject doesnt Exist!, Try Another!")
                        else:
                            i[1][subject_name]= int(input(f'Enter grade for Subject {subject_name}: '))#if found ask for grade for the subject and updated the grade
                            print(f'Student {student} successfully updated his {subject_name} grade!')
                            break
        exist(student) #function call of the exist function that checks if the student exist

def average(x): #function getting average of all subject
    ''' sum=0  #manual of getting average
    ave=0
    for k,v in x[1].items():  
        sum+= v
    ave= sum/len(x[1])
    return x[0],ave'''
    return x[0],mean(x[1].values()) #getting average
def display_ave(ave):#display average
    for i,v in ave.items():
        print(f'Student {i}\t Average: {v:.2f}')
def display():#display records
    for i in record:
        print(f'Student Name: {i[0]}\t Math: {i[1]['Math']}\tEnglish: {i[1]['English']}\tScience: {i[1]['Science']}')

while True: #condtion for loop
    #menu driven
    print("\nStudent Record Management System!")
    print("[1]. Add New Student")
    print("[2]. Remove Student")
    print("[3]. Update Grade")
    print("[4]. Average of the Student")
    print("[5]. Display all students")
    print("[6]. Total number of the students")
    print("[7]. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:#add student
        name_exist = []
        for i in record:
            name_exist.append(i[0]) #storing existing name
        while True:
            student_name = input("Enter Student: ")
            if student_name in name_exist:# check if the student exist in a list of names
                print("Student Already Exist!, Try Another!") #if exist it will ask again for other name that does not exist
            else:
                break #if student is new then it will break
        math, english, science = map(
            int,
            input(
                "Enter grades for math, english and science(example : 90 89 90): "
            ).split(), #getting the grade for math, english and science
        )
        #function calling of add_stud function
        add_stud(student_name, {'Math':math,'English':english,'Science':science})
    elif choice == 2:# remove a student record based on input student
        action = 'remove' #set as remove action
        student_name = input("Enter Student: ") #ask for student to remove
        action_stud(student_name,action)#function calling action_stud
    elif choice == 3:#update grade
        action = 'update' #setting as update
        student_name = input("Enter Student: ") #ask for student to update
        action_stud(student_name,action) #function calling of action_stud
    elif choice == 4:#getting the average
        average1 = dict(map(average,record)) #using map to calculate the average and calling function average
        display_ave(average1) #function calling of display_ave
    elif choice == 5:#display student record
        display()#function calling
    elif choice == 6:#getting the total student that has record using len of a record list
        #explanation because each element in record list is equivalent to 1 student
        print(f'The total Student that has records is {len(record)}')
    elif choice == 7: #exiting 
        print("' thank you for using our system'".upper())
        break #exiting and breaking the loop
    else: #if the user input something that is not in menu
        print("Invalid Input, Try Again!")
