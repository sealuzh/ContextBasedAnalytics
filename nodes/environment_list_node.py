from node import Node
#from model.environment_list import EnvironmentList
from extraction.crawler.environment_crawler import EnvironmentCrawler

class EnvironmentListNode(Node):

  label = "Environment"

  def __init__(self, service, timespan):
    super(EnvironmentListNode, self).__init__(service, timespan)


  def load_entities(self):
    crawler = EnvironmentCrawler(self.service, self.timespan)
    return crawler.load_entities()

  def graph_nodes(self):
    items = self.load_entities()
    nodes = items.keys()

    return { 'expand_nodes' : nodes, 'data' : items }

  def infer_context(self):
    return []