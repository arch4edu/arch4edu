# Maintainer:  Gerasimos Chourdakis <chourdak at in dot tum dot de>
pkgname=openfoam-selector
pkgver=1.0.6
pkgrel=1
pkgdesc="A simple tool to help manage multiple installed OpenFOAM versions"
arch=('any')
url="https://develop.openfoam.com/Community/feature-scripts/"
license=('BSD')
depends=('perl')
source=("https://sourceforge.net/projects/openfoam/files/utils/${pkgname}-${pkgver}.tgz")
md5sums=('371aabdbb72fa612c2404b2bfcd39401')

build() {
    cd "${pkgname}-${pkgver}"
	./configure \
    	--prefix=/usr \
    	--localstatedir=/var \
    	--with-sysconf-dir=/etc/openfoam \
    	--with-shell-startup-dir=/etc/profile.d
    make
}

package() {
    cd "${pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}/" install
    
    # install license
    install -Dm 644 LICENSE ${pkgdir}/usr/share/licenses/$pkgname/LICENSE
}
