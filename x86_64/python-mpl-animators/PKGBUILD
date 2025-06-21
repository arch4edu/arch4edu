# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-mpl-animators
_pname=${pkgbase#python-}
_pyname=${_pname/-/_}
pkgname=("python-${_pname}" "python-${_pname}-doc")
pkgver=1.2.4
pkgrel=1
pkgdesc="An interative animation framework for matplotlib"
arch=('any')
url="https://sunpy.org"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm>=8.0.0'
             'python-build'
             'python-installer'
             'python-sphinx-automodapi'
             'python-sphinx-changelog'
             'python-sphinx-gallery'
             'python-sunpy-sphinx-theme'
             'python-matplotlib'
             'python-sunpy'
             'python-scipy'
#            'ipython'
             'graphviz')  # wheel required by new setuptools
checkdepends=('python-pytest-doctestplus'
#             'python-pytest-xdist'
              'python-pytest-mpl')  # matplotlib, astropy already in makedepends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063302_0171_lowres.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063307_0193_lowres.fits"
#       'examples-use-local-fits.patch'
#   )
md5sums=('5562c7e115ddbbac0ff013a0a25dd68f')

get_pyinfo() {
    [[ $1 == "site" ]] && python -c "import site; print(site.getsitepackages()[0])" || \
        python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}


#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    cp ${srcdir}/*.fits examples
#    patch -Np1 -i "${srcdir}/examples-use-local-fits.patch"
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-mpl-animators() {
    depends=('python-matplotlib>=3.5.0')
    optdepends=('python-astropy>=5.3.0: make line or image plots for a numpy array and associated WCS object'
                'python-mpl-animators-doc: Documentation for mpl-animators')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
#   rm -r ${pkgdir}/$(get_pyinfo site)/{docs,examples,licenses}
}

package_python-mpl-animators-doc() {
    pkgdesc="Documentation for Python mpl-animators"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 ../../LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
