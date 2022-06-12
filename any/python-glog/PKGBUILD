# Maintainer : Daniel Bermond < gmail-com: danielbermond >

pkgbase=python-glog
pkgname=('python-glog' 'python2-glog')
pkgver=0.3.1
pkgrel=3
pkgdesc='A simple Google-style logging wrapper for Python'
arch=('any')
url='https://github.com/benley/python-glog/'
license=('BSD')
makedepends=('python' 'python2' 'python-setuptools' 'python2-setuptools')
source=("${pkgbase}-${pkgver}.tar.gz"::"https://github.com/benley/python-glog/archive/${pkgver}.tar.gz")
sha256sums=('b01af6f1118d2fa769c7657971deac8cecd71a3c6afe3e08328366740e802351')

prepare() {
    cp -a "${pkgbase}-${pkgver}" "${pkgbase}-${pkgver}-py2"
}

build() {
    printf '%s\n' '  -> Building for Python...'
    cd "${pkgbase}-${pkgver}"
    python setup.py build
    
    printf '%s\n' '  -> Building for Python2...'
    cd "${srcdir}/${pkgbase}-${pkgver}-py2"
    python2 setup.py build
}

package_python-glog() {
    depends=('python' 'python-gflags' 'python-six')
    
    cd "${pkgbase}-${pkgver}"
    python setup.py install --root="$pkgdir" --skip-build --optimize='1'
    
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_python2-glog() {
    pkgdesc='A simple Google-style logging wrapper for Python2'
    depends=('python2' 'python2-gflags' 'python2-six')
    
    cd "${pkgbase}-${pkgver}-py2"
    python2 setup.py install --root="$pkgdir" --skip-build --optimize='1'
    
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
