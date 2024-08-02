# Maintainer: Marco Rubin <marco.rubin@protonmail.com>
# Contributor: Brett Cornwall <ainola@archlinux.org>
# Contributor: Sergey Mastykov

_name=LinkChecker
pkgname=linkchecker
pkgver=10.4.0
pkgrel=2
pkgdesc="check links in web documents or full websites"
arch=('any')
url="https://github.com/linkcheck/linkchecker"
license=('GPL2')
depends=('python>=3.9' 'python-beautifulsoup4>=4.8.1' 'python-dnspython>=2.0' 'python-requests>=2.20')
makedepends=('python-hatch-vcs' 'python-hatchling>=1.8.0' 'python-installer' 'python-polib' 'python-setuptools-scm>=7.1.0')
optdepends=(
    'python-argcomplete>=1.8.1: For command-line completion'
    'python-pdfminer>=20181108: For reading PDF files'
)
source=("$url/archive/v$pkgver.tar.gz")
b2sums=('26d464f3bbef4e64f541e8d03e16679796198b75471408555cd2e9679c8c5355fc7ec66f89cd5214f179a0ff7d9adb186302d4ce56402819b8b231b69919a775')

build() {
    cd $pkgname-$pkgver
    hatchling build
}

package() {
    cd $pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}
