import os
import shutil


class MyCMD:
    cur_dir: str

    def __init__(self, cur_dir: str):
        self.cur_dir = cur_dir

    def show_dir(self) -> None:
        cnt, cnt1 = 0, 0
        for i in os.scandir(self.cur_dir):
            if i.is_dir():
                print(i)
                cnt += 1
            if i.is_file():
                cnt1 += 2
        print(f'Number of directories: {cnt}\nNumber of files: {cnt1}')
        
    def change_dir(self, new_dir=None) -> None:
        if new_dir is None:
            self.__change_dir()
            return
        try:
            if self.cur_dir[len(self.cur_dir) - 1] != '/':
                os.chdir(self.cur_dir + '/' + new_dir)
                self.cur_dir += '/'
            else:
                os.chdir(self.cur_dir + new_dir)

            self.cur_dir += new_dir
        except:
            print('No such directory!')

    def remove_dir(self, dir_name):
        try:
            size = len(os.listdir(self.cur_dir + '/' + dir_name))
            if size == 0:
                os.rmdir(self.cur_dir + '/' + dir_name)
            else:
                if input('Directory is not empty. Continue deleting?\ny/n\n') == 'y':
                    shutil.rmtree(self.cur_dir + '/' + dir_name)
        except:
            print("No such directory")
    
    def __change_dir(self) -> None:
        ind = -1
        for i in range(0 , len(self.cur_dir)):
            if self.cur_dir[i] == '/':
                ind = i
        
        if ind != -1:
            os.chdir(self.cur_dir[:ind])
            self.cur_dir = self.cur_dir[:ind]
            
    def del_file(self, f_name):
        try:
            os.remove(self.cur_dir + '/' + f_name)
        except:
            print('No such file!')
            
    def read_file(self, f_name):
        try:
            with open(self.cur_dir + '/' + f_name) as f:
                for l in f.readlines():
                    print(l, end='')
                print()
        except IOError:
            print('File not found!')
            
    def rename(self, name, new_name):
        try:
            print(name, new_name)
            # os.rename(self.cur_dir + '/' + name, new_name)
        except:
            print('No such file or directory')
    
    def prettify(self):
        self.cur_dir = self.cur_dir.replace("\ "[0], '/')
    
    def __str__(self) -> str:
        return f'{self.cur_dir}>'
    