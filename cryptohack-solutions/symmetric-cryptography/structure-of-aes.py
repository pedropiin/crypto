def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    bytes_arr = []
    for i in range(len(matrix)):
        for num in matrix[i]:
            bytes_arr.append(num)

    return bytes_arr

def bytes_to_ascii(arr):
    result = ''
    for num in arr:
        result += chr(num)

    return result

if __name__ == "__main__":
    matrix = [
        [99, 114, 121, 112],
        [116, 111, 123, 105],
        [110, 109, 97, 116],
        [114, 105, 120, 125],
    ]
    bytes_arr = matrix2bytes(matrix)
    print(bytes_to_ascii(bytes_arr))

    

