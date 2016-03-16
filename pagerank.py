# -*- coding: utf-8 -*-

# written by Soo. 16.03.16.
# weighted directed graph with Adjacency list
# But adjacencies of each node to others are implemented by array.
# combination of list and array

from utils import Node, cal_page_rank, compare_page_rank_array, round_graph, round_page_rank_array

graph = [
    Node([1], [1, 2]),
    Node([0, 2], [0]),
    Node([0], [1])
]

while True:
    previous_page_rank_array = []
    for node in graph:
        previous_page_rank_array.append(node.page_rank / float(len(graph)))
    print(previous_page_rank_array)

    cal_page_rank(graph)

    next_page_rank_array = []
    for node in graph:
        next_page_rank_array.append(node.page_rank / float(len(graph)))

    print('=====')
    if compare_page_rank_array(previous_page_rank_array, next_page_rank_array):
        break

print('=====result=====')
print(round_page_rank_array(next_page_rank_array))