# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

pkgbase=python-glog
pkgname=('python-glog' 'python2-glog')
pkgver=0.3.1
pkgrel=1
arch=('any')
url="https://github.com/benley/python-glog/"
license=('BSD')
makedepends=('python' 'python2' 'python-setuptools' 'python2-setuptools')
source=("${pkgbase}-${pkgver}.tar.gz"::"https://github.com/benley/python-glog/archive/${pkgver}.tar.gz")
sha256sums=('b01af6f1118d2fa769c7657971deac8cecd71a3c6afe3e08328366740e802351')

prepare() {
    cp -a "${pkgbase}-${pkgver}" "${pkgbase}-${pkgver}-py2"
}

build() {
    msg2 "Building for Python3..."
    cd "${pkgbase}-${pkgver}"
    python setup.py build
    
    msg2 "Building for Python2..."
    cd "${srcdir}/${pkgbase}-${pkgver}-py2"
    python2 setup.py build
}

package_python-glog() {
    pkgdesc="A simple Google-style logging wrapper for Python3"
    depends=('python' 'python-gflags' 'python-six')
    
    cd "${pkgbase}-${pkgver}"
    python setup.py install --root="$pkgdir" --optimize=1
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-glog() {
    pkgdesc="A simple Google-style logging wrapper for Python2"
    depends=('python2' 'python2-gflags' 'python2-six')
    
    cd "${pkgbase}-${pkgver}-py2"
    python2 setup.py install --root="$pkgdir" --optimize=1
    
    # license
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
