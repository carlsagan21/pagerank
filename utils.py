# -*- coding: utf-8 -*-

# written by Soo. 16.03.16.


class Node:
    def __init__(self, forward_index_array, back_index_array):
        self.page_rank = float(1)
        self.forward_index_array = forward_index_array
        self.back_index_array = back_index_array


def sum_of_array(array):
    total = 0
    for elem in array:
        total += elem
    return total


def num_of_forward(node):
    return len(node.forward_index_array)


def edge_weight(node):
    weight = node.page_rank / float(num_of_forward(node))
    return weight


def cal_page_rank(graph):
    new_node_page_rank = []

    for node in graph:
        back_array = map(lambda x: graph[x], node.back_index_array)
        edge_weight_array = map(edge_weight, back_array)
        new_node_page_rank.append(sum_of_array(edge_weight_array))

    i = 0
    for node in graph:
        node.page_rank = new_node_page_rank[i]
        i += 1

    return


def compare_page_rank_array(prev, next):
    flag = True
    i = 0
    for prev_rank in prev:
        # if abs(prev_rank - next[i]) != 0:
        if abs(prev_rank - next[i]) > 0.001:
            flag = False
            break
        i += 1

    return flag


def round_graph(graph):
    rank_array = []
    for node in graph:
        rank_array.append(round(node.page_rank, 2))

    return rank_array


def round_page_rank_array(array):
    rank_array = []
    for rank in array:
        rank_array.append(round(rank, 2))

    return rank_array