import unittest


class AdjacencyMatrix(object):
    def __init__(self, weighted=False, directed=False):
        self.graph = []
        self.weighted = weighted
        self.directed = directed

    def __str__(self):
        temp = []
        columns = []
        out_string = ""
        top_str = " " * 3
        for item in self.graph:
            for sub_item in item:
                temp.append(sub_item)
        for index, item in enumerate(temp):
            if len(item) == 1:
                out_string += "\n" + str(item) + " |"
                columns.append(item)
            else:
                if len(str(temp[index][1])) < 8:
                    padding = 8 - len(str(temp[index][1]))
                    out_string += str(temp[index][1]) + (padding * " ") + "|"
                else:
                    out_string += str(temp[index][1]) + "|"
        for index, item in enumerate(columns):
            if columns[index]:
                top_str += str(item) + (" " * 8)
            else:
                top_str += str(item)
        out_string = top_str + out_string
        return out_string

    def hasEdge(self, vertex1, vertex2):
        edge_found = False
        for row_index, row in enumerate(self.graph):
            if row[0] == vertex1:
                for column_index, column in enumerate(self.graph[row_index]):
                    if not len(column) == 1:
                        if column[0] == vertex2:
                            if not self.weighted:
                                edge_found = column[1]
                            elif float(column[1]) > 0:
                                edge_found = True
        return edge_found

# Additional Methods___________________________________________________________
    def __has_row_column(self, vertex1, vertex2):
        row_column_found = False
        if not self.__find_index(vertex1, vertex2) == []:
            row_column_found = True
        return row_column_found

    def __find_index(self, vertex1, vertex2):
        index = []
        for row_index, row in enumerate(self.graph):
            if self.graph[row_index][0] == vertex1:
                for column_index, column in enumerate(self.graph[row_index]):
                    if not len(self.graph[row_index][column_index]) == 1:
                        if self.graph[row_index][column_index][0] == vertex2:
                            index.append(row_index),
                            index.append(column_index)
        return index
