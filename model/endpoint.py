import re

class Endpoint(object):

  def __init__(self, method, name, status, response_time, url, timestamp):
    self.method = method
    self.name = name
    self.status = status
    self.response_time = response_time
    self.url = url
    self.timestamp = timestamp
    self.label = self.assign_label()

  def assign_label(self):
    return self.method + " " + self.name

  @staticmethod
  def create_from_log(log_statement, timestamp):
    # possible log statement 172.17.0.1 - - [13/Jul/2016 13:47:54] "POST /v1/c3714fbd-eee7-4503-bb2b-8bbc139e4357/update/ HTTP/1.1" 201 - [10429ms] [update_record_action: create]
    http_methods = [u"GET", u"POST", u"PUT", u"DELETE", u"PATCH"]

    # TODO: clean up this workaround
    if log_statement.find('"') == -1:
      return None

    _, method_and_name, status_and_response_time = log_statement.split('"')
    method, url, _ = method_and_name.split(' ')

    # preconditions
    if not (method in http_methods):
      return None

    # extracting name has DOMAIN KNOWLEDGE!! TODO: this can be extracted into its own abstraction
    url_components = url.split('/')
    if len(url_components) > 3:
      name = url_components[3]
    else:
      name = url

    status, rest = status_and_response_time.split(' -')
    status = status.strip()

    number_regex = re.search("([0-9])+", rest)
    response_time = number_regex.group(0)

    return Endpoint(method, name, status, response_time, url, timestamp)