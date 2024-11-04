import sys
sys.setrecursionlimit(10**6)

def find_root(nodes):
    return max(nodes, key=lambda x:x[2])

def divide_nodes(nodes, y):
    for i, node in enumerate(nodes):
        if y == node[2]:
            return nodes[:i], nodes[i + 1:]

def solution(nodeinfo):
    nodes = [(i + 1, x, y) for i, (x, y) in enumerate(nodeinfo)]
    pre_list, post_list = [], []
    
    def make_tree(nodes):
        if not nodes: return
        i, x, y = find_root(nodes)
        pre_list.append(i)
        x_nodes = sorted(nodes, key=lambda x:x[1])
        left_nodes, right_nodes = divide_nodes(x_nodes, y)
        make_tree(left_nodes)
        make_tree(right_nodes)
        post_list.append(i)
    
    make_tree(nodes)
    
    answer = [pre_list, post_list]
    return answer