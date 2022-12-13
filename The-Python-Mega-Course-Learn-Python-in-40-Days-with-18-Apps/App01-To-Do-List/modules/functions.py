
def print_action_prompt(cases):
    print("Choose an action:")
    for i, x in cases.items():
        print(f"{i} - {x}")

def print_all(to_do_list):
    print("***** List of items *****")
    for index, item in enumerate(to_do_list):
        print(f"*\t{index+1} - {item}")
    print("*************************")

def read_todos_from_file(filename):
    # READ file
    try:
        to_do_list = []
        with open(filename, 'r') as todo_file:
            for line in todo_file.readlines():
                to_do_list.append(line.replace('\n', ''))
            return to_do_list
    except:
        print(f"ERROR while opening file: {filename}")
        exit(1)
def flush_to_disk(to_do_list, filename):
    try:
        with open(filename, 'w') as todofile:
            for item in to_do_list:
                todofile.writelines(item + '\n')
    except:
        print(f"ERROR while opening file: {filename}")