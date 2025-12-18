# Maintainer: Groctel <aur@taxorubio.com>
# Maintainer: Naveen M K <naveen521kk@gmail.com>
# shellcheck disable=SC2034,SC2154,SC2164

pkgbase=manimce
pkgname=manim
pkgver=0.19.0
pkgrel=1
pkgdesc="Animation engine for explanatory math videos (community edition)."

arch=("any")
license=("MIT" "custom")
url="https://github.com/ManimCommunity/manim"

source=("$url/releases/download/v$pkgver/$pkgname-$pkgver.tar.gz")
sha512sums=('b106df03f0b826ccd928abe941665e4f57960d149e6b836f18fc900da5065f752e8eeec951919c92c7aedc36188f45d03826378bb3249bdcb79bc19f7dc3f6e1')

conflicts=("python-manimlib")

depends=(
    "ffmpeg"
    "python"
    "python-beautifulsoup4"
    "python-cairo"
    "python-click"
    "python-decorator"
    "python-importlib-metadata"
    "python-numpy"
    "python-pillow"
    "python-pygments"
    "python-rich"
    "python-scipy"
    "python-tqdm"
    "python-typing_extensions"
    "python-watchdog"
    "python-networkx"
    # Aur dependencies
    "python-audioop-lts"
    "python-av"
    "python-cloup"
    "python-backports.cached_property"
    "python-glcontext"
    "python-isosurfaces"
    "python-manimpango"
    "python-mapbox-earcut"
    "python-moderngl"
    "python-moderngl-window"
    "python-pydub"
    "python-screeninfo"
    "python-skia-pathops"
    "python-srt"
    "python-svgelements"
)
makedepends=(
    "python-build"
    "python-installer"
    "python-poetry-core"
    "python-setuptools"
    "python-wheel"
)
optdepends=(
    "python-dearpygui: Graphical frontend"
    "jupyterlab: Jupyter integration"
    "python-grpcio-tools: WebGL renderer"
    "texlive-core: LaTeX support"
)

build () {
    cd "$srcdir/$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package () {
    cd "$srcdir/$pkgname-$pkgver"

    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -D -m644 LICENSE.community "$pkgdir/usr/share/licenses/$pkgname/LICENSE.community"
}
