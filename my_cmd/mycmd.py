class MyCMD:
    cur_dir: str

    def __init__(self, cur_dir: str):
        self.cur_dir = cur_dir

    # def change_dir(self):

    def __str__(self):
        return f'{self.cur_dir}:'