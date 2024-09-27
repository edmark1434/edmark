print("Patient Record Management System!")  # title
# initialize Student_data list with 5 dictionary patient records
Student_data = [
    {"name": "Luke Skywalker", "Patient ID": 1010, "Diagnosis": "Force Fatigue"},
    {"name": "Darth Vader", "Patient ID": 1011, "Diagnosis": "Respiratory Issues"},
    {"name": "Leia Organa", "Patient ID": 1012, "Diagnosis": "Stress Disorder"},
    {"name": "Yoda", "Patient ID": 1013, "Diagnosis": "Age-related Health Decline"},
    {"name": "Han Solo", "Patient ID": 1014, "Diagnosis": "Blaster Burn"},
]
while True:  # condition for loop, stops if user exits or press 8
    print("[1]. Add Patient")
    print("[2]. Remove a Patient")
    print("[3]. Update patient")
    print("[4]. Display All Patient")
    print("[5]. Search Patient")
    print("[6]. List Patients with Diagnosis")
    print("[7]. Show total number of patient")
    print("[8]. Exit the system")
    choice = int(input("Enter your choice: "))  # input choice
    if choice == 1:  # condition for 1
        patientid_list = []  # create a list for all exist patient id
        for i in Student_data:
            patientid_list.append(i["Patient ID"])  # store all patient id
        patient_name = input("Enter Patient name: ")  # add name
        while True:
            patient_id = int(input("Enter Patient Id: "))  # add patient id
            if patient_id in patientid_list:  # condition check if the id exist
                print("Id already Exist. Try again")  # if it exist it will ask again
            else:  # if patient id does not exist it will break
                break
        patient_diag = input("Enter Patient Diagnos: ")  # input diagnosis
        Student_data.append(
            {"name": patient_name, "Patient ID": patient_id, "Diagnosis": patient_diag}
        )  # store and added to student list
        print("Successfully Added to the System!")
        print()
    elif choice == 2:
        remove = 0  # initialize remove as 0
        patient_id = int(input("Enter Patient Id: "))  # input patient id
        for i in Student_data:  # loop to find the if exist
            if (
                patient_id == i["Patient ID"]
            ):  # condition if id input exist or equals to existing patient id
                Student_data.remove(i)  # remove the records of a patient
                remove += 1  # set 1 means successfully remove or id exist
                print("Successfully removed patient {}".format(i["name"]))  # display
        if remove == 0:  # condition to check if the id exist
            print(f"{patient_id} does not exist")
        print()
    elif choice == 3:  # condition to choices 3
        update = 0  # initialize update to 0
        patient_id = int(input("Enter Patient Id: "))  # patient id input
        for i in Student_data:  # loop to find the id
            if (
                patient_id == i["Patient ID"]
            ):  # condition if the found id is equals to input id
                i["Diagnosis"] = input(
                    f"Enter Diagnosis of patient {patient_id}: "
                )  # update or overide existing patient diagnosis
                print(
                    f"Successfully Updated Diagnosis of patient {patient_id}"
                )  # display
                update += 1  # id found
        if update == 0:  # condition to check if the id exist
            print(f"patient {patient_id} does not exist")
        print()
    elif choice == 4:  # choices 4 condition
        for i in Student_data:  # display all the records of patient registered
            print(
                "name: {} | Patient id: {} | Diagnosis: {}".format(
                    i["name"], i["Patient ID"], i["Diagnosis"]
                )
            )
        print()
    elif choice == 5:  # searching patient record by id
        search = 0  # intialize search to 0
        patient_id = int(input("Enter Patient Id: "))
        for i in Student_data:  # loop to find id
            if (
                patient_id == i["Patient ID"]
            ):  # condition if the patient id is equals to found id
                print(
                    "name: {} | Patient id: {} | Diagnosis: {}".format(
                        i["name"], i["Patient ID"], i["Diagnosis"]
                    )
                )  # display
                search += 1  # id found
        if search == 0:  # condition to check if the id exist
            print(f"{patient_id} does not exist")
        print()
    elif choice == 6:
        diag = 0
        patient_diag = input("Enter Diagnosis: ")  # input diagnosis
        for i in Student_data:  # loop to print all patient with same diagnosis
            if (
                patient_diag == i["Diagnosis"]
            ):  # condition check the patient with the diagnosis input
                print(
                    "name: {} | Patient id: {} | Diagnosis: {}".format(
                        i["name"], i["Patient ID"], i["Diagnosis"]
                    )
                )
                diag += 1
        if diag == 0:  # check if there is a patient diagnos with the input diagnosis
            print(f"No patient with {patient_diag} found")
        print()
    elif choice == 7:  # display current number of patient
        print(f"There are {len(Student_data)} number of patients in total")
        print()
    elif choice == 8:  # exits
        print("Exiting! Thank you for Using!")
        break  # it will break loop and exits
    else:
        print("Invalid Input!")  # print if the input of choices is invalid
        print()  # to add spaces every loop
