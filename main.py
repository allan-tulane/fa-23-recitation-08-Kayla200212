from collections import deque 
#dont feel confident using deque+isnt required in the instructions
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    frontier = [(0,0,source)]#init the frontier using heappush.
    #0 nodes, 0 edges, starting at source and adding this to the top of the frontier
    visited = {} #for storing the final visited nodes path in dict

    while len(frontier) != 0:#while frontier isnt empty
      weight, edges, node = heappop(frontier)
      #heapop will take from the frontier the smallest elements n assign in order
      if node not in visited: #if the node we pulled isnt already visited
        visited[node] = (weight,edges)#add to visited index of the node weight n edge
        for neighbor, weight_neighbor in graph[node]:#adds neighbor nodes to frontier
          heappush(frontier, (weight+weight_neighbor,edges+1,neighbor))
          #push to frontier: 
    return visited
  
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parent={source:None}#make a dictionary for the parents but init node has no parents
    frontier = [(0,0,source)]#init the frontier using heappush.
    visited = set()#not sure what storage type this needs to be but add works like this
  #for each visit made to a frontier value, remove the left node and add it to visited
  
    while len(frontier) != 0:
      node = frontier.popleft()#remove leftmost part of queue
      visited.add(node)#and add that to visited
      for neighbor in graph[node]:
        if neighbor not in visited and neighbor not in frontier:
          parent[neighbor] = node
          frontier.append(neighbor)
    return parent

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    if destination in parents:#is destination node a parent node
      return get_path(parents, parents[destination])+parents[destination]
    #then recursively call to get the parents of the destination
    else:
      return ''#else return empty since ur already there/stop looking