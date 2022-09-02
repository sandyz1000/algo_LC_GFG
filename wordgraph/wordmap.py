import sys
from collections import defaultdict


class Vertex:
    """Vertex class to create a vertex of a graph"""
    def __init__(self, key):
        self.__id = key
        self.__connected_to = {}
        self.__color = "white"
        self.__predecessor = None
        self.__distance = 0

    def get_id(self):
        return self.__id

    def add_neighbour(self, nbr, weight=0):
        self.__connected_to[nbr] = weight

    def __str__(self):
        return str(self.__id) + ' connectedTo: ' + str([x.id for x in self.__connected_to])

    def get_connections(self):
        return self.__connected_to.keys()

    def get_weight(self, nbr):
        return self.__connected_to[nbr]

    def get_color(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def get_predecessor(self):
        return self.__predecessor

    def set_predecessor(self, predecessor):
        self.__predecessor = predecessor

    def get_distance(self):
        return self.__distance

    def set_distance(self, distance):
        self.__distance = distance


class Graph:
    """Graph class to create a graph from all nodes and adding a edge of the connected nodes"""
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        self.vert_list[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vert_list[key]

    def add_edge(self, k, f, weight=0):
        if k not in self.vert_list:
            self.vert_list[k] = Vertex(k)
        if f not in self.vert_list:
            self.vert_list[f] = Vertex(f)

        self.vert_list[k].add_neighbour(self.vert_list[f], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __contains__(self, item):
        return item in self.vert_list


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) <= 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class WordList:
    """Word list will use all the above DS to form the graph of connected words"""
    def __init__(self):
        self.word_file_list = []
        self.graph = Graph()
        self.word_map = defaultdict(list)
        with open('wordlist', 'r') as wordfile:
            self.word_file_list = [line[:-1] for line in wordfile if line != ""]

        self.word_mapper()  # Form a bucket
        self.build_graph()  # Build network graph of words

    def getGraph(self):
        return self.graph

    def word_mapper(self):
        for word in self.word_file_list:
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                self.word_map[bucket].append(word)

    def build_graph(self):
        # Build graph that put all edge in the current bucket
        # Get all the combination of edges in the bucket
        for bucket in self.word_map.keys():
            for word1 in self.word_map[bucket]:
                for word2 in self.word_map[bucket]:
                    if word1 != word2:
                        self.graph.add_edge(word1, word2)

    def search(self, start_node):
        start_node.set_distance(0)
        start_node.set_predecessor(None)
        vert_queue = Queue()
        vert_queue.enqueue(start_node)

        while vert_queue.size() > 0:
            current_vertex = vert_queue.dequeue()

            for nbr in current_vertex.get_connections():
                if nbr.get_color() == 'white':
                    nbr.setColor('gray')
                    nbr.set_distance(current_vertex.get_distance() + 1)
                    nbr.set_predecessor(current_vertex)
                    vert_queue.enqueue(nbr)
            current_vertex.setColor('black')

    def traverse(self, start_node):
        x = start_node
        path = []

        while x.get_predecessor():
            path.append(x.get_id())
            x = x.get_predecessor()
        path.append(x.get_id())
        path.reverse()
        return path


if __name__ == "__main__":
    wordlist = WordList()
    arg1, arg2 = sys.argv[1:]
    if arg1 and arg2:
        source = wordlist.getGraph().get_vertex(arg1)
        dest = wordlist.getGraph().get_vertex(arg2)
        wordlist.search(source)
        shortest_path = wordlist.traverse(dest)
        print(shortest_path)
    else:
        print("Pass valid argument")
