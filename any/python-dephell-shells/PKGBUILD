# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell_shells
pkgname=python-dephell-shells
pkgver=0.1.5
pkgrel=3
pkgdesc="Activate virtual environment for current shell"
arch=('any')
url="https://github.com/dephell/${_pkgname}"
license=('MIT')
depends=('python-attrs' 'python-pexpect' 'python-shellingham')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('77150b732db135d436f41c2c6f12694e6058a8609214117ee80f6c40234ac2d5')
b2sums=('6cc99191ddd5ca5585aa45f8e6f3815a1f2ee2de1176e8e41f96bf65c6611fb744a368cbd727d1de2642f6f42cf6462ca364a90f76f4cec0f50059c111b6d9fd')

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
