def func_1(arg_x):
    var1 = 'scope_1\n'
    return arg_x + var1

def func_2(arg_y, func_y):
    def func_3(arg_z):
        var3 = 'scope_3\n'
        return arg_z + var3

    var2 = 'scope_2\n'
    valor = func_3(arg_y) 
    return func_y(valor) + var2

var0 = 'scope_general\n'
output = func_2(var0,func_1)

print('contextos:\n')
print(output)
