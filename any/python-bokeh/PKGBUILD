# Maintainer: Pierpaolo Valerio <gondsman@techgeek.co.in>
# Contributor: Excitable Snowball <excitablesnowball@gmail.com>

pkgname=python-bokeh
pkgver=3.3.4
pkgrel=1
pkgdesc='Interactive Web Plotting for Python'
arch=('any')
url='http://bokeh.pydata.org/'
license=('BSD')
source=(
  "https://pypi.io/packages/source/b/bokeh/bokeh-$pkgver.tar.gz"
)
sha256sums=(
  '73b7982dc2b8df15bf660cdddc8d3825e829195c438015a5d09824f1a7028368'
)
depends=('python-jinja'
         'python-contourpy'
         'python-numpy'
         'python-packaging'
         'python-pandas'
         'python-pillow'
         'python-yaml'
         'python-tornado'
         'python-xyzservices')
optdepends=('python-selenium: svg export'
            'geckodriver: svg export'
            'firefox: svg export'
            'nodejs: extending Bokeh'
            'python-psutil: detailed memory logging'
            'python-networkx: plot directly from NetworkX data'
            'python-sphinx: support sphinx documentation')
makedepends=('python-build' 'python-installer')

build() {
  cd "$srcdir/bokeh-$pkgver"
  python -m build --wheel
} 

package() {
  cd "$srcdir/bokeh-$pkgver"
  python -m installer "--destdir=$pkgdir" ./dist/*.whl
}
