from piece import piece


class rook(piece):
    """Attributes of the class"""
    moved = False

    # Initiate instance
    def __init__(self):
        self.data = []

    """ Override of abstract class """

    # Method for recovering the movement of a piece
    # Return consists on an array of 3 numbers
    # Maximum quantity of square and possible axis, [4,8,3] 4 spaces in 8 possible directions identifies a rook, 0 means no diagonal movement
    def get_movement(self):
        return [7, 4, 0]

    #Check if the piece has made a movement (for special movement validation)
    def hasMoved(self):
        return self.moved()

    #Set the moved attribute to true to avoid special movements
    def setMoved(self):
        self.moved = True