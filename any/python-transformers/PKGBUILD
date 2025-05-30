# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
# Contributor: Filip Graliński <filipg@amu.edu.pl>

pkgname=python-transformers
_pkgname=${pkgname#python-}
pkgver=4.52.4
pkgrel=1
pkgdesc="State-of-the-art Natural Language Processing for Jax, PyTorch and TensorFlow"
arch=('any')
url='https://github.com/huggingface/transformers'
license=('Apache-2.0')
depends=(
  'python-filelock'
  'python-huggingface-hub>=1:0.30.0'
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
  'python-keras: Support for models in Keras 3'
  'python-onnxconverter-common: TensorFlow support'
  'python-pytorch: PyTorch support'
  'python-tensorflow: TensorFlow support'
  'python-tf-keras: Support for models in Keras 2 (e.g. BART)'
  'python-tf2onnx: TensorFlow support'
  'python-hf-xet: xethub support'
)
source=(
  "python-transformers-$pkgver.tar.gz"::"https://github.com/huggingface/transformers/archive/refs/tags/v$pkgver.tar.gz"
)
sha256sums=('2d6303a82681a138993b1d46f4e88d42f6f3c7944079eaa9812487cc1474512d')

prepare() {
  cd "transformers-$pkgver"
  sed -Ei 's/"tokenizers>=.*?"/"tokenizers"/' setup.py
  python setup.py deps_table_update
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
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  python -m installer --compile-bytecode=1 --destdir=$pkgdir \
    $srcdir/$_pkgname-$pkgver/dist/transformers-$pkgver-*-*.whl
}
