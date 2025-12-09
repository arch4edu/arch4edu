# Contributor: twa022 <twa022 at gmail dot com>

pkgname=python-screeninfo
pkgver=0.8.1
pkgrel=2
pkgdesc="Python library to fetch location and size of physical screens"
arch=('any')
url="https://github.com/rr-/screeninfo"
license=('MIT')
depends=('python')
optdepends=('libxinerama: xinerama backend'
           'libxrandr: randr backend'
           'libdrm: experimental DRM backend')
makedepends=('python-build' 'python-poetry-core' 'python-installer')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/rr-/${pkgname/python-/}/archive/${pkgver}.tar.gz")
sha256sums=('f6b3eeb22196a253611df1d3ee8fff549f2654730823ef4d2533018c27f13b09')

build() {
  cd "${srcdir}/${pkgname/python-/}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${pkgname/python-/}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dt "${pkgdir}/usr/share/licenses/${pkgname}" -m644 "${srcdir}/${pkgname/python-/}-${pkgver}/LICENSE.md"
}
