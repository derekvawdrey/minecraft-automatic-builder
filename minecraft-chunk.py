import mcschematic
import random

class MinecraftChunk:
    def __init__(self):
        self.chunk_width = 16
        self.chunk_length = 16
        self.chunk_height = 5
        self.chunk_name = "schemTest"
        self.wall_material = "minecraft:cobbled_deepslate"
        self.schem = mcschematic.MCSchematic()
        self.clearChunk()
        self.generateChunk()

    def clearChunk(self):
        for x in range (0, self.chunk_width):
            for z in range (0, self.chunk_length):
                for y in range (0, self.chunk_height):
                    self.schem.setBlock((x, y, z), "minecraft:air")

    def generateChunk(self):
        for x in range (0, self.chunk_width):
            for z in range (0, self.chunk_length):
                rand_num = random.randint(0, 10)
                if rand_num > 8:
                    self.insertWall(x,z)
    
    def insertWall(self, x, z, wall_height = 0):
        if wall_height == 0:
            wall_height = self.chunk_height
        for y in range (0, wall_height):
            self.schem.setBlock((x, y, z), self.wall_material)

    def saveChunk(self):
        self.schem.save("schem", self.chunk_name, mcschematic.Version.JE_1_9_2)

chunk = MinecraftChunk()
chunk.saveChunk()