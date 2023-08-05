def calculate_fletcher_checksum(message):
    modulo = 255
    sum1 = 0
    sum2 = 0
    message = message.encode()
    for byte in message:
        sum1 = (sum1 + int(byte)) % modulo
        sum2 = (sum2 + sum1) % modulo

    checksum = (sum2 << 8) | sum1

    return checksum

def verify_fletcher_checksum(message, checksum):
    
    calculated_checksum = calculate_fletcher_checksum(message)
    return calculated_checksum == checksum

def calculate_redundant_bits(m):
        for i in range(m):
            if 2 ** i >= m + i + 1:
                return i


def detect_error(arr, nr):
        n = len(arr)
        res = 0

        for i in range(nr):
            val = 0
            for j in range(1, n + 1):
                if j & (2 ** i) == (2 ** i):
                    val = val ^ int(arr[-1 * j])
            res = res + val * (10 ** i)

        return int(str(res), 2)





test_message = "11001101111101010100101101" # original message
expected_checksum = 0xF4F4 # checksum calculated by the sender

print(f"Original Message received: {test_message}")
calculated_checksum = calculate_fletcher_checksum(test_message)
print(f"Calculated Checksum: 0x{calculated_checksum:X}")
print(f"Checksum Matches: {verify_fletcher_checksum(test_message, expected_checksum)}")

modified_message = "11001001110101010100101101"
print(f"Modified Message received: {modified_message}")
print(f"Checksum Matches (Modified Message): {verify_fletcher_checksum(modified_message, expected_checksum)}")



