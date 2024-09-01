# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_versioning
pkgname=python-dephell-versioning
pkgver=0.1.2
pkgrel=5
pkgdesc="Bump project version like a pro"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-packaging')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('9ba7636704af7bd64af5a64ab8efb482c8b0bf4868699722f5e2647763edf8e5')
b2sums=('472a7c209f07880d02e687ad98436e5a7046c9471a4cf408a4611b63e7aac6e9a55bb87cb9b348311bfb6af492b29ae4fcb717f8d1949b8b9f49e164ef0550ae')

build(){
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python setup.py build
}

check() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python -m pytest
}

package() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
