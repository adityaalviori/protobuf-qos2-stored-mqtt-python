#!/bin/bash
# protoc -I=/home/alviori/Documents/controller-simulation/model-non-optional --python_out=/home/alviori/Documents/controller-simulation/main/ /home/alviori/Documents/controller-simulation/model-non-optional/common.proto /home/alviori/Documents/controller-simulation/model-non-optional/controller.proto
protoc -I=/$PWD --python_out=$PWD $PWD/data.proto
# cp *_pb2.py ../main
# rm *_pb2.py
