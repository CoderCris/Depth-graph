import networkx  as nx

from graph_utils import *
from solve       import *

graph = build_digraph_with_weights()
assert nx.is_directed_acyclic_graph(graph)   # Our input graphs must be ok

solution = dfs_topological_sort(graph)

print(dict(sorted(solution.items())))