#______________________________________________________________________________

    def addEdge(self, vertex1, vertex2, edge = None):
        edge_added = False
        if edge:
            print("=" * 41)
            print(f"Adding edge: {vertex1} --> {vertex2} = {edge}")
        if edge == None and not self.weighted:
            edge = True
        if edge == None and self.weighted:
            if self.weighted:
                print("Failed: No weight included")
        elif self.hasEdge(vertex1, vertex2):
            if not self.weighted:
                if edge:
                    print(f"Failed: {vertex1} --> {vertex2} already exists")
            else:
                index = self.__find_index(vertex1, vertex2)
                if not edge == self.graph[index[0]][index[1]][1]:
                    self.graph[index[0]][index[1]][1] = edge
                    print(f"Success: {vertex1} --> {vertex2} with "
                          f"weight {edge} added")
                    edge_added = True
                else:
                    print(f"Failed: {vertex1} --> {vertex2} with "
                          f"weight \n\t {edge} already exists")
        elif not self.__has_row_column(vertex1, vertex2):
            row1 = row2 = False
            for row in self.graph:
                if row[0] == vertex1:
                    row1 = True
                if row[0] == vertex2:
                    row2 = True
            if row1 and row2:
                for rowIndex, row in enumerate(self.graph):
                    if self.graph[rowIndex][0] == vertex1:
                        self.graph[rowIndex].append([vertex2, edge])
        elif self.__has_row_column(vertex1, vertex2) and \
                not self.hasEdge(vertex1, vertex2):
            index = self.__find_index(vertex1, vertex2)
            self.graph[index[0]][index[1]][1] = edge
            if not self.directed:
                index = self.__find_index(vertex2, vertex1)
                self.graph[index[0]][index[1]][1] = edge
            if edge or edge > 0:
                edge_added = True
                print(f"Success: {vertex1} --> {vertex2} added")
        if edge:
            print("=" * 41)
        return edge_added

    def deleteEdge(self, vertex1, vertex2):
        edge_removed = False
        print('_' * 41)
        print(f"Deleting edge: {vertex1} --> {vertex2}")
        if self.hasEdge(vertex1, vertex2):
            index = self.__find_index(vertex1, vertex2)
            if not self.weighted:
                self.graph[index[0]][index[1]][1] = False
            else:
                self.graph[index[0]][index[1]][1] = 0
            edge_removed = True
            print(f"Success: {vertex1} --> {vertex2} removed")
        else:
            edge_removed = False
            print(f"Failed: {vertex1} --> {vertex2} does not exist")
        print("_" * 41, "\n")
        return edge_removed


    def addVertex(self, vertex):
        edges = []
        print("_" * 41)
        print(f"Adding Vertex {vertex}...")
        vertex_added = False
        if self.graph == []:
            self.graph.append([vertex])
            vertex_added = True
        else:
            for row_index, row in enumerate(self.graph):
                if self.graph[row_index][0] == vertex:
                    print(f"Failed: {vertex} already exists")
                    vertex_added = False
                else:
                    self.graph.append([vertex])
                    vertex_added = True
                    break
        if vertex_added:
            for row_index, row in enumerate(self.graph):
                if not self.weighted:
                    if not vertex == self.graph[row_index][0]:
                        self.addEdge(vertex, self.graph[row_index][0], False)
                        self.addEdge(self.graph[row_index][0], vertex, False)
                        edges.append([vertex, self.graph[row_index][0]])
                        edges.append([self.graph[row_index][0], vertex])
                    else:
                        self.addEdge(vertex, self.graph[row_index][0], False)
                        edges.append([vertex, self.graph[row_index][0]])
                else:
                    if not vertex == self.graph[row_index][0]:
                        self.addEdge(vertex, self.graph[row_index][0], 0)
                        self.addEdge(self.graph[row_index][0], vertex, 0)
                        edges.append([vertex, self.graph[row_index][0]])
                        edges.append([self.graph[row_index][0], vertex])
                    else:
                        self.addEdge(vertex, self.graph[row_index][0], 0)
                        edges.append([vertex, self.graph[row_index][0]])
            print("Adding edges... ")
            for edge in edges:
                print(edge)
            print(f"Success: {vertex} added")
        print("_" * 41, "\n")
        return vertex_added


    def deleteVertex(self, vertex):
        vertex_deleted = False
        print('_' * 41)
        print(f"Deleting vertex: {vertex}")
        for row_index, row in enumerate(self.graph):
            for column_index, column in enumerate(self.graph[row_index]):
                if self.graph[row_index][column_index][0] == vertex \
                        and len(self.graph[row_index][column_index]) == 2:
                    self.graph[row_index].pop(column_index)
                    vertex_deleted = True
        if vertex_deleted:
            for row_index, row in enumerate(self.graph):
                if self.graph[row_index][0] == vertex:
                    self.graph.pop(row_index)
            print(f"Success {vertex} deleted")
        else:
            print(f"Failed: {vertex} not found")
        print('_' * 41, "\n")
        return vertex_deleted

    def isSparse(self):
        print("_" * 41)
        print("Checking if Sparse: ")
        numEdges = self.countEdges()
        numVertex = self.countVertices()
        if self.directed:
            percent = numEdges/(numVertex * 2) * 100
        else:
            percent = (numEdges/(3**(numVertex-2) + numVertex)) * 100
        if percent >= 15:
            isSparse = False
        else:
            isSparse = True
        print(isSparse)
        print("_" * 41, "\n")
        return isSparse

    def isDense(self):
        print("_" * 41)
        print("Checking if Dense: ")
        numEdges = self.countEdges()
        numVertex = self.countVertices()
        if self.directed:
            percent = numEdges/(numVertex * 2) * 100
        else:
            percent = ((numEdges * 2)/(3**(numVertex-2) + numVertex)) * 100
        if percent >= 85:
            isDense = True
        else:
            isDense = False
        print(isDense)
        print("_" * 41, "\n")
        return isDense

    def countVertices(self):
        count = 0
        for rowIndex, row in enumerate(self.graph):
            if len(self.graph[rowIndex][0]) == 1:
                count += 1
        return count

    def countEdges(self):
        count = 0
        for rowIndex, row in enumerate(self.graph):
            for columnIndex, column in enumerate(self.graph[rowIndex]):
                if len(self.graph[rowIndex][columnIndex]) == 2 and \
                        (column[1] == True or float(column[1]) > 0):
                    count += 1
        if not self.directed:
            count = int(count/2)
        return count

