import networkx as nx
import pydotplus
import os
from IPython.display import Image

# Create a new NetworkX graph object
G = nx.DiGraph()

# Add nodes to the graph
G.add_node("display")
G.add_node("entry")
G.add_node("buttons")
G.add_node("lambda")
G.add_node("Button")
G.add_node("try")
G.add_node("eval")
G.add_node("except")
G.add_node("Error")

# Add edges to the graph
G.add_edge("entry", "display")
G.add_edge("lambda", "button_click")
G.add_edge("Button", "command")
G.add_edge("display", "try")
G.add_edge("buttons", "Button")
G.add_edge("try", "eval")
G.add_edge("eval", "except")
G.add_edge("except", "display")
G.add_edge("Error", "display")

# Generate block diagram using Graphviz
graph = pydotplus.graph_from_dot_data(nx.drawing.nx_pydot.to_pydot(G).to_string())
graph.write_png('block_diagram.png')

# Show the block diagram
Image(filename='block_diagram.png')
