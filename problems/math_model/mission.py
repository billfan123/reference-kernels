import math
from typing import Tuple

def missile_position(initial_pos: Tuple[float, float, float], velocity: Tuple[float, float, float], time: float) -> Tuple[float, float, float]:
    """
    Calculate the final position of a missile in 3D space.

    :param initial_pos: Initial coordinates as a tuple (x0, y0, z0)
    :param velocity: Velocity as a tuple (vx, vy, vz)
    :param time: Time in seconds
    :return: Final coordinates as a tuple (x, y, z)
    """
    x0, y0, z0 = initial_pos
    vx, vy, vz = velocity
    x = x0 + vx * time
    y = y0 + vy * time
    z = z0 + vz * time
    return x, y, z


def smoke_position(initial_pos: Tuple[float, float, float], velocity: Tuple[float, float, float], time: float, g: float = 9.81) -> Tuple[float, float, float]:
    """
    Calculate the final position of smoke in 3D space, considering gravity in the vertical (z) direction.

    :param initial_pos: Initial coordinates as a tuple (x0, y0, z0)
    :param velocity: Velocity as a tuple (vx, vy, vz)
    :param time: Time in seconds
    :param g: Gravitational acceleration (default 9.81 m/s^2)
    :return: Final coordinates as a tuple (x, y, z)
    """
    x0, y0, z0 = initial_pos
    vx, vy, vz = velocity
    x = x0 + vx * time
    y = y0 + vy * time
    z = z0 + vz * time - 0.5 * g * time ** 2
    return x, y, z


def missile_intersect_smoke(missile_position: Tuple[float, float, float], smoke_position: Tuple[float, float, float], smoke_radius: float, target_position: Tuple[float, float, float]) -> bool:
    """
    Check if the missile-target line intersects with the smoke cloud.

    :param missile_position: Current position of the missile
    :param smoke_position: Current position of the smoke
    :param smoke_radius: Radius of the smoke cloud
    :param target_position: Current position of the target
    :return: True if the missile intersects with the smoke cloud, False otherwise
    """
    mx, my, mz = missile_position
    sx, sy, sz = smoke_position
    tx, ty, tz = target_position

    # Vector from missile to target
    dx = tx - mx
    dy = ty - my
    dz = tz - mz

    # Vector from missile to smoke
    fx = sx - mx
    fy = sy - my
    fz = sz - mz

    a = dx * dx + dy * dy + dz * dz
    b = 2 * (fx * dx + fy * dy + fz * dz)
    c = (fx * fx + fy * fy + fz * fz) - smoke_radius * smoke_radius

    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return False  # No intersection

    discriminant_sqrt = math.sqrt(discriminant)
    t1 = (-b - discriminant_sqrt) / (2 * a)
    t2 = (-b + discriminant_sqrt) / (2 * a)

    if (0 <= t1 <= 1) or (0 <= t2 <= 1):
        return True  # Intersection occurs within the segment

    return False  # No intersection within the segment

# Example usage
if __name__ == "__main__":
    initial_pos = (20000, 0, 2000)
    direction = (-20000, 0, -2000)
    # 归一化方向向量
    norm = math.sqrt(direction[0]**2 + direction[1]**2 + direction[2]**2)
    velocity = (300 * direction[0] / norm, 300 * direction[1] / norm, 300 * direction[2] / norm)  # 300 m/s
    time = 5.1  # seconds

    print("Missile velocity:", velocity)
    final_pos = missile_position(initial_pos, velocity, time)
    print("Missile final position:", final_pos)
    drone_initial_position = (17800, 0, 1800)
    drone_direction = (-17800, 0, -1800)

    norm = math.sqrt(drone_direction[0]**2 + drone_direction[1]**2 + drone_direction[2]**2)
    drone_velocity = (120 * drone_direction[0] / norm, 120 * drone_direction[1] / norm, 120 * drone_direction[2] / norm)  # 120 m/s
    #print("Drone velocity:", drone_velocity)
    time = 1.5  # seconds
    drone_position = missile_position(drone_initial_position, drone_velocity, time)
    #print("Drone final position:", drone_position)

    smoke_initial_position = drone_position
    smoke_velocity = drone_velocity
    smoke_time = 3.6  # seconds
    smoke_position = smoke_position(smoke_initial_position, smoke_velocity, smoke_time)
    print("Smoke final position:", smoke_position)
    target_position = (0, 200, 0)
    print("Target position:", target_position)
    #for t in [i * 0.1 for i in range(1, 100)]:
     #   pos = (final_pos[0] + velocity[0] * t, final_pos[1] + velocity[1] * t, final_pos[2] + velocity[2] * t)
    intersect = missile_intersect_smoke((smoke_position[0] - 11, smoke_position[1], smoke_position[2]), smoke_position, 10, target_position)
    print("Does the missile intersect with the smoke cloud?", intersect)