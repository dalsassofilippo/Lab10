from model.model import Model

model = Model()
model.crea_grafo(1980)
model.prova()
print(model.getNumNodes())
print(model.getNumEdges())
stato=model.getCoutry(2)
print(model.statiRaggiungibili(stato))
print(len(model.statiRaggiungibili(stato)))