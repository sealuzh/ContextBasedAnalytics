from base_elasticsearch import BaseElasticsearch
from model.connection import Connection

class ConnectionElasticsearch(BaseElasticsearch):

  def __init__(self, service, timespan):
    query = 'module:"requests.packages.urllib3.connectionpool"'
    super(ConnectionElasticsearch, self).__init__(service, query, timespan)

  def load_entities(self):
    entities = super(ConnectionElasticsearch, self).load_entities()
    connections = []
    for item in entities:
        connection = Connection.create_from_log(item['_source']['message_payload'], item['_source']['timestamp'])
        if connection is not None:
          connections.append(connection)

    return connections

