from LinkedList import LinkedList


class AdjacencyList(object):
    """This class represents a graph.

    It stores the graph as a Linked List in an adjacency list format.
    """

    def __init__(self, weighted=False, directed=False):
        """Creates an empty graph.

        Weighted and Directed are defaulted to False.
        :param weighted: True if weighted graph, otherwise false
        :param directed: True if directed graph, otherwise false
        :param vertices: List of vertices
        """
        self.graph = []
        self.weighted = weighted
        self.directed = directed
        self.vertices = []
        self.prims = {}
        self.prims_vertices = []

    def __str__(self):
        """Formats the object into a string.

        :return: String representation of object
        """
        string = ""
        for vert in self.graph:
            string += str(vert) + "\n"
        return string

    def hasEdge(self, vertex1, vertex2):
        """Checks if an edge exists between two provided vertices.

        :param vertex1: The starting vertex
        :param vertex2: The destination vertex
        :return: True if the edge is found, otherwise false
        """
        edge_found = False
        if vertex1 in self.vertices and vertex2 in self.vertices:
            for vertex in self.graph:
                if vertex.get_head() == vertex1:
                    edge_found = vertex.has_node(vertex2)
        return edge_found

    def addEdge(self, vertex1, vertex2):
        """Adds an edge between two provided vertices.

        Cannot add an edge if the vertices do not exist in the graph.
        If the graph is undirected the edge is added from vertex1 to vertex2
        and from vertex2 to vertex1.

        If the edge already exists in the graph it will only update the graph
        if it is weighted and the weight
        is different than the one previously stored.

        :param vertex1: The starting vertex
        :param vertex2: The destination/connecting vertex
        :return: True if edge is successfully added, otherwise false
        """
        edge_added = False
        print('=' * 41)
        if vertex1 not in self.vertices and vertex2 not in self.vertices:
            print(f"Adding edge {vertex1} --> {vertex2}")
            print(f"Failed: {vertex1} and {vertex2} do not exist")
        elif vertex1 not in self.vertices:
            print(f"Adding edge {vertex1} --> {vertex2}")
            print(f"Failed: {vertex1} does not exist")
        elif vertex2[0] not in self.vertices:
            print(f"Adding edge {vertex1} --> {vertex2}")
            print(f"Failed: {vertex2} does not exist")
        elif (not self.weighted) and self.hasEdge(vertex1, vertex2[0]):
            print(f"Adding edge {vertex1} --> {vertex2}")
            print(f"Failed: {vertex1} --> {vertex2} already exists")
        elif self.weighted and self.hasEdge(vertex1, vertex2[0])\
                and not self.directed:
            print(f"Updating edge {vertex1} --> {vertex2}")
            for vertex in self.graph:
                if vertex.get_head() == vertex1:
                    for edge in vertex:
                        if edge[0] != vertex1:
                            if edge[0] == vertex2[0] and edge[1] != vertex2[1]:
                                edge[1] = vertex2[1]
                                edge_added = True
                                print\
                                    (f"Success: {vertex1} --> "
                                     f"{vertex2[0]} now has weight {edge[1]}")
                            else:
                                edge_added = False
            if not edge_added:
                print(f"Failed: {vertex1} --> {vertex2[0]}"
                      f" with weight {vertex2[1]} already exists")
        elif self.weighted and (not self.hasEdge(vertex1, vertex2[0])) \
                and (not self.directed):
            print(f"Adding edge {vertex1} <--> {vertex2[0]} with "
                  f"weight {vertex2[1]}")
            for row in self.graph:
                if row.get_head() == vertex1:
                    row.insert(vertex2)
                elif row.get_head() == vertex2[0]:
                    row.insert([vertex1, vertex2[1]])
                    edge_added = True
                    print(f"Success: {vertex1} <--> {vertex2[0]} with"
                          f" weight {vertex2[1]} added")
            if not edge_added:
                print(f"Failed: {vertex1} <--> {vertex2[0]} with"
                      f" weight {vertex2[1]} not added")
        elif self.weighted and self.hasEdge(vertex1, vertex2[0]) \
                and not self.directed:
            print(f"Updating edge {vertex1} <--> {vertex2[0]} with "
                  f"weight {vertex2[1]}")
            for row in self.graph:
                if row.get_head() == vertex1:
                    for edge in row:
                        if edge[0] != vertex1:
                            if edge[0] == vertex2[0] and edge[1] != vertex2[1]:
                                edge[1] = vertex2[1]
                                edge_added = True
                elif row.get_head() == vertex2[0]:
                    for edge in row:
                        if edge[0] != vertex2[0]:
                            if edge[0] == vertex1 and edge[1] != vertex2[1]:
                                edge[1] = vertex2[1]
                                edge_added = True
            if not edge_added:
                print(f"Failed: {vertex1} <--> {vertex2[0]} with "
                      f"weight {vertex2[1]} already exists")
            else:
                print(f"Success: {vertex1} <--> {vertex2[0]} now has "
                      f"weight {vertex2[1]}")
        elif self.weighted and self.hasEdge(vertex1, vertex2[0]) and \
                self.directed:
            print(f"Updating edge {vertex1} --> {vertex2[0]} with "
                  f"weight {vertex2[1]}")
            for row in self.graph:
                if row.get_head() == vertex1:
                    for edge in row:
                        if edge[0] != vertex1:
                            if edge[0] == vertex2[0] and edge[1] != vertex2[1]:
                                edge[1] = vertex2[1]
                                edge_added = True
            if edge_added:
                print(f"Success: {vertex1} --> {vertex2[0]} now has"
                      f" weight {vertex2[1]}")
            else:
                print(f"Failed: {vertex1} <--> {vertex2[0]} with weight"
                      f" {vertex2[1]} already exists")
        elif not self.weighted and not self.hasEdge(vertex1, vertex2) \
                and not self.directed:
            print(f"Adding edge {vertex1} <--> {vertex2}")
            for row in self.graph:
                if row.get_head() == vertex1:
                    row.insert(vertex2)
                elif row.get_head() == vertex2:
                    row.insert(vertex1)
                    edge_added = True
            if edge_added:
                print(f"Success: {vertex1} <--> {vertex2} added")
        elif not self.directed and self.hasEdge(vertex1, vertex2):
            edge_added = False
            print(f"Failed: {vertex1} <--> {vertex2} already exists")
        else:
            print(f"Adding edge {vertex1} --> {vertex2}")
            for vertex in self.graph:
                if vertex.get_head() == vertex1:
                    vertex.insert(vertex2)
                    print(f"Success: {vertex1} --> {vertex2} added")
                    edge_added = True
        print('=' * 41)
        return edge_added

    def deleteEdge(self, vertex1, vertex2):
        """Deletes an edge between two provided vertices.

        :param vertex1: Starting vertex
        :param vertex2: Destination vertex
        :return: True if edge is deleted, False otherwise
        """
        edge_deleted = False
        print("=" * 41)
        print(f"Deleting edge {vertex1} --> {vertex2}...")
        if self.hasEdge(vertex1, vertex2):
            for vertex in self.graph:
                if vertex.get_head() == vertex1:
                    vertex.delete(vertex2)
                    edge_deleted = True
                    print(f"Success: {vertex1} --> {vertex2} deleted")
        if not edge_deleted:
            print(f"Failed: {vertex1} --> {vertex2} not deleted")
        print("=" * 41)
        return edge_deleted

    def addVertex(self, vertex):
        """Adds the provided vertex.

        :param vertex: The vertex to add to the graph
        :return: True if vertex is added, False otherwise
        """
        print('_' * 41)
        print(f"Adding vertex: {vertex}...")
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.graph.append(LinkedList(head_node=vertex))
            print(f"Success: {vertex} added")
            print('_' * 41)
            return True
        else:
            print(f"Failed: {vertex} already exists")
            print('_' * 41, "\n")
            return False

    def deleteVertex(self, vertex):
        """Deletes the provided vertex.

        :param vertex: Vertex to delete
        :return: True if vertex is deleted, False otherwise
        """
        vertex_deleted = False
        print('_' * 41)
        print(f"Deleting vertex: {vertex}...")
        if vertex in self.vertices:
            for row in self.graph:
                if row.get_head() == vertex:
                    self.graph.remove(row)
                    vertex_deleted = True
        else:
            print(f"Failed: {vertex} doesn't exist'")
        if vertex_deleted:
            for row in self.graph:
                if self.hasEdge(row.get_head(), vertex):
                    self.deleteEdge(row.get_head(), vertex)
            if vertex_deleted:
                self.vertices.remove(vertex)
                print(f"Success: {vertex} deleted")
            else:
                print(f"Failed: {vertex} not deleted")
        print("_" * 41)
        return vertex_deleted

    def isSparse(self):
        """Checks if the current graph is sparse.

        The ratio of vertices and edges needs to be below 15%.
        :return: True if sparse, False otherwise
        """
        print("_" * 41)
        print("Checking if Sparse: ")
        num_edges = self.countEdges()
        num_vertex = self.countVertices()
        if self.directed:
            percent = num_edges/(num_vertex * 2) * 100
        else:
            percent = (num_edges/(3**(num_vertex-2) + num_vertex)) * 100
        if percent >= 15:
            is_sparse = False
        else:
            is_sparse = True
        print(is_sparse)
        print("_" * 41, "\n")
        return is_sparse

    def isDense(self):
        """Checks if the current graph is dense.

        The ratio of vertices and edges needs to be above 85%.
        :return: True if sparse, False otherwise
        """
        print("_" * 41)
        print("Checking if Dense: ")
        num_edges = self.countEdges()
        num_vertex = self.countVertices()
        if self.directed:
            percent = num_edges/num_vertex * 2 * 100
        else:
            percent = ((num_edges * 2)/(3**(num_vertex-2) + num_vertex)) * 100
        if percent > 84:
            is_dense = True
        else:
            is_dense = False
        print(is_dense)
        print("_" * 41, "\n")
        return is_dense

    def countVertices(self):
        """Counts the number of vertices in the graph.

        :return: The number of vertices
        """
        return len(self.graph)

    def countEdges(self):
        """Counts the number of edges in the graph.

        :return: The number of edges
        """
        count = 0
        for row in self.graph:
            count += (row.get_length() - 1)
        if not self.directed:
            count = int(count/2)
        return count

    def find_index(self, lst, weight):
        index = 0
        for item in lst:
            while weight > item[1] and index<len(lst):
                index+=1
        return index

    def prims_tree(self):
        if not self.weighted:
            return
        #Create a dictionary to reference of the graph
        graph_dictionary = {}
        for row in self.graph:
            key = row.get_head()
            graph_dictionary[key] = []
            for edge in row:
                if edge[0] != key:
                    if len(graph_dictionary[key]) == 0:
                        graph_dictionary[key].append(edge)
                    else:
                        index = self.find_index(graph_dictionary[key], edge[1])
                        graph_dictionary[key].insert(index, edge)



        #1. Initiate the spanning tree vertices list to a random vertex
        #  from the input vertices list
        self.prims_vertices.append(self.vertices[0])
        self.prims[self.vertices[0]] = []

        #2. Initiate an empty dictionary for the spanning tree edges
            #Ignored - added to initialization of graph

        #3. Iterate through the list of input vertices from 1 to (length - 1)
        # (leave the last vertex because it will be caught later) (for loop)
        for i in range(1, len(self.vertices)):
            lows = []
            lowest = [0, [0, float('inf')]]
            #3.a. Generate a list of valid edges to search weights (for loop)
                #3.a.(1) Confirm that the starting vertex is already in the spanning tree vertices
                #3.a.(2) Confirm that the ending vertex is not in the spanning tree vertices
            for vertex in self.prims_vertices:
                if len(graph_dictionary[vertex]) >= 1:
                    if graph_dictionary[vertex][0][0] not in self.prims_vertices:
                        print("Vertex:", vertex, "\nEdge:", graph_dictionary[vertex][0])
                        lows.append([vertex, graph_dictionary[vertex][0]])

            #3.a.(3) Find the smallest weight
            for low in lows:
                if lowest:
                    if float(low[1][1]) < float(lowest[1][1]):
                        lowest = low
                else:
                    lowest = low
            #3.b. Add the resulted vertex into spanning tree vertices list
            self.prims[lowest[0]] = lowest[1]

            #3.c. Add the resulted edge into the spanning tree edge dictionary
            self.prims_vertices.append(lowest[1][0])

            #Extra: Pop off the edge used
            if len(graph_dictionary[lowest[0]]) >= 1:
                graph_dictionary[lowest[0]].pop(0)
                graph_dictionary[lowest[1][0]].remove([lowest[0], lowest[1][1]])

        #4. Return my edge dictionary
        return self.prims


