# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-ndcube
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=2.3.4
pkgrel=1
pkgdesc="Package for multi-dimensional contiguious and non-contiguious coordinate aware arrays"
arch=('any')
url="https://docs.sunpy.org/projects/ndcube"
license=('BSD-2-Clause')
makedepends=('python-setuptools-scm>=6.0.0'
             'python-build'
             'python-installer'
#            'python-sphinx-automodapi'
#            'python-sphinx-changelog'
#            'python-sphinx-gallery'
#            'python-sphinxext-opengraph'
#            'python-sunpy-sphinx-theme'
#            'python-gwcs'
#            'python-sunpy'
#            'python-mpl-animators'
#            'graphviz'
             )  # wheel required by new setuptools, matplotlib <- mpl-animators
# circular deps
#checkdepends=('python-pytest-doctestplus'
#              'python-pytest-mpl'
#              'python-pytest-xdist'
#              'python-pytest-remotedata'
#              'python-dask'
#              'python-reproject'
#              'python-specutils'
#              'python-gwcs'
#              'python-mpl-animators'
#              'python-sunpy'
#             )  # pytest-doctestplus gwcs mpl-animators sunpy{,sphinx-theme} already in makedep
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
#       'doc-use-local-fits.patch'
#       "https://www.astropy.org/astropy-data/tutorials/FITS-images/HorseHead.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063305_0094_lowres.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063301_0131_lowres.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063302_0171_lowres.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063307_0193_lowres.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063302_0211_lowres.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063334_0304_lowres.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063303_0335_lowres.fits"
#       "https://github.com/sunpy/data/raw/404adbc/sunpy/v1/AIA20110607_063305_1600_lowres.fits"
#       "https://github.com/sunpy/ndcube/raw/main/changelog/README.rst"
#)
md5sums=('d0a78ce5eacd98216167e17eb98adb85')
#        'SKIP')

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
##   install -Dm644 -t changelog ${srcdir}/README.rst # README not needed
##   mkdir -p changelog
#    cp ${srcdir}/*.fits examples
#    patch -Np1 -i "${srcdir}/doc-use-local-fits.patch"
##   sed -e "/datfix/d" -e "/unitfix/d" -i setup.cfg
##   sed -e '/ignore:FLIP/a \	ignore:pkg_resources is deprecated:DeprecationWarning' \
##       -e '/ignore:FLIP/a \	ignore:jsonschema.exceptions.RefResolutionError is deprecated:DeprecationWarning' \
##   sed -e '/ignore:distutils/a \	ignore:"order" was deprecated in version 0.9' \
##       -e "/ignore:distutils/a \	ignore:The default kernel will change from 'Hann' to  'Gaussian'" \
##       -e "/ignore:distutils/a \	ignore:The default boundary mode will change from 'ignore' to  'strict'" \
##       -i setup.cfg
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    # need new opengraph
#   msg "Building Docs"
#   PYTHONPATH="../build/lib" make -C docs html
}

#check() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    pytest -vv -l -ra --color=yes -o console_output_style=count -Wdefault -p xdist -n 4 #|| warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count # -Wdefault
#}

package_python-ndcube() {
    depends=('python>=3.10' 'python-gwcs>=0.18' 'python-scipy>=1.8.0')
    optdepends=('python-matplotlib>=3.5.0: plotting'
                'python-mpl-animators>=1.0: plotting'
                'python-reproject>=0.7.1: reproject'
                'python-ndcube-doc: Documentation for ndcube')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" licenses/*
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-ndcube-doc() {
#    pkgdesc="Documentation for Python ndcube module"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../licenses/*
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
