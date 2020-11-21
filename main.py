from math import cos, log, sin

import ray


@ray.remote
def function():
    for i in range(5 * 10 ** 7):
        sin(cos(log(i + 1)))


if __name__ == "__main__":
    ray.init(address="localhost:6379")

    futures = [function.remote() for _ in range(5)]
    ray.get(futures)

    print("Finished")
