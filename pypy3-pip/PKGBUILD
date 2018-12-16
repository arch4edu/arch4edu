# Maintainer: dustball

pkgname=pypy3-pip
pkgver=18.1
pkgrel=1
pkgdesc="An easy_install replacement for installing pypi python packages"
url="http://www.pip-installer.org/"
arch=('any')
license=('MIT')
depends=('pypy3' 'pypy3-setuptools')
source=(https://files.pythonhosted.org/packages/45/ae/8a0ad77defb7cc903f09e551d88b443304a9bd6e6f124e75c0fbbf6de8f7/pip-18.1.tar.gz)

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

md5sums=('75cad449ad62c88b22de317a26781714')
sha256sums=('c0a292bd977ef590379a3f05d7b7f65135487b67470f6281289a94e015650ea1')
