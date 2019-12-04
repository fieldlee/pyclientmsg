import yaml

def getYaml():
    with open("./config.yaml",'r') as f:
        d = f.read()
        data = yaml.load(d,yaml.FullLoader)
    f.close()
    return data

config = getYaml()
