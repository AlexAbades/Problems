# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:05:37 2022

@author: G531
"""

# create undirected graph with dictionary 
import numpy as np 
from itertools import product 


class Undirected_Graph_Matrix():
    
    
    def __init__(self, n_nodes:int):
        
        self.n_nodes = n_nodes
        self.matrix = np.zeros((n_nodes,n_nodes))
    
    def conected_nodes(self, v, u):
        
        self.matrix[v,u] = 1
        self.matrix[u,v] = 1
        
        
    def display(self):
        
        print(self.matrix)




A = Undirected_Graph_Matrix(10)
A.conected_nodes(0,1)
A.conected_nodes(0,5)
A.conected_nodes(1,6)
A.conected_nodes(1,2)
A.conected_nodes(2,7)
A.conected_nodes(2,3)
A.conected_nodes(3,8)
A.conected_nodes(3,4)
A.conected_nodes(4,9)
A.conected_nodes(4,0)
A.conected_nodes(5,7)
A.conected_nodes(5,8)
A.conected_nodes(7,9)
A.conected_nodes(8,6)
A.conected_nodes(9,6)




class UndirectedGraph_dic():
    
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes 
        self.graph = dict().fromkeys(range(n_nodes))
        self.paths = None
        self.num_paths = None
        
    def node_connections(self, node:int, connection:list):
        """
        Function to create the dicctionary specifying the node ans it's
        connected neighbours

        Parameters
        ----------
        node : int
            The node you are taking in account
        connection : list
            The node connections.

        Returns
        -------
        None.

        """
        self.graph[node] = connection
    
    
    def graph_paths(self):
        """
        Given a dictionray structure of a graph it calculates the connections 
        with other neighbours. It has to be already filled with the conections.
        
        Returns
        ------- 
        List of sets with the connections. 
        
        """
        # Initialize list 
        paths = []
        # Iterate through every node in 
        for key, item in self.graph.items():
            a = [set(i) for i in product([key], item) if set(i) not in paths]
            paths += a
        
        self.paths = paths
        self.num_paths = len(self.paths)
        
        
        
    def DFS(self, v):
        time = 0 
        visited = set()
        initial_time = []
        final_time = []
        print(self.dfs_visit(v, visited, time, initial_time, final_time))
    
    def dfs_visit(self, u:int, visited:set, time, initial_time, final_time):
        """
        
        Parameters
        ----------
        u : int
            Node we want to start from.
        visited : set
            List of nodes we'e seen.

        Returns
        -------
        None.

        """
        time += 1 
        # Mark the node 
        visited.add(u)
        initial_time.append(time)
        print(u, end = ' ')
        
        # Iterate through the nodes neighbour of that node, if they are not in 
        # the visited list, call recursively the function ¡
        for neighbour in self.graph[u]:
            if neighbour not in visited:
                self.dfs_visit(neighbour, visited, time, initial_time, final_time)
        
        
        time += 1
        final_time.append(time)
        return(initial_time, final_time)
        
    
    def iscycle(self):
        """
        Returns True if the graph has a cycle.
        
        """
        
        # Create a list with all the nodes we've visited, initialize to False 
        # We haven't visited anyone.
        
        visited = [False]*self.n_nodes
                
        # Iterate through all the nodes [0-9]
        for node in B.graph.keys():
            # If that node is already visited don't reccur on it
            if visited[node] == False:
                if self.iscycle_unitl(node, visited, -1):
                    return True 
           
      
    def iscycle_unitl(self, v, visited, parent):     
        """
        v-> Node were we currently are
        visited -> Bolean list of nodes we've visited
        parent-> parent node of the node we are gonna visit 
        """
        # Mark the current node as visited
        visited[v]= True
        
        # Check all the connections from that node
        for i in self.graph[v]:
        # If the node is not visited, check the node.
        
            if  visited[i]==False:
                # Chek 
                if(self.iscycle_unitl(i,visited, v)):
                    return True
                # If an adjacent vertex is visited and is not the parent from 
                # that node, then we have a cycle, 
                elif  parent != i:
                    return True
        # If we haven't found any visited node that's not the parent, then we 
        # have a cycle
        return False
    
    
    def breadth_first_search(self, s):
        """
        s-> node were we start the algorithm. (source node)
        
        """
        
        # Create an array of visited nodes 
        visited  = [False]*self.n_nodes
        
        # Create a Queue for the BFS
        queue = []
        
        # Mark the current source node as visited 
        visited[s] = True
        # Add the source node to the queue 
        queue.append(s)
        
        while queue:
            # Dequeue the vertex from the queue (first element)
            s = queue.pop(0)
            
            print(s, end= ' ')
            
            # Get all the neighbours from the node:
            for neighbour in self.graph[s]:
                # If the adjacent node has not been visited, visit the node and
                # add it to the queue 
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    queue.append(neighbour)

    def bfs_shortest_path(self, src, dist, paths):
        """
        adj
        src -> The soirce node we'll start from
        """
        # Create an array of False times number of nodes to track the nodes
        # we've visited 
        visited = [False]*self.n_nodes
        
        # By definition, as we are in the source node the distance is 0 and 
        # we only have 1 path
        dist[src] = 0
        paths[src] = 1
                
        # Create a queue (FIFO) and store the source 
        Q = []
        Q.append(src)
        
        # Mark the node as visited
        visited[src] = True
        
        # Loop until we've visited all nodes, same until we don't have elements 
        # in the queue 
        while Q:
            # Store the first value of the queue
            curr = Q[0]
            # Pop out the first element of the queue
            Q.pop(0)
            
            # loop over the neighbours 
            for child in self.graph[curr]:
                
                # if we haven't visited that node
                if not visited[child]:
                    # Append to the que and mark as visited 
                    Q.append(child)
                    visited[child] = True 
                    
                # means there is a path that goes from the source node to the 
                # child node with a smaller length than the previous path we have
                # Checking if there's a better path
                if dist[child] > dist[curr]+1:
                    dist[child] = dist[curr]+1
                    paths[child] = paths[curr]
                
                # means all the shortest paths that go from the source node to
                # the current node will be added to the number of shortest 
                # paths of the child node.
                # Additionally path found                
                if dist[child] == dist[curr]:
                    paths[child] +=  paths[curr]
                    
    def shortest_path(self, src):
        """
        Time Complexity: O(V + E):
        where V is the number of nodes and E is the number of edges. 
        The reason behind this complexity is that we iterate over each node 
        only once. Therefore, we iterate over its children once. In total, we 
        iterate over each edge once as well.
        """
        # Initialize the distant and paths lists with infinite values for the 
        # distances and 0 vaues for the paths
        
        dist = [float('inf')]*self.n_nodes
        paths = [0] * self.n_nodes
        
        # Call the function 
        self. bfs_shortest_path(src, dist, paths)
        print('Number of paths are: ', end = ' ')
        for pat in paths:
            print(pat, end =' ')
        
                    
                    
    def display(self):
        for key, value in self.graph.items():
            print(key, ':', value)
            
    



B = UndirectedGraph_dic(10)

B.node_connections(0, [1, 4, 5])
B.node_connections(1, [0, 2, 6])
B.node_connections(2, [1, 3, 7])
B.node_connections(3, [2, 4, 8])
B.node_connections(4, [0, 3, 9])
B.node_connections(5, [0, 7, 8])
B.node_connections(6, [1, 8, 9])
B.node_connections(7, [2, 5, 9])
B.node_connections(8, [3, 5, 6])
B.node_connections(9, [4, 6, 7])
B.graph_paths()



#%%

def addEdge(adj: list, u: int, v: int):
    adj[u].append(v)
 
# Driver Code
if __name__ == "__main__":
 
    n = 7 # Number of vertices
    adj = [0] * n
    for i in range(n):
        adj[i] = []
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 2)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 3, 5)
    addEdge(adj, 4, 6)
    addEdge(adj, 5, 6)
    