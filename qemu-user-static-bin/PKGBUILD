# Maintainer: David Herrmann <dh.herrmann@gmail.com>

_pkgname=qemu-user-static
pkgdesc='A generic and open source machine emulator, statically linked'
pkgver=3.1
pkgrel=8
_debrel='+dfsg-8'

pkgname=$_pkgname-bin
arch=('x86_64' 'i686' 'aarch64')
url="http://wiki.qemu.org"
license=('GPL2' 'LGPL2.1')
depends=()
makedepends=('perl')
provides=("$_pkgname" "qemu-user")
conflicts=("$_pkgname" "qemu-user")

if [ "$CARCH" = 'x86_64' ] ; then
  _debsrc="${_pkgname}_${pkgver}${_debrel}_amd64.deb"
  _csum=02578dafdffe8953a15ca62d3cc10e87bbf31294052061966c908a25bddbce46
elif [ "$CARCH" = 'i686' ] ; then
  _debsrc="${_pkgname}_${pkgver}${_debrel}_i386.deb"
  _csum=SKIP
elif [ "$CARCH" = 'aarch64' ] ; then
  _debsrc="${_pkgname}_${pkgver}${_debrel}_arm64.deb"
  _csum=SKIP
else
  _debsrc="${_pkgname}_${pkgver}${_debrel}_${CARCH}.deb"
  _csum=SKIP
fi

source=(
  "qemu-user-static-${pkgver}${_debrel}_${CARCH}.deb::http://ftp.debian.org/debian/pool/main/q/qemu/${_debsrc}"
  "qemu.binfmt" # http://src.fedoraproject.org/rpms/qemu/raw/master/f/qemu.binfmt
)
sha256sums=(
  "$_csum"
  '0c1e998022f3306946cd66678f363b10d93b1309c5bbc9f0e6064080a3b604f9'
)

prepare() {
  rm -Rf build
  mkdir build
}

build() {
  cd build
  tar -xJf ../data.tar.xz -C .
  create_binfmts
}

package() {
  cd build

  mkdir -p "$pkgdir"/usr/bin/
  mkdir -p "$pkgdir"/usr/share/man/man1
  mkdir -p "$pkgdir"/usr/lib/binfmt.d

  cp usr/bin/qemu-*-static "$pkgdir"/usr/bin/
  cp usr/lib/binfmt.d/qemu-*-static.conf "$pkgdir"/usr/lib/binfmt.d/
  cp usr/share/man/man1/qemu-*-static.1.gz "$pkgdir"/usr/share/man/man1/
}

create_binfmts() {
  rm -Rf usr/lib/binfmt.d
  mkdir -p usr/lib/binfmt.d

  # Qemu upstream now has a script to create the binfmt
  # configurations, in ./scripts/qemu-binfmt-conf.sh. We
  # should switch to it, rather than parsing the old
  # Fedora configuration manually.

  for i in \
          aarch64 \
          alpha \
          armeb \
          arm \
          cris \
          i386 \
          i486 \
          m68k \
          microblazeel \
          microblaze \
          mips64el \
          mips64 \
          mipsel \
          mips \
          ppc64abi32 \
          ppc64le \
          ppc64 \
          ppc \
          s390x \
          sh4eb \
          sh4 \
          sparc32plus \
          sparc64 \
          sparc \
          x86_64 \
          ; do

    # Skip emulator of target machine (and dependents)
    if [ "$CARCH" = "$i" ] ; then
      continue
    elif [ "$CARCH" = "x86_64" ] ; then
      if [ "$i" = "i386" ] || \
         [ "$i" = "i486" ] || \
         [ "$i" = "x86_64" ] ; then
        continue
      fi
    elif [ "$CARCH" = "i686" ] ; then
      if [ "$i" = "i386" ] || \
         [ "$i" = "i486" ] ; then
        continue
      fi
    fi

    CFG=$(grep "^:qemu-$i:" "${srcdir}/qemu.binfmt" | tr -d '\n')
    if [ -z "$CFG" ] ; then
        continue
    fi

    echo -E -n "$CFG" >"usr/lib/binfmt.d/qemu-$i-static.conf"
    perl -i -p -e "s/bin\/qemu-([^:]+):\$/bin\/qemu-\1-static:F/" \
            "usr/lib/binfmt.d/qemu-$i-static.conf"
  done
}

# vim:set sw=2 et:
