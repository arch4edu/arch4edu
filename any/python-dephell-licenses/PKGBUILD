# Maintainer: Caleb Maclennan <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>

_pkgname=dephell-licenses
pkgname=python-dephell-licenses
pkgver=0.1.7
pkgrel=6
pkgdesc="Manage OSS licenses: retrieve information, generate"
arch=('any')
url="https://github.com/dephell/${_pkgname/-/_}"
license=('MIT')
depends=('python-attrs' 'python-requests')
makedepends=('python-setuptools')
checkdepends=('python-pytest')
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('f175cec822a32bda5b56442f48dae39efbb5c3851275ecd41cfd7e849ddd2ea6')
b2sums=('954daf4a725dd1061ae60c35a86295b9bcc835eb9f219f3a9fe0e19a710a11ed0fa94ff324b5a4171cf09566abc39c113a96226c71f21a54eae459cf0e10cc18')

build(){
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python setup.py build
}

check() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python -m pytest --deselect tests/test_license.py::test_make_text
}

package() {
    cd "${srcdir}"/${_pkgname}-${pkgver}

    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
