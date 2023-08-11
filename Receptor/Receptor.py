def detectError(arr, nr):
    n = len(arr)
    res = 0
 
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
 

 
        res = res + val*(10**i)
 
    return int(str(res), 2)

def bin_ascii_to_bytes(binary):
    string = ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))
    return string





# encoded_data = "your_encoded_hamming_string_here"
# decoded_binary = decode_hamming_code(encoded_data)
# original_string = bin_ascii_to_string(decoded_binary)

# print("Decoded String:", original_string)
