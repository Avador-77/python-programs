def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    
    rate_per_adult = 37550.0
    
    rate_per_child = (1/3) * rate_per_adult
    
    total_adults_rate = no_of_adults * rate_per_adult
    
    total_child_rate = rate_per_child * no_of_children
    
    ticket_amount = total_adults_rate + total_child_rate
    service_tax = (0.07 * ticket_amount) + ticket_amount
    discount = 0.1 * service_tax
    total_ticket_cost = service_tax - discount
    
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)