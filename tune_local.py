from ray import tune

# from ray.tune.schedulers import ASHAScheduler

from math import sin, log, cos


def to_optimize(config):
    alpha, beta = config["alpha"], config["beta"]

    for i in range(10 ** 7):
        sin(cos(log(i + 1)))

    toto = 2.5 + (alpha - 3) ** 2 + (beta - 5) ** 2
    tune.report(mean_accudracy=toto)


from hyperopt import hp
from ray.tune.suggest.hyperopt import HyperOptSearch

space = {
    "alpha": hp.uniform("alpha", 1, 5),
    "beta": hp.uniform("beta", 2, 6),
}

hyperopt_search = HyperOptSearch(space, metric="mean_accudracy", mode="min")

analysis = tune.run(to_optimize, num_samples=100, search_alg=hyperopt_search, verbose=0)

print("Best config: ", analysis.get_best_config(metric="mean_accudracy", mode="min"))

