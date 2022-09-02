"""
Find number of Employees Under every Employee
Given a dictionary that contains mapping of employee and his manager as a number of
(employee, manager) pairs like below.  

{ "A", "C" },
{ "B", "C" },
{ "C", "F" },
{ "D", "E" },
{ "E", "F" },
{ "F", "F" }

In this example C is manager of A, C is also manager of B, F is manager of C and so on.

----------------------------------------------------
Explanation:
----------------------------------------------------

Write a function to get no of employees under each manager in the hierarchy not just their
direct reports. It may be assumed that an employee directly reports to only one manager. In
the above dictionary the root node/ceo is listed as reporting to himself.

Output should be a Dictionary that contains following.

A - 0
B - 0
C - 2
D - 0
E - 1
F - 5


Solution:

1. Create a reverse map with Manager->DirectReportingEmployee combination. Off-course
employee will be multiple so Value in Map is List of Strings.
    "C" --> "A", "B",
    "E" --> "D"
    "F" --> "C", "E", "F"

2. Now use the given employee-manager map to iterate and at the same time use newly reverse
map to find the count of employees under manager.

    Let the map created in step 2 be 'mngrEmpMap'
    Do following for every employee 'emp'.
        a) If 'emp' is not present in 'mngrEmpMap'
            Count under 'emp' is 0 [Nobody reports to 'emp']
        b) If 'emp' is present in 'mngrEmpMap'
            Use the list of direct reports from map 'mngrEmpMap' and recursively calculate
            number of total employees under 'emp'.

A trick in step 2.b is to use memorization(Dynamic programming) while finding number of
employees under a manager so that we don't need to find number of employees again for any of
the employees. In the below code populateResultUtil() is the recursive function that uses
memoization to avoid re-computation of same results.
"""

from collections import defaultdict


# Java program to find number of persons under every employee

class NumberEmployeeUnderManager:

    def __init__(self):
        # A hashmap to store result. It stores count of employees under every employee,
        # the count may by 0 also
        self.result = {}

    def populate_result(self, dataSet):
        """This function populates 'result' for given input 'dataset
        '"""
        # To store reverse of original map, each key will have 0 to multiple values
        mngr_emp_map = defaultdict(list)

        # To fill mngr_emp_map, iterate through the given map
        for emp, mngr in dataSet.items():
            if emp != mngr:  # excluding emp-emp entry
                # Get the previous list of direct reports under
                # current 'mgr' and add the current 'emp' to the list
                # NOTE: If 'emp' is the first employee under 'mgr' return empty list
                direct_report_list = mngr_emp_map[mngr]

                direct_report_list.append(emp)

                # Replace old value for 'mgr' with new direct_report_list
                mngr_emp_map[mngr] = direct_report_list

        # Now use manager-Emp map built above to populate result with use of populateResultUtil()

        # note- we are iterating over original emp-manager map and
        # will use mngr-emp map in helper to get the count
        for mngr in dataSet.keys():
            self.populate_result_util(mngr, mngr_emp_map)

    def populate_result_util(self, mngr, mngr_emp_map):
        """
        This is a recursive function to fill count for 'mgr' using mngrEmpMap.
        This function uses memoization to avoid re-computations of subproblems.
        """
        # means employee is not a manager of any other employee
        if mngr not in mngr_emp_map:
            self.result[mngr] = 0
            return 0

        # this employee count has already been done by this method, so avoid re-computation
        elif mngr in self.result:
            return self.result[mngr]

        else:
            direct_report_emp_list = mngr_emp_map[mngr]
            count = len(direct_report_emp_list)
            for direct_report_emp in direct_report_emp_list:
                count += self.populate_result_util(direct_report_emp, mngr_emp_map)
            self.result[mngr] = count


if __name__ == '__main__':
    # result = {D=0, E=1, F=5, A=0, B=0, C=2}
    data_set = {"A": "C",
                "B": "C",
                "C": "F",
                "D": "E",
                "E": "F",
                "F": "F"}
    nem = NumberEmployeeUnderManager()
    nem.populate_result(data_set)
    print("result = " + str(nem.result))
