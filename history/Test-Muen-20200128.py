def cat():
    print('Meow')

def dog():
    print('woof')
    
def bird():
    print('chirp')

def duck():
    print('quack')

juice=input('write c,d,dk or b ')
if juice=='c':
    cat()
elif juice=='d':
    dog()
elif juice=='b':
    bird()
elif juice=='dk':
    duck()
else:
    print('???')
