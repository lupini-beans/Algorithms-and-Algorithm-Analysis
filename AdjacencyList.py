from LinkedList import LinkedList


class AdjacencyList(object):
    """This class represents a graph.

    It stores the graph as a Linked List in an adjacency list format.
    """

    def __init__(self, weighted=False, directed=False, vertices=[]):
        """Creates an empty graph.

        Weighted and Directed are defaulted to False.
        :param weighted: True if weighted graph, otherwise false
        :param directed: True if directed graph, otherwise false
        :param vertices: List of vertices
        """
        self.graph = []
        self.weighted = weighted
        self.directed = directed
        self.vertices = vertices

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
        elif self.weighted and self.hasEdge(vertex1, vertex2[0]) \
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
            if edge_added == False:
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
        return(len(self.graph))

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

# Additional Methods___________________________________________________________
    def __find_path(self, start, end, path=None):
        if path == None:
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
        center = None
        edge_max = self.countVertices() - 1
        topo_type = None
        twos = True
        if self.isFullyConnected():
            topo_type = "Fully connected mesh"
        elif self.isConnected():
            for row in self.graph:
                if (row.get_length() - 1) == edge_max:
                    center = row.get_head()
                    for row in self.graph:
                        if row.get_head() != center and row.get_length() == 2:
                            topo_type = "Star"
                while twos:
                    if not row.get_length() == 3:
                        twos = False
                    else:
                        break
        else:
            topo_type = "No topology type found"
        if twos and topo_type == None:
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
                    if not(self.__find_path(start, row.get_head(), \
                                            path=[]) == None):
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

    def readGraph(self, fileName):
        """Reads the graph from a given file.

        :param fileName: Name of the file
        :return: Dictionary of graph values
        """
        inputParams = {'Weighted': None,
                       'Directional': None,
                       'Vertices': [],
                       'Edges': [],
                       'Instructions': [],
                       'Results': []}
        with open(fileName) as f:
            weighted = False
            weightIndex = 0
            directional = False
            directionalIndex = 0
            graphBegin = False
            graphBeginIndex = 0
            verticesIndex = 0
            graphEnd = False
            graphEndIndex = 0
            instructions = 0
            instructionIndex = 0
            results = 0
            resultIndex = 0
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
                        weightIndex = index
                    if line == 'weighted':
                        inputParams['Weighted'] = True
                    elif line == 'unweighted':
                        inputParams['Weighted'] = False
                    else:
                        raise RuntimeError("No weight found")
                elif (index == weightIndex+1) and (not directional):
                    if line == 'directed' or line == 'undirected':
                        directional = True
                        directionalIndex = index
                    if line == 'directed':
                        inputParams['Directional'] = True
                    elif line == 'undirected':
                        inputParams['Directional'] = False
                elif (index == directionalIndex+1) and (not graphBegin):
                    graphBegin = True
                    graphBeginIndex = index
                elif graphBegin and index == graphBeginIndex+1:
                    vertices = line.split()
                    inputParams['Vertices'].extend(vertices)
                    verticesIndex = index
                elif index > verticesIndex and not graphEnd:
                    if not line == 'end':
                        edge = line.split()
                        inputParams['Edges'].append(edge)
                    else:
                        graphEnd = True
                        graphEndIndex = index
                elif index == graphEndIndex+1 or \
                        (index == resultIndex+1 and results > 0):
                    struct = line.split()
                    inputParams['Instructions'].append(struct)
                    instructionIndex = index
                    instructions += 1
                elif index == instructionIndex+1 and instructions > 0:
                    inputParams['Results'].append(line.capitalize())
                    resultIndex = index
                    results += 1
        print(f"_________________________________________\n"
              f"Input Parameters from {fileName}:")
        for item in inputParams:
            print(f"{item}: {inputParams[item]}")
        print("_" * 41, "\n")
        self.__write_graph(inputParams)
        return inputParams

# Additional Method ___________________________________________________________
    def __write_graph(self, inputParams):
        results = []
        true_result = []
        found_struct = []
        self.weighted = inputParams['Weighted']
        self.directed = inputParams['Directional']
        for vertex in inputParams['Vertices']:
            self.addVertex(vertex)
        for edge in inputParams['Edges']:
            if self.weighted:
                self.addEdge(edge[0], [edge[1], edge[2]])
            else:
                self.addEdge(edge[0], edge[1])
        if inputParams['Instructions']:
            print("\n______Executing Instructions______\n")
        for instruction in inputParams['Instructions']:
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
        if inputParams['Results']:
            print("\n______Comparing Results______\n")
            print("Expected Results: ")
            for result in inputParams['Results']:
                true_result.append(result)
            for index, instruction in enumerate(inputParams['Instructions']):
                print(f"\t{instruction}: {true_result[index]}")
            print("\nFound Results:")
            for index, struct in enumerate(found_struct):
                print(f"\t{struct}: {results[index]}")
            if results == inputParams['Results']:
                print("\nSuccess: Expected values match results\n\n")
            else:
                print("\nFailed: Expected values do not match results\n\n")
#______________________________________________________________________________

    def printGraph(self):
        """Formats the graph to be able to print or output to a file.

        :return: List of items to be printed
        """
        toPrint = []
        vertices = ""
        edges = ""
        edgePairs = []
        toPrint.append("* Interpreted Graph:\n")
        if self.weighted:
            toPrint.append("weighted\n")
        else:
            toPrint.append("unweighted\n")
        if self.directed:
            toPrint.append("directed\n")
        else:
            toPrint.append("undirected\n")
        toPrint.append("begin\n")
        for vertex in self.vertices:
            vertices += str(vertex) + " "
        vertices += "\n"
        toPrint.append(vertices)
        for row in self.graph:
            if row.get_length() > 1:
                for edge in row:
                    if row.get_head() != edge[0]:
                        if not self.directed:
                            if (edge[0], row.get_head()) not in edgePairs:
                                if self.weighted:
                                    edgePairs.append((row.get_head(), edge[0]))
                                    edges += str(row.get_head()) + " " \
                                             + str(edge[0]) + " " \
                                             + str(edge[1]) + "\n"
                                else:
                                    edgePairs.append((row.get_head(), edge[0]))
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
        toPrint.append(edges)
        toPrint.append("end")
        return toPrint


if "__main__" == __name__:
    graph = AdjacencyList()
    fileName = input("Input File Name: ")
    graph.readGraph(fileName)
    print(graph)
    toPrint = graph.printGraph()
    for item in toPrint:
        print(item.rstrip())