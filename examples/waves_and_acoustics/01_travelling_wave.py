from physena.waves_and_acoustics import formula as fm
import matplotlib.pyplot as plt
import numpy as np

amp = 2
freq = 2
omega = fm.angular_frequency(frequency = freq)
wavelen = 2
wavenum = fm.wave_number(wavelength=wavelen)

start = 0
stop = 10
points = 500

def static_wave_x():
    x = np.linspace(start, stop, num = points)
    t = 0
    y = []

    for i in x:
        wf = fm.wave_function(
                amplitude = amp,
                angular_frequency = omega,
                position = i,
                time = t,
                wave_number= wavenum
                )
        y.append(wf)
    return x, y

def static_wave_t():
    x = 0
    t = np.linspace(start, stop, num = points)
    y = []
    
    for i in t:
        wf = fm.wave_function(
                amplitude = amp,
                angular_frequency = omega,
                position = x,
                time = i,
                wave_number= wavenum
                )
        y.append(wf)
    return t, y

def particle_velocity():
    t = np.linspace(start, stop, num = points)
    x = 0
    y = []
    for i in t:
        v = fm.sinusoidal_particle_velocity(
            amplitude = amp,
            angular_frequency = omega,
            position = 0,
            time = i,
            wave_number= wavenum
        )
        y.append(v)
    return t, y

def particle_acceleration():
    t = np.linspace(start, stop, num = points)
    y = []
    x = 0
    for i in t:
        a = fm.sinusoidal_particle_acceleration(
            amplitude = amp,
            angular_frequency = omega,
            position = x,
            time = i,
            wave_number = wavenum
        )
        y.append(a)
    return t, y

def spatial_curvature():
    x = np.linspace(start, stop, num = points)
    t = 0
    y = []
    for i in x:
        sp = fm.sinusoidal_spatial_curvature(
            amplitude = amp,
            angular_frequency = omega,
            position = i,
            time = t,
            wave_number = wavenum
        )
        y.append(sp)
    return x, y

def plot_demonstration():
    fig, ax = plt.subplots(3,2)

    # Plot 1

    pl1_x, pl1_y = static_wave_x()

    ax[0,0].set_title("Wave Function - x dependant")
    ax[0,0].plot(pl1_x, pl1_y)
    ax[0,0].set_xlabel("Distance (m)")
    ax[0,0].set_ylabel("Amplitude (m)")

    pl2_x, pl2_y = static_wave_t()

    ax[0,1].set_title("Wave Function - t dependant")
    ax[0,1].plot(pl2_x, pl2_y)
    ax[0,1].set_xlabel("Time (s)")
    ax[0,1].set_ylabel("Amplitude (m)")

    # plot 3

    pl3_x, pl3_y = particle_velocity()

    ax[1,0].set_title("Particle Velocity (Sinusoidal)")
    ax[1,0].plot(pl3_x, pl3_y)
    ax[1,0].set_xlabel("Time (s)")
    ax[1,0].set_ylabel("Velocity (m/s)")

    # plot 4

    pl4_x, pl4_y = particle_acceleration()

    ax[1,1].set_title("Particle Acceleration (Sinusoidal)")
    ax[1,1].plot(pl4_x, pl4_y)
    ax[1,1].set_xlabel("Time (s)")
    ax[1,1].set_ylabel("Acceleration (m/s^2)")

    # plot 5

    pl5_x, pl5_y = spatial_curvature()

    ax[2,0].set_title("Spatial Curvature")
    ax[2,0].plot(pl5_x, pl5_y)
    ax[2,0].set_xlabel("Distance (m)")
    ax[2,0].set_ylabel("Spatial curvature (1/m)")

    return plt.show()


plot_demonstration()