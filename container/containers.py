import json
from container import Container

class Containers(object):

  def __init__(self, list_path="data/repositoryList.txt"):
    self.list_path = list_path
    self.containers = self._retrieve(list_path)

  # if this gets called too often it might make sense to cache it
  def get_dict(self):
    containers_object = {}
    for container in self.containers:
      containers_object[container.name] = container.url
    return containers_object

  def __contains__(self, key):
    return key in self.get_dict()

  @staticmethod
  def _retrieve(list_path):
    containers = []
    with open(list_path) as f:
      repo_entries = [line.rstrip('\n') for line in f.readlines()]

    for repo_entry in repo_entries:
      container = Container(repo_entry)
      containers.append(container)
    return containers