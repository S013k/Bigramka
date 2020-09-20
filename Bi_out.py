import argparse
import random
import pickle


def read_start():
    importer = argparse.ArgumentParser(description='Биграмка')
    importer.add_argument('length', type=int, help='Введите длинну предложения.')
    importer.add_argument('hard', type=int,
                          help='Введите однообразность построения (число от 1 до 3) (чем больше, тем дольше считает, но вероятность получения вменяемого результата больше)')
    importer.add_argument('seed', type=int, help='сид')
    args = importer.parse_args()
    return args.length, args.hard, args.seed


def dicts_to_text(ids=21, hard=2, seed = 651846518):
    with open('dic_st.pickle', 'rb') as f:
        dic_st = pickle.load(f)
    with open('dic_mid.pickle', 'rb') as f:
        dic_mid = pickle.load(f)
    with open('dic_est.pickle', 'rb') as f:
        dic_end = pickle.load(f)
    ans = []
    ans.append(list(dic_st.keys())[seed % len(list(dic_st.keys()))])
    for i in range(ids - 2):
        prev_verb = ans[i]
        arr = sorted(dic_mid.get(prev_verb), key=lambda x: -x[1])
        # print(arr)
        if ids > 20:
            tmp = []
            for i in range(len(arr)):
                for j in range(arr[i][1] ** hard):
                    tmp.append(arr[i][0])
            verb = random.choice(tmp)
            # print(verb)
            # verb = arr[0][0]
        else:
            verb = arr[0][0]
        ans.append(verb)
    prev_verb = ans[-1]
    if prev_verb in dic_end.keys():
        pass
    else:
        verb = random.choice(list(dic_end.keys()))
        ans.append(verb)
        # print(arr)
        # print(ans)
    print(*ans, end="")
    print("!")
    # print(text)
    # print(dic_st)
    # print(dic_mid)
    # print(dic_end)
    f = open('answer.txt', 'w')
    for i in range(len(ans) - 1):
        f.write(ans[i] + " ")

    f.write(ans[-1] + "!")


try:
    dicts_to_text(read_start())
except:
    dicts_to_text(random.randint(21, 50), 3, random.randint(1, 651846518))
