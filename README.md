# docker-cpu-webserver
CPU Intensive webserver - intended for benchmarks

## Motivation
Most publicly available webserver/REST containers are very minimalist - Hello World grade.

This came from a need of benchmarking a K8s cluster with a more realistic workload - to simulate business logic and stress the system somewhat, this container will not only serve a page but calculate the square root of a big number in the process.

## How to tweak
Check dfens-app.py for the code. Feel free to change it to be more CPU intensive, allocate more memory or make external API calls.
