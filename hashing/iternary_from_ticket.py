"""
Find Itinerary from a given list of tickets
Given a list of tickets, find itinerary in order using the given list.

==Example:==

Input:
"Chennai" -> "Bangalore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output:
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,
It may be assumed that the input list of tickets is not cyclic and there is one ticket from every
city except final destination.

------------------------------------------------
Explanation:
------------------------------------------------

One Solution is to build a graph and do Topological Sorting of the graph. Time complexity of this
solution is O(n).

We can also use hashing to avoid building a graph. The idea is to first find the starting point.
A starting point would never be on 'to' side of a ticket. Once we find the starting point,
we can simply traverse the given map to print itinerary in order.

Algorithm:
1) Create a HashMap of given pair of tickets.  Let the created HashMap be 'dataset'. Every entry
of 'dataset' is of the form "from->to" like "Chennai" -> "Banglore"

2) Find the starting point of itinerary.
     a) Create a reverse HashMap.  Let the reverse be 'reverseMap' Entries of 'reverseMap' are of
     the form "to->form". Following is 'reverseMap' for above example.
        "Banglore"-> "Chennai"
        "Delhi"   -> "Bombay"
        "Chennai" -> "Goa"
        "Goa"     ->  "Delhi"
     b) Traverse 'dataset'.  For every key of dataset, check if it is there in 'reverseMap'. If a
     key is not present, then we found the starting point. In the above example, "Bombay" is
     starting point.

3) Start from above found starting point and traverse the 'dataset' to print itinerary.

"""


def print_itinerary(data_set={}):
    # To store reverse of given map
    reverse_map = {}

    # To fill reverse map, iterate through the given map
    for key, value in data_set.items():
        reverse_map[value] = key

    # Find the starting point of itinerary
    start = ""
    for key, value in data_set.items():
        if key not in reverse_map:
            start = key
            break

    # If we could not find a starting point, then something wrong with input
    if start is None and start.strip() == "":
        print("Invalid Input")
        return

    # Once we have starting point, we simple need to go next, next of next using given hash map
    to = data_set[start]
    while to is not None:
        print("%s -> %s" % (start, to))
        start = to
        to = data_set[to] if to in data_set else None


if __name__ == '__main__':
    # Bombay -> Delhi
    # Delhi -> Goa
    # Goa -> Chennai
    # Chennai -> Bangalore

    dataSet = {"Chennai": "Bangalore", "Bombay": "Delhi", "Goa": "Chennai", "Delhi": "Goa"}

    print_itinerary(dataSet)
