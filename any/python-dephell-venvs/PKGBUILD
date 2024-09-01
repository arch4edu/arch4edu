# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_venvs
pkgname=python-dephell-venvs
pkgver=0.1.18
pkgrel=2
pkgdesc="Manage Python virtual environments"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-attrs' 'python-dephell-pythons')
makedepends=('python-setuptools')
checkdepends=('python-pytest' 'python-requests')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('c7307291b754edba325ab27edeb05d85ee4dd2f1487c48872a1ebfc372bf7a2e')
b2sums=('ca3b64a0983ef32f4aec42a26413604d241e00d2ac5d2e6c36fa58b3d354ad1a95562aa495a799245b54a7796c036fea1c3041ab087d3cb915c829caf75e02cd')

prepare() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    # pycache slipped into release tarballs
    find . -name \*.pyc -delete

    # https://github.com/dephell/dephell_venvs/issues/3
    sed -e "s|dephell_venvs.ensurepip||" -e '/package_data/d' -i setup.py
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
