# Maintainer: Leo Mao <leomaoyw at gmail dot com>

pkgname="python-imageio"
_pkgname="imageio"
pkgver=2.5.0
pkgrel=2
pkgdesc="a Python library that provides an easy interface to read and write a wide range of image data"
arch=('x86_64')
_github="imageio/imageio"
_pypiname="imageio"
url="https://github.com/imageio/imageio"
license=('BSD')
depends=('python-numpy' 'python-pillow')
optdepends=('avbin' 'python-imageio-ffmpeg' 'freeimage' 'python-astropy' 'simpleitk')
makedepends=('python' 'python-setuptools')
source=("https://github.com/imageio/imageio/archive/v${pkgver}.tar.gz")
sha256sums=('a504befcd1c538da9ea496d3f043a3c469418d6ec459eba8eed39340946dab81')

build() {
  msg "Building Python 3"
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1 --skip-build
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"

  # remove utilities for downloading binary dependencies
  rm $pkgdir/usr/bin/{imageio_download_bin,imageio_remove_bin}
}

# vim:set ts=2 sw=2 et:<Paste>
