#!/usr/bin/env bash

mkdir -p data

data_dir="$PWD/data"

echo "Directory $data_dir created:"

for i in $(seq 1 $1); do
    filename="${data_dir}/file${i}.txt"
    base64 /dev/urandom | head -c $(shuf -i 256-512 -n 1)  > $filename;
    echo -ne "\tFile $filename created\r"
done

echo -e "\n"