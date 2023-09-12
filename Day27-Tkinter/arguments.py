
def sum(*args):
    sum=0
    for n in args:
        sum += n
    print(sum)

sum(2,3,4,5,6)

def cal(n,**kwargs):
    sum = n + kwargs['add']
    pdt = n * kwargs['multiply']

    print(sum)
    print(pdt)

cal(n=2,add=3,multiply=4)

class Car():

    def __init__(self, **kwargs):
        self.make=kwargs.get('make')
        self.model=kwargs.get('model')
        print(self.make)
        print(self.model)
    
Car(make='Nissan')

    