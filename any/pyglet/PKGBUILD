# Maintainer: konez2k@aur
# Contributor: bruceutut@aur
# Contributor: Kyle Keen <keenerd@gmail.com>
# Contributor: Douglas Soares de Andrade <douglas@archlinux.org>
# Contributor: Ryan Coyner <rcoyner@gmail.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgbase=pyglet
pkgname=('python-pyglet')
pkgver=2.1.12
pkgrel=1
pkgdesc="A cross-platform windowing and multimedia library for Python"
arch=('any')
url="https://github.com/pyglet/pyglet"
license=('BSD-3-Clause')
depends=('python' 'glu')
makedepends=('python-build' 'python-flit-core' 'python-installer' 'python-gobject' 'python-pillow' 'gstreamer')
optdepends=('ffmpeg: provides audio&video support'
    'openal: live audio')
source=("$pkgbase-$pkgver.zip::https://github.com/pyglet/pyglet/archive/refs/tags/v$pkgver.zip")
sha256sums=('1d4fc5075091834c3967c015efc1a1a8b615e67bcb1f8b1b300c4934503bd72a')

prepare() {
    cd "$srcdir/$pkgbase-$pkgver"
}

build() {
    cd "$srcdir/$pkgbase-$pkgver"
    python -m build --wheel --no-isolation
}

package_python-pyglet() {
    depends=('python' 'glu')
    cd "$srcdir/$pkgbase-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
