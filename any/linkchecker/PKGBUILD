# Maintainer: Marco Rubin <marco.rubin@protonmail.com>
# Contributor: Brett Cornwall <ainola@archlinux.org>
# Contributor: Sergey Mastykov

_name=LinkChecker
pkgname=linkchecker
pkgver=10.4.0
pkgrel=3
pkgdesc="check links in web documents or full websites"
arch=('any')
url="https://github.com/linkcheck/linkchecker"
license=('GPL2')
depends=('python>=3.9' 'python-beautifulsoup4>=4.8.1' 'python-dnspython>=2.0' 'python-requests>=2.20')
makedepends=('python-hatch-vcs' 'python-hatchling>=1.8.0' 'python-installer' 'python-polib' 'python-setuptools-scm>=7.1.0')
optdepends=('python-argcomplete>=1.8.1: For command-line completion'
            'python-pdfminer>=20181108: For reading PDF files')
source=("$url/archive/v$pkgver.tar.gz")
b2sums=('9aa5c50c5221cd82b9f28b5533d3bcb29f0917cb842f6b96ce42fc751dcbf8629f86bf6587224828c95097ef106f6d63beda5fc7a3f1e12e9854e6820aae6ff0')

build() {
    cd $pkgname-$pkgver
    hatchling build
}

package() {
    cd $pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
