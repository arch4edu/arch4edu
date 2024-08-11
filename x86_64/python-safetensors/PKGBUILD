# Maintainer: Andrea Manenti <andrea [dot] manenti [at] yahoo [dot] com>
# Contributor: Henry-ZHR <henry-zhr@qq.com>
pkgname=python-safetensors
pkgver=0.4.4
pkgrel=1
pkgdesc='Simple, safe way to store and distribute tensors'
arch=('x86_64')
url='https://github.com/huggingface/safetensors'
license=('Apache')
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
              'python-h5py')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('56d755561054ab24d3bc36e3715b9308901891170e69fc894db70284ba11b730')

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
