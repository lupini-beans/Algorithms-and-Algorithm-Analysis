class DictGraph(object):
    def __init__(self, directional=False, weight=False):
        self.graph = {}
        self.directional = directional
        self.weight = weight

    '''
    Formats the graph to print in the following format:
    unweighted:
        vertex: [edge]
    unweighted:
        vertex: [[edge, weight]]
    '''
    def __str__(self):
        temp = []
        string = ""
        for key in self.graph:
            temp.append(key)
            temp.append(self.graph[key])
        for item in temp:
            if not(type(item) == type([])):
                string += '\n' + str(item) + " : "
            else:
                string += str(item) + "  "
        return string

    def hasEdge(self, vertex1, vertex2):
        found_edge = False
        if vertex1 in list(self.graph.keys()):
            if self.graph[vertex1]:
                if self.weight:
                    for edge in self.graph[vertex1]:
                        if edge[0] == vertex2:
                            vertex2 = edge
                if vertex1 in self.graph and vertex2[0] in self.graph:
                    if vertex2 in self.graph[vertex1]:
                        found_edge = True
                    else:
                        found_edge = False
        return found_edge

    def addEdge(self, vertex1, vertex2):
        edge_added = False
        print("_" * 41)
        if vertex1 in self.graph and vertex2[0] in self.graph:
            if self.hasEdge(vertex1, vertex2):
                print(f"Failed: {vertex1} --> {vertex2} already exists")
            else:
                if self.directional:
                    print(f"Adding Edge {vertex1} --> {vertex2}...")
                    self.graph[vertex1].append(vertex2)
                    print(f"Success: {vertex1} --> {vertex2} added")
                    edge_added = True
                elif not self.directional and not self.weight:
                    print(f"Adding Edge {vertex1} <--> {vertex2}...")
                    self.graph[vertex1].append(vertex2)
                    self.graph[vertex2].append(vertex1)
                    print(f"Success: {vertex1} <--> {vertex2} added")
                    edge_added = True
                elif (not self.directional) and self.weight:
                    print(f"Adding Edge {vertex1} <--> {vertex2[0]} with weight {vertex2[1]}...")
                    self.graph[vertex1].append(vertex2)
                    self.graph[vertex2[0]].append([vertex1, vertex2[1]])
                    print(f"Success: {vertex1} <--> {vertex2} added")
                    edge_added = True
                else:
                    edge_added = False
        else:
            edge_added = False
        print("_" * 41, "\n")
        return edge_added

    def deleteEdge(self, vertex1, vertex2):
        edgeDeleted = False
        print('=' * 41)
        if self.weight:
            for vertices in self.graph[vertex1]:
                if vertices[0] == vertex2:
                    vertex2 = vertices
        if vertex1 in self.graph:
            if self.hasEdge(vertex1, vertex2):
                if self.directional:
                    print(f"Removing Edge {vertex1} --> {vertex2}...")
                    self.graph[vertex1].remove(vertex2)
                    print(f"Success: {vertex1} --> {vertex2} removed")
                    edgeDeleted = True
                elif not (self.directional) and not (self.weight):
                    print(f"Removing Edge {vertex1} <--> {vertex2}...")
                    self.graph[vertex1].remove(vertex2)
                    self.graph[vertex2].remove(vertex1)
                    print(f"Success: {vertex1} <--> {vertex2} removed")
                    edgeDeleted = True
                elif not (self.directional) and self.weight:
                    print(f"Removing Edge {vertex1} <--> {vertex2}...")
                    self.graph[vertex1].remove(vertex2)
                    self.graph[vertex2[0]].remove([vertex1, vertex2[1]])
                    print(f"Success: {vertex1} <--> {vertex2} removed")
                    edgeDeleted = True
                else:
                    print(f"Failed")
                    edgeDeleted = False
            else:
                print(f"Failed: Edge from {vertex1} --> {vertex2} does not exist")
                edgeDeleted = False
        print('=' * 41)
        return edgeDeleted

    def addVertex(self, vertex):
        vertexAdded = False
        for item in vertex:
            print("_" * 41)
            print(f"Adding Vertex {item}...")
            if item in self.graph:
                print(f"Failed: Vertex {item} already exists")
                vertexAdded = False
            else:
                self.graph[item] = []
                print(f"Success: {item} added")
                print("_" * 41, "\n")
                vertexAdded = True
        return vertexAdded

    def deleteVertex(self, vertex):
        vertexDeleted = False
        print("_" * 41)
        print(f"Removing Vertex {vertex}...")
        if vertex in self.graph:
            for item in self.graph:
                if self.hasEdge(item, vertex):
                    self.deleteEdge(item, vertex)
            del self.graph[vertex]
            print(f"Success: {vertex} deleted")
            vertexDeleted = True
        else:
            print(f"Failed: Vertex {vertex} does not exist")
            vertexDeleted = False
        print("_" * 41, "\n")
        return vertexDeleted

    def isSparse(self):
        print("_" * 41)
        print("Checking if Sparse: ")
        numEdges = self.countEdges()
        numVertex =  self.countVertices()
        if self.directional:
            percent = numEdges/numVertex * 2 * 100
        else:
            percent = (numEdges/(3**(numVertex-2) + numVertex)) * 100
        if percent > 15:
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
        if self.directional:
            percent = numEdges/numVertex * 2 * 100
        else:
            percent = (numEdges/(3**(numVertex-2) + numVertex)) * 100
        if percent > 84:
            isDense = False
        else:
            isDense = True
        print(isDense)
        print("_" * 41, "\n")
        return isDense

    def countVertices(self):
        return len(list(self.graph.keys()))

    def countEdges(self):
        edgeLength = 0
        for item in self.graph:
            edgeLength = edgeLength + len(self.graph[item])
        if not graph.directional:
            edgeLength = int(edgeLength/2)
        return edgeLength

