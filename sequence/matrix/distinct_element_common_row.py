"""Find distinct elements common to all rows of a matrix
http://www.geeksforgeeks.org/find-distinct-elements-common-rows-matrix/

Given a n x n matrix. The problem is to find all the distinct elements common to all rows of the
matrix. The elements can be printed in any order.

Examples:
---------------
Input : mat = [[2, 1, 4, 3],
               [1, 2, 3, 2],
               [3, 6, 2, 3],
               [5, 2, 5, 3]]
Output : 2 3

Input : mat = [[12, 1, 14, 3, 16],
               [14, 2, 1, 3, 35],
               [14, 1, 14, 3, 11],
               [14, 25, 3, 2, 1],
               [1, 18, 3, 21, 14]]
Output : 1 3 14

"""
from __future__ import print_function


MAX = 100


class Test:
    @staticmethod
    def sort_rows(mat, n):
        """function to individually sort each row in increasing order"""
        for i in range(n):
            mat[i] = sorted(mat[i])

    def common_elements_method2(self, mat, n):
        """
        Method 2: Sort all the rows of the matrix individually in increasing order. Then apply a
        modified approach of the problem of finding common elements in 3 sorted arrays.

        Python implementation to find distinct elements common to all rows of a matrix

        function to find all the common elements
        Time Complexity: O(n^2log n), each row of size n requires O(nlogn) for sorting and there
        are total n rows.
        Auxiliary Space : O(n) to store current column indexes for each row.
        """
        self.sort_rows(mat, n)  # sort rows individually

        # current column index of each row is stored from where the element is being searched in that row
        curr_index = [0] * n
        f = 0
        while curr_index[0] < n:
            # value present at the current column index of 1st row
            value = mat[0][curr_index[0]]
            present = True

            # 'value' is being searched in all the subsequent rows
            for i in range(1, n):
                # iterate through all the elements of the row from its current column index till an
                # element greater than the 'value' is found or the end of the row is encountered
                while curr_index[i] < n and mat[i][curr_index[i]] <= value:
                    curr_index[i] += 1

                # if the element was not present at the column before to the
                # 'curr_index' of the row
                if mat[i][curr_index[i] - 1] != value:
                    present = False

                # if all elements of the row have been traversed
                if curr_index[i] == n:
                    f = 1
                    break

            # if the 'value' is common to all the rows
            if present:
                print(value)

            # if any row have been completely traversed
            # then no more common elements can be found
            if f == 1:
                break

            curr_index[0] += 1

    def common_elements_method3(self, mat, n):
        """
        Method 3: It uses the concept of hashing. The following steps are:
        1. Map the element of 1st row in a hash table. Let it be hash.
        2. Fow row = 2 to n
        3. Map each element of the current row into a temporary hash table. Let it be temp.
        4. Iterate through the elements of hash and check that the elements in hash are present
        in temp. If not present then delete those elements from hash.
        5. When all the rows are being processed in this manner, then the elements left in hash are
        the required common elements.

        Python program to find distinct elements common to all rows of a matrix
        function to individually sort each row in increasing order
        Time Complexity: O(n2)
        Space Complexity: O(n)
        """
        us = set()

        # map elements of first row into 'us'
        for i in range(n):
            us.add(mat[0][i])

        for i in range(1, n):
            # mapping elements of current row in 'temp'
            temp = set([mat[i][j] for j in range(n)])
            # if an element of 'us' is not present into 'temp', then erase
            # that element from 'us'
            us = us.intersection(temp)
            if len(us) == 0:  # if size of 'us' becomes 0, then there are no common elements
                break

        # print the common elements
        for itr in us:
            print(itr)


if __name__ == '__main__':
    test = Test()
    print("\n---- Method-1------ \n")
    mat = [[12, 1, 14, 3, 16],
           [14, 2, 1, 3, 35],
           [14, 1, 14, 3, 11],
           [14, 25, 3, 2, 1],
           [1, 18, 3, 21, 14]]

    n = 5
    test.common_elements_method2(mat, n)

    print("\n---- Method-2------ \n")
    mat = [[2, 1, 4, 3],
           [1, 2, 3, 2],
           [3, 6, 2, 3],
           [5, 2, 5, 3]]
    n = 4
    test.common_elements_method3(mat, n)
