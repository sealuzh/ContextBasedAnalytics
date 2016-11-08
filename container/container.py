import json
import os
from vcf import VersionControlFetch

def _extract_repository_name(repository_url):
  # split by '/', get last element and strip the '.git' at the end
  return repository_url.split('/')[-1][:-4]

class Container(object):

  # the full entry == the url
  def __init__(self, repo_entry):
      self.name = _extract_repository_name(repo_entry)
      self.url = repo_entry

  def get_api_methods(self):
    vcf = VersionControlFetch(self._get_vcf_service_endpoint())
    api_methods = vcf.api_methods(self.name)

  @staticmethod
  def _get_vcf_service_endpoint():
    return os.getenv('VCF_1_PORT').replace('tcp', 'http') + '/'