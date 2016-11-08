class Memory(object):

  def __init__(self, memory_used, timestamp):
    self.volume = memory_used
    self.timestamp = timestamp
    self.label = self.assign_label()

  def assign_label(self):
    return ""

  @staticmethod
  def create_from_log(json_item):
    return Memory(json_item['volume'], json_item['recorded_at'])

