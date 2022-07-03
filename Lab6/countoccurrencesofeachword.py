#Count occurrence of each word in given sentence

def count_x(a):
    words = list(a.lower().split())

    p = {}

    for i in words:
        if i in p:
            p[i] += 1
        else:
            p[i] = 1

    for key in list(p.keys()):
        print(key, ":", p[key])


a = "John had an orange orange"
count_x(a)