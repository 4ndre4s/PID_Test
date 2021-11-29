import matplotlib.pyplot as plt


def plot(time_values: object, val1: object, val2: object, val3: object) -> object:
    """
    this function is used to plot the values
    :rtype: object
    """

    #plt.style.use('_mpl-gallery')

    plt.subplot(211)
    plt.plot(time, val3, label="Abweichung")
    plt.xlabel('time (s)')
    plt.ylabel('height (mm)')
    plt.legend()

    plt.subplot(212)
    plt.plot(time, val1, label="PID")
    plt.plot(time, val2, label="Goal")
    plt.xlabel('time (s)')
    plt.ylabel('height (mm)')
    plt.legend()

    plt.show()


class PID (object):
    def __init__(self, k_pid, t_n, t_v):
        self.k_pid = k_pid
        self.t_n = t_n
        self.t_v = t_v

    def control(self, s, delta):

        filler = 0

        if self.t_n == 0:
            filler = 0
        else:
            filler = 1 / self.t_n * s

        function = delta * self.k_pid * (1 + filler + self.t_v * s)

        if function > 1:
            function = 1
        elif function < 0:
            function = 0

        return function


class Simulation(object):
    def __init__(self, duration):
        self.duration = duration

    def simulate(self, entry, pid, controller_max, disturbance) -> object:
        time_, value_, goal_, delta_ = [], [], [], []
        old, outcome = 0, 0
        for i in range(self.duration):
            outcome += pid.control(i, (entry-old)) * controller_max + disturbance
            old = outcome

            time_.append(i)
            value_.append(outcome)
            goal_.append(entry)
            delta_.append(entry-old)

        return time_, value_, goal_, delta_


class Track(object):
    def __init__(self):
        self.outflow = 10


simu = Simulation(120)
result: object = simu.simulate(1000, PID(0.05, 0, 0), 30, -20)
time, value, goal, delta = result[0], result[1], result[2], result[3]

plot(time, value, goal, delta)
