import os
from mycmd import MyCMD


def init():
    test = MyCMD(r'C:/')

    while True:
        print(test)
        comand = input().strip().split()
        # print(comand)
        if len(comand) == 1:
            if comand[0] == 'dir':
                print(os.listdir(test.__str__()))
                print('ok')


if __name__ == '__main__':
    init()
