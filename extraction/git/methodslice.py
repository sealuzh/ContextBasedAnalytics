def function_identifier_by_language(path):
  extension_to_identifier = {'py' : 'def', 'go' : 'func'}
  extension = path.split('.')[-1]
  return extension_to_identifier[extension]

def function_end_delimiter_by_language(path):
  extension_to_identifier = {'py' : "\n", 'go' : "}\n"}
  extension = path.split('.')[-1]
  return extension_to_identifier[extension]

# gets a program file on disk, and returns a structure of code fragments (== methods)
# for now limited to python and go (other method definition require more complex parsing)
class MethodSlice:
  def __init__(self, path):
    self.path = path

  def get_code_fragments(self):
    fragments = {}

    with open(self.path, 'r') as f:
      lines = f.readlines()

    i = 0
    identifier = function_identifier_by_language(self.path)
    function_end_delimiter = function_end_delimiter_by_language(self.path)
    while i < len(lines):
      # detect functions
      if lines[i].strip().startswith(identifier):
        function = lines[i].split('(')[0]
        fragments[function] = []

        while i < len(lines) and lines[i] != function_end_delimiter:
          fragments[function].append(lines[i])
          i += 1
        fragments[function].append(function_end_delimiter)

      i += 1
    return fragments

