# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-parfive
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=2.1.0
pkgrel=1
pkgdesc="A HTTP and FTP parallel file downloader"
arch=('any')
url="https://parfive.readthedocs.io"
license=('MIT')
makedepends=('python-setuptools-scm'
             'python-wheel'
             'python-build'
             'python-installer'
             'python-sphinx-automodapi'
             'python-sphinx-autodoc-typehints'
             'python-sphinx-book-theme'
             'python-sphinx_contributors'
             'python-aiohttp'
             'python-tqdm'
             'graphviz')
checkdepends=('python-pytest-socket'
              'python-pytest-localserver'
              'python-pytest-asyncio'
              'python-aioftp'
              'python-aiofiles')   #python-aiohttp tqdm
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('3eea9c15a18d9837d62320d013a7ab28')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python -m build --wheel --no-isolation

    msg "Building Docs"
    PYTHONPATH="../build/lib" make -C docs html
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    # deselect tests that may take long time
    pytest \
        --deselect=parfive/tests/test_downloader.py::test_ftp || warning "Tests failed" # -vv -l -ra --color=yes -o console_output_style=count
}

package_python-parfive() {
    depends=('python>=3.8' 'python-tqdm>=4.27.0' 'python-aiohttp')
    optdepends=('python-aioftp>=0.17.1: For downloads over FTP'
                'python-parfive-doc: Documentation for Parfive')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}

package_python-parfive-doc() {
    pkgdesc="Documentation for Python Parfive"
    cd ${srcdir}/${_pyname}-${pkgver}/docs/_build

    install -D -m644 ../../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
