# Base class for all nodes
class Node(object):

  def __init__(self, service, timespan):
    self.service = service
    self.timespan = timespan


  def load_entities(self):
    raise NotImplementedError()

  def infer_context(self):
    raise NotImplementedError()
