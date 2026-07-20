# Maintainer: Astro Benzene <universebenzene at sina dot com>

pkgbase=python-dask-image
_pname=${pkgbase#python-}
_pyname=${_pname//-/_}
pkgname=("python-${_pname}" "python-${_pname}-doc")
pkgver=2026.5.0
pkgrel=1
pkgdesc="Distributed image processing"
arch=('any')
url="https://image.dask.org"
license=('MIT')
makedepends=('python-setuptools-scm>=8'
             'python-build'
             'python-installer'
             'python-sphinx'
             'python-dask-sphinx-theme'
             'python-dask'
#            'python-pandas'
             'python-pims'
#            'python-pyarrow'
             'python-scipy'
             'python-tifffile')  # wheel required by new setuptools
checkdepends=('python-pytest-timeout'
#             'python-pytest-xdist'
              'python-pandas'
              'python-pyarrow')   # scipy, dask, tifffile, pims
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('f64f2ae3465d883afac29d162ccdb118')

prepare() {
    cd ${srcdir}/${_pyname}-${pkgver}
#
#    sed -i 's/np.in1d/np.isin/' tests/test_dask_image/test_ndmeasure/test_core.py
#    sed -i -e '/--flake8/d' -e '/exclude/a \    "docs*",' pyproject.toml
    sed -i -e '/--flake8/d' pyproject.toml
}

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    PYTHONPATH="." pytest || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count -p xdist -n 4 #
}

package_python-dask-image() {
    depends=('python>=3.9'
             'python-dask>=2024.4.1'
             'python-numpy>=1.18'
             'python-scipy>=1.7'
             'python-pims>=0.4.1'
             'python-tifffile>=2020.10.1'
         )
    optdepends=('python-pandas>=2.0.0: dataframe'
                'python-pyarrow>=16.0: dataframe'
                'python-dask-image-doc: Documentation for dask-image')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-dask-image-doc() {
    pkgdesc="Documentation for Python dask-image"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 ../../LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
