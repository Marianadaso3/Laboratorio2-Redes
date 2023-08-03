# Función de detección de errores: Fletcher checksum
def verificar_fletcher_checksum(mensaje):
    modulo = 255
    sum1 = 0
    sum2 = 0

    for byte in mensaje:
        sum1 = (sum1 + byte) % modulo
        sum2 = (sum2 + sum1) % modulo
    
    checksum = (sum2 << 8) | sum1

    return checksum == 0


def corregir_codigo_hamming(codigo_hamming):
    n = len(codigo_hamming)
    m = 2
    while 2**m < n + m + 1:
        m += 1
    
    error_bit = 0
    for i in range(m):
        parity = 0
        for j in range(1, n + m + 1):
            if j & (2**i):
                parity ^= int(codigo_hamming[j - 1])
        if parity != int(codigo_hamming[2**i - 1]):
            error_bit += 2**i
    
    if error_bit == 0:
        return codigo_hamming[:n]
    else:
        error_bit -= 1
        codigo_hamming = list(codigo_hamming)
        codigo_hamming[error_bit] = "1" if codigo_hamming[error_bit] == "0" else "0"
        return "".join(codigo_hamming)[:n]


def main():
    trama_con_codigo_hamming = input("Ingrese la trama con código de Hamming: ")
    if verificar_fletcher_checksum(trama_con_codigo_hamming):
        trama_corregida = corregir_codigo_hamming(trama_con_codigo_hamming)
        print("Trama recibida:", trama_corregida)
    else:
        print("La trama se descarta por detectar errores.")


if __name__ == "__main__":
    main()
