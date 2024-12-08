# Maintainer: Pierpaolo Valerio <gondsman@techgeek.co.in>
# Contributor: Excitable Snowball <excitablesnowball@gmail.com>

pkgname=python-bokeh
pkgver=3.6.2
pkgrel=1
pkgdesc='Interactive Web Plotting for Python'
arch=('any')
url='http://bokeh.pydata.org/'
license=('BSD')
source=(
  "https://pypi.io/packages/source/b/bokeh/bokeh-$pkgver.tar.gz"
)
sha256sums=(
  '2f3043d9ecb3d5dc2e8c0ebf8ad55727617188d4e534f3e7208b36357e352396'
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
makedepends=('python-build'
             'python-installer'
             'python-wheel'
             'python-setuptools-git-versioning'
             'python-colorama')

build() {
  cd "$srcdir/bokeh-$pkgver"
  python -m build --no-isolation --wheel
} 

package() {
  cd "$srcdir/bokeh-$pkgver"
  python -m installer "--destdir=$pkgdir" ./dist/*.whl
}
