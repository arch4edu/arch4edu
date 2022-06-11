# Maintainer: dustball

pkgname=pypy3-pip
pkgver=20.0.2
pkgrel=1
pkgdesc="An easy_install replacement for installing pypi python packages"
url="https://pip.pypa.io/"
arch=('any')
license=('MIT')
depends=('pypy3' 'pypy3-setuptools')
source=(https://files.pythonhosted.org/packages/8e/76/66066b7bc71817238924c7e4b448abdb17eb0c92d645769c223f9ace478f/pip-20.0.2.tar.gz)

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

md5sums=('7d42ba49b809604f0df3d55df1c3fd86')
sha256sums=('7db0c8ea4c7ea51c8049640e8e6e7fde949de672bfa4949920675563a5a6967f')
