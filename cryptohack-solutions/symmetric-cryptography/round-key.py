def add_round_key(s, k):
    assert(len(s) == len(k))

    xor_arr = []
    for i in range(len(s)):
        for j in range(len(k)):
            xor_arr.append(s[i][j] ^ k[i][j])

    return xor_arr

def bytes_to_ascii(arr):
    result = ''
    for num in arr:
        result += chr(num)

    return result

if __name__ == "__main__":
    state = [
        [206, 243, 61, 34],
        [171, 11, 93, 31],
        [16, 200, 91, 108],
        [150, 3, 194, 51],
    ]

    round_key = [
        [173, 129, 68, 82],
        [223, 100, 38, 109],
        [32, 189, 53, 8],
        [253, 48, 187, 78],
    ]

    xor_arr = add_round_key(state, round_key)
    print(bytes_to_ascii(xor_arr))

