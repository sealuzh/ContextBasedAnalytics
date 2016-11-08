from node import Node
from model.jitter import Jitter
from extraction.http.jitter_cw_http import JitterCwHTTP


class JitterNode(Node):

  label = "Jitter"

  def __init__(self, service, timespan):
    super(JitterNode, self).__init__(service, timespan)


  def load_entities(self):
    return JitterCwHTTP(self.service, self.timespan).load_entities()

  def graph_nodes(self):
    jitter_nodes = self.load_entities()
    items = {}

    for jitter in jitter_nodes:
      if not items.has_key(jitter.label):
        items[jitter.label] = []

      items[jitter.label].append(jitter.__dict__)

    return { 'expand_nodes' : [{"data" : {"id": 'memory', "name": 'Memory used'}}], 'data' : items }


  def infer_context(self):
    return []