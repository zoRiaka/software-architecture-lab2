# software-architecture-lab2
Second laboratory assignment for UCU Software Architecture course

Resuls and conclusions are stored at the results.pdf

## Instructions:

To create and run my cluster I used docker:

```
docker network create hazelcast-network
docker run     -it     --network hazelcast-network     --rm     -e HZ_CLUSTERNAME=my-cluster     -p 5701:5701 hazelcast/hazelcast:5.0.3
```

To create two more nodes execute the following commands from separate terminal windows:

```
docker run     --name my-second-member --network hazelcast-network     -e HZ_CLUSTERNAME=my-cluster     -p 5702:5701 hazelcast/hazelcast:5.0.3

docker run     --name my-third-member --network hazelcast-network     -e HZ_CLUSTERNAME=my-cluster     -p 5703:5701 hazelcast/hazelcast:5.0.3
```

And lastly to open management center execute:

```
docker run     --network hazelcast-network     -p 8080:8080 hazelcast/management-center:5.0
```
