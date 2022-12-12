# Console App

cases = {
    '1': 'Add',
    '2': 'Delete',
    '3': 'Edit',
    '4': 'Show',
    '5': 'Exit'
}
filename = "todofile.txt"

import functions

def __main__():
    # Read todos from the file
    to_do_list = read_todos_from_file()

    # ASK user what to do
    add_prompt = "Enter a ToDo:"

    while True:
        print_action_prompt()
        user_action = input('---> ')
        match user_action:
            # ADD #
            case '1':
                to_do_list.append(input(add_prompt))

                flush_to_disk(to_do_list)
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

