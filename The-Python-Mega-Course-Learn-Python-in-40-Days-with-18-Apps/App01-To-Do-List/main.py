# Console App


action_prompt = "Choose an action:"
add_prompt = "Enter a ToDo:"
to_do_list = []
while True:
    user_action = input(action_prompt)
    match user_action:
        case 'add':
            to_do_list.append(input(add_prompt))
            for item in to_do_list:
                print(item)
        case 'delete':
            print('delete item')
        case 'edit':
            num = int(input("type a todo number to  edit: "))
            to_do_list[num - 1] = "EDITED"
            print(to_do_list)
        case 'exit':
            break
        case _:
            print("Type 'add' or 'delete' or 'exit'")
