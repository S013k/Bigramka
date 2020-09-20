import argparse
import random
import time


def file_to_dict(ids):
    separators = [" ", "-", ",", "", "(", ")"]
    ends = [".", "!", "?"]
    f = open('Bi_text.txt', 'r', encoding='utf-8')
    tmp = f.read()
    tmp = tmp.replace("\n", " ")
    # print(tmp)
    text = []
    dic_st = {}
    dic_end = {}
    verb_start = 0
    flag = False
    for i in range(len(tmp)):
        if tmp[i] in ends:
            verb = tmp[verb_start:i].strip(' ')
            if verb in dic_end.keys():
                xx = dic_end.get(verb)
                xx[1] += 1
                dic_end.update({verb: xx})
            else:
                dic_end.update({verb: ["ENDD", 1]})
            flag = True
            if verb != "":
                text.append(tmp[verb_start:i])
                verb_start = i + 1
            else:
                verb_start = i + 1
        elif tmp[i] in separators:
            verb = tmp[verb_start:i].strip(' ')
            if verb != "":
                text.append(tmp[verb_start:i])
                verb_start = i + 1
                if flag:
                    if verb in dic_st.keys():
                        xx = dic_st.get(verb)
                        xx[1] += 1
                        dic_st.update({verb: xx})
                    else:
                        dic_st.update({verb: ["STARTT", 1]})
                    flag = False
            else:
                verb_start = i + 1
                continue
    # print(text)
    dic_mid = {}
    for i in range(len(text)):
        if i == len(text) - 1:
            continue
        verb = text[i]
        verb_next = text[i + 1]
        # print(i, verb, verb_next)
        # print(dic_mid)
        if verb in dic_mid.keys():
            arr = dic_mid.get(verb)
            # print(arr)
            flag = True
            for j in range(len(arr)):
                if arr[j][0] == verb_next:
                    arr[j][1] += 1
                    dic_mid.update({verb: arr})
                    flag = False
                    break
            if flag:
                arr.append([verb_next, 1])
        else:
            dic_mid.update({verb: [[verb_next, 1]]})
    ans = []
    ans.append(random.choice(list(dic_st.keys())))
    for i in range(ids - 2):
        prev_verb = ans[i]
        arr = sorted(dic_mid.get(prev_verb), key=lambda x: -x[1])
        # print(arr)
        if ids > 50:
            tmp = []
            for i in range(len(arr)):
                for j in range(arr[i][1] ** 2):
                    tmp.append(arr[i][0])
            verb = random.choice(tmp)
            # print(verb)
            # verb = arr[0][0]
        else:
            verb = arr[0][0]
        ans.append(verb)

        # print(arr)
        # print(ans)
    print(*ans, end = "")
    print("!")

    # print(text)
    #print(dic_st)
    #print(dic_mid)
    #print(dic_end)


file_to_dict(97)
