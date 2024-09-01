# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_discover
pkgname=python-dephell-discover
pkgver=0.2.10
pkgrel=6
pkgdesc="Find project modules and data files (packages and package_data for setup.py)"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-attrs')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('a2ad414e5e0fe16c82c537d6a3198afd9818c0c010760eccb23e2d60e5b66df6')
b2sums=('2721bdee22c9edcdc11c7102fb034db4ec92b23bf8ac7c077c87036083cefecf34bbf1474bdb0ddfa252ca47d40181054b5eacff68daef8c4e7bad9f4426ea35')

prepare() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    # pycache slipped into release tarballs
    find . -name \*.pyc -delete
}

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
