#100명의 신장, 체중, 나이 3개의 난수를 2차원 배열에 저장하고 각각의 평균값과 중앙값 구하기
import numpy as np

players = np.zeros( (100, 3) )
players[:, 0] = 10 * np.random.randn(100) + 175
players[:, 1] = 10 * np.random.randn(100) + 70
players[:, 2] = np.floor(10 * np.random.randn(100)) + 22

heights = players[:, 0]
print("신장 평균값 :", np.mean(heights))
print("신장 중앙값 :", np.median(heights))

weights = players[:, 1]
print("체중 평균값 :", np.mean(weights))
print("체중 중앙값 :", np.median(weights))

ages = players[:, 2]
print("나이 평균값 :", np.mean(ages))
print("나이 중앙값 :", np.median(ages))