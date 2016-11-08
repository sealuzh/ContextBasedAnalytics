from node import Node
from model.memory import Memory
from extraction.http.memory_cw_http import MemoryCwHTTP
from extraction.http.jitter_cw_http import JitterCwHTTP


class MemoryNode(Node):

  label = "Memory"

  def __init__(self, service, timespan):
    super(MemoryNode, self).__init__(service, timespan)


  def load_entities(self):
    return MemoryCwHTTP(self.service, self.timespan).load_entities()

  def graph_nodes(self):
    memory_nodes = self.load_entities()
    items = {}

    for memory in memory_nodes:
      if not items.has_key(memory.label):
        items[memory.label] = []

      items[memory.label].append(memory.__dict__)

    return { 'expand_nodes' : [], 'data' : items }


  def infer_context(self):
    return []