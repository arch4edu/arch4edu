# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
# Contributor: Filip Graliński <filipg@amu.edu.pl>

pkgname=python-transformers
_pkgname=${pkgname#python-}
pkgver=5.9.0
pkgrel=1
pkgdesc='State-of-the-art pretrained models for inference and training'
arch=('any')
url='https://github.com/huggingface/transformers'
license=('Apache-2.0')
depends=(
  'python-huggingface-hub>=1:1.3.0'
  'python-numpy'
  'python-packaging'
  'python-regex'
  'python-safetensors'
  'python-tokenizers'
  'python-tqdm'
  'python-typer'
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
sha256sums=('aea88fd01ea5344d4e1a8692ee029258de8040381827211a306c3e2be3ace4ac')

prepare() {
  cd "transformers-$pkgver"
  # Remove annoying dependency check on `tokenizers`.
  sed -i '/tokenizers/c\    "tokenizers": "tokenizers",' \
      src/transformers/dependency_versions_table.py
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
