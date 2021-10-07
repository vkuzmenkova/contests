def is_closing_tag(tag):
    return True if tag[0] + tag[1] == '</' else False


def is_valid(doc: list[str]):
    stack = []

    for docline in doc:
        if is_closing_tag(docline):
            if len(stack) != 0:
                if stack[-1] == docline[2:-1]:
                    stack.pop()
                else:
                    stack.append(docline)
            else:
                stack.append(docline)
        else:
            stack.append(docline[1:-1])

    return True if len(stack) == 0 else False


if __name__ == "__main__":

    try:
        x = int(input())
        data = []

        for j in range(x):
            s = int(input())
            temp = []
            for i in range(s):
                line = input()
                temp.append(line.lower())

            # if len(temp) == 0
            if is_valid(temp):
                print('CORRECT')
            else:
                is_one_tag_broken = False
                broken_tag = ''
                for i in range(len(temp)):
                    temp2 = temp.copy()
                    temp2.pop(i)
                    if is_valid(temp2):
                        is_one_tag_broken = True
                        broken_tag = temp[i].upper()
                        break
                if is_one_tag_broken:
                    print('ALMOST ' + broken_tag)
                else:
                    print('INCORRECT')
            # data.append(temp)

        # for doc in data:
        #     if is_valid(doc):
        #         print('CORRECT')
        #     else:
        #         is_one_tag_broken = False
        #         broken_tag = ''
        #         for i in range(len(doc)):
        #             temp = doc.copy()
        #             temp.pop(i)
        #             if is_valid(temp):
        #                 is_one_tag_broken = True
        #                 broken_tag = doc[i].upper()
        #                 break
        #         if is_one_tag_broken:
        #             print('ALMOST ' + broken_tag)
        #         else:
        #             print('INCORRECT')
    except Exception as e:
        print(e)
