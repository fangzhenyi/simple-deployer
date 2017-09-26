#!/bin/bash

for cmd in $*
do
  if [ -f ./bin/subcommands/${cmd} ]
  then
    ./bin/subcommands/${cmd} || exit $?
  else
    echo \'${cmd}\' is not a valid subcommand.
    echo
    echo Available subcommands:
    ls -1 ./bin/subcommands/
    echo
    exit 1
  fi
done
