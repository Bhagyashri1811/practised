# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 08:24:29 2021

@author: Bhagyashri
"""
import collections

def bsf(graph,root):
    visited,queue=set(),collections.deque([root])
    visited.add(root)
    
    while queue:
        vertex=queue.popleft()
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    
graph={0:[1,2],1:[0,3,4],2:[0,5],3:[1,4],4:[1,3],5:[2]}
bsf(graph,2)