class Simulation(object):
    def __init__(self, duration):
        self.duration = duration

    def simulate(self, entry, pid, controller_max, disturbance, number) -> object:
        time_, value_, goal_, delta_, delta_t_ = [], [], [], [], []
        old, outcome, toggle = 0, 0, 0
        
        for i in range(self.duration):
            outcome += pid.control(i, (entry - old)) * controller_max + disturbance
            old = outcome

            time_.append(i)
            value_.append(outcome)
            goal_.append(entry)

            if entry - old == 0:
                toggle = 1

            if toggle == 1:
                delta_.append(entry - old)
                delta_t_.append(i)

        return time_, value_,  goal_, delta_, delta_t_, number
