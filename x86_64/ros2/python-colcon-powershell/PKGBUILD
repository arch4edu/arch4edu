# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-powershell
_name=${pkgname:7}
pkgver=0.4.0
pkgrel=1
pkgdesc="An extension for colcon-core to provide PowerShell scripts."
arch=(any)
url="https://pypi.org/project/colcon-powershell/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('1fb2a8dadaf547cfca9daaf1b94ffaee3e2958103d5aaadb84e072c4f526906f')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
