# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-asdf_wcs_schemas
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=0.4.0
pkgrel=1
pkgdesc="World Coordinate System (WCS) ASDF schemas "
arch=('any')
url="https://github.com/asdf-format/asdf-wcs-schemas"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer')
#            'python-sphinx-astropy'
#            'python-sphinx-asdf'
#            'python-mistune>=3')
checkdepends=('python-pytest'
              'python-asdf_coordinates_schemas')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('08707642fa2fff2450513a7ac4543ed7')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

#   msg "Building Docs"
#   ln -rs ${srcdir}/${_pyname}-${pkgver}/src/${_pyname/-/_}*egg-info \
#       build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
#   PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    ln -rs ${srcdir}/${_pyname}-${pkgver}/src/${_pyname/-/_}*egg-info \
        build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
    PYTHONPATH="build/lib" pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
}

package_python-asdf_wcs_schemas() {
    depends=('python>=3.9' 'python-asdf-standard>=1.1.0' 'python-asdf_transform_schemas>=0.5.0' 'python-asdf_coordinates_schemas>=0.3.0')
    optdepends=('python-asdf_wcs_schemas-doc: Documentation for ASDF WCS Schemas')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-asdf_wcs_schemas-doc() {
#    pkgdesc="Documentation for ASDF WCS Schemas"
#    cd ${srcdir}/${_pyname}-${pkgver}/build/sphinx
#
#    install -D -m644 ../../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
#    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
