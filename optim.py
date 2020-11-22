from math import cos, log, sin

from hyperopt import fmin, hp, tpe
from hyperopt.mongoexp import MongoTrials


def to_optimize(x):
    for i in range(1 * 10 ** 7):
        sin(cos(log(i + 1)))

    return (x - 5) ** 2


trials = MongoTrials("mongo://mongo:27017/hyperopt_db/jobs", exp_key="exp1")
print("after trials")
best = fmin(
    fn=to_optimize, space=hp.uniform("x", 0, 10), algo=tpe.suggest, max_evals=20, trials=trials
)
print(best)
