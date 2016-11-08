from node import Node
from model.endpoint import Endpoint

from elasticsearch import Elasticsearch
from extraction.elasticsearch.endpoint_elasticsearch import EndpointElasticsearch


class EndpointNode(Node):

  label = "API Endpoints"

  def __init__(self, service, timespan):
    super(EndpointNode, self).__init__(service, timespan)


  def load_entities(self):
    return EndpointElasticsearch(self.service, self.timespan).load_entities()

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