# 多进程

## 进程 process

具有独立功能的程序，对某个数据集合上的一次运行活动。是系统进行资源分配和调度的一个独立单位。

**多进程就是启用多个进程同时运行**

## Python 多进程的优势

由于进程中 *GIL* 的存在，Python中的多线程并不能很好地发挥多核优势。一个进程中的多个线程，同一时刻只能有一个线程运行。

Python 的多进程总体来看是比多线程更有优势。在条件允许的情况下，**尽量使用多进程**。

由于进程是系统进行资源分配和调度的一个独立单位，所以***各个进程之间的数据是无法共享的。***

## Python 多进程的实现

> `multiprocessing` 模块 

`multiprocessing` 的子组件

+ `Process`：进程 

+ `Pipe`：管道

+ `Queue`：队列

+ `Lock`：锁

+ `Semaphore`：信号量

+ `Pool`：进程池

### Process

#### 直接使用 Process 类
在 `multiprocessing` 中，每个进程都用一个Process类来表示

```python
Process([group[, target[, name[,args[,kwargs]]]]])
```

+ `target`：调用对象，可以传入方法的名字

+ `args`：表示被调用对象的位置参数

+ `kwargs`：被调用对象的字典参数

+ `name`：别名，相当于给这个进程取一个名字

+ `group`：分组

```python
import multiprocessing
import time

def process(index):
    time.sleep(index)
    print(f'Process: {index}')

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()
    print(f'CPU number: {multiprocessing.cpu_count()}')
    for p in multiprocessing.active_children():
        print(f'Child process name: {p.name}, id: {p.pid}')
    print('Process Ended')
```

运行结果：

```
Process: 0
CPU number: 8
Child process name: Process-5, id: 2046
Child process name: Process-2, id: 2043
Child process name: Process-4, id: 2045
Child process name: Process-3, id: 2044
Process Ended
Process: 1
Process: 2
Process: 3
Process: 4
```
#### 继承 Process 类

和线程 `Thread` 一样，也可以通过继承的方式创建一个进程类，进程的基本操作在子类的 `run` 方法中实现。

```python
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid}, LoopCount: {count}')


if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.start()
```

#### 守护进程

如果一个进程被设置为守护进程，当父进程结束后，子进程会自动被终止。可以通过设置 `daemon` 属性来控制是否为守护进程。


#### 进程等待

让所有子进程都执行完了，然后再结束，只需要加入 `join` 方法即可。

```python
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid}, LoopCount: {count}')


if __name__ == '__main__':
    processes = []
    for i in range(2, 5):
        p = MyProcess(i)
        processes.append(p)
        p.daemon = True
        p.start()
    for p in processes:
        #p.join()
        p.join(1) # 等待超时时间：1秒
print('Main Process ended')
```

#### 终止进程

终止进程不只有守护进程这一种做法。通过 `terminate` 方法来终止某个子进程，还可以通过 `is_alive` 方法判断进程是否还在运行。

#### 进程互斥锁

#### 信号量

是进程同步过程中一个比较重要的角色。可以*控制临界资源的数量*，实现多个进程同时访问共享资源，限制进程的并发量。

#### 队列

让进程共享数据

#### 管道

可以理解为两个进程之间通信的通道。既可以是单向的，即`half-duplex`：一个进程负责发消息，另一个进程负责收消息；也可以是双向的 `duplex`，即相互收发消息。

默认声明 Pipe 对象是双向管道，如果要创建单向管道，可以在初始化时传入`duplex=False`

#### 进程池

假如有 10000 个任务，每个任务需要启动一个进程来执行，并且一个进程完毕之后，紧接着就要启动下一个进程，同时还需要控制进程的并发数量(不能并发太高，不然cpu处理不过来(如果同时运行的进程能维持在一个最高恒定值，当然利用率是最高的))

进程池可以提供指定数量的进程供用户调用。当有新的请求提交到pool中时，如果池还没有满，就会创建一个新的进程来执行该请求。如果池中进程数已经达到规定最大值，那么该请求就会等待直到池中有进程结束，才会创建新的进程来执行它。

##### map 方法的使用

第1个参数是要启动的进程对应执行的方法；第2个参数是一个可迭代对象，其中每个元素都会被传递给这个执行方法。
