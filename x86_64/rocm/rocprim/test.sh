#! /usr/bin/env sh

OUT=$(mktemp -d)
# rocPRIM uses C++14 extensions but hipcc uses C++11 by default
/opt/rocm/bin/hipcc -std=gnu++14 -o "$OUT"/test test.cpp
"$OUT"/test
