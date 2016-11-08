from base_crawler import BaseCrawler

class EnvironmentCrawler(BaseCrawler):

  def __init__(self, container_name, timestamp):
    #timestamp = '2016-07-15T10:00-04:00' #TODO: replace that with actual passed timestamp
    super(EnvironmentCrawler, self).__init__(timestamp)
    self.features = "dockerinspect"
    self.container_name = container_name


  def load_entities(self):
    entities = super(EnvironmentCrawler, self).load_entities()

    if not entities: return {}

    env_vars_raw = entities[entities.keys()[1]]['Config']['Env']

    environment = {}
    for env_var_raw in env_vars_raw:
      env_var, env_var_value = env_var_raw.split('=')
      environment[env_var] = env_var_value

    return environment
