# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-astropy-header
_pyname=${pkgname#python-}
pkgver=0.1.1
pkgrel=1
pkgdesc="Pytest plugin to add diagnostic information to the header of the test output"
arch=('i686' 'x86_64')
url="https://github.com/astropy/pytest-astropy-header"
license=('BSD')
depends=('python-pytest>=2.8')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('4d50f5632ce04a1412ba1a351b5d2cbf')

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
