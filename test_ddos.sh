#!/bin/bash

URL="http://localhost:8080"

NUM_REQUESTS=5

DELAY=0

echo "Sending $NUM_REQUESTS requests to $URL with a delay of $DELAY seconds between requests..."

for i in $(seq 1 $NUM_REQUESTS); do
    curl -s -o /dev/null -w "Request $i: HTTP %{http_code}\n" $URL &
    sleep $DELAY
done

wait

echo "All requests completed."
