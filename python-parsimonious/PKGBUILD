# Maintainer: Wojciech Szymecki <w.szymecki-at-g;mail-com>
_name="parsimonious"

pkgbase="python-${_name}"
pkgname=("python-${_name}" "python2-${_name}")
pkgver=0.8.1
pkgrel=1
arch=('any')
url="https://pypi.python.org/pypi/${_name}/${pkgver}"
license=('MIT')
makedepends=('python-setuptools' 'python2-setuptools')
pkgdesc="Fast parser based on parsing expression grammars (PEGs)"
source=("https://files.pythonhosted.org/packages/source/${_name:0:1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('3add338892d580e0cb3b1a39e4a1b427ff9f687858fdd61097053742391a9f6b')

prepare() {
    cp -r "${srcdir}/${_name}-${pkgver}" "${srcdir}/${_name}-${pkgver}-python2"
}

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python3 setup.py build
    cd "${srcdir}/${_name}-${pkgver}-python2"
    python2 setup.py build
}

package_python-parsimonious() {
  pkgdesc="Fast parser based on parsing expression grammars (PEGs) - Python 3 version."
  depends=('python>=3.3')

  cd "${srcdir}/${_name}-${pkgver}"

  python3 setup.py install --skip-build --root="${pkgdir}" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-parsimonious() {
  pkgdesc="Fast parser based on parsing expression grammars (PEGs) - Python 2 version."
  depends=('python>=2.7')

  cd "${srcdir}/${_name}-${pkgver}-python2"

  python2 setup.py install --skip-build --root="${pkgdir}" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
