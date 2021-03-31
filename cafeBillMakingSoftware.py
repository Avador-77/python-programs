def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if(food_type == "V"):
        if(quantity_ordered >= 1):
            
            if(distance_in_kms >0 and distance_in_kms <= 3):
                bill_amount = (120 * quantity_ordered) + (distance_in_kms * 0)
            elif(distance_in_kms > 3 and distance_in_kms <=6):
                distance_in_kms -= 3
                bill_amount = (120 * quantity_ordered) + (distance_in_kms * 3)
            elif(distance_in_kms > 6):
                distance_in_kms -= 6
                bill_amount = (120 * quantity_ordered) + 9 + (distance_in_kms * 6)
        else:
            bill_amount = -1
    elif(food_type == "N"):
        if(quantity_ordered >= 1):
            
            if(distance_in_kms >0 and distance_in_kms <= 3):
                bill_amount = (150 * quantity_ordered) + (distance_in_kms * 0)
            elif(distance_in_kms > 3 and distance_in_kms <=6):
                distance_in_kms -= 3
                bill_amount = (150 * quantity_ordered) + (distance_in_kms * 3)
            elif(distance_in_kms > 6):
                distance_in_kms -= 6
                bill_amount = (150 * quantity_ordered) + 9 + (distance_in_kms * 6)
        else:
            bill_amount = -1
    else:
        bill_amount = -1
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,8)
print(bill_amount)