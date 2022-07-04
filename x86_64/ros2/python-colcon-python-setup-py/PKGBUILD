# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-python-setup-py
_name=${pkgname:7}
pkgver=0.2.7
pkgrel=2
pkgdesc="An extension for colcon-core to identify packages with a setup.py file by introspecting the arguments to the setup() function call of setuptools."
arch=(any)
url="https://pypi.org/project/colcon-python-setup-py"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(
    "https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz"
    "af88dbc6ecf8e6a0f6c50b50b1c7a8df2256cdf2.patch"
)
sha256sums=(
    'eec293085c4301797706d9e61634fa0cb2136be9b820aa556b2b8baa0bde412d'
    'e5d00fe5a1db81fa0dd706afb95680fb5e57f2fc306a6b1499656fe62ad6ae8a'
)

prepare(){
    cd ${srcdir}/${_name}-${pkgver}
    patch --strip=1 --input="${srcdir}/af88dbc6ecf8e6a0f6c50b50b1c7a8df2256cdf2.patch"
}

package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
