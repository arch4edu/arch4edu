# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-asdf_transform_schemas
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}")
pkgver=0.5.0
pkgrel=1
pkgdesc="ASDF schemas for transforms"
arch=('any')
url="https://github.com/asdf-format/asdf-transform-schemas"
license=('BSD-3-Clause')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer')
#            'python-sphinx-asdf'   # circular depends
#            'python-mistune>=3'
#            'python-numpy'
#            'python-toml')
#checkdepends=('python-pytest' 'python-asdf<3')   # circular depends
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('c6f1197bd8bc6eb857b4cc34f1288632')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}

    python -m build --wheel --no-isolation

#   msg "Building Docs"
#   ln -rs ${srcdir}/${_pyname}-${pkgver}/src/${_pyname}*egg-info \
#       build/lib/${_pyname}-${pkgver}-py$(get_pyver .).egg-info
#   PYTHONPATH="../build/lib" make -C docs html
}

#check() {
#    cd ${srcdir}/${_pyname}-${pkgver}
#
#    PYTHONPATH="build/lib" pytest -vv -l -ra --color=yes -o console_output_style=count #|| warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
#}

package_python-asdf_transform_schemas() {
    depends=('python>=3.9' 'python-asdf-standard>=1.1.0')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
