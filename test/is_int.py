def is_int(list_with_number):
    string_to_int = True
    for i in list_with_number:
        string_to_int = i.isnumeric()
        if string_to_int == False:
            return string_to_int
    return string_to_int
        
    