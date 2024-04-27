# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Yf146UNpUWC2d8niwJ4wwTn__VJVoeIr
"""

import numpy as np

def linear_regression(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    Sxy = np.sum((x - x_mean) * (y - y_mean)) / (n - 1)
    Sxx = np.sum((x - x_mean) ** 2) / (n - 1)
    b = Sxy / Sxx
    a = y_mean - b * x_mean
    return a, b

def standard_deviation(y, y_pred):
    return np.sqrt(np.sum((y - y_pred) ** 2) / (len(y) - 1))

def std_error_estimation(sy, x, x_mean):
    return sy * np.sqrt(1 - 1 / len(x) - ((x - x_mean) ** 2).sum() / ((x - x_mean) ** 2).sum())

def coefficient_of_determination(y, y_pred):
    Syy = np.sum((y - np.mean(y)) ** 2)
    S_res = np.sum((y - y_pred) ** 2)
    return 1 - (S_res / Syy)

def correlation_coefficient(x, y):
    Sxy = np.sum((x - np.mean(x)) * (y - np.mean(y)))
    Sxx = np.sum((x - np.mean(x)) ** 2)
    Syy = np.sum((y - np.mean(y)) ** 2)
    return Sxy / np.sqrt(Sxx * Syy)
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.1, 0.3, 0.9, 1.7, 2.8, 4.5, 6.9])

a, b = linear_regression(x, y)

y_pred = a + b * x

sy = standard_deviation(y, y_pred)


s_Ty_x = std_error_estimation(sy, x, np.mean(x))

r_squared = coefficient_of_determination(y, y_pred)

r = correlation_coefficient(x, y)
print("Desviación estándar (sy):", sy)
print("Error estándar de la estimación (sΤy|x):", s_Ty_x)
print("Coeficiente de determinación (r²):", r_squared)
print("Coeficiente de correlación (r):", r)

