# Maintainer: Zhirui Dai <daizhirui@hotmail.com>

pkgname=python-dash
_pkgname=dash
pkgver=3.2.0
pkgrel=1
pkgdesc="A python framework for building analytical web applications"
arch=('any')
url="https://plot.ly/products/dash/"
license=('MIT')
depends=(
  python
  python-flask
  python-importlib-metadata
  python-nest-asyncio
  python-plotly
  python-requests
  python-retrying
  python-setuptools
  python-yaml
  python-werkzeug
)
optdepends=(python-flask-compress)
makedepends=(python-build python-installer python-setuptools python-wheel)
provides=('python-dash-core-components' 'python-dash-html-components' 'python-dash-renderer' 'python-dash-table')
conflicts=('python-dash-core-components' 'python-dash-html-components' 'python-dash-renderer' 'python-dash-table')
source=("https://pypi.org/packages/source/${_pkgname:0:1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=('93300b9b99498f8b8ed267e61c455b4ee1282c7e4d4b518600eec87ce6ddea55')

build(){
  cd "$_pkgname-$pkgver"
  python -m build -wn
}

package(){
  cd "$_pkgname-$pkgver"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  mkdir -p "${pkgdir}/etc/xdg"
  mv "${pkgdir}/usr/etc/jupyter" "${pkgdir}/etc/xdg"
  rmdir "${pkgdir}/usr/etc"
}

## vim:ts=2:sw=2:et:
