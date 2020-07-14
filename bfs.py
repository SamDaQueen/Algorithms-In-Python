# bfs code reference taken from 'DFS and BFS Search in Python · Edd Mann'

# the given tree to be traversed
tree = {'0': ['1', '4'],
        '1': ['2', '3'],
        '4': ['5', '6'],
        '2': [],
        '3': [],
        '5': [],
        '6': []}


def bfs(tree, start):
    """Function to traverse the tree using breadth first search.
    It uses a open for implementation.

    Args:
        tree (dictionary): The tree with children as value of parent key
        start (String): the start node

    Returns:
        closed (list): path taken by algorithm
    """
    closed = []  # list for track expanded nodes
    open = []  # list to track explored nodes
    open.append(start)  # adding start node to be expanded
    while open:
        print("open:", open)
        current = open.pop(0)  # get first node to expand
        if current not in closed:  # check if node was previously visited
            closed.append(current)  # add node to closed
            # add unvisited nodes to open
            open.extend(set(tree[current]) - set(closed))
    return closed


def main():
    print("The path taken by BFS`` is: ", bfs(tree, '0'))


if __name__ == "__main__":
    main()
