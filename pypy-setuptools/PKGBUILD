# vim: set filetype=sh:
# Maintainer: Daniel Milde <daniel@milde.cz>

pkgbase='pypy-setuptools'
pkgname=(pypy-setuptools pypy3-setuptools)
_name=setuptools
pkgver=38.2.3
pkgrel=1
epoch=1
pkgdesc="Easily download, build, install, upgrade, and uninstall Python packages"
arch=('any')
license=('PSF')
url="http://pypi.python.org/pypi/setuptools"
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.zip")
sha512sums=('43fda5f6148e03070a2574671ca1b0cf1906b981bc45f4255fa95d28bb3a9bd967b9f3d631e286a391a32287881e2dbabb2c6fbe9b3e198993e1846444d19c45')
makedepends=('pypy3' 'pypy')

prepare() {
  cd "${srcdir}"/setuptools-${pkgver}
  sed -i -e "s|^#\!.*/usr/bin/env python|#!/usr/bin/env pypy|" setuptools/command/easy_install.py
}

# Rename the following function to check() to enable checking
_check_pypy-setuptools() {
  # Workaround UTF-8 tests by setting LC_CTYPE

  # Check pypy3 module
  cd "${srcdir}"/setuptools-${pkgver}
  LC_CTYPE=en_US.utf8 pypy setup.py ptr
}

# Rename the following function to check() to enable checking
_check_pypy3-setuptools() {
  # Workaround UTF-8 tests by setting LC_CTYPE

  # Check pypy3 module
  cd "${srcdir}"/setuptools-${pkgver}
  LC_CTYPE=en_US.utf8 pypy3 setup.py ptr
}

package_pypy-setuptools() {
  depends=('pypy')
  provides=('pypy-distribute')
  replaces=('pypy-distribute')
  cd "${srcdir}/setuptools-${pkgver}"
  pypy setup.py install --prefix=/opt/pypy --root="${pkgdir}" --optimize=1
}

package_pypy3-setuptools() {
  depends=('pypy3')
  provides=('pypy3-distribute')
  replaces=('pypy3-distribute')
  cd "${srcdir}/setuptools-${pkgver}"
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
}

