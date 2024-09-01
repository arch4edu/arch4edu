# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell-archive
pkgname=python-dephell-archive
pkgver=0.1.7
pkgrel=2
pkgdesc="Pathlib for archives"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-attrs')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('bb263492a7d430f9e04cef9a0237b7752cc797ab364bf35e70196af09c73ea37')
b2sums=('c07e703fd177072a29bc45b70b15273d23d889ab2a0de9434b30ac272c46c648e7214f5d8aaab136f868e0dadfbd290279b160dfd7183603cfcebf3b5bea435c')

prepare() {
    cd ${_pkgname}-${pkgver}

    # pycache slipped into release tarballs
    find . -name \*.pyc -delete
}

build(){
    cd ${_pkgname}-${pkgver}

    python setup.py build
}

check() {
    cd ${_pkgname}-${pkgver}

    python setup.py test
}

package() {
    cd ${_pkgname}-${pkgver}

    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
