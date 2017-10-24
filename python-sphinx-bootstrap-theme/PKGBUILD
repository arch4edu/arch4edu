# Maintainer: Miguel de Val-Borro <miguel at archlinux dot net>
pkgname=('python-sphinx-bootstrap-theme' 'python2-sphinx-bootstrap-theme')
pkgver=0.6.0
pkgrel=1
pkgdesc="Sphinx documentation theme that integrates the Bootstrap framework"
arch=('any')
url="http://ryan-roemer.github.io/sphinx-bootstrap-theme/"
license=('MIT')
makedepends=('python-setuptools' 'python2-setuptools')
source=("https://files.pythonhosted.org/packages/source/s/sphinx-bootstrap-theme/sphinx-bootstrap-theme-${pkgver}.tar.gz")
md5sums=('9c9e46f57e5cd7bef70453c66e2d2af5')

build() {
  cp -r ${srcdir}/sphinx-bootstrap-theme-${pkgver} ${srcdir}/sphinx-bootstrap-theme-${pkgver}-py2

  cd ${srcdir}/sphinx-bootstrap-theme-${pkgver}
  python setup.py build

  cd ${srcdir}/sphinx-bootstrap-theme-${pkgver}-py2
  python2 setup.py build
}

package_python-sphinx-bootstrap-theme() {
  cd ${srcdir}/sphinx-bootstrap-theme-${pkgver}
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
  python setup.py install --prefix=/usr --root=${pkgdir}
}

package_python2-sphinx-bootstrap-theme() {
  cd ${srcdir}/sphinx-bootstrap-theme-${pkgver}-py2
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
  python2 setup.py install --prefix=/usr --root=${pkgdir}
}
