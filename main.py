# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_all_at_once():
    '''Read all the contents of the file grade_info.txt
    as a string. Check some data types. Print the file contents.'''
    filename = 'grade_info.txt'

    with open(filename) as f_obj:
        contents = f_obj.read()

    print(type(contents))
    print(type(f_obj))
    print(contents)

def read_all_at_once_wrong():
    '''Read all the contents of the file grade_info.txt
    as a string. Check some data types. Print the file contents.'''
    filename = 'siddhartha.txt'

    with open(filename) as f_obj:
        contents = f_obj.read()

    print(type(contents))
    print(type(f_obj))
    print(contents)

def read_with_exception_handling():
    '''Read all the contents of the file grade_info.txt
    as a string. Check some data types. Print the file contents.'''
    filename = 'siddhartha.txt'

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
        print(type(contents))
        print(type(f_obj))
        print(contents)
    except FileNotFoundError:
        print(f"Can't find file {filename}.")



def read_line_by_line():
    '''Read date from the file grade_info.txt line-by-line
    and print it out with the newline character \n stripped
    from the end of each line.'''
    filename = 'grade_info.txt'
    with open(filename) as f_obj:
        for line in f_obj:
            print(line.rstrip())


def store_lines_in_list():
    '''Read the lines from the file credits and store them
    in a list.'''
    filename = 'credits'
    with open(filename) as f_obj:
        lines = f_obj.readlines()
    for line in lines:
        print(line.rstrip())
    print(lines)


def read_and_write_credits():
    '''Read the lines from the file credits and store them
    in a list.'''
    # Store the name of the file in a variable filename.
    filename = 'credits'
    # Read the lines from a file and store them in a list.
    with open(filename) as f_obj:
        lines = f_obj.readlines()
    print(lines)
    credits_string = ''
    credit_numbers = []
    for line in lines:
        credits_for_class = line.rstrip()
        print(credits_for_class)
        print(type(credits_for_class))
        credit_numbers.append(int(credits_for_class))
        credits_string += credits_for_class + ','
    print(credit_numbers)

    output_file = 'credits_results.txt'
    # Pass the 'w' argument to open() to indicate
    # we will write to an empty file.
    with open(output_file, 'w') as f:
        # As an alternative to print, we can
        # write a string to the file.
        f.write(credits_string + '\n')
        f.write(f'Total credits: {str(sum(credit_numbers))}\n')


def append_to_a_file():
    # Pass the 'a' argument to open() to indicate
    # we will write append into a file with
    # existing contents.
    output_file = 'credits_results.txt'
    with open(output_file, 'a') as f:
        # As an alternative to print, we can
        # write a string to the file.
        f.write('New text\n')
        f.write('Additional text\n')


def exception_practice():
    print(5 / 0)

def exception_practice2():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("You can't divide by zero!")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # read_all_at_once()
    # read_line_by_line()
    # store_lines_in_list()
    # read_and_write_credits()
    # append_to_a_file()
    # exception_practice2()
    # read_all_at_once_wrong()
    read_with_exception_handling()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
