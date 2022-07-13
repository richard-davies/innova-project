from datetime import date

def get_today():
  today = date.today()
  d1 = today.strftime("%y%m%d%a")
  return d1[:-1]

def get_todays_folder(generic_path = "\\\\D35B311J\Documentos c\clt"):
  todays_working_folder = get_today()
  return  generic_path + "\\" + todays_working_folder