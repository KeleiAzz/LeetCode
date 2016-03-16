class UndirectedGraphNode(object):
    def __init__(self, label):
        self.label = label
        self.neighbors = []

def cloneGraph(node):
    '''
    DFS with a stack
    :param node:
    :return:
    '''
    if not node:
        return None
    cloned = {}
    stack = [node]
    while stack:
        to_clone = stack.pop()
        if to_clone.label not in cloned:
            cloned[to_clone.label] = UndirectedGraphNode(to_clone.label)
        for neighbor in to_clone.neighbors:
            if neighbor.label not in cloned:
                cloned[neighbor.label] = UndirectedGraphNode(neighbor.label)
                stack.append(cloned[neighbor.label])
            cloned[to_clone.label].neighbors.append(cloned[neighbor.label])

    return cloned[node.label]

def cloneGraph2(self, node):
    """
    BFS using a for loop
    :type node: UndirectedGraphNode
    :rtype: UndirectedGraphNode
    """
    if not node:
        return None
    cloned = {}
    queue = [node]
    for original_node in queue:
        if original_node.label not in cloned:
            cloned[original_node.label] = UndirectedGraphNode(original_node.label)
        for neighbor in original_node.neighbors:
            if neighbor.label not in cloned:
                cloned[neighbor.label] = UndirectedGraphNode(neighbor.label)
                queue.append(neighbor)
            cloned[original_node.label].neighbors.append(cloned[neighbor.label])
    return cloned[node.label]