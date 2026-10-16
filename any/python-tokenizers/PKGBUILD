# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
# Contributor: Filip Graliński <filipg@amu.edu.pl>
# Maintainer: Mohamed Amine Zghal (medaminezghal) <medaminezghal at outlook dot com>

_name=tokenizers
pkgname=python-$_name
pkgver=0.23.3
pkgrel=3
pkgdesc='Fast State-of-the-Art Tokenizers optimized for Research and Production'
arch=('x86_64' 'aarch64' 'i686')
url="https://github.com/huggingface/tokenizers"
license=('Apache-2.0')
depends=('python'
         'python-huggingface-hub'
         'libgcc'
         'libstdc++'
         'glibc')
makedepends=('python-maturin'
             'python-build'
             'python-installer')
checkdepends=('python-pytest'
              'python-pytest-asyncio'
              'python-numpy'
              'python-datasets')
options=('!lto')
source=("$_name-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('2a0ff80c61f263cca608264a99b43dd487a3194a362d20c31193bc083e16a46b')

prepare() {
  cd "$_name-$pkgver/bindings/python"
  # Remove the benchmark suite (dropped upstream after 0.23.3), its data isn't fetched by make test-data
  rm tests/test_benchmarks.py
}

build() {
  cd "$_name-$pkgver/bindings/python"
  python -m build --wheel --no-isolation
}

check() {
  local pytest_options=(
    -vv
    --disable-warnings
  )
  cd "$_name-$pkgver/bindings/python"
  export HF_HOME="$srcdir"/hf-home
  export RUN_SLOW=1
  make test-data
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -P -m pytest "${pytest_options[@]}" tests
  cargo test --frozen --no-default-features
}

package() {
  cd "$_name-$pkgver/bindings/python"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
