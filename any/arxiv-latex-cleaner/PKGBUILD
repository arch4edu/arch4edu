# Maintainer: Junfeng Qiao <qiaojunfeng at outlook.com>
# Contributor: 

pkgname=arxiv-latex-cleaner
_pkgname=arxiv-latex-cleaner
pkgver=1.0.8
pkgrel=1
pkgdesc="Easily clean the LaTeX code of your paper to submit to arXiv"
arch=('any')
url='https://github.com/google-research/arxiv-latex-cleaner'
license=('Apache')
makedepends=(git python-build python-installer python-wheel python-setuptools)
depends=('python>=3' 'python-absl' 'python-pillow>=6.2.0' 'python-pyyaml' 'python-regex')
source=("${_pkgname}::git+https://github.com/google-research/arxiv-latex-cleaner")

sha256sums=('SKIP')

build() {
  cd $_pkgname
  git checkout v$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd $_pkgname
  python -m installer --destdir="$pkgdir" "dist/arxiv_latex_cleaner-${pkgver}-py3-none-any.whl"
  install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE
}
