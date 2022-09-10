from os import mkdir, isfile
from ..filemanagement import isdir, get_path, lstdir, get_path_str
from typing import Optional
class project:
  def __new__(self, ProjectName: str):
    if isdir((self.path := get_path)) is False: raise ValueError("No such project")
    self.name = ProjectName
    self.files = lstdir(ProjectName)
    self.path_str = get_path_str(ProjectName)
    return self

  def run(self, File: str, *, endfunc = None) -> Optional[dict]:
    '''
  Run a translated tython code
  '''
  FileName = f'{self.path_str}/{File}'
  if isfile(FileName) is False: raise ValueError('No such file')
  p = subprocess.Popen(f'python3 {FileName}', shell=True)
  out, err = p.communicate()
  print(f"Code exited.\nSubprocess Ouput : {out}\nSubprocess error : {err}")
  if endfunc is None:
    if out is not None or err is not None:
      return {"out": out, "error": err}
    return None
  endfunc(out, err)
  return None
  
  def add_file(self, Name: str, Content: str):
    with open(f'{self.path_str}/{Name}', 'x') as f:
      f.write(Content)
    self.get_files()
    return self

  def edit_file(self, Name: str, Content: str):
    with open(f'{self.path_str}/{Name}', 'w') as f:
      f.write(Content)
    return self

  def add_folder(self, Name: str):
    mkdir(Name)
    return self

  def get_files(self):
    self.files = lstdir(self.name)
    return self

  def ls(self):
    '''
    The ls command (same as the __str__ method)
    '''
    return ', '.join(self.files)
  
  def __str__(self):
    return ', '.join(self.files)
