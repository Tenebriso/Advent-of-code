class Velocity:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


class Planet:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vel = Velocity()

    def add_gravity(self, other_planet):
        if self.x < other_planet.x:
            self.vel.x += 1
            other_planet.vel.x -= 1
        elif self.x > other_planet.x:
            self.vel.x -= 1
            other_planet.vel.x += 1
        if self.y < other_planet.y:
            self.vel.y += 1
            other_planet.vel.y -= 1
        elif self.y > other_planet.y:
            self.vel.y -= 1
            other_planet.vel.y += 1
        if self.z < other_planet.z:
            self.vel.z += 1
            other_planet.vel.z -= 1
        elif self.z > other_planet.z:
            self.vel.z -= 1
            other_planet.vel.z += 1

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self):
        return abs(self.vel.x) + abs(self.vel.y) + abs(self.vel.z)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def __str__(self):
        return "position: ({x} {y} {z}), velocity: ({vx} {vy} {vz})".format(
            x=self.x, y=self.y, z=self.z, vx=self.vel.x,
            vy=self.vel.y, vz=self.vel.z)


def compute_position(planets):
    for planet in planets:
        planet.x += planet.vel.x
        planet.y += planet.vel.y
        planet.z += planet.vel.z


def compute_velocity(planets):
    """Go over each planet in the list and compare it to the others """
    for i in range(len(planets) - 1):
        for j in range(i+1, len(planets)):
            planets[i].add_gravity(planets[j])


def total_energy(planets):
    sum = 0
    for planet in planets:
        sum += planet.total_energy()
    return sum


if __name__ == "__main__":
    planets = [Planet(-8, -18, 6), Planet(-11, -14, 4), Planet(8, -3, -10),
               Planet(-2, -16, 1)]
    for _ in range(1000):
        compute_velocity(planets)
        compute_position(planets)
    print(total_energy(planets))
