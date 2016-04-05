def bfs(root):
    if not root:
        return
    queue = [(root, 0)]
    res = []
    while root:
        node, level = queue.pop(0)
        if not res or res[-1][1] < level:
            res = [node]
        else:
            res.append(node)
        for child in node.children:
            if child:
                queue.append((child, level + 1))

    return res[0], res[-1] # what if there is only one node in the deepest level?


getFirstTarget, tmpLCA, LCA, shallowest = False, None, None, 0


def treeLCA(root, p, q, curLev):
    global getFirstTarget, tmpLCA, LCA, shallowest
    if root == p or root == q:
        if not getFirstTarget:
            getFirstTarget = True
            shallowest = curLev
            tmpLCA = root
        LCA = tmpLCA

    if getFirstTarget and curLev <= shallowest:
        shallowest = curLev
        tmpLCA = root

    for child in root.children:
        treeLCA(child, p, q, curLev + 1)
        if getFirstTarget and curLev <= shallowest:
            shallowest = curLev
            tmpLCA = root

deepest = 0
def treeLCA2(root, curLev):
    global getFirstTarget, tmpLCA, LCA, shallowest, deepest
    if not root.children:
        if not getFirstTarget:
            getFirstTarget = True
            shallowest = curLev
            deepest = curLev
            tmpLCA = root

        if curLev == deepest:
            LCA = tmpLCA

        if curLev > deepest:
            # getFirstTarget = False
            deepest = curLev
            shallowest = deepest
            tmpLCA = root
            LCA = tmpLCA

    if getFirstTarget and curLev <= shallowest:
        shallowest = curLev
        tmpLCA = root

    for child in root.children:
        treeLCA2(child, curLev + 1)
        if getFirstTarget and curLev <= shallowest:
            shallowest = curLev
            tmpLCA = root

