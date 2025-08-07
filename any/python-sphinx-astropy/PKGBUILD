# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgname=python-sphinx-astropy
_pname=${pkgname#python-}
_pyname=${_pname//-/_}
pkgver=1.10
pkgrel=1
pkgdesc="Sphinx extensions and configuration specific to the Astropy project"
arch=('any')
url="https://github.com/astropy/sphinx-astropy"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer')
checkdepends=('python-pytest-doctestplus'
              'python-astropy-sphinx-theme'
#             'python-pytest-xdist'
###           'python-matplotlib'
              'python-numpydoc'
              'python-sphinxcontrib-jquery'
              'python-sphinx-automodapi'
              'python-pydata-sphinx-theme'
              'python-sphinx-copybutton')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('61f702f3b73a165e3b74b5e36cda3ef9')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    # skip tests that cost times through internet
    pytest || warning "Tests failed" #\
#       --deselect=sphinx_astropy/tests/test_conf.py::test_conf #|| warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package() {
    depends=('python-packaging'
             'python-sphinx>=4.0.0'
             'python-astropy-sphinx-theme'
             'python-sphinx-automodapi'
             'python-sphinx-gallery'
             'python-numpydoc'
             'python-sphinxcontrib-jquery'
             'python-pillow'
             'python-pytest-doctestplus>=0.11')
    optdepends=('python-pydata-sphinx-theme: To use the new pydata-sphinx-theme with sphinx_astropy.conf.v2'
                'python-sphinx-copybutton: To use the new pydata-sphinx-theme with sphinx_astropy.conf.v2')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
