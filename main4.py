import os
from math import cos, log, sin

import ray


@ray.remote
def function():
    for i in range(5 * 10 ** 7):
        sin(cos(log(i + 1)))


if __name__ == "__main__":
    if "RAY_HEAD_SERVICE_HOST" not in os.environ or os.environ["RAY_HEAD_SERVICE_HOST"] == "":
        raise ValueError(
            "RAY_HEAD_SERVICE_HOST environment variable empty." "Is there a ray cluster running?"
        )

    redis_host = os.environ["RAY_HEAD_SERVICE_HOST"]
    ray.init(address=redis_host + ":6379")

    futures = [function.remote() for _ in range(36)]
    print("before get futures", flush=True)
    ray.get(futures)
    print("after get futures", flush=True)

    print("Finished", flush=True)
