def compare_layers(e1, e2):
    return e1.layer < e2.layer



class EM:


    def __init__(self):
        self.entities = []


    def add(self, *args):
        for entity in args:
            if entity not in self.entities:
                self.entities.append(entity)
        self.entities = sorted(self.entities, 
                key=lambda entity: entity.layer)


    def destroy(self, entity):
        pass


    def update(self, entity):
        for entity in self.entities:
            entity.update()


    def draw(self, entity):
        for entity in self.entities:
            entity.draw()


    def push(self, entity):
        for i, e in enumerate(self.entities):
            if e == entity:
                self.entities += [self.entities.pop(i)]
