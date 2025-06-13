# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-asdf-astropy
_pname=${pkgbase#python-}
_pyname=${_pname/-/_}
#_pyname=${_pname}
pkgname=("python-${_pname}")
#"python-${_pname}-doc")
pkgver=0.8.0
pkgrel=1
pkgdesc="ASDF serialization support for astropy"
arch=('any')
url="https://asdf-astropy.readthedocs.io"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer')
##            'python-sphinx-astropy'
##            'python-astropy'
#             'python-sphinx-asdf'
#             'python-matplotlib'
#             'python-tomli'
#             'python-asdf_coordinates_schemas'
#             'graphviz'
#             )    # avoid cascading dep of sphinx-asdf; wheel required by new setuptools
checkdepends=('python-pytest-astropy-header'
#             'python-pytest-xdist'
              'python-pytest-doctestplus'
              'python-astropy'
              'python-scipy'
              'python-asdf_coordinates_schemas')   # 'python-asdf' 'python-astropy' by sphinx-asdf
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('add43908577274ccf97710c3e4f0a0b8')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

#   msg "Building Docs"
#   ln -rs ${srcdir}/${_pyname}-${pkgver}/${_pyname/-/_}*egg-info \
#       build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
#   PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-asdf-astropy() {
    depends=('python>=3.11'
             'python-astropy>=5.2.0'
             'python-asdf>=2.15.0'
             'python-asdf_coordinates_schemas>=0.4'
             'python-asdf_transform_schemas>=0.6'
             'python-packaging>=19')
    optdepends=('python-asdf-astropy-doc: Documentation for Python ASDF-AstroPy')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE.rst
    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" licenses/*
    install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" README.rst
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-asdf-astropy-doc() {
#    pkgdesc="Documentation for Python ASDF-AstroPy"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE.rst
#    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../licenses/*
#    install -dm755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
