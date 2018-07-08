# Maintainer: dustball

pkgname=pypy3-pip
pkgver=10.0.1
pkgrel=1
pkgdesc="An easy_install replacement for installing pypi python packages"
url="http://www.pip-installer.org/"
arch=('any')
license=('MIT')
depends=('pypy3' 'pypy3-setuptools')
source=(https://files.pythonhosted.org/packages/ae/e8/2340d46ecadb1692a1e455f13f75e596d4eab3d11a57446f08259dee8f02/pip-10.0.1.tar.gz)

package_pypy3-pip() {

  cd "$srcdir/pip-$pkgver"
  pypy3 setup.py build
  pypy3 setup.py install --prefix=/opt/pypy3/ --root="$pkgdir"

  mkdir -p "$pkgdir/usr/bin/"
  mv "$pkgdir/opt/pypy3/bin/pip" "$pkgdir/usr/bin/pip-pypy3"
  sed -i "s|#!/usr/bin/env python$|#!/usr/bin/env pypy3|" \
    ${pkgdir}/opt/pypy3/site-packages/pip/__init__.py
  
  install -D -m644 LICENSE.txt \
	  "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

md5sums=('83a177756e2c801d0b3a6f7b0d4f3f7e')
sha256sums=('f2bd08e0cd1b06e10218feaf6fef299f473ba706582eb3bd9d52203fdbd7ee68')
