# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-astropy-sphinx-theme
_pyname=${pkgname#python-}
pkgver=1.1
pkgrel=1
pkgdesc="The sphinx theme for Astropy and affiliated packages."
arch=('any')
url="https://github.com/astropy/astropy-sphinx-theme"
license=('BSD')
depends=('python-sphinx>=1.6')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
sha256sums=('ee1dafa0cf4d109455f7a0d19da4cdd608ad24d380ed2eb8090bb945a3d286f9')

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}
