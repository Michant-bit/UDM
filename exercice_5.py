def repeter(n, t):
    texte = ''
    for n in range(n):
        texte += t
    return texte

def extraireChiffre(n, p):
    return (n // p) % 10

def chiffreRomain(n, symboleRomain1, symboleRomain2, symboleRomain3):
    if(0 <= n <= 3):
        return repeter(n, symboleRomain1)
    elif(n == 4):
        return symboleRomain1 + symboleRomain2
    elif(5 <= n <= 8):
        return symboleRomain2 + repeter(n - 5, symboleRomain1)
    elif(n == 9):
        return symboleRomain1 + symboleRomain3

def romain(n):
    texte = ''
    if (n // 1000 != 0):
        texte += repeter(extraireChiffre(n, 1000), 'M')
    elif(n // 100 != 0):
        texte += chiffreRomain(extraireChiffre(n, 100), 'C', 'D', 'M')
    elif(n // 10 != 0):
        texte += chiffreRomain(extraireChiffre(n, 100), 'X', 'L', 'C')
    else:
        texte += chiffreRomain(extraireChiffre(n, 100), 'I', 'V', 'X')
    return texte

print(romain(389))