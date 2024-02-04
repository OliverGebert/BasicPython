from food import Food

food = Food(100, 100)

def test_color():
    assert food.color()[0] in food.colors

def test_position():
    x, y = food.position()
    assert x > -101 and x < 101
    assert y > -101 and y < 101
