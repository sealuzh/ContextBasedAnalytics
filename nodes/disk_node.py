from node import Node
from model.disk import Disk
from extraction.http.disk_cw_http import DiskCwHTTP


class DiskNode(Node):

  label = "Disk"

  def __init__(self, service, timespan):
    super(DiskNode, self).__init__(service, timespan)


  def load_entities(self):
    return DiskCwHTTP(self.service, self.timespan).load_entities()

  def graph_nodes(self):
    disk_nodes = self.load_entities()
    items = {}

    for disk in disk_nodes:
      if not items.has_key(disk.label):
        items[disk.label] = []

      items[disk.label].append(disk.__dict__)

    return { 'expand_nodes' : [], 'data' : items }


  def infer_context(self):
    return []