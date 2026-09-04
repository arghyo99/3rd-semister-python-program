import re

paragraph = """hi, i am a python developer .
 i am expart telegram bot and computer tools developer .
 python is my pashon . i like python language .
 you eazaly hear me with your python developer
  """

x = re.findall('python', paragraph)
print(  x.count('python') , 'python found ' )