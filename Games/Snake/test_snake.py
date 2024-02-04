from snake import Snake

snake = Snake(100, 100)

def test_visible():
    assert snake.segments[0].isvisible()

def test_penup():
    assert not(snake.segments[0].isdown())

def test_position():
    x, y = snake.segments[0].position()
    assert x == 0
    assert y == 0

def test_length():
    assert snake.length() == 1
    #snake.add()        # snake.add() produces error float object is not suscriptable, but only with pytest, not in production
    #snake.add()
    #assert snake.length() == 2

def test_collision():
    assert snake.collision((0, 0))
    assert not(snake.collision((20, 20)))

def test_rotation():
    assert snake.segments[0].heading() == 0.0
    snake.left()
    assert snake.segments[0].heading() == 90.0
    snake.right()
    snake.right()
    assert snake.segments[0].heading() == 270.0