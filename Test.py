import hashcryption

foo = input('Encrypt:')
bah = hashcryption.encrypt(foo, 'c')
print(bah[0])
print(bah[1])
abc = hashcryption.decrept(bah[0], bah[1])
print(abc)