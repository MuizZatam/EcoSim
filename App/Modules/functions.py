import numpy as np
from scipy.spatial import cKDTree

class BiomeType:

    def __init__(self):

        self.biome_data = {

            "Tundra": [(-5, 20), (0, 30)],
            "Boreal Forest": [(0, 150), (5, 200)],
            "Temperate Grassland": [(10, 50), (15, 75)],
            "Woodland/Shrubland": [(15, 100), (20, 125)],
            "Temperate Seasonal Forest": [(10, 175), (15, 225)],
            "Temperate Rainforest": [(15, 250), (20, 300)],
            "Subtropical Desert": [(25, 50), (30, 100)],
            "Tropical Seasonal Forest/Savanna": [(25, 150), (30, 175)],
            "Tropical Rainforest": [(25, 300), (30, 400)]
        }

        self.points = []
        self.labels = []
        for biome, data_points in self.biome_data.items():
            for point in data_points:
                self.points.append(point)
                self.labels.append(biome)

        self.tree = cKDTree(self.points)

    def classify(self, temperature, precipitation, k=3):
        
        query_point = np.array([temperature, precipitation])
        distances, indices = self.tree.query(query_point, k=k)

        nearest_biomes = [self.labels[i] for i in indices]

        return max(set(nearest_biomes), key=nearest_biomes.count)