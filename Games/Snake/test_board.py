from board import Board

board = Board()

def test_hidden():
    assert not(board.isvisible())

def test_penup():
    assert not(board.isdown())

def test_position():
    x, y = board.position()
    assert x == 0
    assert y > -300 and y < 300