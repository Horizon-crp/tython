from os import rmdir
from ..filemanagement import isdir, get_path
def rmproject(Name: str) -> None:
  '''
  Delete a minimal project
  '''
  if isdir(f'/data/project/{Name}') is False:
    raise ValueError('Project doesn\'t exist, to create a project please check the function mkproject')
  rmdir(get_path(Name))
