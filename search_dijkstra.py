def get_shortest_path(parent_dict, target_node):
    """ returns an array (list) of all nodes in correct order, given the shortest path parent has table and the requested target node"""
    start_node = "start"
    shortest_path = []                  # stores entries for shortest path
    shortest_path.append(target_node)   # target node first entry in list
    child = target_node                 # start with target_node as current child
    while parent_dict[child] != start_node:       # while parent of child is not start, process
        shortest_path.append(parent_dict[child])    # add parent to shortest path
        child = parent_dict[child]                   # set parent as new child
    shortest_path.append(start_node)    # start node last entry in list
    shortest_path.reverse()             # reverse order to provide correct order for shortest path
    return shortest_path


def find_lowest_cost_node(costs, processed):
    """ gets the node of the costs table with lowest costs"""
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:          # step through all entries in cost hash table
        cost = costs[node]
        if cost < lowest_cost and node not in processed:        # if new cost of current node is smaller and not yet processed update cost and node to remember
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_shortest_path(graph, costs, parents, target_node):
    processed = []                          # array (list())to keep track of all nodes already visited
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]                  # get costs of current node
        neighbours = graph[node]            # get has table for all links for current node
        for n in neighbours.keys():         # iterate all nieghbours
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs, get_shortest_path(parents, target_node)


if __name__ == "__main__":
    """ only execute, if programm call is from script, dont run if imported as module"""

    # hash table for all graph relation on which to calculate shortest weigthed path
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["c"] = 0     # test node
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["d"] = 2
    graph["b"]["fin"] = 5

    graph["c"] = {}         # test node
    graph["c"]["d"] = 2

    graph["d"] = {}         # test node

    graph["fin"] = {}

    # costs hash table for costs known initially
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["c"] = infinity
    costs["d"] = infinity
    costs["fin"] = infinity

    # parents hash table (dict()) to remember parent when discovered a new shortest path
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["c"] = None
    parents["d"] = None
    parents["fin"] = None

    print("These nodes are in the graph: ", ", ".join(graph.keys()))
    node_name = ""
    while node_name not in graph.keys():
        node_name = input("enter node for which to search shortest path from start: ")
    
    # call main def to calculate shortest dijkstra path of give graph
    result_costs, result_path = find_shortest_path(graph, costs, parents, node_name)
    print("shortest path: ", result_path)
    print("The shoretst path has %d of total costs." % costs[node_name])
