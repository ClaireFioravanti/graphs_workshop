import json

def bfs(network, source):
    '''
    Purpose: Perform a breadth-first search on network starting
    from the source.

    Parameters: 
        network - a graph adjacency list; dict
        source - the node in the network from which to start
        the BFS.

    Return Values: 
        distance - the distance from the source to any other node; dict
        predecessor - the predecessor for each note resulting from 
        a BFS run; dict
    '''    
    # Dictionaries to track which nodes have been visited,
    # the distance from the source, and the predecessors

    visited = {}
    distance = {}
    predecessor = {}

    # Setup: For each node
    # visited is set to False
    # distance is set to infinity
    # there are no predecessors at this point

    for node in network:
        visited[node] = False
        distance[node] = float("inf")
        predecessor[node] = None
    
    # We now do the setup for the source
    visited[source] = True
    distance[source] = 0
    queue = [source]

    # While the queue has something on it, we will update the
    # information and explore the neighbors of the current node

    while queue != []:
        front = queue.pop(0)

        for neighbor in network[front]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[front] + 1
                predecessor[neighbor] = front
                queue.append(neighbor)
    
    return distance, predecessor

with open("social_network.json", "r") as file:
    graph = json.load(file)

def node_query(network, source, dist):
    '''
    Purpose: To return a list containing all nodes in the network
    that are dist distance from the source.
 
    Parameters:
        network - graph adjacency list; dict
        source - the node to start the BFS run
        dist - the desired distance of the nodes to be found.
 
    Return Value: A list of nodes at distance dist from the source; list
    '''
    distances, _ = bfs(network, source)

    distanced_nodes = []

    for node in distances:  
        
        if distances[node] == dist:

            distanced_nodes.append(node)

    return distanced_nodes