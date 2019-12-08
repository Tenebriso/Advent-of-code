"""
Now, you just need to figure out how many orbital transfers you (YOU)
need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting.
An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

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
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN

In this example, YOU are in orbit around K, and SAN is in orbit around I.
To move from K to I, a minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to
the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)

Your puzzle answer was 454.
"""
import queue

SRC = 'YOU'
DST = 'SAN'

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
            if child_planet not in orbits:
                orbits[child_planet] = [parent_planet]
            else:
                orbits[child_planet].append(parent_planet)
    return orbits


def count_indirect_orbits(orbits):
    """ Count the indirect orbits from the HEAD to each of the nodes and return them as the levels
    dictionary. The HEAD is at level 0 """
    bfs_queue = queue.Queue()
    src = orbits[SRC][0]
    bfs_queue.put(src)
    dest = {src: 0}
    while not bfs_queue.empty():
        current_node = bfs_queue.get()
        for child in orbits[current_node]:
            if not child in dest:
                dest[child] = dest[current_node] + 1
                bfs_queue.put(child)
            if child == orbits[DST][0]:
                return dest[child]

    return None


ORBITS = get_orbits('small_input')
print(count_indirect_orbits(ORBITS))
