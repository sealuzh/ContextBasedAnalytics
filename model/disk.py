class Disk(object):

  def __init__(self, display_name, disk_usage):
    self.key = display_name
    self.value = disk_usage
    self.timestamp = None
    self.label = self.assign_label()

  def assign_label(self):
    return self.key

  @staticmethod
  def create_from_log(json_item):
    return Disk(json_item['display_name'], json_item['volume'])

