import pygame

class AStar:
    def __init__(self, graph="digital"):
        self.graph_type = graph
        pygame.init()
        self.display = pygame.display.set_mode((1200, 900))
        self.clock = pygame.time.Clock()
        self.running = False
        self.agent_radius = 10
        self.objs = []
        self.forbiden_areas = []

    def placeObjects(self, objs):
        self.objs = objs

    def generateGraph(self):
        self.forbiden_areas = []
        for obj in self.objs:
            f_area = [obj[0]-self.agent_radius, obj[1]-self.agent_radius, obj[2]+2*self.agent_radius, obj[3]+2*self.agent_radius]
            self.forbiden_areas.append(f_area)


    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.display.fill("purple")
                for f_area in self.forbiden_areas:
                    r_area_rect = pygame.Rect(f_area[0], f_area[1], f_area[2], f_area[3])
                    pygame.draw.rect(self.display, (100,0,0), r_area_rect)
                for obj in self.objs:
                    obj_rect = pygame.Rect(obj[0], obj[1], obj[2], obj[3])
                    pygame.draw.rect(self.display, (0,0,0), obj_rect)
                pygame.display.flip()
                self.clock.tick(60)
        pygame.quit()



if __name__ == "__main__":
    aStar = AStar()
    objs = [[20,20,100,300],[300,50,100,200],[60,700,200,50],[1000,500,300,50],[400,300,320,234],[400,320,654,23],[303,540,430,320],[674,875,44,465]]
    aStar.placeObjects(objs)
    aStar.generateGraph()
    aStar.run()
