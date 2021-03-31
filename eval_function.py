def eval_loop():
    expression = " "
    while expression != "done":
        expression = input("Enter an expression to evaluate: ")
        if expression != "done":
            result = eval(expression)
            print(result,"\n")
            last_result = result
    return last_result

last_expression_value = eval_loop()
print("The value of last expression evaluated was ",last_expression_value)
