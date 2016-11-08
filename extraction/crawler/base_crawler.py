import urllib2, json, os
import datetime

class BaseCrawler(object):
  def __init__(self, timestamp):
    self.search_service_host = os.environ['CRAWLER_HOST']
    self.namespace = os.environ['CRAWLER_NAMESPACE'] + '/{container_id}'
    self.container_name = ''
    self.timestamp = timestamp
    self.url = "http://{host}/config/frame?namespace={namespace}&features={features}&timestamp={timestamp}"
    self.features = ""

  def load_entities(self):
    entity_url = self.url
    entity_url = entity_url.replace('{host}', self.search_service_host)
    entity_url = entity_url.replace('{namespace}', self.namespace.replace('{container_id}', self._container_id(self.container_name)))

    if not isinstance(self.features, basestring):
      features = "&".join(self.features)
    else:
      features = self.features

    entity_url = entity_url.replace('{features}', features)

    # convert timestamp format --> '2016-07-15T10:00-04:00'
    crawler_timestamp = self._timestamp_to_iso8601(int(self.timestamp['start']))
    entity_url = entity_url.replace('{timestamp}', crawler_timestamp)

    try:
      response = urllib2.urlopen(entity_url).read()

      return json.loads(response)
    except urllib2.HTTPError as e:
      return []


  @staticmethod
  def _timestamp_to_iso8601(timestamp_in_ms):
    return datetime.datetime.fromtimestamp(timestamp_in_ms/1000).strftime('%Y-%m-%dT%H:%MZ')

  @staticmethod
  def _container_id(service):
    #TODO: get those id's by quering the crawler elasticsearch with something like unique dockerinspect.Config.Image:"xdevops/update-engine"
    container_ids = { 'update-server' : os.environ['CONTAINER_UPDATE_SERVER'], 'update-engine' :  os.environ['CONTAINER_UPDATE_ENGINE']}
    return container_ids[service]
