import multiprocessing
import time

def process():
    print('Starting')
    time.sleep(5)
    print('Finished')

if __name__ == '__main__':
    p = multiprocessing.Process(target=process)
    print('Before:', p, p.is_alive())

    p.start()
    print('During:', p, p.is_alive())
    
    p.terminate()
    print('Terminate:', p, p.is_alive())

    p.join()
    print('Joined:', p, p.is_alive())

# -- 运行结果 --
# Before: <Process name='Process-1' parent=3447 initial> False
# During: <Process name='Process-1' pid=3448 parent=3447 started> True
# Terminate: <Process name='Process-1' pid=3448 parent=3447 started> True
# Joined: <Process name='Process-1' pid=3448 parent=3447 stopped exitcode=-SIGTERM> False
