class MyItterator:
    def __init__(self, string):
        self.string = string
        self.current = len(string)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.string[self.current]
    
    def __call__(self, *args, **kwds):
        print("hello world")

str = MyItterator("Hello World")
for char in str:
    print(char)

str()
