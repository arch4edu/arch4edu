# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-theano-pymc
_pname=${pkgbase#python-}
_pyname=Theano-PyMC
pkgname=("python-${_pname}" "python-${_pname}-doc")
pkgver=1.1.2
pkgrel=3
pkgdesc="Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs"
arch=('any')
url="https://pypi.org/project/Theano-PyMC"
license=('BSD-3-Clause')
makedepends=('python-setuptools')
#            'python-wheel'
#            'python-build'
#            'python-installer'
#            'python-sphinx')
checkdepends=('python-pytest' 'python-scipy' 'python-filelock' 'python-pydot')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
#       'Makefile')
md5sums=('5ed1cb188fbe417946480219b5ba334b')

get_pyver() {
    python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))'
}

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}

#   ln -s ${srcdir}/Makefile doc
    sed -i -e 's/SafeConfigParser/ConfigParser/' -e 's/readfp/read_file/' versioneer.py
    sed -e '/import numpy.distutils/d' -e '/^import theano/a import numpy' \
        -e 's/numpy.distutils.misc_util.get_numpy_include_dirs()/[numpy.get_include()]/' \
        -e '/^\    except KeyError/s/KeyError/Exception/' -i theano/link/c/cmodule.py
    sed -e '/^import numpy.distutils/d' -i theano/tensor/blas.py
    sed -e '/CASTING/a np.bool = np.bool_' -i theano/scalar/basic.py
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
#   python -m build --wheel --no-isolation
    python setup.py build

#   msg "Building Docs"
#   cd ${srcdir}/${_pyname}-${pkgver}/doc
#   for _ftxt in $(find . -name '*.txt'); do mv -v ${_ftxt} ${_ftxt%.txt}.rst; done
#   PYTHONPATH="../build/lib" make html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
}

package_python-theano-pymc() {
    depends=('python>=3.6' 'python-scipy>=0.14' 'python-filelock')
    optdepends=('python-theano-pymc-doc: Documentation for Theano-PyMC')
    provides=('python-theano')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE.txt
    install -Dm644 -t "${pkgdir}/usr/share/doc/${pkgname}" README.rst
#   python -m installer --destdir="${pkgdir}" dist/*.whl
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    rm -r "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/tests"
    rm -r "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/bin/"/__{init__.py,pycache__}
}

package_python-theano-pymc-doc() {
    pkgdesc="Documentation for Python Theano-PyMC"
    cd ${srcdir}/${_pyname}-${pkgver}
#   cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -Dm644 -t "${pkgdir}/usr/share/licenses/${pkgname}" LICENSE.txt
#   install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE.txt
    install -dm755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a doc/* "${pkgdir}/usr/share/doc/${pkgbase}"
#   cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
