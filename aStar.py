import pygame

class AStar:
    def __init__(self, graph="digital"):
        self.graph_type = graph
        pygame.init()
        self.display = pygame.display.set_mode((1200, 900))
        self.display_width = 1200
        self.display_height = 900 
        self.clock = pygame.time.Clock()
        self.running = False
        self.agent_radius = 10
        self.objs = []
        self.forbiden_areas = []
        self.graph_resoultion = 0

    def placeObjects(self, objs):
        self.objs = objs

    def generatePath(self, start, dest):
        start_tile = start // self.graph_resoultion
        dest_tile = dest // self.graph_resoultion

    def generateDigitalGraph(self, resolution=20):
        self.forbiden_areas = []
        self.graph_resoultion = resolution
        for obj in self.objs:
            f_area = [obj[0]-self.agent_radius, obj[1]-self.agent_radius, obj[2]+2*self.agent_radius, obj[3]+2*self.agent_radius]
            self.forbiden_areas.append(f_area)
        self.graph = [[0 for _ in range(self.display_height // resolution)] for _ in range(self.display_width // resolution)]
        for row in range(len(self.graph)):
            for col in range(len(self.graph[0])):
                tile = pygame.Rect(row*resolution, col*resolution, resolution, resolution)
                if self.inForbidenArea(tile):
                    self.graph[row][col] = 1

    def inForbidenArea(self, rect):
        for f_area in self.forbiden_areas:
            f_area_rect = pygame.Rect(f_area[0], f_area[1], f_area[2], f_area[3])
            if pygame.Rect.colliderect(f_area_rect, rect):
                return True
        return False

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.display.fill("purple")
                for row in range(len(self.graph)):
                    for col in range(len(self.graph[0])):
                        if self.graph[row][col] == 1:
                            tile_rect = pygame.Rect(row*self.graph_resoultion, col*self.graph_resoultion, self.graph_resoultion, self.graph_resoultion)
                            pygame.draw.rect(self.display, (0,200,0), tile_rect)
                for f_area in self.forbiden_areas:
                    f_area_rect = pygame.Rect(f_area[0], f_area[1], f_area[2], f_area[3])
                    pygame.draw.rect(self.display, (200,0,0), f_area_rect)
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
    aStar.generateDigitalGraph()
    aStar.run()
