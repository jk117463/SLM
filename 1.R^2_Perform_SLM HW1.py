import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import time

sizes = np.arange(10, 210, 10)
# print(sizes)
reps = 10000


def sim_r_squared(n):
    x = np.random.randn(n).reshape(-1, 1)
    y = 1 + x.reshape(-1) + np.random.randn(n)
    # print(x)
    # print(y)
    # print('before model')
    # print(n)
    model = LinearRegression().fit(x, y)
    # print('after model')
    return model.score(x, y)


r_squared_q95 = []
r_squared_q5 = []
r_squared_mean = []

start_time = time.time()

for i in range(len(sizes)):
    result = []
    #result = np.repeat(sim_r_squared(sizes[i]), reps)
    for j in range(reps):
        result.append(sim_r_squared(sizes[i]))
    # print(np.mean(result))
    r_squared_mean.append(np.mean(result))
    r_squared_q95.append(np.quantile(result,0.95))
    r_squared_q5.append(np.quantile(result,0.05))
    #print(result)
    #print(r_squared_mean[i])
exec_time = time.time() - start_time

# print(r_squared_mean)
# print(r_squared_q5)
# print(r_squared_q95)


print("Execution time: " + str(exec_time))
plt.scatter(sizes, r_squared_mean)
plt.plot(sizes, r_squared_q5)
plt.plot(sizes, r_squared_q95)
plt.ylim(min(r_squared_q5), max(r_squared_q95))
plt.xlabel("sample size")
plt.ylabel("R^2")
plt.show()

