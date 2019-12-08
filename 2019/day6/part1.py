"""
You've landed at the Universal Orbit Map facility on Mercury.
Because navigation in space often involves transferring between orbits,
the orbit maps here are useful for finding efficient routes between, for example, you and Santa.
You download a map of the local orbits (your puzzle input).

Except for the universal Center of Mass (COM), every object in space is in orbit around exactly one
other object. An orbit looks roughly like this:

                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /
In this diagram, the object BBB is in orbit around AAA. The path that BBB takes around AAA
(drawn with lines) is only partly shown. In the map data, this orbital relationship is
written AAA)BBB, which means "BBB is in orbit around AAA".

Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the
download. To verify maps, the Universal Orbit Map facility uses orbit count checksums - the total
number of direct orbits (like the one shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C.
This chain can be any number of objects long: if A orbits B, B orbits C, and C orbits D, then A
indirectly orbits D.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
In this visual representation, when two objects are connected by a line, the one on the right
directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7 orbits.
COM orbits nothing.
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?

Your puzzle answer was 227612.
"""

import queue

HEAD = 'COM'

def get_orbits(file_name):
    """ Read the orbits from the input and build the dictionary of parent - child orbits """
    orbits = {}
    with open(file_name) as orbits_file:
        for line in orbits_file:
            parent_planet, child_planet = line.strip().split(')')
            if parent_planet not in orbits:
                orbits[parent_planet] = [child_planet]
            else:
                orbits[parent_planet].append(child_planet)
    return orbits


def count_indirect_orbits(orbits):
    """ Count the indirect orbits from the HEAD to each of the nodes and return them as the levels
    dictionary. The HEAD is at level 0 """
    levels = {HEAD: 0}
    bfs_queue = queue.Queue()
    bfs_queue.put(HEAD)
    while not bfs_queue.empty():
        parent = bfs_queue.get()
        if not parent in orbits:
            continue
        for child in orbits[parent]:
            if child in levels:
                levels[child] = min(levels[child], levels[parent] + 1)
            else:
                levels[child] = levels[parent] + 1
            bfs_queue.put(child)
    return levels


ORBITS = get_orbits('small_input')
print(sum(count_indirect_orbits(ORBITS).values()))
