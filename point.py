'''
CIS 211
Nick Swanson
mini project 1: Point
'''
class Point:
    def __init__(self, x: int, y: int):
        '''takes 2 integers, a and y, and stores them as instance variables.'''
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        '''takes 2 integer arguments, dx and dy, and decreases or increases self x and self y by dx and dy.'''
        self.x += dx
        self.y += dy

    def __eq__(self, other) -> bool:
        '''returns true or false if self object and other point object are equal.'''
        return self.x == other.x and self.y == other.y

    def __str__(self):
        '''returns preferred string representation of an object'''
        return '(%g, %g)' % (self.x, self.y)
