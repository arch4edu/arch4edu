# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-reproject
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=0.21.0
pkgrel=1
pkgdesc="Python-based Astronomical image reprojection"
arch=('i686' 'x86_64')
url="http://reproject.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('cython>=3.1'
             'python-setuptools-scm'
             'python-extension-helpers>=1.4'
             'python-build'
             'python-installer'
#            'python-tomli'
             'python-numpy>=2'
             'python-sphinx-astropy'
             'python-sphinx-copybutton'
#            'python-matplotlib'
             'python-astropy-healpix'
             'python-dask-image'
             'python-pyavm'
             'python-pyvo')  # scipy <- dask-image; wheel required by new setuptools
#            'python-mimeparse')    # numpy for package itself
#checkdepends=('python-pytest-arraydiff'
#              'python-pytest-astropy-header'
#              'python-pytest-doctestplus'
#              'python-pytest-remotedata'
##             'python-matplotlib'
#              'python-sunpy'
#              'python-mpl-animators'
#              'python-gwcs'
#              'python-shapely'
#              'python-zarr')     # astropy-healpix dask scipy already in makedep
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('af73e5bdea72aa39014707e615626e5f')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    sed -i -e "/cython/s/==/>=/" -e "/oldest-supported-numpy/d" pyproject.toml
##   sed -i "/NaNs/a \	ignore:Subclassing validator classes is not intended:DeprecationWarning" setup.cfg
##   patch -Np1 -i "${srcdir}/doc-use-local-fits.patch"
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation --skip-dependency-check

    msg "Building Docs"
    ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname/-/_}*egg-info \
        build/lib.linux-${CARCH}-cpython-$(get_pyver)/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
#   PYTHONPATH="../build/lib.linux-${CARCH}-cpython-$(get_pyver)" make SPHINXOPTS="-D disable_intersphinx=1" -C docs html
    PYTHONPATH="../build/lib.linux-${CARCH}-cpython-$(get_pyver)" make -C docs html
}

#check() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    # Cost more than 10 min
#    pytest "build/lib.linux-${CARCH}-cpython-$(get_pyver)" -vv -l -ra --color=yes -o console_output_style=count --remote-data #|| warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
#}

package_python-reproject() {
    depends=('python>=3.11'
             'python-numpy>=1.23'
             'python-dask>=2024.4.1'
             'python-dask-image>=2025.11.0'
             'python-fsspec>=2021.9'
             'python-scipy>=1.9'
             'python-astropy>=5.0'
             'python-astropy-healpix>=1.0'
             'python-pillow>=10.0'
             'python-pyavm>=0.9.6'
             'python-zarr>=2.17.0')
    optdepends=('python-shapely>=1.6: For some of the mosaicking functionality'
                'python-reproject-doc: Documentation for Reproject'
                'python-pytest-astropy: For testing')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-reproject-doc() {
    pkgdesc="Documentation for Python Reproject module"
    arch=('any')
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
