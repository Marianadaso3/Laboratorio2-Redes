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



test_message = "10101001110" # original message
expected_checksum = 0x9018 # checksum calculated by the sender

print(f"Original Message received: {test_message}")
calculated_checksum = calculate_fletcher_checksum(test_message)
print(f"Calculated Checksum: 0x{calculated_checksum:X}")
print(f"Checksum Matches: {verify_fletcher_checksum(test_message, expected_checksum)}")

modified_message = "Hello, worm!"
print(f"Checksum Matches (Modified Message): {verify_fletcher_checksum(modified_message, expected_checksum)}")



print("\n\n\n")
test_message_with_error = "11101001110" # message with error
r = calculate_redundant_bits(len(test_message))
print("Error Data is " + test_message_with_error)
correction = detect_error(test_message_with_error, r)
if(correction==0):
    print("There is no error in the received message.")
else:
    print("The position of error is ",len(test_message_with_error)-correction+1,"from the left")

