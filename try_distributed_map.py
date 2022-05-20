import hazelcast
import random

# Start the Hazelcast Client and connect to an already running Hazelcast Cluster
client = hazelcast.HazelcastClient(cluster_name="my-cluster")
# Get the Distributed Map from Cluster.
my_map = client.get_map("my-distributed-map1").blocking()
# Standard Put
for i in range(1000):
    my_map.put(str(i), str(random.randint(0, 500)))

# print("Map size:", my_map.size().result())
client.shutdown()
