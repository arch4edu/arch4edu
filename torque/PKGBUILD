# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor:  Martin C. Doege <mdoege at compuserve dot com>

pkgname="torque"
pkgver=6.1.0
pkgrel=1
linknum="3170"
pkgdesc='An open source resource manager providing control over batch jobs and distributed compute nodes'
arch=('i686' 'x86_64')
url="http://www.adaptivecomputing.com/products/open-source/torque/"
license=('custom')
depends=('openssh' 'libxml2' 'tk' 'boost-libs')
makedepends=('make' 'gcc' 'boost')
backup=(var/spool/torque/server_name var/spool/torque/mom_priv/config var/spool/torque/serv_priv/{nodes,serverdb})
options=(!libtool)
install=torque.install
source=("torque-"$pkgver".tar.gz"::'http://www.adaptivecomputing.com/index.php?wpfb_dl='$linknum)
md5sums=('346a5d7cafb9ad0baa8193897a0e7acc')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	sed 's/#include <sys\/tty.h>/#include <linux\/tty.h>/' -i src/resmom/mom_inter.c
	sed 's/\/sbin\/ldconfig/:/g' -i src/resmom/Makefile.{am,in}
	CPPFLAGS="-DUSE_INTERP_ERRORLINE -DUSE_INTERP_RESULT -Wno-misleading-indentation -Wno-deprecated-declarations" ./configure --prefix="/usr" --sbindir="/usr/bin" --disable-gui
	make
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make DESTDIR="$pkgdir" install
	# License
	install -D -m644 "${srcdir}/$pkgname-$pkgver/"PBS_License.txt "${pkgdir}/usr/share/licenses/torque/PBS_License.txt"
}

