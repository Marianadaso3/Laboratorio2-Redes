def compute_hamming_code(data):
    def calculate_redundant_bits(m):
        for i in range(m):
            if 2 ** i >= m + i + 1:
                return i

    def add_redundant_bits(data, r):
        j = 0
        k = 1
        m = len(data)
        res = ''

        for i in range(1, m + r + 1):
            if i == 2 ** j:
                res = res + '0'
                j += 1
            else:
                res = res + data[-1 * k]
                k += 1

        return res[::-1]

    def calculate_parity_bits(arr, r):
        n = len(arr)

        for i in range(r):
            val = 0
            for j in range(1, n + 1):
                if j & (2 ** i) == (2 ** i):
                    val = val ^ int(arr[-1 * j])
            arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]

        return arr

    r = calculate_redundant_bits(len(data))
    arr = add_redundant_bits(data, r)
    arr = calculate_parity_bits(arr, r)
    return arr

data = '110011011110101010101'
print("Data transferred is " + data)
hamming_code = compute_hamming_code(data)
print("Transferred data with Hamming code: " + hamming_code)

