# Console App

cases = {
    '1': 'Add',
    '2': 'Delete',
    '3': 'Edit',
    '4': 'Show',
    '5': 'Exit'
}

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
def __main__():


    with open("todofile.txt", 'r') as todo_file:
        for line in todo_file.readlines():
            to_do_list.append(line.replace('\n', ''))

    add_prompt = "Enter a ToDo:"

    while True:
        print_action_prompt()
        user_action = input('---> ')
        match user_action:
            case '1':
                to_do_list.append(input(add_prompt))

                with open('todofile.txt', 'w') as todofile:
                    for item in to_do_list:
                        todofile.writelines(item + '\n')
            case '2':
                num = int(input("type a todo number to  delete: "))
                deleted_item = to_do_list.pop(num-1)
                print(f"Item: {deleted_item.upper()} has been deleted!")
            # Edit #
            case '3':
                num = int(input("type a todo number to  edit: "))
                to_do_list[num - 1] = input("type a new value: ")
                print_all()
            # Show #
            case '4':
                print_all()
            case '5':
                break
            case _:
                print("Type 'add' or 'delete' or 'exit'")

__main__()

