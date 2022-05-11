# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:03:01 2022

@author: G531
"""

from itertools import product

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