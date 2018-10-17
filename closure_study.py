def circle_area_func(pi):
    """Example python closure.
    Args:
        pi (int): pi
    Returns:
        circle_area: The return value.
    """
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = circle_area_func(3.15)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))
