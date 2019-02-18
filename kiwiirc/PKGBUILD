# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: Jack Allnutt <jack@allnutt.eu>
pkgname=kiwiirc
pkgver=1.1.0.r2044.g4c979963
pkgrel=1
pkgdesc="A hand-crafted web-based IRC client that you can enjoy"
arch=('any')
url="https://kiwiirc.com/"
license=('APACHE')
makedepends=('git' 'yarn')
install='kiwiirc.install'
source=(git+https://github.com/kiwiirc/kiwiirc)
md5sums=('SKIP')

pkgver () {
    cd "${pkgname}"
    (
        set -o pipefail
        git describe --long 2>/dev/null | sed -e 's/\([^-]*-g\)/r\1/;s/-/./g' -e 's/^v//'||
        printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
    )
}

build() {
    cd "$srcdir/$pkgname"
    yarn install
    yarn run build
}

package() {
    cd "$srcdir/$pkgname"

    mkdir -p $pkgdir/usr/share/webapps/
    cp -r dist $pkgdir/usr/share/webapps/kiwiirc
    sed 's/welcome/personal/' -i $pkgdir/usr/share/webapps/kiwiirc/static/config.json
}
