"""
    File Structure

        -Core

    Looking up Functions

        To find a function, use ctrl + f, and search for "def {function_name}", where the function name is defined below -> function -- "function_name"

    Functions

        - Angular Frequency -- "angular_frequency"
        - Frequency -- "frequency" --- Needs to be written
        - Period -- "period"
        - Sinusoidal Particle Acceleration -- "sinusoidal_particle_acceleration"
        - Sinusoidal Particle Velocity -- "sinusoidal_particle_velocity"
        - Sinusoidal Spatial Curvature -- "sinusoidal_spatial_curvature"
        - Wave Function -- "wave_function"
        - Wavelength -- "wavelength"
        - Wave Number -- "wave_number"
        - Wave Speed -- "wave_speed"
"""

import numpy as np

####################################################
###                                              ###
###                     CORE                     ###
###                                              ###
####################################################

def angular_frequency(*,frequency = None, period = None):
    if frequency is not None and period is not None:
        raise ValueError("Provide either frequency or period.")

    if frequency is not None:
        return 2 * np.pi * frequency

    if period is not None:
        return (2 * np.pi) / period

    raise ValueError("Provide a relevant value.")

def frequency(*, angular_frequency = None, period = None):
    if angular_frequency is not None and period is not None:
        raise ValueError("Provide either angular frequency or period.")
    if angular_frequency is not None:
        return angular_frequency / (2 * np.pi)
    if period is not None:
        return 1 / period
    raise ValueError("Provide a relevant value.")

def period(*, frequency = None, angular_frequency = None):
    if frequency is not None and angular_frequency is not None:
        raise ValueError("Provide either frequency or angular frequency")

    if frequency is not None:
        return 1 / frequency

    if angular_frequency is not None:
        return 2 * np.pi / angular_frequency

    raise ValueError("Provide a value")

def wavelength(*, wave_speed = None, frequency = None, period = None):
    if frequency is not None and period is not None:
        raise ValueError("Provide either frequency or period")

    if wave_speed is not None and frequency is not None:
        return wave_speed/frequency

    if wave_speed is not None and period is not None:
        return wave_speed * period

    raise ValueError("Provide relevant values")

def wave_number(*, wavelength = None):
    if wavelength is not None:
        return 2 * np.pi / wavelength
    raise ValueError("Provide relevant values")

def wave_speed(*, wavelength = None, frequency = None, period = None):
    if frequency is not None and period is not None:
        raise ValueError("Provide either frequency or period")

    if wavelength is not None and frequency is not None:
        return wavelength * frequency

    if wavelength is not None and period is not None:
        return wavelength/period

    raise ValueError("Provide relevant values")

####################################################
###                                              ###
###               SINUSOIDAL WAVES               ###
###                                              ###
####################################################

def sinusoidal_particle_acceleration(*, amplitude = None, angular_frequency = None, position = None, time = None, wave_number = None):
    if angular_frequency is not None:
        return - (angular_frequency**2) * amplitude * np.cos(wave_number * position - angular_frequency * time)
    raise ValueError("Provide relevant values")

def sinusoidal_particle_velocity(*, amplitude = None, angular_frequency = None, position = None, time = None, wave_number = None):
    if angular_frequency is not None:
        return angular_frequency * amplitude * np.sin(wave_number * position - angular_frequency * time)
    raise ValueError("Provide relevant values")

def sinusoidal_spatial_curvature(*, amplitude = None, angular_frequency = None, position = None, time = None, wave_number = None):
    if angular_frequency is not None:
        return - (wave_number**2) * amplitude * np.cos(wave_number * position - angular_frequency * time)
    raise ValueError("Provide relevant values")

def wave_function(*, amplitude = None, angular_frequency = None, position = None, time = None, wave_number = None):
    if angular_frequency is not None:
        return amplitude * np.cos(wave_number * position - angular_frequency * time)
    raise ValueError("Provide relevant values")