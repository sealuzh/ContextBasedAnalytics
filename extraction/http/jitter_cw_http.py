from cw_http import CwHTTP
from model.jitter import Jitter

class JitterCwHTTP(CwHTTP):

  def __init__(self, service, timespan):
    metric_name = 'host.max_jitter'
    super(JitterCwHTTP, self).__init__(service, metric_name, timespan)

  def load_entities(self):
    entities = super(JitterCwHTTP, self).load_entities()
    jitter_nodes = []
    for item in entities:
        node = Jitter.create_from_log(item)
        if node is not None:
          jitter_nodes.append(node)

    return jitter_nodes

