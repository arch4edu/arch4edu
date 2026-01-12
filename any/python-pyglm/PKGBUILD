# Maintainer: Michal Wojdyla < micwoj9292 at gmail dot com >
# Contributor: Mubashshir <ahmubashshir@gmail.com>
# from: pypi
# what: PyGLM

pkgname='python-pyglm'
pkgver='2.8.3'
pkgrel=1
pkgdesc="OpenGL Mathematics library for Python"
url="https://github.com/Zuzu-Typ/PyGLM"
depends=('glm' 'python')
makedepends=(
    'git'
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
license=('Zlib')
arch=('x86_64')
source=("$pkgname::git+https://github.com/Zuzu-Typ/PyGLM.git#tag=$pkgver")
sha256sums=('4b36d8bd25bfcb4ba450513d00cb994f67f649ea920e1762cb838bde1e0d07a4')

build() {
    cd "$srcdir/$pkgname"
    CFLAGS="$CFLAGS -Wno-all" python -m build --wheel --no-isolation
}

package() {
    cd "$srcdir/$pkgname"
    python -m installer --destdir="$pkgdir" --compile-bytecode=1 dist/*.whl
}
