from .data import data
from ..run import run
def reset_indent(content: str) -> str:
  e = 0
  for i in content:
    if i != ' ':
      return content[e:]
    e += 1
  return ''

def frst(Content: str) -> str:
  return Content[0] + Content[1] + Content[2] + Content[3]

class indentation:
  def __init__(self):
    self.indent: int = 0

  def __str__(self):
    e: str = ''
    for i in range(self.indent):
      e += '\t'
    return e

def compile(File: str, /, *, CompiledPlace: str = None, autorun: bool = True) -> None:
  '''
  Compile a ty file into python code
  '''
  indent = indentation()
  with open(File, 'r') as f:
    content = f.read()
  py: str = ''
  nl: str = ''
  for line in content.split('\n'):
    print(line)
    line = reset_indent(line)
    print(line)
    try:
      nl, indent = data[frst(line)](line, indent)
    except KeyError:
      nl += line
    py += f'{indent}{nl}\n'
  if CompiledPlace is not None:
    with open(CompiledPlace, 'w') as f:
      f.write(py)
  if autorun is True:
    run(py, File)
  return py
