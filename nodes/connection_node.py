from node import Node
from model.connection import Connection
from extraction.elasticsearch.connection_elasticsearch import ConnectionElasticsearch


class ConnectionNode(Node):

  label = "Connection"

  def __init__(self, service, timespan):
    super(ConnectionNode, self).__init__(service, timespan)


  def load_entities(self):
    return ConnectionElasticsearch(self.service, self.timespan).load_entities()

  def graph_nodes(self):
    connections = self.load_entities()
    items = {}

    for connection in connections:
      if not items.has_key(connection.label):
        items[connection.label] = []

      items[connection.label].append(connection.__dict__)

    return { 'expand_nodes' : [], 'data' : items }


  def infer_context(self):
    return []