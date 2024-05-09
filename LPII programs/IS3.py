# Initial permutation
IP = [2, 6, 3, 1, 4, 8, 5, 7]
# Final permutation
FP = [4, 1, 3, 5, 7, 2, 8, 6]
# Expansion permutation
EP = [4, 1, 2, 3, 2, 3, 4, 1]
# P4 permutation
P4 = [2, 4, 3, 1]
# P8 permutation
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
# P10 permutation
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
# S0 box
S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]
# S1 box
S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

def permute(bits, permutation):
    return ''.join(bits[i - 1] for i in permutation)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def key_generation(key):
    key = permute(key, P10)
    key_left = left_shift(key[:5], 1) + left_shift(key[5:], 1)
    k1 = permute(key_left, P8)
    key_left = left_shift(key_left, 2)
    k2 = permute(key_left, P8)
    return k1, k2

def f_k(bits, key):
    bits = permute(bits, EP)
    bits = bin(int(bits, 2) ^ int(key, 2))[2:].zfill(8)
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1:3], 2)
    bits = '{0:02b}'.format(S0[row][col]) + '{0:02b}'.format(S1[row][col])
    return permute(bits, P4)

def encrypt(plain_text, key):
    k1, k2 = key_generation(key)
    plain_text = permute(plain_text, IP)
    left, right = plain_text[:4], plain_text[4:]
    right = bin(int(left, 2) ^ int(f_k(right, k1), 2))[2:].zfill(4)
    left, right = right, left
    right = bin(int(left, 2) ^ int(f_k(right, k2), 2))[2:].zfill(4)
    return permute(left + right, FP)

def decrypt(cipher_text, key):
    k1, k2 = key_generation(key)
    cipher_text = permute(cipher_text, IP)
    left, right = cipher_text[:4], cipher_text[4:]
    right = bin(int(left, 2) ^ int(f_k(right, k2), 2))[2:].zfill(4)
    left, right = right, left
    right = bin(int(left, 2) ^ int(f_k(right, k1), 2))[2:].zfill(4)
    return permute(left + right, FP)

def main():
    plain_text = input("Enter 8-bit plain text: ")
    key = input("Enter 10-bit key: ")
    cipher_text = encrypt(plain_text, key)
    print("Encrypted text:", cipher_text)
    decrypted_text = decrypt(cipher_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
