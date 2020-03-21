def cat():
    print('Meow')

def dog():
    print('woof')
    
def bird():
    print('chirp')

juice=input('write c,d or b ')
if juice=='c':
    cat()
elif juice=='d':
    dog()
elif juice=='b':
    bird()
else:
    print('???')
