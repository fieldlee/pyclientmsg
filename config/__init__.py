import yaml

configfile = "./config.yaml"

def getYaml(path:str):
    data = ""
    with open(path,'r') as f:
        d = f.read()
        data = yaml.load(d,yaml.FullLoader)
    f.close()
    return data

config = getYaml(configfile)
