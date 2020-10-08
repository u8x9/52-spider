from multiprocessing import Pool
import time

def function(idx):
    print(f'Start Process: {idx}')
    time.sleep(3)
    print('End Process:', idx)

if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply_async(function, args=(i,))

    print('Main Process Started')
    pool.close()
    pool.join()
    print('Main process ended')
