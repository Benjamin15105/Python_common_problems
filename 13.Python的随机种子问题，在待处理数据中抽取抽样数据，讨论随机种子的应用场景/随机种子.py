import random

random.seed(42)  # 设置随机数种子
print(random.randint(1, 100))  # 输出固定，例如：81
print(random.random())         # 输出固定，例如：0.6394267984578837

# 再次设置相同种子，结果相同
random.seed(42)
print(random.randint(1, 100))  # 输出仍然是：81
print(random.random())         # 输出仍然是：0.6394267984578837
