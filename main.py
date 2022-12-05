# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def read_all_at_once():
    filename = 'grade_info.txt'

    with open(filename) as f_obj:
        contents = f_obj.read()

    print(type(contents))
    print(type(f_obj))
    print(contents)

def read_line_by_line():
    filename = 'grade_info.txt'
    with open(filename) as f_obj:
        for line in f_obj:
            print(line.rstrip())

def store_lines_in_list():
    filename = 'credits'
    with open(filename) as f_obj:
        lines = f_obj.readlines()
    for line in lines:
        print(line.rstrip())

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # read_all_at_once()
    # read_line_by_line()
    store_lines_in_list()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
