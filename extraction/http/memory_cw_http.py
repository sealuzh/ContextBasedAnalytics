from cw_http import CwHTTP
from model.memory import Memory

class MemoryCwHTTP(CwHTTP):

  def __init__(self, service, timespan):
    metric_name = 'mem_used'
    super(MemoryCwHTTP, self).__init__(service, metric_name, timespan)

  def load_entities(self):
    entities = super(MemoryCwHTTP, self).load_entities()
    memory_nodes = []
    for item in entities:
        node = Memory.create_from_log(item)
        if node is not None:
          memory_nodes.append(node)

    return memory_nodes

