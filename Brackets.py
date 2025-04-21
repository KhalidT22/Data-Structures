data = input()

def brackets_check(data):
    stack = []
    check = True
    stack_index = []
    for s in range(0,len(data)):
        if data[s] in ["(","{","["]:
            stack.append(data[s])
            stack_index.append(s+1)
        else:

            if data[s] in ["}","]",")"]:
                if not stack:
                    print(s+1)
                    check = False
                    break
                else:
                    top = stack.pop()
                    stack_index.pop()
                    if (data[s] == "}" and top == "{") or (data[s] == "]" and top == "[") or (data[s] == ")" and top == "(") :
                        continue
                    else:

                        print(s+1)
                        check = False
                        break

            else:
                continue
    if check:
        if not stack:
            print("Success")
        else:
            print(stack_index[0])


brackets_check(data)
