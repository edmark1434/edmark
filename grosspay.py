employee = []
hours = []
rates = []
gross_pay = []
for i in range(2):
    employee.append((input(f"Enter employee {i+1}: ")))
    hours.append(float(input(f"Enter hours spend: ")))
    rates.append(float(input(f"Enter hours rate: ")))
    if hours[i] > 40:
        gross_pay.append((hours[i] * rates[i]) + ((hours[i] - 40)) * rates[i] * 1.5)
    else:
        gross_pay.append(hours[i] * rates[i])
for i in range(2):
    print(f"Employee: {employee[i]}")
    print(f"Hours Spend: {hours[i]}")
    print(f"Gross Pay: {gross_pay[i]}")
