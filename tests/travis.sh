#!/bin/sh

set -ev

# Run all tests
./run_tests.py --coverage --with-mpi --verbose
