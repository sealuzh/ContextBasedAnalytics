from flask import Flask, Response, redirect, render_template, request, send_from_directory
import urllib2
import json
import os
from context_graph import ContextGraph
import datetime
from container.containers import Containers
from nodes.cpu_node import CPUNode
from nodes.jitter_node import JitterNode
from nodes.code_fragment_node import CodeFragmentNode
from nodes.disk_node import DiskNode
from nodes.memory_node import MemoryNode
from extraction.crawler.environment_crawler import EnvironmentCrawler

from extraction.git.methodslice import MethodSlice

app = Flask(__name__)



@app.route("/fragment/<file>")
def fragment(file):
  m = MethodSlice('repos/ext-auth-srv/' + file)
  return json_response(m.get_code_fragments())

@app.route("/test")
def test():
  crawler = EnvironmentCrawler('update-server')

  return json_response(crawler.load_entities())

@app.route("/contextgraph/expand/<service_name>/<node>/<start>/<end>")
def node_expand(service_name, node, start, end):

  if not service_name or not node: return '[]'

  node_ = node.split(':')
  node_type = node_[0]
  node_id = None
  if len(node_) > 1:
    node_id = node_[1]

  node_classes = { 'cpu': CPUNode,
                   'jitter' : JitterNode,
                   'code_fragment' : CodeFragmentNode,
                   'disk' : DiskNode,
                   'memory' : MemoryNode
                   }

  timespan = {'start': start, 'end': end}

  node = node_classes[node_type](service_name, timespan)
  if node_id:
    subgraph = node.graph_nodes(node_id)
  else:
    subgraph = node.graph_nodes()

  return json_response(subgraph)


@app.route("/")
def index():
    containers = Containers()
    return render_template('index.html', containers = containers.get_dict())


@app.route("/contextgraph/<service_name>")
def get_context_graph(service_name):
  containers = Containers()
  context_graph = ContextGraph(containers).get_initial_graph(service_name)
  return json_response(context_graph)


@app.route("/containers")
def get_containers_json():
  containers = Containers()
  return json_response(containers)


def json_response(data):
  return Response(response=json.dumps(data), status=200, mimetype="application/json")


## template filter

@app.template_filter('format_date')
def format_date(timestamp):
    if not timestamp: return ""
    return datetime.datetime.fromtimestamp(timestamp)


# for now, just remove "-" in strings for them to be able to be in function names
@app.template_filter('functionify')
def functionify(s):
    return s.replace("-", "")






if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=4000)
