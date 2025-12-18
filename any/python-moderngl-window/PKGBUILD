# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC1091,SC2034,SC2154,SC2164

_name=moderngl-window

pkgname=python-moderngl-window
pkgver=3.1.1
pkgrel=2
pkgdesc="A utility library for ModernGL making window creation and resource loading simple."

arch=("any")
license=("MIT")
url="https://github.com/moderngl/moderngl-window"

source=("$url/archive/refs/tags/$pkgver.tar.gz")
sha512sums=('16835aafd0f93094fb47b81001f2e5ab838dfd37b4c009b461c92ab6aeb93beabdbbedc3f0712766320cefa167578ea5f8c16b2d2d768f0f89358cc87000f3d6')

depends=(
    "python-moderngl"
    "python-numpy"
    "python-pillow"
    # AUR dependencies
    "python-pyglet"
    "python-pyglm"
    "python-pyrr"
)
makedepends=(
    "python-build"
    "python-installer"
    "python-setuptools"
    "python-wheel"
)
checkdepends=(
    "python-pytest"
    "python-pywavefront"
    "python-scipy"
    "python-trimesh"
    "python-virtualenv"
)

build () {
    cd "$srcdir/$_name-$pkgver"
    python -m build --wheel --no-isolation
}

check () {
    cd "$srcdir/$_name-$pkgver"

    if [ -z "$XDG_SESSION_TYPE" ]; then
        echo "Tests only work on X11 sessions. Skipping..."
        return
    fi

    python -m venv --system-site-packages venv
    source venv/bin/activate
    pip install ./dist/*.whl
    python -m pytest
    rm -rf venv
}

package () {
    cd "$srcdir/$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
