import urllib2, json, os
import datetime

class CwHTTP(object):
  def __init__(self, service, metric_name, timestamp):
    self.host = os.environ['CW_HOST']
    self.metric_name = metric_name
    self.timestamp = timestamp
    self.url = "http://{host}/full/{metric_name}"
    self.features = ""

  def load_entities(self):
    entity_url = self.url
    entity_url = entity_url.replace('{host}', self.host)
    entity_url = entity_url.replace('{metric_name}', self.metric_name)

    try:
      response = urllib2.urlopen(entity_url).read()

      return json.loads(response)
    except urllib2.HTTPError as e:
      return []
