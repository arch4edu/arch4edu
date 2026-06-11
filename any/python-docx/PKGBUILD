# Maintainer: Michał Wojdyła < micwoj9292 at gmail dot com >
# Contributor: Raymond W. Ko <r   a y     m  o nd DOT  w DOT k  o AT g  m ai l DOT COM>
_python=python
_distname=docx
pkgname=$_python-$_distname
pkgver=1.2.0
pkgrel=1
pkgdesc="Create and modify Word documents with Python"
arch=(any)
url="https://github.com/python-openxml/python-docx"
license=('MIT')
depends=('python' 'python-lxml' 'python-typing_extensions')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=("https://github.com/python-openxml/${pkgname}/archive/v${pkgver}.tar.gz")
md5sums=('dc385b78e0670ba792e6bd924d5f9a30')

build() {
    cd "${pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${pkgname}-${pkgver}"
    python -m installer --destdir=${pkgdir} dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
