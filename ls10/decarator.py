from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int 
    y: int
    z: int = 0

    @property
    def magnitude(self):
        return (self.x **2 + self.y ** 2 + self.z ** 2) ** 0.5


p = Point(3, 4, 0)
print(p.magnitude)
p.x = 10