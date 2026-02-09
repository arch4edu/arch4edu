startup --output_user_root=${srcdir}/base

build --repository_cache=${srcdir}/repo
build --disk_cache=${srcdir}/cache
build --sandbox_base=${srcdir}/sandbox

build --repo_env=HERMETIC_PYTHON_VERSION=3.14

build --repo_env=BAZEL_COMPILER="/usr/lib/llvm20/bin/clang-20"
build --repo_env=CC="/usr/lib/llvm20/bin/clang-20"
build --repo_env=CXX="/usr/lib/llvm20/bin/clang++"

build --action_env=CLANG_COMPILER_PATH="/usr/lib/llvm20/bin/clang-20"

build --config=avx_posix
build --config=clang
build --config=clang_local
build --config=mkl_open_source_only
build --define=xnn_enable_avxvnniint8=false

build --jobs=12
build --local_resources=cpu=12
build --verbose_failures=true
