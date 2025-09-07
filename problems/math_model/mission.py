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
    print("Drone velocity:", drone_velocity)
    time = 1.5  # seconds
    drone_position = missile_position(drone_initial_position, drone_velocity, time)
    print("Drone final position:", drone_position)

    smoke_initial_position = drone_position
    smoke_velocity = drone_velocity
    smoke_time = 3.6  # seconds
    smoke_position = smoke_position(smoke_initial_position, smoke_velocity, smoke_time)
    print("Smoke final position:", smoke_position)
    target_position = (0, 200, 0)
    
    target_visible_direction = (smoke_position[0] - 10 - target_position[0], smoke_position[1] - target_position[1], smoke_position[2] - target_position[2])
    target_invisible_direction = (smoke_position[0] + 10 - target_position[0], smoke_position[1] - target_position[1], smoke_position[2] - target_position[2])
