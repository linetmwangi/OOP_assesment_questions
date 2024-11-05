class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(3, 4)
vector2 = Vector(1, 2)

result = vector1 + vector2

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Result of Vector1 + Vector2:", result)
