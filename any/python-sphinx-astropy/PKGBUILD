# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgname=python-sphinx-astropy
_pyname=${pkgname#python-}
pkgver=1.8.0
pkgrel=1
pkgdesc="Sphinx extensions and configuration specific to the Astropy project"
arch=('any')
url="https://github.com/astropy/sphinx-astropy"
license=('BSD')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer')
checkdepends=('python-pytest-doctestplus'
              'python-astropy-sphinx-theme'
              'python-numpydoc'
              'python-sphinxcontrib.jquery'
              'python-sphinx-automodapi'
             )
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('1080a54c73c327fe6511764110b09508')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # -vv --color=yes
}

package() {
    depends=('python-packaging'
             'python-sphinx>=1.7'
             'python-astropy-sphinx-theme'
             'python-sphinx-automodapi'
             'python-sphinx-gallery'
             'python-numpydoc'
             'python-sphinxcontrib.jquery'
             'python-pillow'
             'python-pytest-doctestplus>=0.11')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
