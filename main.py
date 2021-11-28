import matplotlib.pyplot as plt


def plot(x_values: object, y_values: object):
    """
    this function is used to plot the values
    :rtype: object
    """

    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()

    ax.plot(x_values, y_values)
    plt.show()


class PID (object):
    def __init__(self, k_pid, t_n, t_v):
        self.k_pid = k_pid
        self.t_n = t_n
        self.t_v = t_v

    def control(self, s):
        if s == 0:
            s = 1
        if self.t_n == 0:
            self.t_n = 1
        if self.t_v == 0:
            self.t_v = 1

        function = self.k_pid * (1 + 1 / self.t_n * s + self.t_v * s)
        return function


class Simulation(object):
    def __init__(self, duration):
        self.duration = duration

    def simulate(self, entry, pid, disturbance):
        time = []
        values = []
        old = 0
        for i in range(self.duration):
            outcome = (entry-old) * pid.control(i) + disturbance * i
            old = outcome

            time.append(i)
            values.append(outcome)

        return time, values


class Track(object):
    def __init__(self):
        self.outflow = 10


simu = Simulation(1000)
result = simu.simulate(100, PID(1, 0, 0), 20)
x, y = result[0], result[1]

plot(x, y)
