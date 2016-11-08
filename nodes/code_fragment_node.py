from node import Node
from extraction.git.methodslice import MethodSlice


class CodeFragmentNode(Node):

  label = "CodeFragment"

  def __init__(self, service, timespan):
    super(CodeFragmentNode, self).__init__(service, timespan)

  def graph_nodes(self, func_name):
    # return just 1 method for now

    filename = 'a__Validate.go'
    m = MethodSlice('repos/ext-auth-srv/' + filename)
    fragments = m.get_code_fragments()
    key = 'func ' + func_name
    if key in fragments.keys():
      method = "".join(fragments[key]).lstrip()


    return { 'expand_nodes' : [], 'data' : method }


  def infer_context(self):
    return []