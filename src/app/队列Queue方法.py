import queue
import threading
import time

num = 0
exi_flag = False

def addTask(q: queue.Queue):
    while True:
        global num
        if num >= 5:
            global exi_flag
            exi_flag = True
            break
        time.sleep(1)
        q.put(item='task%d' % num)
        num += 1

def test():
    q = queue.Queue(10)
    print('开始添加任务上班了！')
    # 开启模拟添加任务到队列
    t = threading.Thread(target=addTask, args=(q,))
    t.start()

    while True:
        if exi_flag:
            print("所有任务执行完成，开始下班！")
            break
        print(q.get())
        pass

if __name__ == '__main__':
    test()
