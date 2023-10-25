def length_of_last_word(s):
    words = s.split()
    
    if len(words) == 0:
        return 0
    
    return len(words[-1])

while True:
    words = input("Enter a string: ")
    
    if len(words) == 0:
        print("Error: input string cannot be empty.")
    elif not all(c.isalpha() or c.isspace() for c in words):
        print("Error: input string must contain only letters and spaces.")
    else:
        print("Length of last word:", length_of_last_word(words))
        break