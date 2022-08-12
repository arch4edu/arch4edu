# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=python-nvd3
pkgver=0.15.0
pkgrel=5
_commit='f9f811ebc5abd625d63da79e936d9015497b5f58'
pkgdesc='Python wrapper for the NVD3 chart generator'
arch=('any')
url='https://github.com/areski/python-nvd3/'
license=('MIT')
depends=('python-jinja' 'python-slugify')
optdepends=('ipython: for Jupyter notebook support')
makedepends=('git' 'python-build' 'python-installer' 'python-setuptools' 'python-wheel')
checkdepends=('python-nose')
source=("git+https://github.com/areski/python-nvd3.git#commit=${_commit}")
sha256sums=('SKIP')

build() {
    cd python-nvd3
    python -m build --wheel --no-isolation
}

check() {
    cd python-nvd3
    nosetests
}

package() {
    python -m installer --destdir="$pkgdir" python-nvd3/dist/*.whl
    install -D -m644 python-nvd3/MIT-LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
