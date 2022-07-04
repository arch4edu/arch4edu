# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-powershell
_name=${pkgname:7}
pkgver=0.3.7
pkgrel=1
pkgdesc="An extension for colcon-core to provide PowerShell scripts."
arch=(any)
url="https://pypi.org/project/colcon-powershell/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz)
sha256sums=('886b4ab34a6863a3c51e1cb5918bc921c2f4d2a36d07e5a345674cc8c7f02ed7')


package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
