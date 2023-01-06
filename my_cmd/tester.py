import os
from mycmd import MyCMD

def validate_input(s: list) -> None:
    if len(s) > 2 and s[0] != 'ren':
        for i in range(2, len(s)):
            s[1] += ' ' +  s[i]
    elif s[0] == 'ren':
        s[1] = s[1].replace('"', '')
        s[2] = s[2].replace('"', '')

def init():
    test = MyCMD(r'C:/')
    os.chdir(test.cur_dir)
    while True:
        print(test, end = " ")
        comand = input().strip().split()
        if comand[0] == 'q':
            break
        validate_input(comand)
        match comand[0]:
            case 'dir':
                test.show_dir()
            case 'cd':
                if comand[1] == '..':
                    test.change_dir()
                else:
                    test.change_dir(comand[1])
            case 'rm':
                test.remove_dir(comand[1])
            case 'del':
                test.del_file(comand[1])
            case 'ren':
                test.rename(comand[1], comand[2])
            case 'read':
                test.read_file(comand[1])
            case _:
                print('Invalid command!')
        test.prettify()


if __name__ == '__main__':
    init()


# C:\Users\User\pp projects\PP1 CM\new_cmd\CMD