# Additional Method____________________________________________________________
    def __find_path(self, start, end, path=None):
        if path == None:
            path = []
        path.append(start)
        if start == end:
            return path
        for rowIndex, row in enumerate(self.graph):
            if row[0] == start:
                for columnIndex, column in enumerate(row):
                    if (column[0] not in path) and \
                            (self.hasEdge(row[0], column[0])):
                        newpath = self.__find_path(column[0], end, path)
                        if newpath:
                            return newpath
        return None
# _____________________________________________________________________________

    def isConnected(self):
        print("=" * 41)
        print("Checking if connected: ")
        connected = True
        for rowIndex, row in enumerate(self.graph):
            start = row[0]
            not_edgeCount = 0
            for columnIndex, column in enumerate(self.graph[rowIndex]):
                if len(self.graph[rowIndex][columnIndex]) == 2:
                    if column[1] == False or column[1] == 0:
                        not_edgeCount += 1
                        if not_edgeCount == (len(self.graph[rowIndex]) - 1):
                            connected = False
                            break
                    else:
                        connected = True
                if not connected:
                    break
            if connected:
                if not (self.__find_path(start, column[0], path = []) == None):
                    continue
                else:
                    connected = False
        print(connected)
        print("=" * 41)
        return connected

    def isFullyConnected(self):
        print("_" * 41)
        print("Checking if fully connected: ")
        vertices = []
        fully_connected = True
        for row in self.graph:
            vertices.append(row[0])
        if not self.isConnected():
            fully_connected = False
        if fully_connected:
            for vertex1 in vertices:
                for vertex2 in vertices:
                    if not self.hasEdge(vertex1, vertex2) and \
                            (not vertex1 == vertex2):
                        print(f"{vertex1} --> {vertex2} does not exist")
                        fully_connected = False
                        break
                if not fully_connected:
                    break
        print(fully_connected)
        print("_" * 41, "\n")
        return fully_connected

    def __edge_counter(self, vertex):
        count = 0
        for row in self.graph:
            if row[0] == vertex:
                for column in row:
                    if len(column) == 2 and (column[1] == True or
                                             float(column[1]) > 0):
                        count += 1
        return count

    def topo(self):
        center = None
        edge_max = self.countVertices()-1
        topo_type = None
        twos = True
        if self.isFullyConnected():
            print("MY DICK")
            topo_type = "Fully connected mesh"
        elif self.isConnected():
            for row in self.graph:
                if self.__edge_counter(row[0]) == edge_max:
                    center = row[0]
                    for row in self.graph:
                        if row[0] != center and \
                                self.__edge_counter(row[0]) == 1:
                            topo_type = "Star"
                while twos:
                    if not self.__edge_counter(row[0]) == 2:
                        twos = False
                    else:
                        break
        else:
            topo_type = "No topology type found"
        if twos and topo_type == None:
            topo_type = "Ring"
        print(topo_type)
        return topo_type


    def readGraph(self, fileName):
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
        self.__writeGraph(inputParams)
        return inputParams

# Addition Method______________________________________________________________
    def __writeGraph(self, inputParams):
        results = []
        true_result = []
        found_struct = []
        self.weighted = inputParams['Weighted']
        self.directed = inputParams['Directional']
        for vertex in inputParams['Vertices']:
            self.addVertex(vertex)
        for edge in inputParams['Edges']:
            if self.weighted:
                self.addEdge(edge[0], edge[1], edge[2])
            else:
                self.addEdge(edge[0], edge[1])
        if inputParams['Instructions']:
            print("\n")
            print("*" * 50, "\n")
            print("\n______Executing Instructions______\n")
        for instruction in inputParams['Instructions']:
            found_struct.append(instruction)
            if instruction[0] == "hasEdge":
                results.append(str(self.hasEdge(instruction[1],
                                                instruction[2])))
            elif instruction[0] == "addEdge" and self.weighted:
                results.append(str(self.addEdge(instruction[1],
                                                instruction[2],
                                                instruction[3])))
            elif instruction[0] == "addEdge" and not self.weighted:
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
                results.append(str(self.topo()))
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
        toPrint = []
        vertices = ""
        edges = ""
        edgePairs = []
        toPrint.append("\n\n* Interpreted Graph:\n")
        if self.weighted:
            toPrint.append("weighted\n")
        else:
            toPrint.append("unweighted\n")
        if self.directed:
            toPrint.append("directed\n")
        else:
            toPrint.append("undirected\n")
        toPrint.append("begin\n")
        for row in self.graph:
            vertices += str(row[0]) + " "
        vertices += "\n"
        toPrint.append(vertices)
        for rowIndex, row in enumerate(self.graph):
            for column in self.graph[rowIndex]:
                if self.hasEdge(row[0], column[0]):
                    if not self.directed:
                        if self.weighted:
                            if (column[0], row[0]) not in edgePairs:
                                edgePairs.append((row[0], column[0]))
                                edges += row[0] + " " + column[0] +\
                                         " " + column[1] + "\n"
                        else:
                            if (column[0], row[0]) not in edgePairs:
                                edgePairs.append((row[0], column[0]))
                                edges += row[0] + " " + column[0] + "\n"
                    else:
                        if self.weighted:
                            edges += row[0] + " " + column[0] +\
                                     " " + column[1] + "\n"
                        else:
                            edges += row[0] + " " + column[0] + "\n"
        toPrint.append(edges)
        toPrint.append("end")
        return toPrint

