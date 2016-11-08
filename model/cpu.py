class CPU(object):

  def __init__(self, cpu_util, timestamp):
    self.volume = cpu_util
    self.timestamp = timestamp
    self.label = self.assign_label()

  def assign_label(self):
    return ""

  @staticmethod
  def create_from_log(json_item):
    return CPU(json_item['volume'], json_item['recorded_at'])

