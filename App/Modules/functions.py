import numpy as np
from scipy.spatial import cKDTree

class BiomeType:
    def __init__(self):
        self.biome_data = {
            "Tundra": [(-10, 10), (-5, 20), (0, 30)],
            "Boreal Forest": [(0, 30), (0, 75), (5, 125)],
            "Temperate Grassland": [(5, 30), (10, 50), (15, 75)],
            "Woodland/Shrubland": [(10, 30), (15, 60), (20, 100)],
            "Temperate Seasonal Forest": [(5, 100), (10, 150), (15, 200)],
            "Temperate Rainforest": [(10, 200), (15, 300), (20, 350)],
            "Subtropical Desert": [(20, 0), (25, 20), (30, 50)],
            "Tropical Seasonal Forest / Savanna": [(20, 60), (25, 150), (30, 200)],
            "Tropical Rainforest": [(25, 200), (25, 300), (30, 450)]
        }
        self.points = []
        self.labels = []
        for biome, data_points in self.biome_data.items():
            for point in data_points:
                self.points.append(point)
                self.labels.append(biome)
        self.tree = cKDTree(self.points)

    def classify(self, temperature, precipitation, k=5):
        query_point = np.array([temperature, precipitation])
        distances, indices = self.tree.query(query_point, k=k)
        nearest_biomes = [self.labels[i] for i in indices]
        return max(set(nearest_biomes), key=nearest_biomes.count)

    def get_biome_boundaries(self):
        boundaries = {}
        for biome, points in self.biome_data.items():
            temp_min = min(point[0] for point in points)
            temp_max = max(point[0] for point in points)
            precip_min = min(point[1] for point in points)
            precip_max = max(point[1] for point in points)
            boundaries[biome] = {
                'temp_range': (temp_min, temp_max),
                'precip_range': (precip_min, precip_max)
            }
        return boundaries