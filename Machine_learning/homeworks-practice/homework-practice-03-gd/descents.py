from dataclasses import dataclass
from enum import auto
from enum import Enum
from typing import Dict
from typing import Type

import numpy as np


@dataclass
class LearningRate:
    lambda_: float = 1e-3
    s0: float = 1
    p: float = 0.5

    iteration: int = 0

    def __call__(self):
        """
        Calculate learning rate according to lambda (s0/(s0 + t))^p formula
        """
        self.iteration += 1
        return self.lambda_ * (self.s0 / (self.s0 + self.iteration)) ** self.p


class LossFunction(Enum):
    MSE = auto()
    MAE = auto()
    LogCosh = auto()
    Huber = auto()


class BaseDescent:
    """
    A base class and templates for all functions
    """

    def __init__(self, dimension: int, lambda_: float = 1e-3, loss_function: LossFunction = LossFunction.MSE):
        """
        :param dimension: feature space dimension
        :param lambda_: learning rate parameter
        :param loss_function: optimized loss function
        """
        self.w: np.ndarray = np.random.rand(dimension)
        self.lr: LearningRate = LearningRate(lambda_=lambda_)
        self.loss_function: LossFunction = loss_function

    def step(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        return self.update_weights(self.calc_gradient(x, y))

    def update_weights(self, gradient: np.ndarray) -> np.ndarray:
        """
        Template for update_weights function
        Update weights with respect to gradient
        :param gradient: gradient
        :return: weight difference (w_{k + 1} - w_k): np.ndarray
        """
        pass

    def calc_gradient(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Template for calc_gradient function
        Calculate gradient of loss function with respect to weights
        :param x: features array
        :param y: targets array
        :return: gradient: np.ndarray
        """
        pass

    def calc_loss(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate loss for x and y with our weights
        :param x: features array
        :param y: targets array
        :return: loss: float
        """
        # TODO: implement loss calculation function
        # raise NotImplementedError('BaseDescent calc_loss function not implemented')

        # Вариант 1 - Работает медленее
        # np.sum((x @ w - y) ** 2) / y.shape[0]
        if self.loss_function == LossFunction.MSE:
            sqr = y - x @ self.w
            return (sqr.T @ sqr) / y.shape[0]
        if self.loss_function == LossFunction.LogCosh:
            return np.sum(np.log(np.cosh(y - x @ self.w))) / y.shape[0]
        if self.loss_function == LossFunction.MAE:
            return np.sum(x @ self.w - y) / y.shape[0]
        if self.loss_function == LossFunction.Huber:
            nu = 1
            if np.sum(np.abs(y - self.predict(x))) < nu:  # В данный блок мы вообще не заходим, где-то ошибка
                return np.sum((y - self.predict(x)) ** 2) / 2
            elif np.sum(np.abs(y - self.predict(x))) >= nu:
                return nu * (np.sum(np.abs(y - self.predict(x))) - 1 / 2 * nu)

    def predict(self, x: np.ndarray) -> np.ndarray:
        """
        Calculate predictions for x
        :param x: features array
        :return: prediction: np.ndarray
        """
        # raise NotImplementedError('BaseDescent predict function not implemented')
        # TODO: implement prediction function
        return x @ self.w


class VanillaGradientDescent(BaseDescent):
    """
    Full gradient descent class
    """

    def update_weights(self, gradient: np.ndarray) -> np.ndarray:
        """
        :return: weight difference (w_{k + 1} - w_k): np.ndarray
        """
        # TODO: implement updating weights function
        # raise NotImplementedError('VanillaGradientDescent update_weights function not implemented')
        delta = self.lr() * gradient
        self.w -= delta
        return -delta

    def calc_gradient(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        # TODO: implement calculating gradient function
        # raise NotImplementedError('VanillaGradientDescent calc_gradient function not implemented')
        if self.loss_function == LossFunction.MSE:
            return 2 * x.T @ (x @ self.w - y) / y.shape[0]
        if self.loss_function == LossFunction.LogCosh:
            return np.tanh(x @ self.w - y) @ x / y.shape[0]
        if self.loss_function == LossFunction.MAE:
            signw = np.sign(x.T @ (x @ self.w - y))
            return signw
        if self.loss_function == LossFunction.Huber:
            nu = 1
            if np.sum(np.abs(y - self.predict(x))) < nu:  # В данный блок мы вообще не заходим, где-то ошибка
                return x.T.dot(x @ self.w - y) / y.shape[0]
            elif np.sum(np.abs(y - self.predict(x))) >= nu:
                return nu * np.sign(x.T @ (x @ self.w - y))


class StochasticDescent(VanillaGradientDescent):
    """
    Stochastic gradient descent class
    """

    def __init__(self, dimension: int, lambda_: float = 1e-3, batch_size: int = 50,
                 loss_function: LossFunction = LossFunction.MSE):
        """
        :param batch_size: batch size (int)
        """
        super().__init__(dimension, lambda_, loss_function)
        self.batch_size = batch_size

    def calc_gradient(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        # TODO: implement calculating gradient function
        # raise NotImplementedError('StochasticDescent calc_gradient function not implemented')

        # Вариант 1 - работает быстро, но могут быть повторы
        # inds = np.random.randint(x.shape[0], size=self.batch_size)

        # Вариант 1 - Работает очень медленно при больших выборках
        inds = np.random.choice(np.arange(x.shape[0]), size=self.batch_size, replace=False)
        upd_x = x[inds]
        upd_y = y[inds]
        return super().calc_gradient(upd_x, upd_y)


class MomentumDescent(VanillaGradientDescent):
    """
    Momentum gradient descent class
    """

    def __init__(self, dimension: int, lambda_: float = 1e-3, loss_function: LossFunction = LossFunction.MSE):
        super().__init__(dimension, lambda_, loss_function)
        self.alpha: float = 0.9

        self.h: np.ndarray = np.zeros(dimension)

    def update_weights(self, gradient: np.ndarray) -> np.ndarray:
        """
        :return: weight difference (w_{k + 1} - w_k): np.ndarray
        """
        # TODO: implement updating weights function
        # raise NotImplementedError('MomentumDescent update_weights function not implemented')
        self.h = self.h * self.alpha + self.lr() * gradient
        self.w -= self.h
        return -self.h


class Adam(VanillaGradientDescent):
    """
    Adaptive Moment Estimation gradient descent class
    """

    def __init__(self, dimension: int, lambda_: float = 1e-3, loss_function: LossFunction = LossFunction.MSE):
        super().__init__(dimension, lambda_, loss_function)
        self.eps: float = 1e-8

        self.m: np.ndarray = np.zeros(dimension)
        self.v: np.ndarray = np.zeros(dimension)

        self.beta_1: float = 0.9
        self.beta_2: float = 0.999

        self.iteration: int = 0

    def update_weights(self, gradient: np.ndarray) -> np.ndarray:
        """
        :return: weight difference (w_{k + 1} - w_k): np.ndarray
        """
        # TODO: implement updating weights function
        # raise NotImplementedError('Adagrad update_weights function not implemented')
        self.m = self.beta_1 * self.m + (1 - self.beta_1) * gradient
        self.v = self.beta_2 * self.v + (1 - self.beta_2) * (gradient ** 2)
        self.iteration += 1

        hat_m = self.m / (1 - self.beta_1 ** self.iteration)
        hat_v = self.v / (1 - self.beta_2 ** self.iteration)

        adam_moment = - self.lr() * hat_m / (hat_v ** 0.5 + self.eps)

        self.w += adam_moment
        return adam_moment


class BaseDescentReg(BaseDescent):
    """
    A base class with regularization
    """

    def __init__(self, *args, mu: float = 0, **kwargs):
        """
        :param mu: regularization coefficient (float)
        """
        super().__init__(*args, **kwargs)

        self.mu = mu

    def calc_gradient(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Calculate gradient of loss function and L2 regularization with respect to weights
        """
        l2_gradient: np.ndarray = self.w.copy()  # TODO: replace with L2 gradient calculation
        l2_gradient[-1] = 0
        return super().calc_gradient(x, y) + l2_gradient * self.mu


class VanillaGradientDescentReg(BaseDescentReg, VanillaGradientDescent):
    """
    Full gradient descent with regularization class
    """


class StochasticDescentReg(BaseDescentReg, StochasticDescent):
    """
    Stochastic gradient descent with regularization class
    """


class MomentumDescentReg(BaseDescentReg, MomentumDescent):
    """
    Momentum gradient descent with regularization class
    """


class AdamReg(BaseDescentReg, Adam):
    """
    Adaptive gradient algorithm with regularization class
    """


def get_descent(descent_config: dict) -> BaseDescent:
    descent_name = descent_config.get('descent_name', 'full')
    regularized = descent_config.get('regularized', False)

    descent_mapping: Dict[str, Type[BaseDescent]] = {
        'full': VanillaGradientDescent if not regularized else VanillaGradientDescentReg,
        'stochastic': StochasticDescent if not regularized else StochasticDescentReg,
        'momentum': MomentumDescent if not regularized else MomentumDescentReg,
        'adam': Adam if not regularized else AdamReg
    }

    if descent_name not in descent_mapping:
        raise ValueError(f'Incorrect descent name, use one of these: {descent_mapping.keys()}')

    descent_class = descent_mapping[descent_name]

    return descent_class(**descent_config.get('kwargs', {}))
