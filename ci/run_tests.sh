#!/usr/bin/env bash
# Run tests

# echo path
echo $DIR, `pwd`

# execute specified tests
py.test -x -vv -s `pwd`/tests/