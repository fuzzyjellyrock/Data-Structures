from queues import QueueClass

if __name__ == "__main__":
    q = QueueClass()
    q.offer(2)
    q.offer(3)
    q.offer('a')
    q.print()
    q.poll()
    q.print()
    print(q.peek())
