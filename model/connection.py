class Connection(object):

  def __init__(self, method, status, url, timestamp):
    self.method = method
    self.status = status
    self.url = url
    self.timestamp = timestamp
    self.label = self.assign_label()

  def assign_label(self):
    parameter_url_split = self.url.split('?')
    if len(parameter_url_split) > 1:
      return parameter_url_split[0]
    else:
      return self.url

  @staticmethod
  def create_from_log(log_statement, timestamp):
    # TODO: actually crawl the method regexp and apply it to get unique urls
    # possible log statement "PUT /jurgen-updates-new/887b7ae6-de80-4445-ab4b-019a0d9a2d73 HTTP/1.1\" 201 99
    # structure {HTTP_METHOD} {base-url-path}?{url-parameters} HTTP/?.? {HTTP-Status} {??}
    http_methods = [u"GET", u"POST", u"PUT", u"DELETE", u"PATCH"]

    log_structure = log_statement.split(" ")

    method = log_structure[0].lstrip('"')


    # preconditions
    if not (method in http_methods):
      return None

    url = log_structure[1]
    status = log_structure[3]
    return Connection(method, status, url, timestamp)




