# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
# Contributor: Filip Graliński <filipg@amu.edu.pl>

pkgname=python-transformers
_pkgname=${pkgname#python-}
pkgver=4.42.4
pkgrel=1
pkgdesc="State-of-the-art Natural Language Processing for Jax, PyTorch and TensorFlow"
arch=('any')
url='https://github.com/huggingface/transformers'
license=('Apache')
depends=(
  'python-filelock'
  'python-huggingface-hub'
  'python-numpy'
  'python-packaging'
  'python-regex'
  'python-requests'
  'python-safetensors>=0.4.1'
  'python-tokenizers>=0.19'
  'python-tqdm'
  'python-yaml'
)
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
optdepends=(
  'python-bitsandbytes: 8-bit support for PyTorch'
  'python-flax: JAX support'
  'python-onnxconverter-common: TensorFlow support'
  'python-pytorch: PyTorch support'
  'python-tensorflow: TensorFlow support'
  'python-tf2onnx: TensorFlow support'
)
source=(
  "python-transformers-$pkgver.tar.gz"::"https://github.com/huggingface/transformers/archive/refs/tags/v$pkgver.tar.gz"
)
sha256sums=('14e656c9dfcac828b79a21274219af9cfa7999f64c5f7d997f68857d408738ba')

prepare() {
    sed -i 's/"numpy>=1.17,<2.0",/"numpy",/' transformers-$pkgver/setup.py
    sed -i '/"numpy",/d' \
        transformers-$pkgver/src/transformers/dependency_versions_check.py
}

build() {
  python -m build -nw "transformers-$pkgver"
}

check() {
  cd "transformers-$pkgver"
  PYTHONPATH=$PWD/src python -c 'import transformers'
}

package() {
  cd "transformers-$pkgver"
  python -m installer \
    --compile-bytecode 1 \
    --destdir $pkgdir \
    $srcdir/$_pkgname-$pkgver/dist/transformers-$pkgver-*-*.whl
}
