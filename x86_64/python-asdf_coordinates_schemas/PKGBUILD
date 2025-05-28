# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-asdf_coordinates_schemas
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
#"python-${_pyname}-doc")
pkgver=0.4.0
pkgrel=1
pkgdesc="ASDF schemas for coordinates"
arch=('any')
url="https://github.com/asdf-format/asdf-coordinates-schemas"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-build'
             'python-installer')  # wheel required by new setuptools
#            'python-sphinx-asdf'    # avoid cascading dep of sphinx-asdf
#            'python-sphinx-furo'
#            'python-tomli'
checkdepends=('python-pytest'
#             'python-pytest-xdist'
              'python-asdf')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('94731a4761c1e508440758711cd76fae')

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

#   ln -rs ${srcdir}/${_pyname}-${pkgver}/src/${_pyname/-/_}*egg-info \
#       build/lib/${_pyname/-/_}-${pkgver}-py$(get_pyver .).egg-info
    PYTHONPATH="src" pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
#   PYTHONPATH="build/lib" pytest -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 # || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-asdf_coordinates_schemas() {
    depends=('python>=3.9' 'python-asdf>=2.12.1' 'python-asdf-standard>=1.1.0')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

#package_python-asdf_coordinates_schemas-doc() {
#    pkgdesc="Documentation for Python ASDF coordinates schemas"
#    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build
#
#    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE
#    install -dm755 "${pkgdir}/usr/share/doc/${pkgbase}"
#    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
#}
