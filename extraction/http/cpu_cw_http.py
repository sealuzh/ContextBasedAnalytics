from cw_http import CwHTTP
from model.cpu import CPU

class CpuCwHTTP(CwHTTP):

  def __init__(self, service, timespan):
    metric_name = 'cpu_util'
    super(CpuCwHTTP, self).__init__(service, metric_name, timespan)

  def load_entities(self):
    entities = super(CpuCwHTTP, self).load_entities()
    cpu_nodes = []
    for item in entities:
        node = CPU.create_from_log(item)
        if node is not None:
          cpu_nodes.append(node)

    return cpu_nodes

