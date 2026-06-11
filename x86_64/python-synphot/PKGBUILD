# Maintainer: Astro Benzene <universebenzene at sina dot com>
# Contributor: Miguel de Val-Borro <miguel dot deval at gmail dot com>

pkgbase=python-synphot
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=1.6.0
pkgrel=1
pkgdesc="Synthetic Photometry using Astropy"
arch=('i686' 'x86_64')
url="https://synphot.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer'
             'python-numpy>=2.0.0'
             'python-sphinx-astropy'
             'python-matplotlib'
             'python-astropy'
             'python-scipy'
             'graphviz')  # wheel required by new setuptools
checkdepends=('python-pytest-astropy-header'
              'python-pytest-doctestplus'
              'python-pytest-remotedata'
#             'python-pytest-xdist'
              'python-dust-extinction'
              'python-specutils')   # astropy scipy already in makedepends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('852419c081c9b9f230d23d613a17eb31')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    sed -i "/CCM89/a \	ignore:The Spectrum1D class is deprecated:astropy.utils.exceptions.AstropyDeprecationWarning" setup.cfg
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation --skip-dependency-check

    msg "Building Docs"
    ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname/-/_}*egg-info \
        build/lib.linux-${CARCH}-cpython-$(get_pyver)/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
    PYTHONPATH="../build/lib.linux-${CARCH}-cpython-$(get_pyver)" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    mv {,_}${_pyname}
    pytest "build/lib.linux-${CARCH}-cpython-$(get_pyver)" docs || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 --remote-data=any
}

package_python-synphot() {
    depends=('python-numpy>=1.23'
             'python-astropy>=6'
             'python-scipy>=1.9')
    optdepends=('python-matplotlib: Plotting support'
                'python-specutils>=1.10: Manipulating spectroscopic data'
                'python-synphot-doc: Documentation for synphot')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE.rst
    install -D -m644 -t "${pkgdir}/usr/share/doc/${pkgname}" README.rst
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-synphot-doc() {
    pkgdesc="Documentation for Python Synthetic Photometry (synphot)"
    arch=('any')
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 ../../LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
