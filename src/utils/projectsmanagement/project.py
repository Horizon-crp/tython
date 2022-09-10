from os import mkdir
from ..filemanagement import isdir, get_path, lstdir, get_path_str 
class project:
  def __new__(self, ProjectName: str):
    if (self.path := isdir(self.path)) is False: raise ValueError("No such project")
    self.name = ProjectName
    self.files = lstdir(ProjectName)
    self.path_str = get_path_str(ProjectName)
    return self

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

  def __str__(self):
    return str(self.files)