class methodTest(unittest.TestCase):

    def test_empty_graph(self):
        self.assertEqual(AdjacencyMatrix().graph, [])

# Has Edge Tests_______________________________________________________________
    def test_has_edge_directed_unweighted(self):
        test_graph = AdjacencyMatrix()
        test_graph.directed = True
        test_graph.weighted = False
        test_graph.addVertex('A')
        test_graph.addVertex('B')
        test_graph.addEdge('A', 'B', True)
        self.assertTrue(test_graph.hasEdge('A', 'B'))
        self.assertFalse(test_graph.hasEdge('B', 'A'))
        del test_graph

    def test_has_edge_directed_weighted(self):
        test_graph = AdjacencyMatrix()
        test_graph.directed = True
        test_graph.weighted = True
        test_graph.addVertex('A')
        test_graph.addVertex('B')
        test_graph.addEdge('A', 'B', 1.0)
        self.assertTrue(test_graph.hasEdge('A', 'B'))
        self.assertFalse(test_graph.hasEdge('B', 'A'))
        del test_graph

    def test_has_edge_undirected_unweighted(self):
        test_graph = AdjacencyMatrix()
        test_graph.directed = False
        test_graph.weighted = False
        test_graph.addVertex('A')
        test_graph.addVertex('B')
        test_graph.addEdge('A', 'B', True)
        self.assertTrue(test_graph.hasEdge('A', 'B'))
        self.assertTrue(test_graph.hasEdge('B', 'A'))
        del test_graph

    def test_has_edge_undirected_weighted(self):
        test_graph = AdjacencyMatrix()
        test_graph.directed = False
        test_graph.weighted = False
        test_graph.addVertex('A')
        test_graph.addVertex('B')
        test_graph.addEdge('A', 'B', 1.0)
        self.assertTrue(test_graph.hasEdge('A', 'B'))
        self.assertTrue(test_graph.hasEdge('B', 'A'))
        del test_graph
#______________________________________________________________________________
    def test_add_edge_directed_unweighted(self):
        test_graph = AdjacencyMatrix()
        test_graph.directed = True
        test_graph.weighted = False
        test_graph.addVertex('A')
        test_graph.addVertex('B')
        self.assertTrue(test_graph.addEdge('A', 'B', True))
        self.assertFalse(test_graph.addEdge('A', 'C', True))
        self.assertFalse(test_graph.addEdge('A', 'B'))
        del test_graph

    def test_add_edge_directed_weighted(self):
        test_graph = AdjacencyMatrix()
        test_graph.directed = True
        test_graph.weighted = True
        test_graph.addVertex('A')
        test_graph.addVertex('B')
        self.assertTrue(test_graph.addEdge('A', 'B', 1.0))
        self.assertFalse(test_graph.addEdge('A', 'B', 1.0))


if "__main__" == __name__:
    graph = AdjacencyMatrix()
    fileName = input("Input File Name: ")
    graph.readGraph(fileName)
    print(graph)
    toPrint = graph.printGraph()
    for item in toPrint:
        print(item.rstrip())