# Additional Methods___________________________________________________________
    def __find_path(self, start, end, path=None):
        if path is None:
            path = []
        path.append(start)
        if start == end:
            return path
        for row in self.graph:
            if row.get_head() == start:
                for edge in row:
                    if (edge[0] not in path) and \
                            (self.hasEdge(row.get_head(), edge[0])):
                        newpath = self.__find_path(edge[0], end, path)
                        if newpath:
                            return newpath
        return None

    def __edge_counter(self, vertex):
        count = 0
        for row in self.graph:
            if row.get_head() == vertex:
                count = row.get_length() - 1
        return count

    def topo(self):
        """Checks for the topology type of the graph.

        :return: Fully connected mesh, star, or ring
        """
        edge_max = self.countVertices() - 1
        topo_type = None
        twos = True
        if self.isFullyConnected():
            topo_type = "Fully connected mesh"
        elif self.isConnected():
            for row in self.graph:
                if (row.get_length() - 1) == edge_max:
                    center = row.get_head()
                    for rows in self.graph:
                        if rows.get_head() != center and\
                                rows.get_length() == 2:
                            topo_type = "Star"
                while twos:
                    if not row.get_length() == 3:
                        twos = False
                    else:
                        break
        else:
            topo_type = "No topology type found"
        if twos and topo_type is None:
            topo_type = "Ring"
        print(topo_type)
        return topo_type
