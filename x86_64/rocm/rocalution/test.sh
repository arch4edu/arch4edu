#! /usr/bin/env sh

OUT=$(mktemp -d)
/opt/rocm/bin/hipcc -o "$OUT"/test test.cpp -lrocalution -lrocrand -lrocsolver -lrocblas
"$OUT"/test
