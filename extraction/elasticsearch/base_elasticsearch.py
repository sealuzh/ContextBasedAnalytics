import os
from elasticsearch import Elasticsearch

class BaseElasticsearch(object):
  def __init__(self, service, query, timespan):
    self.es_host = os.environ['ES_HOST']
    self.es = Elasticsearch([{'host' : self.es_host}])
    self.query = query
    self.timespan = timespan
    self.service = service
    # standard fields, subclass can override
    self.fields = ["message_payload",  "timestamp"]

  def load_entities(self):
    result = self.es.search(index = 'logstash-*', body={"_source": self.fields,
            "query": {
              "filtered": {
                "query": {
                  "bool": {
                    "should": [
                      {
                        "query_string": {
                          "query": self.query + " AND _type:\"" + self.service + "\""
                        }
                      }
                    ]
                  }
                },
                "filter": {
                  "bool": {
                    "must": [
                      {
                        "range": {
                          "@timestamp": {
                            "from" : self.timespan['start'],
                            "to" : self.timespan['end']
                          }
                        }
                      }
                    ]
                  }
                }
              }
            },
            "size": 2000,
            "sort": [
              {
                "@timestamp": {
                  "order": "desc",
                  "ignore_unmapped": True
                }
              },
              {
                "@timestamp": {
                  "order": "desc",
                  "ignore_unmapped": True
                }
              }
            ]})

    result_raw = result['hits']['hits']
    return result_raw
