# Maintainer: Pierpaolo Valerio <gondsman@techgeek.co.in>
# Contributor: Excitable Snowball <excitablesnowball@gmail.com>

pkgname=python-bokeh
pkgver=3.1.1
pkgrel=1
pkgdesc='Interactive Web Plotting for Python'
arch=('any')
url='http://bokeh.pydata.org/'
license=('BSD')
source=(
  "https://pypi.io/packages/source/b/bokeh/bokeh-$pkgver.tar.gz"
  'patch'
)
sha256sums=(
  'ba0fc6bae4352d307541293256dee930a42d0acf92e760c72dc0e7397c3a28e9'
  'cb7cf3d3189282521206a04ad32f1cbb2667a408426ece88b4f3d26bb873e9b9'
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

prepare() {
  patch -d "$srcdir/bokeh-$pkgver" -p1 < ./patch  # workaround for https://github.com/bokeh/bokeh/issues/13122
}

build() {
  cd "$srcdir/bokeh-$pkgver"
  python -m build --wheel
} 

package() {
  cd "$srcdir/bokeh-$pkgver"
  python -m installer "--destdir=$pkgdir" ./dist/*.whl
}
