pkgbase=pywbem
pkgname=('python-pywbem')
pkgver=0.17.2
pkgrel=1
pkgdesc="Python WBEM Client and Provider Interface"
arch=('any')
url='https://github.com/pywbem/pywbem'
license=('LGPLv2.1+')
makedepends=('python3' 'python-pip' 'python-yaml' 'python-ply')
source=("https://github.com/$pkgbase/$pkgbase/archive/${pkgver}/${pkgbase}-${pkgver}.tar.gz")
sha256sums=('63ec0bf03a109d3bfa962a05da26830a884144510376ac6f826c5f226a17a3af')
depends=("python-six" "python-ply" "python-pyaml" "python-pbr")

build() {
    :
}

package_python-pywbem() {
    _PY3_SITELIB=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
    cd $srcdir/$pkgbase-${pkgver}
    export PYTHONPATH="$pkgdir/$_PY3_SITELIB"
    export PBR_VERSION="${pkgver}"
    python3 setup.py build || return 1
    python3 setup.py install --root=$pkgdir || return 1
    rm -fv $pkgdir/usr/bin/*.bat
}
