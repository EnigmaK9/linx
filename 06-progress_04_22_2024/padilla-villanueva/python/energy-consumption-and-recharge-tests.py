import numpy as np
import random
import math
import csv
import matplotlib.pyplot as plt

# Constants
EARTH_RADIUS = 6371000  # Meters
PERIHELION_DISTANCE = 147.1e6  # Kilometers
PERIHELION_IRRADIANCE = 1367  # W/m^2 (average solar constant)
BATTERY_CAPACITY = 5200  # mAh (Lithium-ion battery capacity)

# System parameters
MAX_BATTERY = BATTERY_CAPACITY  # mAh
MIN_BATTERY = (BATTERY_CAPACITY/100)30  # mAh
CAMERA_CONSUMPTION = 115.0  # mAh/hour
PARTICLE_DETECTOR_CONSUMPTION = 288.0  # mAh/hour
DATA_DOWNLOAD_CONSUMPTION = 1080.0  # mAh/hour
DATA_UPLOAD_CONSUMPTION = 144  # mAh/hour
BATTERY_DEGRADATION = 0.01  # % per hour
OBC_CONSUMPTION = 2880  # mAh/hour
initial_battery = BATTERY_CAPACITY  # mAh

# Solar panel parameters
PANEL_AREA = 0.4  # m²
PANEL_EFFICIENCY = 0.25  # %

# Definition of tasks
TASKS = {
    "camera": {
        "id": 1,
        "consumption": CAMERA_CONSUMPTION,
        "duration": 216.0 / 60.0,  # hours
    },
    "spectrometer": {
        "id": 2,
        "consumption": PARTICLE_DETECTOR_CONSUMPTION,
        "duration": 8.0,  # hours
    },
    "data_download": {
        "id": 3,
        "consumption": DATA_DOWNLOAD_CONSUMPTION,
        "duration": 216 / 60,  # hours
    },
    "data_upload": {
        "id": 4,
        "consumption": DATA_UPLOAD_CONSUMPTION,
        "duration": 24,  # hours
    },
    "OBC": {
        "id": 5,
        "consumption": OBC_CONSUMPTION,
        "duration": 24,  # hours
    }
}

# Function to calculate the energy consumption of a task
def calculate_consumption(task, time):
    return task["consumption"] * time / 60.0  # Convert from mAh/hour to mAh/minute

# Function to update battery status
def update_battery(battery, consumption, charge):
    new_battery = battery - consumption + charge
    return max(min(new_battery, MAX_BATTERY), MIN_BATTERY)

# Function to make a decision about activating a task
def make_decision(battery, orbit, task):
    # TODO: Implement the reinforcement learning algorithm
    return random.random() > 0.5

# Function to calculate solar charge
def calculate_solar_charge(height, time):
    # Calculate the distance between the satellite and the sun (approximately constant for simplification)
    distance = EARTH_RADIUS + height

    # Use the inverse square law of distance
    irradiance = PERIHELION_IRRADIANCE * (PERIHELION_DISTANCE / distance) ** 2

    # Sigmoid function parameters
    a = 0.5 * irradiance * PANEL_AREA * PANEL_EFFICIENCY  # Maximum power achievable
    b = 0  # Minimum power
    c = 0.01  # Slope of the sigmoid curve
    d = 720  # Midpoint of the sigmoid curve (half the total time)

    # Sigmoid function to model the gradual increase in power
    generated_power = a / (1 + math.exp(-c * (time - d))) + b

    return generated_power

# Function to simulate an orbit
def simulate_orbit(battery, orbit, height, orbit_time):
    decisions = []

    for task in TASKS.values():
        if task["id"] == 3 and orbit == 0:
            # Download data only in the first orbit
            decision = True
        else:
            decision = make_decision(battery, orbit, task)

        if decision:
            consumption = calculate_consumption(task, task["duration"])
            battery -= consumption

        decisions.append(int(decision))

    solar_charge = calculate_solar_charge(height, orbit * orbit_time)
    battery = update_battery(battery, 0, solar_charge)

    return battery, decisions

# Main simulation
battery = initial_battery  # mAh
orbit_height = 500000  # Meters
number_of_orbits = 15
orbit_time = 90.0  # minutes

# List to store the battery status
battery_history = [battery]

# List to store solar charge per orbit
solar_charge_history = []

for orbit in range(number_of_orbits):
    battery, decisions = simulate_orbit(battery, orbit, orbit_height, orbit_time)
    battery_history.append(battery)
    solar_charge_history.append(calculate_solar_charge(orbit_height, orbit * orbit_time))

    # Print orbit information
    print(f"Orbit {orbit + 1}:")
    print(f" - Battery: {battery:.2f} mAh ({battery / MAX_BATTERY * 100:.2f}%)")
    print(f" - Solar Charge: {solar_charge_history[-1]:.2f} mAh")
    print(f" - Decisions: {decisions}")

# Plot battery status
plt.plot(range(number_of_orbits + 1), battery_history)
plt.xlabel("Orbit")
plt.ylabel("Battery (mAh)")
plt.grid(True)
plt.show()

# Plot solar charge
plt.plot(range(number_of_orbits), solar_charge_history)
plt.xlabel("Orbit")
plt.ylabel("Solar Charge (mAh)")
plt.grid(True)
plt.show()

# Calculate total energy consumption
total_consumption = sum(calculate_consumption(task, task["duration"]) for task in TASKS.values())

# Calculate battery life
battery_life = initial_battery / total_consumption

# Calculate energy efficiency
efficiency = (initial_battery - total_consumption) / total_consumption

# Print results
print(f"Total energy consumption: {total_consumption:.2f} mAh")
print(f"Battery life: {battery_life:.2f} orbits")
print(f"Energy efficiency: {efficiency:.2f}%")

