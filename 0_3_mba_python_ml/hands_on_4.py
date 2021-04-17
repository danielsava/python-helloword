dic = {
    'name': 'Daniel',
    'last_name': 'Sava',
    'age': 31,
    'curso': 'Machine Learning',
}

print(dic)
print(dic['name'])
print(dic['last_name'])

dic['last_name'] = 'Silva'

# Copia
new_dic = dic.copy()
new_dic['last_name'] = 'Pupak'

print(dic)
print(new_dic)

