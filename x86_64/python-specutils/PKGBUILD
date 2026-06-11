# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-specutils
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=2.2.0
pkgrel=1
pkgdesc="Astropy Affiliated package for 1D spectral operations"
arch=('any')
url="http://specutils.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer'
             'python-sphinx-astropy'
             'python-matplotlib'
             'python-gwcs'
             'python-ndcube>=2.0'
             'graphviz')  # wheel required by new setuptools
checkdepends=('python-pytest-astropy-header'
              'python-pytest-asdf-plugin'
              'python-pytest-doctestplus'
#             'python-pytest-xdist'
              'python-pytest-remotedata') # matplotlib, gwcs, ndcube already in makedepends; header in conftest.py
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz"
        "https://stsci.box.com/shared/static/28a88k1qfipo4yxc4p4d40v4axtlal8y.fits"
        "https://data.sdss.org/sas/dr16/sdss/spectro/redux/26/spectra/1323/spec-1323-52797-0012.fits"
        'use_local_doc_fits_offline.patch')
#https://dr15.sdss.org/sas/dr15/manga/spectro/redux/v2_4_3/8485/stack/manga-8485-1901-LOGRSS.fits.gz
md5sums=('404e9b9699e621799fdaea23ec1e8059'
         '6de4c8ee5659e87a302e3de595074ba5'
         '3586c5d0810108a182ba9146908dc180'
         '1bda649a83a3d021e75dc09a0da395b3')

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

    cp ${srcdir}/*.fits docs
    patch -Np1 -i "${srcdir}/use_local_doc_fits_offline.patch"
#   sed -i "/astropy.utils.exceptions/a \	ignore:Subclassing validator classes is not intended:DeprecationWarning" setup.cfg
#   sed -i "/astropy.utils.exceptions/a \	ignore:pkg_resources is deprecated as an API:DeprecationWarning" setup.cfg
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}
    # skip some tests that need lots of online data or cost lots of time
    pytest --ignore=docs/_build \
        --ignore=specutils/io/asdf/tags/tests/test_spectra.py \
        --ignore=specutils/io/default_loaders/tests/test_apogee.py \
        --deselect=specutils/tests/test_loaders.py::test_ctypye_not_compliant[remote_data_path0] \
        --deselect=specutils/tests/test_loaders.py::test_hst_cos[remote_data_path0] \
        --deselect=specutils/tests/test_loaders.py::test_hst_cos[remote_data_path1] \
        --deselect=specutils/tests/test_loaders.py::test_hst_stis[remote_data_path0] \
        --deselect=specutils/tests/test_loaders.py::test_hst_stis[remote_data_path1] \
        --deselect=specutils/tests/test_loaders.py::test_hst_stis[remote_data_path2] \
        --deselect=specutils/tests/test_loaders.py::test_apstar_loader \
        --deselect=specutils/tests/test_loaders.py::test_manga_cube \
        --deselect=specutils/tests/test_loaders.py::test_manga_cube \
        --deselect=specutils/tests/test_loaders.py::test_manga_rss \
        --deselect=specutils/tests/test_loaders.py::test_sdss_spplate \
        --deselect=specutils/tests/test_loaders.py::test_sdss_spspec \
        --deselect=specutils/tests/test_loaders.py::test_sdss_compressed[gzip] \
        --deselect=specutils/tests/test_loaders.py::test_sdss_compressed[bzip2] \
        --deselect=specutils/tests/test_loaders.py::test_sdss_compressed[xz] \
        --deselect=specutils/tests/test_loaders.py::TestAAOmega2dF::test_with_rwss[remote_data_path0] \
        --deselect=specutils/tests/test_loaders.py::TestAAOmega2dF::test_without_rwss[remote_data_path0] \
        --deselect=specutils/tests/test_loaders.py::TestAAOmega2dF::test_with_rwss_guess[remote_data_path0] \
        --deselect=specutils/tests/test_loaders.py::TestAAOmega2dF::test_without_rwss_guess[remote_data_path0] \
        --deselect=specutils/tests/test_loaders.py::test_apvisit_loader \
        --deselect=specutils/tests/test_loaders.py::test_iraf_multispec_chebyshev \
        --deselect=specutils/tests/test_loaders.py::test_iraf_multispec_legendre \
        --deselect=specutils/tests/test_loaders.py::test_muscles_loader \
        --deselect=specutils/tests/test_loaders.py::test_subaru_pfs_loader \
        --deselect=specutils/tests/test_spectral_axis.py::test_create_spectral_axis || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4
}

package_python-specutils() {
    depends=('python>=3.11' 'python-scipy>=1.14' 'python-gwcs>=0.22' 'python-ndcube>=2.0') # astropy asdf asdf-astropy required by gwcs
    optdepends=('python-specutils-doc: Documentation for Specutils')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" licenses/*
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-specutils-doc() {
    pkgdesc="Documentation for Python Specutils module"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../licenses/*
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