# Addition Method_______________________________________________________________________________________________________
    def __find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not self.weight:
            for vertex in self.graph[start]:
                if vertex not in path:
                    newpath = self.__find_path(vertex, end, path)
                    if newpath:
                        return newpath
        else:
            for vertex in self.graph[start]:
                if vertex[0] not in path:
                    newpath = self.__find_path(vertex[0], end, path)
                    if newpath:
                        return newpath

#_______________________________________________________________________________________________________________________

    def isConnected(self):
        print("=" * 41)
        print("Checking if connected: ")
        is_connected = True
        for vertex in list(self.graph.keys()):
            start = vertex
            for row in self.graph:
                if self.graph[row] == []:
                    is_connected = False
                    break
            if is_connected:
                for row in self.graph:
                    if not (self.__find_path(start, row, path=[]) == None):
                        continue
                    else:
                        is_connected = False
        print(is_connected)
        print("=" * 41)
        return is_connected

    def isFullyConnected(self):
        print("_" * 41)
        print("Checking if fully connected: ")
        isFullyConnected = True
        vertices = list(self.graph.keys())
        if not self.isConnected():
            isFullyConnected = False
        if isFullyConnected:
            for vertex1 in self.graph:
                for vertex2 in vertices:
                    if not self.hasEdge(vertex1, vertex2) and vertex1 != vertex2:
                        print(f"{vertex1} is not connected to {vertex2}")
                        isFullyConnected = False
                        break
                if not isFullyConnected:
                    break
        print(isFullyConnected)
        print("_" * 41, "\n")
        return isFullyConnected

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
                        self.weight = True
                    elif line == 'unweighted':
                        inputParams['Weighted'] = False
                        self.weight = False
                    else:
                        raise RuntimeError("No weight found")
                elif (index == weightIndex+1) and (not directional):
                    if line == 'directed' or line == 'undirected':
                        directional = True
                        directionalIndex = index
                    if line == 'directed':
                        inputParams['Directional'] = True
                        self.directional = True
                    elif line == 'undirected':
                        inputParams['Directional'] = False
                        self.directional = False
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
                elif index == graphEndIndex+1 or (index == resultIndex+1 and results > 0):
                    struct = line.split()
                    inputParams['Instructions'].append(struct)
                    instructionIndex = index
                    instructions += 1
                elif index == instructionIndex+1 and instructions > 0:
                    inputParams['Results'].append(line.capitalize())
                    resultIndex = index
                    results += 1
        print(f"_________________________________________\nInput Parameters from {fileName}:")
        for item in inputParams:
            print(f"{item}: {inputParams[item]}")
        print("_" * 41, "\n")
        self.__write_graph(inputParams)
        return inputParams

