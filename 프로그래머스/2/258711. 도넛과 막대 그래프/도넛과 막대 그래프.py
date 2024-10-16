def solution(edges):
    answer = [0, 0, 0, 0]
    
    graphs_out = {}
    graphs_in = {}
    
    maximum_node = 0
    
    for edge in edges:
        current, to = edge[0], edge[1]
        
        maximum_node = max(maximum_node, current, to)
        if current in graphs_out:
            graphs_out[current].append(to)
        else:
            graphs_out[current] = [to]
            
        
        if to in graphs_in:
            graphs_in[to].append(current)
        else:
            graphs_in[to] = [current]
            
    graphs_out_keys = graphs_out.keys()
    

    for node in range(1, maximum_node+1):
        if node in graphs_out and len(graphs_out[node]) >= 2 and not node in graphs_in:
            answer[0] = node
            continue
        
        if node in graphs_in and not node in graphs_out:
            answer[2] += 1
            
    for node in graphs_out_keys:      
        if len(graphs_out[node]) >= 2 and node in graphs_in and len(graphs_in[node]) >= 2:
            answer[3] += 1
            continue

    answer[1] = len(graphs_out[answer[0]]) - answer[3]- answer[2]

    return answer