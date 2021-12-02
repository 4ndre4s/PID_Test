import matplotlib.pyplot as plt

class graph(object):

    def addValues(values: list) -> object:
        time_axis = values[0]
        siumalated_value = values[1]
        target_value = values[2]
        target_value_delta = values[3]
        time_axis_delta = value[4]
        simulation_counter = values[5]

        plt.subplot(211)
        plt.plot(time_axis_delta, target_value_delta, label="Abweichung " + str(simulation_counter))

        plt.subplot(212)

        plt.plot(time_axis, target_value, label="Goal " + str(simulation_counter))
        plt.plot(time_axis, siumalated_value, label="PID " + str(simulation_counter))


    def setupMetadata():
        plt.subplot(211)
        plt.xlabel('time (s)')
        plt.ylabel('height (mm)')
        plt.legend()
        plt.subplot(212)
        plt.xlabel('time (s)')
        plt.ylabel('height (mm)')
        plt.legend()
        plt.show()

