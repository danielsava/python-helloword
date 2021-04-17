import statistics

# input de dados
num = input('Informe um número: ')          

# converte string para int
num = int(num)                              

is_par = num % 2 == 0

if num > 0:  
    print("{0} é um número positivo".format(num))  
elif num == 0:  
    print("{0} é igual a zero".format(num))   
else:  
    print("{0} é um número negativo".format(num))

mediana_range = range(num-5, num+6)

mediana = []

for n in mediana_range:
    mediana.append(n)

print(mediana)

num_decremento = num - 1

if num_decremento > 0:
    print(num_decremento)