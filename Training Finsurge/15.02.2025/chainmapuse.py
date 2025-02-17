#Merging Multiple Dictionaries Without Modifying Them 
from collections import ChainMap

default_config = {'theme': 'light', 'font': 'Arial', 'size': 12}
user_config = {'theme': 'dark', 'size': 14} 

settings = ChainMap(user_config, default_config)
print(settings) 
print(settings['theme'])  # Output: dark
print(settings['font'])  #fallback to default_config)


data = {'mode': 'production', 'version': 1}
temporary = {'mode': 'debug'}  # Temporary changes

config = ChainMap(temporary, data)

print(config['mode'])  # Output: debug 

c = config.parents #past stage 
print(c) 
print(c['mode'])

#dynamically updates 
d= ChainMap({'feature': 'enabled'}, {'feature': 'disabled'})

d.maps['feature'] = 'experimental'

print(d['feature']) 