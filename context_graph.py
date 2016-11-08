import json

from nodes.cpu_node import CPUNode
from nodes.jitter_node import JitterNode
from nodes.disk_node import DiskNode


class ContextGraph(object):
  def __init__(self, services):
    self.services = services

  def get_initial_graph(self, container):

    root = {"data": {"id": "root", "name": container, "weight": 0}}

    nodes = [root]
    edges = []

    # initial edges go from root through all other nodes
    initial_nodes = [CPUNode, JitterNode, DiskNode] #, PacketlossNode, MemoryUsageNode, DiskUsageNode]

    for n in initial_nodes:
      node_id = n.label.lower().replace(' ', '_')
      nodes.append({"data" : {"id": node_id, "name": n.label}})
      edges.append({"data": {"source": root["data"]["id"], "target": node_id }})

    graph = {
      "nodes": nodes,
      "edges": edges
    }

    return graph
