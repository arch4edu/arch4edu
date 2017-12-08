# Maintainer: Vic Luo <vicluo96 at gmail.com>

pkgname=cquery-git
_pkgname=cquery
pkgver=695.336ba46
pkgrel=1
pkgdesc='Low-latency vscode language server for large C++ code-bases, powered by libclang.'
arch=('any')
url='https://github.com/jacobdufault/cquery/'
license=('MIT')
depends=('clang' 'libtinfo5')
makedepends=("git" "python2")
source=('git+https://github.com/jacobdufault/cquery.git' 'cquery-sh')
md5sums=(
    'SKIP'
    'cdefbd32658ab9c6a531deb64c512c5d'
)

pkgver() {
    cd $_pkgname
    echo $(git rev-list --count master).$(git rev-parse --short master)
}

prepare() {
    cd $_pkgname
    git submodule update --init --recursive
    sed -e "s/, '-Werror'//g" -i ./wscript
    sed -e "s/rpath=\[CLANG_LIB_DIR\]/rpath=\['lib'\]/g" -i ./wscript
}

build() {
    cd $_pkgname
    python2 waf configure
    python2 waf build
    cd build
    ls -l lib || ln -s clang+llvm*/lib lib
}

check() {
    cd $_pkgname/build
    yes | ./app --test-unit --test-index
}

package() {
    install -m 755 -d "${pkgdir}/opt/cquery/"
    cd $_pkgname/
    cp -rf ./clang_resource_dir ${pkgdir}/opt/cquery/ 
    cd build/
    install -m 755 ./app "${pkgdir}/opt/cquery/cquery"
    install -m 755 -d "${pkgdir}/opt/cquery/lib"
    install -m 755 -t "${pkgdir}/opt/cquery/lib" lib/*.so*
    install -m 755 -d "${pkgdir}/usr/bin"
    install -D -m 755 "${srcdir}/cquery-sh" "${pkgdir}/usr/bin/cquery"
}
