class Jitter(object):

  def __init__(self, jitter, timestamp):
    self.volume = jitter
    self.timestamp = timestamp
    self.label = self.assign_label()

  def assign_label(self):
    return ""

  @staticmethod
  def create_from_log(json_item):
    return Jitter(json_item['volume'], json_item['recorded_at'])

