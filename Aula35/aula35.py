# var = 'valor'


def func():
    print(var)


def func2(arg=None):
    # global var
    # var = 'Outro valor'
    # print(var)
    # arg = arg.replace('v', 'c')
    return arg

func()
outra_variavel = func2(arg=var)

print(var)
print(outra_variavel)
