#!/bin/sh
# This shell script repeats building scipy with and without an environment variable needed since newest versions of
# the intel C compiler lack support for float128 while glibc expects this.
# The set environment variable, however, precludes compiling C++ code
# So, if the build process fails, it is re-run without the environment variable und continues until failing again etc.
set +e
build="python setup.py config --compiler=intelem --fcompiler=intelem build_clib --compiler=intelem --fcompiler=intelem build_ext --compiler=intelem --fcompiler=intelem -j$(nproc)"

method1() {
	echo Retry: $retry Method: 1
	$build
}

method2() {
	echo Retry: $retry Method: 2
	__INTEL_PRE_CFLAGS="$__INTEL_PRE_CFLAGS -D_Float32=float -D_Float64=double -D_Float128=\"long double\" -D_Float32x=_Float64 -D_Float64x=_Float128" $build
}

# It will end at 'Retry: 5 Method: 2' for scipy 1.1.0 and intel-parallel-studio-xe 2018.3.222
for retry in $(seq 10); do
	method1 && break
	#method2 && break
done
