# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor:  Martin C. Doege <mdoege at compuserve dot com>

pkgname=torque
pkgver=6.1.3.h5
pkgrel=1
pkgdesc='An open source resource manager providing control over batch jobs and distributed compute nodes'
arch=('x86_64' 'armv6h' 'armv7h' 'aarch64')
url="http://www.adaptivecomputing.com/products/open-source/torque/"
license=('custom')
depends=('openssh' 'libxml2' 'tcl' 'boost-libs')
makedepends=('make' 'boost' 'tk')
backup=(var/spool/torque/server_name var/spool/torque/mom_priv/config var/spool/torque/serv_priv/{nodes,serverdb})
install=torque.install
source=("https://github.com/adaptivecomputing/torque/archive/refs/heads/${pkgver}.tar.gz")
md5sums=('121347809f32353f02385f982cb980a3')

prepare() {
  cd "$srcdir/$pkgname-$pkgver"

  sed '511s/job_mutex/job_mutex != NULL/' -i src/server/job_container.c
  sed 's/\/sbin\/ldconfig/:/g' -i src/resmom/Makefile.am
}

build() {
  cd "$srcdir/$pkgname-$pkgver"

  sed -e '/^CC="$CXX"$/d' -i configure.ac
  ./autogen.sh

  CPPFLAGS="$CPPFLAGS -O2 -fpermissive --std=c++0x" \
  ./configure --prefix="/usr" --sbindir="/usr/bin" --disable-gcc-warnings

  sed 's/gcc/g++/g' -i $(find . -name Makefile)
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install

  # License
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/torque/LICENSE"
}

# vim:set ts=2 sw=2 et:
