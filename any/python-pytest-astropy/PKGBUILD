# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-pytest-astropy
_pyname=${pkgname#python-}
pkgver=0.11.0
pkgrel=1
pkgdesc="Metapackage for all the testing machinery used by the Astropy Project"
arch=('any')
url="https://github.com/astropy/pytest-astropy"
license=('BSD')
depends=('python>=3.7'
         'python-pytest>=4.6'
         'python-pytest-doctestplus>=1.0.0'
         'python-pytest-remotedata>=0.4.1'
         'python-pytest-arraydiff>=0.5'
         'python-pytest-astropy-header>=0.2.2'
         'python-pytest-filter-subpackage>=0.1.2'
         'python-pytest-cov>=2.3.1'
         'python-pytest-mock>=2.0'
         'python-attrs>=19.2.0'
         'python-hypothesis>=5.1')
makedepends=('python-setuptools-scm' 'python-wheel' 'python-build' 'python-installer')
checkdepends=('python-nose')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('51cfee1d56dbe731f1d65b752d2d567f')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    nosetests #-v -x
}

package() {
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
