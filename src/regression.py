# -*- coding: utf-8 -*-
import numpy as np


class LineFunction(object):
    def __init__(self, b0, b1):
        self.b0 = b0
        self.b1 = b1
        self.SST = None
        self.SSE = None
        self.SSR = None
        # coefficient of determination
        self.r2 = None

    def __call__(self, x):
        return self.b0 + self.b1*x

    def summary(self):
        print("line: y_hat={b0} + {b1}x\nb0:{b0}\nb1:{b1}\nSST:{sst}\nSSR:{ssr}\nr2:{r2}".format(
            b0=self.b0,
            b1=self.b1,
            r2=self.r2,
            ssr=self.SSR,
            sst=self.SST,
            ))


def regression(independent_var, dependent_var):
    """ Calculate line parameters b0(Y intersect) and b1(line slope) based on data.
    
    return: function
    """
    indep_mean = independent_var.mean()
    dep_mean = dependent_var.mean()

    # calc deviation
    indep_dev = independent_var - indep_mean
    error = dependent_var - dep_mean
    dev_prod = indep_dev * error
    indep_sqrt = indep_dev * indep_dev

    squered_errors = error**2
    SST = squered_errors.sum()

    # y_hat = b0 +b1*x
    # where bo is value of Y axis intersection
    # and b1 is the slope of the regration line

    b1 = dev_prod.sum()/indep_sqrt.sum()
    b0 = dep_mean - b1*indep_mean
    # return {"b1": b1, "b0": b0}
    # define model
    model = LineFunction(b0, b1)

    # estimate model
    vmodel = np.vectorize(model)
    y_hat = vmodel(independent_var)

    regression_error = dependent_var - y_hat
    regression_error_squared = regression_error**2
    SSE = regression_error_squared.sum()

    # set model estimators
    model.SST = SST
    model.SSE = SSE
    model.SSR = SST - SSE
    model.r2 = model.SSR / SST
    return model


if __name__ == "__main__":
    data = np.array([
    [34, 5],
    [108, 17],
    [64, 11],
    [88, 8],
    [99, 14],
    [51, 5],
    ], dtype=np.float64)


    res = regression(data[:, 0], data[:, 1])
    res.summary()
    # print(res(34))
