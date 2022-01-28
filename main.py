from calculator import Calculator
import time
import tracemalloc
import random


def timer(start_count,finish_count):
    tracemalloc.start()
    startTime = time.time()
    calculator = Calculator()

    res = [1,2,3]
    for i in range(start_count,finish_count):
        res.append(random.randint(1,100))
    print(len(res))
    #calculator.boat_brute_force(res)
    calculator.monte_carlo(res)

    #TIMING STUFF
    timeConsupmtion = (time.time() - startTime) * 1000
    memoryConsumption = tracemalloc.get_tracemalloc_memory()
    tracemalloc.stop()

    print("Spotreba pameti: " + str(memoryConsumption/1024) + " KBytes")
    print("Spotreba casu: " + str(timeConsupmtion) + " sec");


for i in range(1,100):
    timer(3,i)