# _____________________________________________________________________________

    def isConnected(self):
        """Checks if the graph is connected.

        If there is a path from every vertex to every other vertex, the graph
        is connected.
        :return: True if connected, False otherwise
        """
        print("=" * 41)
        print("Checking if connected: ")
        is_connected = True
        for vertex in self.vertices:
            start = vertex
            for row in self.graph:
                if row.get_length() == 1:
                    is_connected = False
                    break
            if is_connected:
                for row in self.graph:
                    if not(self.__find_path(start, row.get_head(),
                                            path=[]) is None):
                        continue
                    else:
                        is_connected = False
        print(is_connected)
        print("=" * 41)
        return is_connected

    def isFullyConnected(self):
        """Checks if the graph is fully connected.

        If there is an edge from every vertex to every other vertex, the graph
        is fully connected.
        :return: True if fully connected, False otherwise
        """
        print("_" * 41)
        print("Checking if fully connected:")
        is_fully_connected = True
        if not self.isConnected():
            is_fully_connected = False
        if is_fully_connected:
            for vertex1 in self.vertices:
                for vertex2 in self.vertices:
                    if not self.hasEdge(vertex1, vertex2) and \
                            (not vertex1 == vertex2):
                        print(f"{vertex1} --> {vertex2} does not exist")
                        is_fully_connected = False
                        break
                    if not is_fully_connected:
                        break
        print(is_fully_connected)
        print("_" * 41)
        return is_fully_connected

    def readGraph(self, file_name):
        """Reads the graph from a given file.

        :param file_name: Name of the file
        :return: Dictionary of graph values
        """
        input_params = {'Weighted': None,
                        'Directional': None,
                        'Vertices': [],
                        'Edges': [],
                        'Instructions': [],
                        'Results': []}
        with open(file_name) as f:
            weighted = False
            weight_index = 0
            directional = False
            directional_index = 0
            graph_begin = False
            graph_begin_index = 0
            vertices_index = 0
            graph_end = False
            graph_end_index = 0
            instructions = 0
            instruction_index = 0
            results = 0
            result_index = 0
            lines = []
            for line in f.readlines():
                line = line.strip('\n')
                lines.append(line)
            for index, line in enumerate(lines):
                if line[0] == '*':
                    continue
                elif not weighted:
                    if line == 'weighted' or line == 'unweighted':
                        weighted = True
                        weight_index = index
                    if line == 'weighted':
                        input_params['Weighted'] = True
                    elif line == 'unweighted':
                        input_params['Weighted'] = False
                    else:
                        raise RuntimeError("No weight found")
                elif (index == weight_index+1) and (not directional):
                    if line == 'directed' or line == 'undirected':
                        directional = True
                        directional_index = index
                    if line == 'directed':
                        input_params['Directional'] = True
                    elif line == 'undirected':
                        input_params['Directional'] = False
                elif (index == directional_index+1) and (not graph_begin):
                    graph_begin = True
                    graph_begin_index = index
                elif graph_begin and index == graph_begin_index+1:
                    vertices = line.split()
                    input_params['Vertices'].extend(vertices)
                    vertices_index = index
                elif index > vertices_index and not graph_end:
                    if not line == 'end':
                        edge = line.split()
                        input_params['Edges'].append(edge)
                    else:
                        graph_end = True
                        graph_end_index = index
                elif index == graph_end_index+1 or \
                        (index == result_index+1 and results > 0):
                    struct = line.split()
                    input_params['Instructions'].append(struct)
                    instruction_index = index
                    instructions += 1
                elif index == instruction_index+1 and instructions > 0:
                    input_params['Results'].append(line.capitalize())
                    result_index = index
                    results += 1
        print(f"_________________________________________\n"
              f"Input Parameters from {fileName}:")
        for parameter in input_params:
            print(f"{parameter}: {input_params[parameter]}")
        print("_" * 41, "\n")
        self.__write_graph(input_params)
        return input_params

