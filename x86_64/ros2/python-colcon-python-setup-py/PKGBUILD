# Maintainer: Achmad Fathoni<fathoni.id(at)gmail.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-python-setup-py
_name=${pkgname:7}
pkgver=0.2.8
pkgrel=3
pkgdesc="An extension for colcon-core to identify packages with a setup.py file by introspecting the arguments to the setup() function call of setuptools."
arch=(any)
url="https://pypi.org/project/colcon-python-setup-py"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(
    "https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz"
)
sha256sums=('83f719f237bb852544de124635d4376a0ad861c14c752830fbdfffbd38cd95aa')

package() {
    cd ${srcdir}/${_name}-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
