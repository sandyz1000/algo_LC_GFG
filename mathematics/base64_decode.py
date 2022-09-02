"""
http://www.geeksforgeeks.org/decode-encoded-base-64-string-ascii-string/

Decode an Encoded Base 64 String to ASCII String

Prerequisite : What is base64 Encoding and why we encode strings to base64 format

Base64 encoding is performed at sending node before transmitting bits over a network,
and receiving node decodes that encoded data back to original ASCII string.

Base64 character set is
- - - - - - - - - - - - - - - - - - - - - - - -
// 64 characters
char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz0123456789+/"
- - - - - - - - - - - - - - - - - - - - - - - -

==Examples:==
- - - - - - - - - - - - - - - - - - - - - - - -
Input : TUVO04= // (Encoded into base64 format)
Output : MENON  //  (Decoded back to ASCII string)

Input : Z2Vla3Nmb3JnZWVrcw==
Output : geeksforgeeks
- - - - - - - - - - - - - - - - - - - - - - - -

=Approach:=

1. Here each character in encoded string is considered to be made of 6 bits. We will take 4
characters each from Encoded String at one time i.e 4 * 6 = 24 bits. For each 4 characters of
encoded string we will produce 3 characters of original string which will be of 8 bits each i.e 3
* 8 = 24 bits.

2. Find their respective position in char_set and store it inside a variable (num) by using '|'
OR operator for storing bits and (LEFT – SHIFT) by 6 to make room for another 6 bits. NOTE : We
used '=' in encoder to substitute for 2 missing bits, So here in decoder we have to reverse the
process. Whenever we encounter a '=' we have to delete 2 bits of num by using (RIGHT – SHIFT) by 2.

3. After we have stored all the bits in num we will retrieve them in groups of 8, by using &
operator with 255 (11111111), that will store the 8 bits from num and that will be our original
character from ASCII string.

Time Complexity: O(N)
Space Complexity : O(1)

"""

# Python Program to decode a base64 Encoded string back to ASCII string

SIZE = 100


# char_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

class Base64Decode:
    def base64_decoder(self, encoded, len_str):
        decoded_string = [None] * SIZE
        k = 0

        # selects 4 characters from encoded string at a time. find the position of each encoded
        # character in char_set and stores in num.
        for i in range(0, len_str, 4):
            num = 0  # stores the bitstream.

            # count_bits stores current number of bits in num.
            count_bits = 0
            for j in range(4):
                # make space for 6 bits.
                if encoded[i + j] != '=':
                    num = num << 6
                    count_bits += 6

                # Finding the position of each encoded character in char_set and storing in
                # "num", use OR '|' operator to store bits.

                # encoded[i + j] = 'E', 'E' - 'A' = 5, 'E' has 5th position in char_set.
                if 'A' <= encoded[i + j] <= 'Z':
                    num = num | (ord(encoded[i + j]) - ord('A'))
                # encoded[i + j] = 'e', 'e' - 'a' = 5, 5 + 26 = 31, 'e' has 31st position in
                # char_set.
                elif 'a' <= encoded[i + j] <= 'z':
                    num = num | (ord(encoded[i + j]) - ord('a') + 26)
                # encoded[i + j] = '8', '8' - '0' = 8, 8 + 52 = 60, '8' has 60th position in
                # char_set.
                elif '0' <= encoded[i + j] <= '9':
                    num = num | (ord(encoded[i + j]) - ord('0') + 52)
                # '+' occurs in 62nd position in char_set.
                elif encoded[i + j] == '+':
                    num = num | 62
                # '/' occurs in 63rd position in char_set.
                elif encoded[i + j] == '/':
                    num = num | 63
                # ( str[i + j] == '=' ) remove 2 bits to delete appended bits during encoding.
                else:
                    num = num >> 2
                    count_bits -= 2

            while count_bits != 0:
                count_bits -= 8
                decoded_string[k] = chr((num >> count_bits) & 255)  # 255 in binary is 11111111
                k += 1

        # place NULL character to mark end of string.
        decoded_string[k] = '&#092;&#048;'
        return "".join(decoded_string[:k])


if __name__ == '__main__':
    # Encoded string : TUVO04=
    # Decoded string : MENON

    test = Base64Decode()
    encoded_string = "TUVOT04="
    len_str = len(encoded_string)

    print("Encoded string : %s\n" % encoded_string)
    print("Decoded_string : %s\n" % test.base64_decoder(encoded_string, len_str))
