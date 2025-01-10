# Maintainer: envolution
# Contributor: Andrea Manenti <andrea [dot] manenti [at] yahoo [dot] com>
# Contributor: Henry-ZHR <henry-zhr@qq.com>
# shellcheck shell=bash disable=SC2034,SC2154
pkgname=python-safetensors
pkgver=0.5.2
pkgrel=1
pkgdesc='Simple, safe way to store and distribute tensors'
arch=('x86_64')
url='https://github.com/huggingface/safetensors'
license=('Apache-2.0')
depends=('python')
makedepends=('python-build'
  'python-installer'
  'python-maturin'
  'python-wheel'
  'python-setuptools-rust')
optdepends=('python-jax'
  'python-flax'
  'python-jaxlib'
  'python-numpy'
  'python-paddlepaddle'
  'python-tensorflow'
  'python-pytorch')
checkdepends=('python-pytorch'
  'python-numpy'
  'python-tensorflow'
  'python-jax'
  'python-flax'
  'python-jaxlib'
  # 'python-paddlepaddle'
  'python-black'
  'python-isort'
  'flake8'
  'python-click'
  'python-huggingface-hub'
  'python-pytest'
  'python-pytest-benchmark'
  'python-hypothesis'
  'python-h5py')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('f2d6aeacb909f14925508abd7842cd3da72cd45d79d4aec7d278c66af1afbf2f')

prepare() {
  mkdir -p "safetensors-${pkgver}/.git"
}

build() {
  cd "safetensors-${pkgver}/bindings/python"

  export RUSTUP_TOOLCHAIN=stable
  python -m build --wheel --no-isolation
}

check() {
  cd "safetensors-${pkgver}/bindings/python"
  local python_version=$(python -V | sed -e 's/Python \([0-9]\.[0-9]\+\)\..*/\1/')
  mkdir "${PWD}/test_build"
  python -m installer --destdir="${PWD}/test_build" dist/*.whl
  # Disable temporarily paddlepaddle and tensorflow tests
  PYTHONPATH="${PWD}/test_build/usr/lib/python${python_version}/site-packages" pytest tests/ \
    --ignore=tests/test_paddle_comparison.py \
    --ignore=tests/test_tf_comparison.py
}

package() {
  cd "safetensors-${pkgver}/bindings/python"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
