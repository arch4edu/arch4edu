# Maintainer: Pierpaolo Valerio <gondsman@techgeek.co.in>
# Contributor: Excitable Snowball <excitablesnowball@gmail.com>

pkgname=python-bokeh
pkgver=3.10.0
pkgrel=1
pkgdesc='Interactive Web Plotting for Python'
arch=('any')
url='http://bokeh.pydata.org/'
license=('BSD')
source=(
  "https://pypi.io/packages/source/b/bokeh/bokeh-$pkgver.tar.gz"
)
sha256sums=(
  '73f0b0c06d7925ca2b6d52b2dc51c2533a11f667cc6944f1f06c039ccc57c5ce'
)
depends=('python-jinja'
         'python-narwhals'
         'python-numpy'
         'python-packaging'
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
            'python-sphinx: support sphinx documentation'
            'python-contourpy: contour plot'
            'python-pandas: dataframe')
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
