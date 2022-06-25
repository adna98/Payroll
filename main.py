wh = input("Pleas enter your working hours for this month\n")  # Asking from the user to enter working hours
wh_number = float(wh)  # casting
wd = wh_number/8    # Based of the working hours we calculate working days with full time
wd_number = float(wd)
currency = "KM"
hourly_rate = 7.5  # This is usually defined in employee contract.


def salary(wh_number):
    return f"For {wh_number} working hours, your salary is {wh_number*hourly_rate}  {currency} "


total_salary = salary(wh_number)
print(total_salary)

vacation = input("Pleas enter the number of your vacation days in this month\n")
vacation_number = int(vacation)
field_fee = input("Pleas enter your field days for this month\n")
field_fee_number = int(field_fee)
food = 9  # This is a daily payment for your mael
transport = 83  # This is fee for the transport ticket
field_per_day = 25  # This amount of money is paid per day on field


def total(field_fee_number):
    if field_fee_number >= 1:
        return f"Total salary is {wd_number*food+transport+wh_number*hourly_rate+field_fee_number*field_per_day-vacation_number*food} {currency}"
    else:
        return f"Your salary is {wd_number*food+transport+wh_number*hourly_rate-vacation_number*food} {currency}"


total_number = total(field_fee_number)
print(total_number)

Q_input = input("Do you want to know your finance stability (Answer this question with yes or no) \n")
Q1 = "yes"
Q2 = "no"


if Q_input == Q1:
    user_input = input("Pleas enter your total salary to know your finance stability\n")
    user_input_number = float(user_input)


    def answare(user_input_number):
        if user_input_number > 1667:  # this is the average gross salary in FBiH for 04/2022
            return "Your salary is bigger then average gross salary in FBiH this days\n" \
                   "Congratulations, and wish you much more success in your future career"
        elif user_input_number <= 1000:
            return "I am really sorry, but your salary is much below average gross salary in FBiH\n " \
                   "I belive that you can do it better!\n" \
                   "Good luck with finding new job!"
        else:
            return "Your salary is below average gross salary in FBiH"


    final_answare = answare(user_input_number)
    print(final_answare)
elif Q_input == Q2:
    print("Thank you for using this program, I hope you found it useful")
else:
    print("Your answer is not complete please enter yes or no")
