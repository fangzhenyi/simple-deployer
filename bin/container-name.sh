#!/bin/bash

CONTAINER_NAME=${CONTAINER_NAME:-$(whoami)}

echo "${CONTAINER_NAME}" | sed -e 's@[\/_\.]@-@g'
