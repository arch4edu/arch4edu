# Maintainer: Marco Rubin <marco.rubin@protonmail.com>
# Contributor: Brett Cornwall <ainola@archlinux.org>
# Contributor: Sergey Mastykov

_name=LinkChecker
pkgname=linkchecker
pkgver=10.6.0
pkgrel=1
pkgdesc="check links in web documents or full websites"
arch=('any')
url="https://github.com/linkcheck/linkchecker"
license=('GPL2')
depends=('python>=3.9' 'python-beautifulsoup4>=4.8.1' 'python-dnspython>=2.0' 'python-requests>=2.20')
makedepends=('python-hatch-vcs' 'python-hatchling>=1.8.0' 'python-installer' 'python-polib' 'python-setuptools-scm>=7.1.0')
optdepends=('python-argcomplete>=1.8.1: For command-line completion'
            'python-pdfminer>=20181108: For reading PDF files')
source=("$url/archive/v$pkgver.tar.gz")
b2sums=('50a1f1e0004565f649c653d49ddccb78f7fc98b7bb364b1b2520aa9292c6498f3754195cf09f02b9680f5ffc41a3b567bfd3dcebe42cc68c375b8ab28cc6b5de')

build() {
    cd $pkgname-$pkgver
    hatchling build
}

package() {
    cd $pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
