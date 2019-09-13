# -*- coding: utf-8 -*-

"""
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so,
you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet.
There are two types: Mach bombs (M) and Facula bombs (F).
The bombs, once released into the LAMBCHOP's inner workings,
will automatically deploy to all the strategic points you've identified and destroy them at the same time.

But there's a few catches.
First, the bombs self-replicate via one of two distinct processes:
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs,
they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs.
The replication process can be changed each cycle.

Second, you need to ensure that
you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device.
Too few, and the device might survive. Too many, and you might overload the mass capacitors
and create a singularity at the heart of the space station - not good!

And finally, you were only able to smuggle one of each type of bomb
- one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with.
(Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!)

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs
to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed.
Return the fewest number of generations (as a string) that need to pass
before you'll have the exact number of bombs necessary to destroy the LAMBCHOP,
or the string "impossible" if this can't be done!
M and F will be string representations of positive integers no larger than 10^50.
For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1".
However, if M = "2" and F = "4", it would not be possible.


Test cases
==========

Inputs:
    (string) M = "2"
    (string) F = "1"
Output:
    (string) "1"

Inputs:
    (string) M = "4"
    (string) F = "7"
Output:
    (string) "4"
"""


class InvalidCycleError(Exception):
    pass


class BombCycle:
    def __init__(self, m_count, f_count, cycle_count):
        self.m = m_count
        self.f = f_count
        self.cycle = cycle_count

    def is_point(self):
        return self.m == 1 and self.f == 1

    def reverse_cycle(self):
        if self.m * self.f == 0:
            raise InvalidCycleError

        if self.m > self.f:
            opt_count = int((self.m - 1) / self.f)
            return BombCycle(self.m - (self.f * opt_count), self.f, self.cycle + opt_count)
        elif self.f > self.m:
            opt_count = int((self.f - 1) / self.m)
            return BombCycle(self.m, self.f - (self.m * opt_count), self.cycle + opt_count)
        else:
            raise InvalidCycleError


def answer(M, F):
    last_cycle = BombCycle(int(M), int(F), 0)

    while True:
        if last_cycle.is_point():
            return str(last_cycle.cycle)

        try:
            last_cycle = last_cycle.reverse_cycle()
        except InvalidCycleError:
            return "impossible"


if __name__ == "__main__":
    assert answer("2", "1") == "1"
    assert answer("2", "4") == "impossible"
    assert answer("4", "7") == "4"
