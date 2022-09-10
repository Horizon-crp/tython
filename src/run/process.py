import subprocess
from typing import Optional
project_path = __file__[: -(len((e := __file__.split('/'))[-1]) + len(e[-2]))] + '/data/run'
def run(Code: str, FileName: str = 'Runner.ty', *, endfunc = None) -> Optional[dict]:
  '''
  Run a translated tython code
  '''
  FileName = f"{project_path.replace('.ty', '.py').replace('/', '.')}/{FileName}"
  with open(FileName, 'w') as f:
    f.write(Code)
  p = subprocess.Popen(f'python3 {FileName}', shell=True)
  out, err = p.communicate()
  print(f"Code exited.\nSubprocess Ouput : {out}\nSubprocess error : {err}")
  if endfunc is None:
    if out is not None or err is not None:
      return {"out": out, "error": err}
    return None
  endfunc(out, err)
  return None
