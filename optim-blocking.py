
import hazelcast

client = hazelcast.HazelcastClient(cluster_name="my-cluster")
distributed_map = client.get_map("my-distributed-map").blocking()

key = "1"
distributed_map.put(key, 0)

print("Starting")

for i in range(1000):
    while True:
        value = distributed_map.get(key)
        new_value = value + 1
        if distributed_map.replace_if_same(key, value, new_value):
            # distributed_map.put(key, new_value)
            break

print("Finished! Result =", distributed_map.get(key))

client.shutdown()