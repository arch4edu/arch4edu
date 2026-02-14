# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-pyvo
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=1.8.1
pkgrel=1
pkgdesc="Astropy affiliated package for accessing Virtual Observatory data and services"
arch=('any')
url="https://pyvo.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer'
             'python-sphinx-astropy'
##           'python-matplotlib'
             'python-astropy'
             'graphviz')  # wheel required by new setuptools
# conftest.py
checkdepends=('python-pytest-astropy-header'
#             'python-pytest-xdist'
#             'python-pytest-timeout'
              'python-pytest-doctestplus'
              'python-pytest-remotedata'
              'python-requests-mock'
              'python-pillow')  #astropy already in makedepends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('16bb27c5ac6dd7729e16f2740edb4c11')

#prepare() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    sed -i "/error/a \	ignore:leap-second auto-update failed:astropy.utils.exceptions.AstropyWarning" setup.cfg
#}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}
    # Some costs lost of time
    PYTHONPATH="." pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 --remote-data #
#       --deselect=pyvo/mivot/tests/test_user_api.py::test_with_dict \
#       --deselect=pyvo/mivot/tests/test_user_api.py::test_mivot_tablerow_next \
#       --deselect=pyvo/mivot/tests/test_user_api.py::test_with_full_dict \
#       --deselect=pyvo/mivot/tests/test_user_api.py::test_mivot_viewer_next \
#       --deselect=pyvo/mivot/tests/test_vizier_cs.py::test_bad_ref \
#       --deselect=pyvo/mivot/tests/test_vizier_cs.py::test_with_id \
#       --deselect=pyvo/mivot/tests/test_vizier_cs.py::test_with_name \
#       --deselect=pyvo/registry/tests/test_regtap.py::TestGetTables::test_get_tables_limit_enforced \
#       --deselect=pyvo/registry/tests/test_regtap.py::TestGetTables::test_get_tables_names \
#       --deselect=pyvo/registry/tests/test_regtap.py::TestGetTables::test_get_tables_table_instance \
#       --deselect=pyvo/registry/tests/test_regtap.py::TestGetTables::test_get_tables_column_meta \
#       --deselect=pyvo/registry/tests/test_regtap.py::TestGetTables::test_get_tables_utype \
#       --deselect=pyvo/discover/tests/test_imagediscovery.py::test_single_sia1 \
#       --deselect=pyvo/dal/tests/test_sia2_remote.py::TestSIACadc::test_reg_sia2 \
#       --deselect=pyvo/registry/tests/test_regtap.py::test_maxrec \
#       --deselect=pyvo/discover/tests/test_imagediscovery.py::test_cone_and_spectral_point \
#       --deselect=pyvo/registry/tests/test_regtap.py::test_get_contact \
#       --deselect=pyvo/discover/tests/test_imagediscovery.py::test_servedby_elision \
#       --deselect=pyvo/registry/tests/test_rtcons.py::test_all_constraints \
#       --deselect=pyvo/registry/tests/test_regtap.py::test_get_alt_identifier \
#       --deselect=pyvo/discover/tests/test_imagediscovery.py::test_access_url_elision \
#       --deselect=docs/dal/index.rst::index.rst \
#       --deselect=pyvo/registry/tests/test_regtap.py::TestDatamodelQueries::test_obscore \
#       --deselect=pyvo/discover/tests/test_imagediscovery.py::test_cancelling \
#       --deselect=docs/index.rst::index.rst \
#       --deselect=pyvo/registry/tests/test_regtap.py::TestDatamodelQueries::test_epntap \
#       --deselect=docs/registry/index.rst::index.rst \
#       --deselect=pyvo/registry/tests/test_regtap.py::TestDatamodelQueries::test_regtap \
#       --deselect=pyvo/registry/tests/test_regtap.py::test_sia2_service_operation
        # || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 --remote-data #
}

package_python-pyvo() {
    depends=('python-astropy>=4.2' 'python-requests')
    optdepends=('python-pillow: all functions'
                'python-defusedxml: all functions'
                'python-pyvo-doc: Documentation for PyVO')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 licenses/* -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-pyvo-doc() {
    pkgdesc="Documentation for Python PyVO module"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../licenses/*
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