# Additional Method ___________________________________________________________
    def __write_graph(self, input_params):
        results = []
        true_result = []
        found_struct = []
        self.weighted = input_params['Weighted']
        self.directed = input_params['Directional']
        for vertex in input_params['Vertices']:
            self.addVertex(vertex)
        for edge in input_params['Edges']:
            if self.weighted:
                self.addEdge(edge[0], [edge[1], edge[2]])
            else:
                self.addEdge(edge[0], edge[1])
        if input_params['Instructions']:
            print("\n______Executing Instructions______\n")
        for instruction in input_params['Instructions']:
            found_struct.append(instruction)
            if instruction[0] == "hasEdge":
                results.append(str(self.hasEdge(instruction[1],
                                                instruction[2])))
            elif instruction[0] == "addEdge":
                if self.weighted:
                    results.append(str(self.addEdge(instruction[1],
                                                    [instruction[2],
                                                     instruction[3]])))
                else:
                    results.append(str(self.addEdge(instruction[1],
                                                    instruction[2])))
            elif instruction[0] == "deleteEdge":
                results.append(str(self.deleteEdge(instruction[1],
                                                   instruction[2])))
            elif instruction[0] == "addVertex":
                results.append(str(self.addVertex(instruction[1])))
            elif instruction[0] == "deleteVertex":
                results.append(str(self.deleteVertex(instruction[1])))
            elif instruction[0] == "isSparse":
                results.append(str(self.isSparse()))
            elif instruction[0] == "isDense":
                results.append(str(self.isDense()))
            elif instruction[0] == "countVertices":
                results.append(str(self.countVertices()))
            elif instruction[0] == "countEdges":
                results.append(str(self.countEdges()))
            elif instruction[0] == "isConnected":
                results.append(str(self.isConnected()))
            elif instruction[0] == "isFullyConnected":
                results.append(str(self.isFullyConnected()))
            elif instruction[0] == "topo":
                results.append(self.topo())
            else:
                raise RuntimeError("No instruction found")
        if input_params['Results']:
            print("\n______Comparing Results______\n")
            print("Expected Results: ")
            for result in input_params['Results']:
                true_result.append(result)
            for index, instruction in enumerate(input_params['Instructions']):
                print(f"\t{instruction}: {true_result[index]}")
            print("\nFound Results:")
            for index, struct in enumerate(found_struct):
                print(f"\t{struct}: {results[index]}")
            if results == input_params['Results']:
                print("\nSuccess: Expected values match results\n\n")
            else:
                print("\nFailed: Expected values do not match results\n\n")

    def printGraph(self):
        """Formats the graph to be able to print or output to a file.

        :return: List of items to be printed
        """
        to_print = []
        vertices = ""
        edges = ""
        edge_pairs = []
        to_print.append("* Interpreted Graph:\n")
        if self.weighted:
            to_print.append("weighted\n")
        else:
            to_print.append("unweighted\n")
        if self.directed:
            to_print.append("directed\n")
        else:
            to_print.append("undirected\n")
        to_print.append("begin\n")
        for vertex in self.vertices:
            vertices += str(vertex) + " "
        vertices += "\n"
        to_print.append(vertices)
        for row in self.graph:
            if row.get_length() > 1:
                for edge in row:
                    if row.get_head() != edge[0]:
                        if not self.directed:
                            if (edge[0], row.get_head()) not in edge_pairs:
                                if self.weighted:
                                    edge_pairs.append((row.get_head(),
                                                      edge[0]))
                                    edges += str(row.get_head()) + " " \
                                        + str(edge[0]) + " " \
                                        + str(edge[1]) + "\n"
                                else:
                                    edge_pairs.append((row.get_head(),
                                                       edge[0]))
                                    edges += str(row.get_head() + " "
                                                 + str(edge[0]) + "\n")
                        else:
                            if self.weighted:
                                edges += str(row.get_head() + " "
                                             + str(edge[0]) + " "
                                             + str(edge[1]) + "\n")
                            else:
                                edges += str(row.get_head()) \
                                         + " " + str(edge[0]) + "\n"
        to_print.append(edges)
        to_print.append("end")
        return to_print


if "__main__" == __name__:
    graph = AdjacencyList()
    fileName = input("Input File Name: ")
    graph.readGraph(fileName)
    print('type: ', type(graph))
    print(graph)
    toPrint = graph.printGraph()
    for item in toPrint:
        print(item.rstrip())
    graph_dict = graph.prims_tree()
    print("\nDictionary:")
    print(graph_dict)
