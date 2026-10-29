def navigate(commands):
    history_list = ["Home"]
    current_pointer = 0
    for command in commands:
        if command == "Back":
            if current_pointer > 0:
                current_pointer -= 1
        elif command == "Forward":
            if current_pointer < len(history_list)-1:
                current_pointer += 1
        else:
            history_list = history_list[:current_pointer + 1]
            history_list.append(command.replace("Visit ", "",1))
            
            current_pointer +=1

    return history_list[current_pointer]