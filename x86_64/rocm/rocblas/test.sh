#! /usr/bin/env sh

OUT=$(mktemp -d)
/opt/rocm/bin/hipcc -o "$OUT"/test test.cpp -lrocblas
"$OUT"/test
