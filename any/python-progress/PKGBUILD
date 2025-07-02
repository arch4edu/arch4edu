# Maintainer: envolution
# Contributor: Carl Smedstad <carl.smedstad at protonmail dot com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
# Contributor: Guillaume Brogi <gui-gui at netcourrier dot com>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=python-progress
_name=${pkgname#python-}
pkgver=1.6.1
pkgrel=1
pkgdesc="Easy to use progress bars for Python"
arch=(any)
url="https://github.com/verigak/progress"
license=(ISC)
depends=(python)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
depends=(python)
source=("https://pypi.org/packages/source/${_name:0:1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('c1ba719f862ce885232a759eab47971fe74dfc7bb76ab8a51ef5940bad35086c')

_archive="$_name-$pkgver"

build() {
  cd "$_archive"

  python -m build --wheel --no-isolation
}

check() {
  cd "$_archive"

  python test_progress.py
}

package() {
  cd "$_archive"

  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
# vim: ts=2 sw=2 et:
# vim:set ts=2 sw=2 et:
