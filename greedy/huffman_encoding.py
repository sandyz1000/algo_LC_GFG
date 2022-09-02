"""
Greedy Algorithms | Set 3 (Huffman Coding)
http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/
http://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/

Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length
codes to input characters, lengths of the assigned codes are based on the frequencies of
corresponding characters. The most frequent character gets the smallest code and the least
frequent character gets the largest code.
The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit
sequences) are assigned in such a way that the code assigned to one character is not prefix of
code assigned to any other character. This is how Huffman Coding makes sure that there is no
ambiguity when decoding the generated bit stream.
Let us understand prefix codes with a counter example. Let there be four characters a, b,
c and d, and their corresponding variable length codes be 00, 01, 0 and 1. This coding leads to
ambiguity because code assigned to c is prefix of codes assigned to a and b. If the compressed
bit stream is 0001, the de-compressed output may be "cccd" or "ccb" or "acd" or "ab".

See this for applications of Huffman Coding.

There are mainly two major parts in Huffman Coding
1) Build a Huffman Tree from input characters.
2) Traverse the Huffman Tree and assign codes to characters.

----------------------------------------------------
Steps to build Huffman Tree
----------------------------------------------------
Input is array of unique characters along with their frequency of occurrences and output is
Huffman Tree.

1.  Create a leaf node for each unique character and build a min heap of all leaf nodes (Min Heap
    is used as a priority queue. The value of frequency field is used to compare two nodes in min
    heap. Initially, the least frequent character is at root)
2.  Extract two nodes with the minimum frequency from the min heap.
3.  Create a new internal node with frequency equal to the sum of the two nodes frequencies. Make
    the first extracted node as its left child and the other extracted node as its right child. Add
    this node to the min heap.
4.  Repeat steps#2 and #3 until the heap contains only one node. The remaining node is the root
    node and the tree is complete.

Let us understand the algorithm with an example:
- - - - - - - - - - - - - - - - - - - -
character   Frequency
    a	        5
    b           9
    c           12
    d           13
    e           16
    f           45
- - - - - - - - - - - - - - - - - - - -

Step 1. Build a min heap that contains 6 nodes where each node represents root of a tree with
single node.

Step 2 Extract two minimum frequency nodes from min heap. Add a new internal node with frequency
5 + 9 = 14.
                    14
                  /    \
                a|5   b|9

Now min heap contains 5 nodes where 4 nodes are roots of trees with single element each, and one
heap node is root of tree with 3 elements
- - - - - - - - - - - - - - - - - - - -
character           Frequency
       c               12
       d               13
 Internal Node         14
       e               16
       f               45
- - - - - - - - - - - - - - - - - - - -

Step 3: Extract two minimum frequency nodes from heap. Add a new internal node with frequency
12 + 13 = 25
                    25
                  /    \
                c|12  d|13

Now min heap contains 4 nodes where 2 nodes are roots of trees with single element each, and two
heap nodes are root of tree with more than one nodes.

- - - - - - - - - - - - - - - - - - - -
character           Frequency
Internal Node          14
       e               16
Internal Node          25
       f               45
- - - - - - - - - - - - - - - - - - - -

Step 4: Extract two minimum frequency nodes. Add a new internal node with frequency
14 + 16 = 30
                    30
                  /    \
                 14   e|16
                /  \
              a|5  b|9

Now min heap contains 3 nodes.
- - - - - - - - - - - - - - - - - - - -
character          Frequency
Internal Node         25
Internal Node         30
      f               45
- - - - - - - - - - - - - - - - - - - -

Step 5: Extract two minimum frequency nodes. Add a new internal node with frequency
25 + 30 = 55
                     55
                  /     \
                25      30
              /   \    /   \
            c|12 d|13 14  e|16
                     /  \
                   a|5  b|9

Now min heap contains 2 nodes.
- - - - - - - - - - - - - - - - - - - -
character     Frequency
       f         45
Internal Node    55
- - - - - - - - - - - - - - - - - - - -

Step 6: Extract two minimum frequency nodes. Add a new internal node with frequency
45 + 55 = 100
                    100
                  /     \
               f|45     55
                     /      \
                   25        30
                  /  \      /   \
                c|12 d|13  14   e|16
                          /  \
                        a|5 b|9

Now min heap contains only one node.
- - - - - - - - - - - - - - - - - - - -
character      Frequency
Internal Node    100
- - - - - - - - - - - - - - - - - - - -

Since the heap contains only one node, the algorithm stops here.

==Steps to print codes from Huffman Tree:=
Traverse the tree formed starting from the root. Maintain an auxiliary array. While moving to
the left child, write 0 to the array. While moving to the right child, write 1 to the array.
Print the array when a leaf node is encountered.


The codes are as follows:
- - - - - - - - - - - - - - - - - - - -
character   code-word
    f          0
    c          100
    d          101
    a          1100
    b          1101
    e          111
- - - - - - - - - - - - - - - - - - - -
"""
from __future__ import print_function
import heapq
import os


class HeapNode(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __cmp__(self, other):
        if other is None:
            return -1
        if not isinstance(other, HeapNode):
            return -1
        return self.freq > other.freq


class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # functions for compression
    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            if character not in frequency:
                frequency[character] = 0
            frequency[character] += 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency:
            node = HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text

    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    def get_byte_array(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            b.append(int(byte, 2))
        return b

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))

        print("Compressed")
        return output_path

    # functions for decompression
    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:]
        encoded_text = padded_encoded_text[:-1 * extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text

    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""

            byte = file.read(1)
            while byte != "":
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)

            output.write(decompressed_text)

        print("Decompressed")
        return output_path


if __name__ == "__main__":
    path = "/Volumes/Transcend/Downloads/sample.txt"

    h = HuffmanCoding(path)

    output_path = h.compress()
    print("Output path ", output_path)
    h.decompress(output_path)
    print("Done")
