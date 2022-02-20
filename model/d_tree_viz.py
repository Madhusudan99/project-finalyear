# import graphviz
# with open("model/d_tree.dot") as f:
#     dot_graph = f.read()
# graphviz.Source(dot_graph)

import pydot

(graph,) = pydot.graph_from_dot_file('model/d_tree.dot')
graph.write_png('model/d_tree.png')