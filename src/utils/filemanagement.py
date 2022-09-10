project_path = __file__[: -(len((e := __file__.split('/'))[-1]) + len(e[-2]))] + '/data/project'
from os import path, listdir
def isdir(Name: str) -> bool:
  return path.isdir(get_path(Name))

def get_path(AnyPath: str):
  return path.join(f'{project_path}/', AnyPath)

def get_path_str(AnyPath: str) -> str:
  return f'{project_path}/{AnyPath}'

def lstdir(Name: str) -> list:
  e: list = []
  for i in listdir(get_path_str(Name)): e.append(i)
  return e
