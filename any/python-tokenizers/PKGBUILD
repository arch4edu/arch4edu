# Maintainer: Daniel Bershatsky <bepshatsky@yandex.ru>
# Contributor: Filip Graliński <filipg@amu.edu.pl>
# Maintainer: Mohamed Amine Zghal (medaminezghal) <medaminezghal at outlook dot com>

_name=tokenizers
pkgname=python-$_name
pkgver=0.23.3
pkgrel=1
pkgdesc='Fast State-of-the-Art Tokenizers optimized for Research and Production'
arch=('x86_64' 'aarch64' 'i686')
url="https://github.com/huggingface/tokenizers"
license=('Apache-2.0')
depends=('python-huggingface-hub'
         'libgcc'
         'libstdc++'
         'glibc')
makedepends=('git'
             'python-build'
             'python-installer'
             'python-maturin')
checkdepends=('python-pytest'
              'python-pytest-asyncio'
              'python-numpy'
              'python-datasets')
options=('!lto')
source=("$_name::git+$url.git#tag=v$pkgver")
sha256sums=('3906634820f9e6e02d5c9c9c6c2deebb9ff164e7fcdac4d4015ca7e5997477f2')

build() {
  cd "$srcdir"/$_name/bindings/python
  python -m build --wheel --no-isolation
}

check() {
  local pytest_options=(
    -vv
    --disable-warnings
  )
  cd "$srcdir"/$_name/bindings/python
  export HF_HOME="$srcdir"/hf-home
  export RUN_SLOW=1
  make test-data
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -P -m pytest "${pytest_options[@]}" tests
  cargo test --frozen --no-default-features
}

package() {
  cd "$srcdir"/$_name
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  cd "bindings/python"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
