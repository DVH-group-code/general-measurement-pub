#%%
import yaml
#%%
import Parameters as pm
msys = pm.MSys()
ry = pm.RecordYaml(msys)
path = 'C:\\Users\\yg\\Desktop\\tmp'
#%%
ry.build_dict()
ry.export(path, 'test.yaml')

#%%
f = open(path+ '\\' + 'test.yaml', 'r')
text = pm.yaml.safe_load(f)
f.close()

#%%
a = 1
f = open(path+'\\tmp.yaml','w')
text = yaml.dump({'a':a}, f)
f.close()
print(text)
#%%
class Monster(yaml.YAMLObject):
    yaml_tag = u'!Monster'
    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks
    def __repr__(self):
        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
        self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)

