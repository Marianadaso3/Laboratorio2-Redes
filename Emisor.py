
#Función de corrección de errores: Código de Hamming
def calcular_codigo_hamming(mensaje):
    n = len(mensaje)
    m = 2
    while 2**m < n + m + 1:
        m += 1
    
    codigo_hamming = [0] * (n + m)
    j = 0

    for i in range(1, n + m + 1):
        if i == 2**j:
            j += 1
        else:
            codigo_hamming[i - 1] = int(mensaje[j])
            j += 1
    
    for i in range(m):
        parity = 0
        for j in range(1, n + m + 1):
            if j & (2**i):
                parity ^= codigo_hamming[j - 1]
        codigo_hamming[2**i - 1] = parity

    return "".join(map(str, codigo_hamming))
