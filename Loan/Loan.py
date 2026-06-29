#Mark Lorenz P.Natividad
#1ICT-105

try:
    salary = int(input("Please provide annual salary: "))

    if (salary >= 30000):
        years_worked = int(input("Please provide years on the job: "))
        if(years_worked >= 2):
            print("You are qualified of the highest loan.")
        else:
            print("You must be employed for at least 2 years to avail of the loan.")
    elif ((salary >= 15000) and (salary < 29000)):
        years_worked = int(input("Please provide years on the job: "))
        if (years_worked >= 2):
            print("You are qualified to avail of the lowest-range loan.")
        else:
            print("You must be employed for at least 2 years to avail of the loan.")
    else:
        print("You must earn at least Php 30,000.00 to avail of the loan.")

except ValueError:
    print("That is an invalid input.")

print("\n***************************************************End of first problem.***************************************************\n")












