import yaml

def readConfig(filename):
    with open(filename, 'r') as stream:
        return yaml.load(stream)

config = readConfig('./config.yaml')

