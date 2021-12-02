import matplotlib.pyplot as plt

class graph(object):

    def add(values: list) -> object:
        plt.subplot(211)
        plt.plot(values[4], values[3], label="Abweichung " + str(values[5]))

        plt.subplot(212)
        plt.plot(values[0], values[2], label="Goal " + str(values[5]))
        plt.plot(values[0], values[1], label="PID " + str(values[5]))


    def show():
        plt.subplot(211)
        plt.xlabel('time (s)')
        plt.ylabel('height (mm)')
        plt.legend()
        plt.subplot(212)
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

    def simulate(self, entry, pid, controller_max, disturbance, number) -> object:
        time_, value_, goal_, delta_, delta_t_ = [], [], [], [], []
        old, outcome, toggle = 0, 0, 0
        for i in range(self.duration):
            outcome += pid.control(i, (entry-old)) * controller_max + disturbance
            old = outcome

            time_.append(i)
            value_.append(outcome)
            goal_.append(entry)

            if entry-old == 0:
                toggle = 1
            if toggle == 1:
                delta_.append(entry-old)
                delta_t_.append(i)

        return time_, value_,  goal_, delta_, delta_t_, number


class Track(object):
    def __init__(self):
        self.outflow = 10


simu = Simulation(120)

result1: object = simu.simulate(1000, PID(0.05, 0, 0), 30, -20, 0)
result2: object = simu.simulate(1000, PID(0.1, 0, 0), 30, -20, 1)
result3: object = simu.simulate(1000, PID(0.15, 0, 0), 30, -20, 2)
result4: object = simu.simulate(1000, PID(20, 0, 0), 30, -20, 3)
result5: object = simu.simulate(1000, PID(25, 0, 0), 30, -20, 4)

graph.add(result1)
graph.add(result2)
graph.add(result3)
graph.add(result4)
graph.add(result5)

graph.show()
