# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-dust-extinction
_pname=${pkgbase#python-}
_pyname=${_pname//-/_}
pkgname=("python-${_pname}" "python-${_pname}-doc")
pkgver=1.6
pkgrel=1
pkgdesc="Interstellar Dust Extinction Models"
arch=('any')
url="https://dust-extinction.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer'
             'python-sphinx-automodapi'
             'python-matplotlib'
             'python-astropy'
             'python-scipy'
             'graphviz')  # wheel required by new setuptools
checkdepends=('python-pytest-astropy-header'
#             'python-pytest-xdist'
              'python-pytest-doctestplus')   # astropy, scipy already in makedepends; header in conftest.py
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('592b8b2c8491a87ee3bdd18b50c51531')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    sed -i -e "/sys.modules/a pkgver = '${pkgver}'" -e 's/package.__version__/pkgver/g' docs/conf.py
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname/-/_}*egg-info \
        build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
#   PYTHONPATH="../build/lib" make SPHINXOPTS="-D disable_intersphinx=1" -C docs html
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest --ignore=docs/_build || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-dust-extinction() {
    depends=('python-astropy'
             'python-scipy')
    optdepends=('python-dust-extinction-doc: Documentation for dust-extinction')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-dust-extinction-doc() {
    pkgdesc="Documentation for Astronomical dust extinction"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 ../../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
