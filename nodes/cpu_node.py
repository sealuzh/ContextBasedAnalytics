from node import Node
from model.cpu import CPU
from extraction.http.cpu_cw_http import CpuCwHTTP


class CPUNode(Node):

  label = "CPU"

  def __init__(self, service, timespan):
    super(CPUNode, self).__init__(service, timespan)


  def load_entities(self):
    return CpuCwHTTP(self.service, self.timespan).load_entities()

  def graph_nodes(self):
    cpu_nodes = self.load_entities()
    items = {}

    for cpu in cpu_nodes:
      if not items.has_key(cpu.label):
        items[cpu.label] = []

      items[cpu.label].append(cpu.__dict__)

    return { 'expand_nodes' : [{"data" : {"id": 'code_fragment:validate', "name": 'func validate() (Go)'}}], 'data' : items }


  def infer_context(self):
    return []