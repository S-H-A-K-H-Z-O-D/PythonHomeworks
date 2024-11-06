from __future__ import annotations
import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, arg: Vector3D):
        return Vector3D(self.x + arg.x, self.y + arg.y, self.z + arg.z)
    
    def __bool__(self):
        return not (self.x == 0 and self.y == 0 and self.z == 0)
    
    def __abs__(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __getitem__(self, index):
        match index:
            case 0:
                return self.x
            case 1:
                return self.y
            case 2:
                return self.z
            
    def __setitem__(self, index, value):
        match index:
            case 0:
                self.x = value
            case 1:
                self.y = value
            case 2:
                self.z = value

    def __sub__(self, arg: Vector3D):
        return Vector3D(self.x - arg.x, self.y - arg.y, self.z - arg.z)
    
    def __mul__(self, arg: Vector3D | int | float):
        if isinstance(arg, Vector3D):
            return self.x * arg.x + self.y * arg.y + self.z * arg.z
        elif isinstance(arg, (int, float)):
            return Vector3D(self.x * arg, self.y * arg, self.z * arg)
        else:
            raise TypeError("Unsupported type for multiplication")
        
    def __eq__(self, arg: Vector3D):
        return self.x == arg.x and self.y == arg.y and self.z == arg.z
    
    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)



v1 = Vector3D(1, 2, 3)
v2 = Vector3D(2, 3, 4)
v1[1] = 10
print(v1 * 2)

print(v1 == Vector3D(1, 10, 3))

print(-v1)