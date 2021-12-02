simu = Simulation(120)

pid1 = PID(0.05, 0, 0)
result1: object = simu.simulate(1000, pid1, 30, -20, 0)

pid2 = PID(0.1, 0, 0)
result2: object = simu.simulate(1000, pid2, 30, -20, 1)

pid3 = PID(0.15, 0, 0)
result3: object = simu.simulate(1000, pid3, 30, -20, 2)

pid4 = PID(20, 0, 0)
result4: object = simu.simulate(1000, pid4, 30, -20, 3)

pid5 = PID(25, 0, 0)
result5: object = simu.simulate(1000, pid5, 30, -20, 4)

graph.add(result1)
graph.add(result2)
graph.add(result3)
graph.add(result4)
graph.add(result5)

graph.show()
