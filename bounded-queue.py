import hazelcast
import threading
import time

client = hazelcast.HazelcastClient(cluster_name="my-cluster")

queue = client.get_queue("my-queue").blocking()
max_size = 100
to_consume = 100


def produce():
    i = 0
    while queue.size() <= max_size and i <= 100:
        queue.offer("value-" + str(i))
        # print("putting value", i)
        i += 1
    # print('STOP', queue.size())


def consume():
    global to_consume
    while to_consume >= 0:
        if queue.size() > 0:
            head = queue.take()
            # print("Consuming {} ".format(head), threading.current_thread().ident)
            to_consume -= 1


producer_thread = threading.Thread(target=produce)
consumer_thread = threading.Thread(target=consume)
#consumer_thread2 = threading.Thread(target=consume)

producer_thread.start()
consumer_thread.start()
#consumer_thread2.start()

producer_thread.join()
consumer_thread.join()
#consumer_thread2.join()

client.shutdown()
