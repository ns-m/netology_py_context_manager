import datetime


class MyContextManager():

    def __enter__(self):
        self.start = datetime.datetime.now()
        print(f'Time of start : {self.start}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = datetime.datetime.now()
        print(f'End Time : {self.end}')
        self.time_prog = self.end - self.start
        print(f'Program execution time : {self.time_prog}')


