def command_ln(cmd_num):
    cmd_list = []
    # insert a number of times (N) to execute commands
    for line in range(cmd_num):
        command = list(input().split())
#        print("Command #" + str(line) + ": " + str(command[0]))
        if command[0] == "insert":
            cmd_list.insert(int(command[1]), int(command[2]))
#            print("Inserting [" + str(command[2]) + "] at position " + str(command[1] + ": " + str(cmd_list)))
        elif command[0] == "print":
            print(cmd_list)
#            print("Printing cmd_list: " + str(cmd_list))
        elif command[0] == "remove":
            try:
                cmd_list.remove(int(command[1]))
#                print("Removing the first value of: " + str(command[1])+ " | " + str(cmd_list))
            except:
#                print("Value [" + str(command[1])+ "] is not in the list | " + str(cmd_list))
                continue
        elif command[0] == "append":
            cmd_list.append(int(command[1]))
        elif command[0] == "sort":
            cmd_list.sort()
        elif command[0] == "pop":
            cmd_list.pop()
        elif command[0] == "reverse":
            cmd_list.reverse()
        else:
            continue
    return 0


if __name__ == '__main__':
    # insert a number of times (N) to execute commands
    N = int(input())
    blank_list = []
    command_ln(N)
