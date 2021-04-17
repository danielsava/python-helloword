
# Anotação @validartemp
def validartemp(func):
    def wrapper(t):
        print('debug [antes]', t)
        if t < 0:
            t = 0
        print('debug [depois]', t)
        return func(t)
    return wrapper


@validartemp
def converter_celsius(tempf):
    return 5 * (temp_f - 32) / 9


temp_f = int(input('Informa a temperatura(°F): '))

print(temp_f)

temp_c = converter_celsius(temp_f)

print(temp_c)