def reverse_string(s):
    my_string = s
    reversed_string = my_string[::-1]
    print(f'{my_string} in reverse is:\n {reversed_string}')
        

def capitalize_string(s):
    my_string = s
    capitalized_string = my_string.capitalize()
    print(f'{my_string} capitalized is:\n {capitalized_string}')

def capitalize_every_other_letter(s):
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    return print(''.join(result))