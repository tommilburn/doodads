import os

def createTemplate(templateName, folder ="/out"):
  folder = os.getcwd() + folder
  if not os.path.exists(folder):
    os.makedirs(folder)
  return open(folder + '/' + templateName + '.md', 'w+')