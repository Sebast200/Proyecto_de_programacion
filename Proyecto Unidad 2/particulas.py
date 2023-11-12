import random, globales
class Particulas:
    def __init__(self):

        self.particulas = []
        self.vGlobales = globales.Globaless()

    def crear_particula(self):
        x = random.randint(self.vGlobales.ancho_gris/2,self.vGlobales.WIDTH*1.2)
        y = 0
        return {'x': x,'y': y, 'vy': 1, 'masa': random.uniform(0.1,1)}
    
    def update(self,viento):
        for i in range(1):
            self.particulas.append(self.crear_particula())
        
        for particula in self.particulas:
            particula['vy'] += 0.1 * particula['masa']

        for particula in self.particulas:
            particula['y'] += 2
            particula['x'] += viento
            if (particula['y'] > self.vGlobales.HEIGHT):
                self.particulas.remove(particula)

            