from os import mkdir
from ..filemanagement import isdir, get_path
def mkproject(Name: str) -> None:
  '''
  Make a minimal project, to work with

  Here's the files that will appear without nothing

  main.py
  ```python
  print("Hello, world !")
  ```
  '''
  if isdir(f'/data/project/{Name}'):
    raise ValueError('Project already exist, to delete a project please check the function rmproject')
  path = get_path(Name)
  mkdir(path)
  with open(f'{path}/main.py', 'x') as f:
    f.write("Print(\"Hello, world !\")")
  return None
