#PF-Assgn-20

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    
    if(account_number >= 1000 and account_number <= 1999):
        if(account_balance >= 100000):
            if(loan_type == "Car" and (salary > 25000 and salary < 50000)):
                if(loan_amount_expected <= 500000 and customer_emi_expected <= 36):
                    eligible_loan_amount = 500000
                    bank_emi_expected = 36
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif(loan_type == "House" and (salary > 50000 and salary < 75000)):
                if(loan_amount_expected <= 6000000 and customer_emi_expected <= 60):
                    eligible_loan_amount = 6000000
                    bank_emi_expected = 60
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            elif(loan_type == "Business" and (salary > 75000)):
                if(loan_amount_expected <= 7500000 and customer_emi_expected <= 84):
                    eligible_loan_amount = 7500000
                    bank_emi_expected = 84
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        
        else:
            print("Insufficient account balance")
    
    else:
        print("Invalid account number")
        


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)