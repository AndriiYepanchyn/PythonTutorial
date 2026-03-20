import first_for_028 as go

def func2():
    print('Func2 from second file')

print('Hello top level from second')
go.func1()


if __name__ == '__main__':
    print('second file run directly')
else: 
    print('second has been imported')    