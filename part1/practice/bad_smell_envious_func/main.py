# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class CubeVolumeCalculator:
    def __init__(self, cube):
        self.cube = cube

    def get_x(self):
        return self.cube.x

    def get_y(self):
        return self.cube.y

    def get_z(self):
        return self.cube.z

    @staticmethod
    def calc_cube_volume(self):
        return self.get_x() * self.get_y() * self.get_z()


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return self.x * self.y * self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.get_volume()