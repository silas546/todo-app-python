import utilities


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = utilities.get_todos()

        todos.append(todo + '\n')

        utilities.write_todos(todos)

    elif user_action.startswith("show"):
        todos = utilities.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todo_index = int(user_action[5:]) - 1

            todos = utilities.get_todos()

            new_todo = input('Enter new todo: ') + "\n"
            todos[todo_index] = new_todo

            utilities.write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith("complete"):
        try:
            todo_index = int(user_action[9:]) - 1

            todos = utilities.get_todos()

            todo_to_remove = todos[todo_index].strip('\n')
            todos.pop(todo_index)

            utilities.write_todos(todos)

            print(f"Todo {todo_to_remove} was removed from the list")

        except IndexError:
            print("There is no item of that number")
            continue

    elif user_action.startswith("clear"):
        todos = utilities.get_todos()

        todos.clear()

        utilities.write_todos(todos)

        print("Cleared the todo list")
        continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print('Goodbye')
