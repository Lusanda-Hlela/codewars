def to_jaden_case(string):
    # Format the string to lowercases & create a list
    lower_case = string.split()
    capitalized_words = []

    for i in lower_case:
        capitalized_words.append(i.capitalize())

    # Create a string of all capitalized words
    answer = " ".join(capitalized_words)

    return answer