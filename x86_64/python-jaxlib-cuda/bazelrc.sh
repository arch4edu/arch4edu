startup --output_user_root=${srcdir}/base

build --repository_cache=${srcdir}/repo
build --disk_cache=${srcdir}/cache
build --sandbox_base=${srcdir}/sandbox

build --repo_env=HERMETIC_PYTHON_VERSION=3.14

build --repo_env=LOCAL_CUDA_PATH="${srcdir}/local-cuda"
build --repo_env=LOCAL_CUDNN_PATH="${srcdir}/local-cudnn"
build --repo_env=LOCAL_NCCL_PATH="${srcdir}/local-nccl"
#
# TODO(@daskol): This variables controls `@rules_ml_toolchain` in theory.
# build:cuda --repo_env=LOCAL_CUDA_PATH="/opt/cuda/targets/x86_64-linux"
# build:cuda --repo_env=LOCAL_CUDNN_PATH="/usr/include"
# build:cuda --repo_env=LOCAL_NCCL_PATH="/usr/include"
# build:cuda --repo_env=LOCAL_NVSHMEM_PATH="/usr/include"
#
# NOTE Adjust HERMETIC_CUDA_COMPUTE_CAPABILITIES for actual devices.
# https://github.com/google-ml-infra/rules_ml_toolchain/tree/main/gpu
build --repo_env=HERMETIC_CUDA_COMPUTE_CAPABILITIES="sm_80,sm_86,sm_87,sm_90,sm_100,sm_103"

build --repo_env=BAZEL_COMPILER="/usr/lib/llvm20/bin/clang-20"
build --repo_env=CC="/usr/lib/llvm20/bin/clang-20"
build --repo_env=CXX="/usr/lib/llvm20/bin/clang++"

build --action_env=CLANG_COMPILER_PATH="/usr/lib/llvm20/bin/clang-20"
build --action_env=CLANG_CUDA_COMPILER_PATH="/usr/lib/llvm20/bin/clang-20"
build --action_env=CUDAHOSTCXX="/usr/lib/llvm20/bin/clang++"

build --config=avx_posix
build --config=build_cuda_with_nvcc
build --config=clang
build --config=cuda13
build --config=cuda_clang_local
build --config=cuda_libraries_from_stubs
build --config=mkl_open_source_only
build --define=xnn_enable_avxvnniint8=false

build --jobs=4
build --local_resources=cpu=4
build --verbose_failures=true
