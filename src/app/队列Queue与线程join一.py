import threading
from queue import Queue
from threading import Thread
from time import sleep


def getTicket(ticketList: list):
    while True:
        sleep(1)
        if len(ticketList) == 0:
            print(threading.currentThread().name, "子执行任务完成！")
            break
        ticket = ticketList.pop()
        print('开始执行买票行动====> %d' % ticket)
        pass


if __name__ == '__main__':
    tickets = []
    for ticket in range(1000):
        tickets.append(ticket)

    threads = []
    for te in range(50):
        t = Thread(target=getTicket, args=(tickets,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("所有任务执行完成！", threading.currentThread().name)
