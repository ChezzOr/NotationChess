from piece import piece

class bishop(piece):

    # Initiate instance
    def __init__(self):
        self.data = []
        self.name = 'b'

    """ Override of abstract class """

    # Method for recovering the movement of a piece
    # Return consists on an array of 3 numbers
    # Maximum quantity of square and possible axis, [7,4,1] 8 spaces in 4 possible directions identifies a bishop, 1 means diagonal included
    def get_movement(self):
        return [7,4,1]

    def validate_move(self):
        return False

    def get_fpw(self):
        return "sprites/bw.png"

    def get_fpb(self):
        return "sprites/bb.png"