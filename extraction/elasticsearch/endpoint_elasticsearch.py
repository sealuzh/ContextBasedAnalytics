from base_elasticsearch import BaseElasticsearch
from model.endpoint import Endpoint

class EndpointElasticsearch(BaseElasticsearch):

  def __init__(self, service, timespan):
    query = 'module:"werkzeug"'
    super(EndpointElasticsearch, self).__init__(service, query, timespan)

  def load_entities(self):
    entities = super(EndpointElasticsearch, self).load_entities()
    response_times = []
    for item in entities:
        rt = Endpoint.create_from_log(item['_source']['message_payload'], item['_source']['timestamp'])
        if rt is not None:
          response_times.append(rt)

    return response_times

