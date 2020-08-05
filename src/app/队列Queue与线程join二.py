import threading
import time
from queue import Queue
from threading import Thread


def excute(q: Queue):
    while True:
        time.sleep(1)
        print('正在执行任务', q.get())
        q.task_done()
    pass


if __name__ == '__main__':
    tickQueue = Queue(1000)
    for task in range(1000):
        tickQueue.put(task)
    for t in range(100):
        Thread(target=excute, args=(tickQueue,)).start()
    tickQueue.join()
    print('所有任务执行完毕', threading.currentThread().name)
