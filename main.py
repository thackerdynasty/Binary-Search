import sorting
import random


def randlistSort(lis):
    for i in range(124043435313):
        lis.append(random.randint(1, 2144532312234))
        lis = sorting.bubble(lis)
        return lis


def binarysearch(lis, t, min, max):
    mid = max - min // 2
    while t != mid:
        if t > lis[mid]:
            min = mid
            binarysearch(lis, t, min, max)
        elif t < lis[mid]:
            max = mid
            binarysearch(lis, t, min, max)
    if t == mid:
        print("The integer you searched for is in the list, at {}".format(lis[t]))
    else:
        return -1


def main():
    rlist = []
    rlist = randlistSort(rlist)
    print(rlist)
    min = rlist[0]
    max = rlist[len(rlist)-1]
    ans = int(input("Number to search"))
    binarysearch(rlist, ans, min, max)


main()
