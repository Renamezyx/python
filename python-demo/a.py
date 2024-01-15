import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

start_time = time.time()

result = fibonacci(40)

end_time = time.time()

print(f"Result: {result}")
print(f"Time taken with loop: {end_time - start_time} seconds")


import threading
import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calculate_fibonacci():
    global result
    result = fibonacci(40)

start_time = time.time()

# 创建两个线程
thread1 = threading.Thread(target=calculate_fibonacci)
thread2 = threading.Thread(target=calculate_fibonacci)

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

end_time = time.time()

print(f"Result: {result}")
print(f"Time taken with multithreading: {end_time - start_time} seconds")
