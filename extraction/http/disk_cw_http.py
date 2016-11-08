from cw_http import CwHTTP
from model.disk import Disk

class DiskCwHTTP(CwHTTP):

  def __init__(self, service, timespan):
    metric_name = 'cpu_util'
    super(DiskCwHTTP, self).__init__(service, metric_name, timespan)

  def load_entities(self):
    entities = super(DiskCwHTTP, self).load_entities()
    disk_map = {}

    for item in entities:
      key = item['metadata']['display_name']
      if key in disk_map:
        disk_map[key].append(item['volume'])
      else:
        disk_map[key] = [item['volume']]

    disk = []
    for display_name in disk_map:
      disk.append(Disk.create_from_log({'display_name': display_name, 'volume': ",".join(map(str, disk_map[display_name]))}))

    return disk

