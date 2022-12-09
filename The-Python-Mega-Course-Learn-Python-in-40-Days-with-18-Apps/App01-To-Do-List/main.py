# Console App

cases = {
    '1': 'Add',
    '2': 'Delete',
    '3': 'Edit',
    '4': 'Show',
    '5': 'Exit'
}
filename = "todofile.txt"
to_do_list = []

def print_action_prompt():
    print("Choose an action:")
    for i, x in cases.items():
        print(f"{i} - {x}")

def print_all():
    print("***** List of items *****")
    for index, item in enumerate(to_do_list):
        print(f"*\t{index+1} - {item}")
    print("*************************")

def read_todos_from_file():
    # READ file
    try:
        with open(filename, 'r') as todo_file:
            for line in todo_file.readlines():
                to_do_list.append(line.replace('\n', ''))
    except:
        print(f"ERROR while opening file: {filename}")
        exit(1)
def flush_to_disk():
    try:
        with open(filename, 'w') as todofile:
            for item in to_do_list:
                todofile.writelines(item + '\n')
    except:
        print(f"ERROR while opening file: {filename}")

def __main__():
    # Read todos from the file
    read_todos_from_file()

    # ASK user what to do
    add_prompt = "Enter a ToDo:"

    while True:
        print_action_prompt()
        user_action = input('---> ')
        match user_action:
            # ADD #
            case '1':
                to_do_list.append(input(add_prompt))

                flush_to_disk()
            # DELETE #
            case '2':
                num = int(input("type a todo number to  delete: "))
                deleted_item = to_do_list.pop(num-1)
                print(f"Item: {deleted_item.upper()} has been deleted!")
            # EDIT #
            case '3':
                num = int(input("type a todo number to  edit: "))
                to_do_list[num - 1] = input("type a new value: ")
                print_all()
            # SHOW #
            case '4':
                print_all()
            # EXIT"
            case '5':
                print("Bye!")
                break
            case _:
                print("Type 'add' or 'delete' or 'exit'")

__main__()

