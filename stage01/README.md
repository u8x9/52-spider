## 并发(concurrency)

同一时刻，只能有一条指令执行，但多个线程的对应的指令被快速轮换地执。宏观上看起来，多个线程在同时运行。但微观上只是这个处理器在连续不断地在多个线程之间切换和执行。

**在单处理器和多处理系统中都可以存在。仅靠一个核就可以实现并发。**

## 并行(parallel)

同一时刻，有多条指令在多个处理器上同时执行。并行必须要依赖于多个处理器。不论宏观上还是微观上，多个线程都是在同一时刻一起执行的。

**只能在多处理器系统中存在。如果计算机处理器只有一个核，就不可能实现并行**

## 多线程适用场景

> IO密集型

网络爬虫：在向服务器发起请求之后，有一段时间必须要等服务器的响应返回，这种任务就属于io密集型任务

## 多线路程不适用场景

> 计算密集型/cpu密集型任务：任务的运行一直需要处理器参与

如果开启多线程，一个处理器从一个计算密集型任务切换到另一个计算密集型任务上，处理器依然不会停下来，会始终忙于计算。

## Python 实现多线程

> 模块名：`threading`

```python
import threading
import time

def target(second):
    print(f'Threading {threading.current_thread().name} is running')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is running')
for i in [1,5]:
    t = threading.Thread(target=target, args=[i])
    t.start()
    t.join()
print(f'Threading {threading.current_thread().name} is ended')
```

