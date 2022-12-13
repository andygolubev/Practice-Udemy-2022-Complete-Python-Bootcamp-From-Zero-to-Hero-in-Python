

# Console App

from modules import functions

cases = {
    '1': 'Add',
    '2': 'Delete',
    '3': 'Edit',
    '4': 'Show',
    '5': 'Exit'
}
filename = "todofile.txt"


def __main__():
    # Read todos from the file
    to_do_list = functions.read_todos_from_file(filename)

    # ASK user what to do
    add_prompt = "Enter a ToDo:"

    while True:
        functions.print_action_prompt(cases)
        user_action = input('---> ')
        match user_action:
            # *************
            # ADD
            # *************
            case '1':
                to_do_list.append(input(add_prompt))
                functions.flush_to_disk(to_do_list, filename)

            #*************
            # DELETE
            #*************
            case '2':
                num = int(input("type a todo number to  delete: "))
                deleted_item = to_do_list.pop(num-1)
                print(f"Item: {deleted_item.upper()} has been deleted!")
                functions.flush_to_disk(to_do_list, filename)

            # *************
            # EDIT
            # *************
            case '3':
                num = int(input("type a todo number to  edit: "))
                to_do_list[num - 1] = input("type a new value: ")
                functions.print_all(to_do_list)
                functions.flush_to_disk(to_do_list, filename)

            # *************
            # SHOW
            # *************
            case '4':
                functions.print_all(to_do_list)

            # *************
            # EXIT"
            # *************
            case '5':
                print("Bye!")
                break

            # *************
            # ERROR
            # *************
            case _:
                print("Type 'add' or 'delete' or 'exit'")

__main__()

