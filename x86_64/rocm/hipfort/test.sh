#! /usr/bin/env sh

OUT=$(mktemp -d)
/opt/rocm/bin/hipfc test.f03 test.cpp -o "$OUT"/test
"$OUT"/test
