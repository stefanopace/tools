with open('nuovo') as nuovo:
    mc_nuove = nuovo.readlines()

with open('vecchio') as vecchio:
    mc_vecchie = vecchio.readlines()

define_nuovi = [line for line in mc_nuove if line.startswith('define')]
define_vecchi = [line for line in mc_vecchie if line.startswith('define')]


print('define che appaiono in quello nuovo ma non in quello vecchio:')
for define in define_nuovi:
    if define not in define_vecchi:
        print(define)

print('define che appaiono in quello vecchio ma non in quello nuovo:')
for define in define_vecchi:
    if define not in define_nuovi:
        print(define)
