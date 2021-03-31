def scholarship(course_fee, marks, extra_fees):

    scholarship_percentage = marks/2

    scholarship_amount = (scholarship_percentage/100) * course_fee

    course_fee = course_fee - scholarship_amount

    amount_payment = course_fee + extra_fees

    return amount_payment

final_payment = scholarship(25000, 70, 1500)

print(final_payment)