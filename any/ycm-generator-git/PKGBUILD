# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: ssfdust <ssfdust@gmail.com>

pkgname=ycm-generator-git
pkgver=r128.b501516
pkgrel=1
pkgdesc="Generates config files for YouCompleteMe (https://github.com/Valloric/YouCompleteMe)"
arch=('any')
url="https://github.com/PaulHaeger/YCM-Generator"
license=('GPL')
depends=('make' 'python' 'clang')
provides=('ycm-generator')
conflicts=('ycm-generator')
install=ycm-generator.install
makedepends=('git')
optdepends=('cmake' 'autoconf' 'automake')
source=("git+${url}")
md5sums=('SKIP')

pkgver() {
    cd "${srcdir}"/YCM-Generator/
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
    cd "${srcdir}"/YCM-Generator/
    DESTDIR="${pkgdir}"/usr/share/YCM-Generator
    VIMPLUGIN="${pkgdir}"/usr/share/vim/vimfiles/plugin
    sed "s/expand(\"<sfile>:p:h:h\")/\"\/usr\/share\/YCM\-Generator\/\"/g" -i plugin/ycm-generator.vim
    mkdir -p "${DESTDIR}"
    mkdir -p "${VIMPLUGIN}"
    cp -r * "${DESTDIR}"

    #move vim plugin directory
    mv ${DESTDIR}/plugin/* ${VIMPLUGIN}

    #link the execute file to /usr/bin
    mkdir -p  "${pkgdir}"/usr/bin
    ln -s /usr/share/YCM-Generator/config_gen.py "${pkgdir}"/usr/bin/ycm_generator
}
