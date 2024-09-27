import math as m

grade1, grade2, grade3, grade4, grade5 = 85.0, 88.0, 75.0, 87.0, 78.0
total = average = variance = 0.0
username = "admin"
password = "admin"
arr = [grade1, grade2, grade3, grade4, grade5]
u = input("Enter Username: ")
p = input("Enter Password: ")
while u == username and p == password:
    choice = 0
    while choice != 6:
        print("[1]. View Grades Data and Statistics")
        print("[2] Add points Data for Grade")
        print("[3] Change Password")
        print("[4] Calculate Variance")
        print("[5] Calculate Standard Deviation")
        print("[6] Exit")
        try:
            choice = int(input("Enter Choices: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer choice.")
            continue
        if choice == 1:
            for i in range(len(arr)):
                print(f"Grade-{i}: {arr[i]}")
            print()
            total = grade1 + grade2 + grade3 + grade4 + grade5
            average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
            print("Sales Data and Statistics:")
            print(f"Total Grades: {total:.1f}")
            print(f"Average: {average:.1f}")
            arr.sort()
            print(f"Highest Grade: {arr[-1]}")
            print(f"Lowest Grade: {arr[0]}")
            print(f"Grade with Above Average: {sum(1 for i in arr if i > average)}")
        elif choice == 2:
            prod_num = int(input("Enter the grade number(1-5): "))
            grade_val = int(input("Enter the grade value: "))
            arr[prod_num - 1] += grade_val
            print(f"Value for grade{prod_num} has been updated")
        elif choice == 3:
            old_pass = input("Enter old password: ")
            if old_pass == password:
                new_pass = input("Enter new password: ")
                password = new_pass
                print("Change password Successfully!")
            else:
                print("Incorrect Password!")
        elif choice == 4:
            sum_sqr = 0
            for i in arr:
                diff = i - average
                sum_sqr += m.pow(diff, 2)
            variance = sum_sqr / len(arr)
            print(variance)
        elif choice == 5:
            standard_dev = m.sqrt(variance / len(arr))
            print(standard_dev)
        elif choice == 6:
            print("Exit")
        else:
            print("Invalid input")
