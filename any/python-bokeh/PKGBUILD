# Maintainer: Pierpaolo Valerio <gondsman@techgeek.co.in>
# Contributor: Excitable Snowball <excitablesnowball@gmail.com>

pkgname=python-bokeh
pkgver=3.2.0
pkgrel=1
pkgdesc='Interactive Web Plotting for Python'
arch=('any')
url='http://bokeh.pydata.org/'
license=('BSD')
source=(
  "https://pypi.io/packages/source/b/bokeh/bokeh-$pkgver.tar.gz"
)
sha256sums=(
  'cdb3a8c3109d8d91a2814f4cddea045c14d049021f7fb6ce2a6b2c15e224bb17'
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
