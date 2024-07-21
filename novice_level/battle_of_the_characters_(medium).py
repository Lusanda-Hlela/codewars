def battle(x: str, y: str) -> str:
    # Determining the sum of the first argument: x
    
    # Lower Cases
    lower_case = dict()
    count = 0
    for i in range(ord("a"), ord("z") + 1):
        count += 0.5
        lower_case[chr(i)] = count
    
    # Upper Cases
    upper_case = dict()
    count = 0
    for i in range(ord("A"), ord("Z") + 1):
        count += 1
        upper_case[chr(i)] = count
    
    x_list_letters = list(x)
    x_list_numbers = []
    x_sum = 0
    
    for i in x_list_letters:
        if i.islower():
            lower_value = lower_case[i]
            x_sum += lower_value
            x_list_numbers.append(lower_value)
        else:
            upper_value = upper_case[i]
            x_sum += upper_value
            x_list_numbers.append(upper_value)
            
    # Determining the sum of the second argument: y
    y_list_letters = list(y)
    y_list_numbers = []
    y_sum = 0