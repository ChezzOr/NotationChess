from piece import piece


class queen(piece):

    # Initiate instance
    def __init__(self):
        self.data = []

    """ Override of abstract class """

    # Method for recovering the movement of a piece
    # Return consists on an array of 3 numbers
    # Maximum quantity of square and possible axis, [8,8,1] 8 spaces in 4 possible directions identifies a queen, 1 means diagonal included
    def get_movement(self):
        return [7, 8, 1]
