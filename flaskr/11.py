from werkzeug.security import check_password_hash, generate_password_hash

a = generate_password_hash(':LFKJ;laskdjf;l:JI:Lefj;lk;alk;flk209348u')
b = generate_password_hash(':LFKJ;laskdjf;l:JI:Lefj;lk;alk;flk209348u')

print(a)
print(b)
z = check_password_hash(a, ':LFKJ;laskdjf;l:JI:Lefj;lk;alk;flk209348u')
x = check_password_hash(b, ':LFKJ;laskdjf;l:JI:Lefj;lk;alk;flk209348u')
print('z,x', z, x)

print(a == b)
print(type(a))
