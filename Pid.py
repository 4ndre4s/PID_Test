class PID (object):
    def __init__(self, k_pid, t_n, t_v):
        self.k_pid = k_pid
        self.t_n = t_n
        self.t_v = t_v

    def calculatePid(self, s, delta):

        filler = 0

        if self.t_n != 0:
            filler = 1 / self.t_n * s          

        function = delta * self.k_pid * (1 + filler + self.t_v * s)

        if function > 1:
            function = 1
        elif function < 0:
            function = 0

        return function

