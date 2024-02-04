from turtle import Turtle


class Snake:

    def __init__(self, x, y):
        self.segments = []
        self.alive = True
        self.xmax = int(x)
        self.ymax = int(y)
        self.xmin = -int(x)
        self.ymin = -int(y)
        self.status = "ok"
        # create first segment in snake
        segment = Turtle(shape="square")
        segment.color("grey")
        segment.penup()
        segment.speed(0)
        segment.teleport(0, 0)        # teleport on same position as last segment
        self.segments.append(segment)

    def collision_boarder(self):
        """check whether the head of the snake collided with one of the boarders and return bool"""
        x, y = self.segments[0].position()
        if x < self.xmin or x > self.xmax or y < self.ymin or y > self.ymax:
            self.status = "boarder hit"
            return True
        return False

    def collision_tail(self):
        """check whether the head collided with one of the other segments and return as bool"""
        for segment in self.segments[1:]:
            if self.collision(segment.position()):
                self.status = "tail hit segment"
                return True 
        return False
    
    def collision(self, position):
        return self.segments[0].distance(position) < 19 

    def move(self):
        if len(self.segments) > 1:                           # if segments has more than one segments, 
            for i in range(len(self.segments)-1, 0, -1):         # every segment gets moved to the position of his predecessor, starting with last segment, without head segment
                self.segments[i].setpos(self.segments[i-1].position())
        self.segments[0].fd(20)                              # head move according to set direction of head
        self.alive = not(self.collision_boarder() or self.collision_tail())     # if boarder or tail hit, than set alive flag to False

    def color(self, clr):
        for segment in self.segments:
            segment.color(clr)

    def left(self):
        self.segments[0].left(90)                           # turn head

    def right(self):
        self.segments[0].right(90)                          # turn head

    def add(self, clr: str = "white"):
        segment = Turtle(shape="square")
        segment.color(str(clr))
        segment.penup()
        segment.teleport(self.segments[-1].position)        # teleport on same position as last segment
        self.segments.append(segment)

    def length(self):
        return len(self.segments)