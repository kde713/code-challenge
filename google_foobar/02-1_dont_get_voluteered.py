# -*- coding: utf-8 -*-

"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker.
It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that
 everyone working for her is sufficiently quick-witted,
 Commander Lambda has installed new flooring outside the henchman dormitories.
 It looks like a chessboard, and every morning and evening you have to solve
 a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen,
 but instead, you have to be the knight. Worse, if you take too much time solving the puzzle,
 you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called answer(src, dest)
which takes in two parameters: the source square, on which you start, and the destination square,
which is where you need to land to solve the puzzle.  The function should return an integer representing
the smallest number of moves it will take for you to travel from the source square to the destination square
using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular
to that direction, or vice versa, in an "L" shape).  Both the source and destination squares
will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Test cases
==========

Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1

Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3
"""

from Queue import Queue


class BoardUtil:
    BOARD_SIZE = 8
    KNIGHT_MOVES = (
        (2, 1), (2, -1),
        (1, 2), (1, -2),
        (-1, 2), (-1, -2),
        (-2, 1), (-2, -1),
    )

    @staticmethod
    def num_to_pos(num):
        return num % BoardUtil.BOARD_SIZE, int(num / BoardUtil.BOARD_SIZE)

    @staticmethod
    def pos_to_num(x, y):
        return y * BoardUtil.BOARD_SIZE + x

    @staticmethod
    def is_inboard(x, y):
        return 0 <= x < BoardUtil.BOARD_SIZE and 0 <= y < BoardUtil.BOARD_SIZE


class Cell:
    def __init__(self, x, y, step_count):
        self.x = x
        self.y = y
        self.step_count = step_count

    def is_equal(self, x, y):
        return self.x == x and self.y == y


class CheckBoard:
    def __init__(self, size):
        self._check_board = []
        for loop_y in range(0, size):
            self._check_board.append([])
            for _ in range(0, size):
                self._check_board[loop_y].append(False)

    def mark_cell(self, x, y):
        self._check_board[y][x] = True

    def is_marked(self, x, y):
        return self._check_board[y][x]


def search_node(src_pos, dest_pos):
    board = CheckBoard(BoardUtil.BOARD_SIZE)

    node_queue = Queue()
    node_queue.put(Cell(src_pos[0], src_pos[1], 0))
    board.mark_cell(src_pos[0], src_pos[1])

    while not node_queue.empty():
        target_cell = node_queue.get()
        if target_cell.is_equal(dest_pos[0], dest_pos[1]):
            return target_cell.step_count

        for knight_move in BoardUtil.KNIGHT_MOVES:
            new_x, new_y = target_cell.x + knight_move[0], target_cell.y + knight_move[1]
            if BoardUtil.is_inboard(new_x, new_y):
                node_queue.put(Cell(new_x, new_y, target_cell.step_count + 1))


def answer(src, dest):
    src_x, src_y = BoardUtil.num_to_pos(src)
    dest_x, dest_y = BoardUtil.num_to_pos(dest)

    return search_node(
        (src_x, src_y),
        (dest_x, dest_y)
    )


if __name__ == "__main__":
    assert answer(19, 36) == 1
    assert answer(0, 1) == 3
