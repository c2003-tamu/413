#!/bin/sh

make bad
make good

echo "vulnerable, press enter for shell:"
python3 payloads/ret2libc.py > payloads/ret2libcinput
cat payloads/ret2libcinput - | ./bad

echo "safe, same payload, press enter to exit:"
cat payloads/ret2libcinput - | ./good
