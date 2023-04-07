import pandas as pd
import numpy as np


chat_id = 294776608 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    mu = np.log(391) 
    sigma = np.sqrt(np.log(1 + (b / 391) ** 2))
    log_x = np.log(x)
    log_x_mean = log_x.mean()
    a_estimate = np.exp(log_x_mean - mu) 
    return a_estimate
