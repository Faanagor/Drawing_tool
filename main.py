from input_file import InputFile


def main():
    path_file = 'input.txt'
    InputFile1 = InputFile(path_file)
    line = InputFile1.read_file()
    canvas_created = False
    list_result = []
    list_result.append(canvas_created)
    for number_line in range(len(line)):
        list_line = []
        error = InputFile1.validate_commands(line[number_line], number_line)
        if error == True:
            break
        list_line = line[number_line].split(" ")
        list_result = InputFile1.selector(list_line, list_result)


if __name__ == "__main__":
    main()