# Additional Method_____________________________________________________________________________________________________
    def __writeGraph(self, inputParams):
        results = []
        true_result = []
        found_struct = []
        self.addVertex(inputParams['Vertices'])
        for edge in inputParams['Edges']:
            if self.weight:
                vertex1 = edge[0]
                vertex2 = [edge[1], edge[2]]
                self.addEdge(vertex1, vertex2)
            else:
                vertex1 = edge[0]
                vertex2 = edge[1]
                self.addEdge(vertex1, vertex2)
        if inputParams['Instructions']:
            print("\n______Executing Instructions______\n")
        for index, command in enumerate(inputParams['Instructions']):
            found_struct.append(command)
            if command[0] == "hasEdge":
                print("_" * 41)
                print(f"Checking for edge {command[1]} --> {command[2]}:")
                foundEdge = self.hasEdge(command[1], command[2])
                results.append(str(foundEdge))
                print(foundEdge)
                print("_" * 41, "\n")
            elif command[0] == "addEdge":
                if self.weight:
                    vertex1 = command[1]
                    vertex2 = [command[2], command[3]]
                    results.append(str(self.addEdge(vertex1, vertex2)))
                else:
                    vertex1 = command[1]
                    vertex2 = command[2]
                    results.append(str(self.addEdge(vertex1, vertex2)))
            elif command[0] == "deleteEdge":
                vertex1 = command[1]
                vertex2 = command[2]
                results.append(str(self.deleteEdge(vertex1, vertex2)))
            elif command[0] == "addVertex":
                results.append(str(self.addVertex([command[1]])))
            elif command[0] == "deleteVertex":
                results.append(str(self.deleteVertex(command[1])))
            elif command[0] == "isSparse":
                results.append(str(self.isSparse()))
            elif command[0] == "isDense":
                results.append(str(self.isDense()))
            elif command[0] == "countVertices":
                results.append(str(self.countVertices()))
            elif command[0] == "countEdges":
                results.append(str(self.countEdges()))
            elif command[0] == "isConnected":
                results.append(str(self.isConnected()))
            elif command[0] == "isFullyConnected":
               results.append(str(self.isFullyConnected()))
            else:
                raise RuntimeError("Command not found")
        print("\n______Comparing Results______\n")
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
#_______________________________________________________________________________________________________________________

    def printGraph(self):
        toPrint = []
        vertices = ""
        edges = ""
        edgePairs = []
        toPrint.append("* Interpreted Graph:")
        if self.weight:
            toPrint.append("weighted")
        else:
            toPrint.append("unweighted")
        if self.directional:
            toPrint.append("directed")
        else:
            toPrint.append("undirected")
        toPrint.append("begin")
        for item in self.graph:
            vertices += str(item) + " "
        toPrint.append(vertices)
        for vertex1 in vertices:
            for vertex2 in vertices:
                if self.hasEdge(vertex1, vertex2):
                    if not self.directional:
                        if not (vertex2, vertex1) in edgePairs:
                            edgePairs.append((vertex1, vertex2))
                            if self.weight:
                                for edge in self.graph[vertex1]:
                                    if edge[0] == vertex2:
                                        edges += str(vertex1) + " " + str(edge[0]) + " " + str(edge[1]) + "\n"
                            else:
                                edges += (vertex1 + " " + vertex2) + "\n"
                    else:
                        edges += (vertex1 + " " + vertex2) + "\n"
        toPrint.append(edges.rstrip())
        toPrint.append("end")
        return toPrint

if "__main__" == __name__:
    graph = DictGraph()
    fileName = input("Input File Name: ")
    graph.readGraph(fileName)
    print("_____Current Graph_____")
    print(graph, "\n")
    toPrint = graph.printGraph()
    for item in toPrint:
        print(item.rstrip())