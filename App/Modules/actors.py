class Biome:

    def __init__(self, name, area, temperature, precipitation, biome_type):

        self.name = name
        self.area = area
        self.temperature = temperature
        self.precipitation = precipitation
        self.biome_type = biome_type

    @property
    def name(self):

        return self._name
    
    @name.setter
    def name(self, name):

        self._name = name

    @property
    def area(self):

        return self._area
    
    @area.setter
    def area(self, area):

        self._area = area

    @property
    def temperature(self):

        return self._temperature
    
    @temperature.setter
    def temperature(self, temperature):

        self._temperature = temperature

    @property
    def precipitation(self):

        return self._precipitation
    
    @precipitation.setter
    def precipitation(self, precipitation):

        self._precipitation = precipitation

    @property
    def biome_type(self):

        return self._biome_type
    
    @biome_type.setter
    def biome_type(self, biome_type):

        self._biome_type = biome_type


    