# Maintainer: graysky <therealgraysky AT protonmail DOT com>
# Contributor: Jason Plum <jplum@archlinuxarm.org>
# Contributor: Kevin Mihelich <kevin@archlinuxarm.org>

pkgbase='distccd-alarm'
_subarchs=(armv7h armv8)
pkgname=("${_subarchs[@]/#/$pkgbase-}")
_date=20260119
pkgver=15.2.1.$_date
pkgrel=1
_URL="https://archlinuxarm.org/builder/xtools"
#_URL="https://archlinuxarm.org/builder/xtools/$pkgver-$pkgrel"
arch=('x86_64')
license=('GPL' )
pkgdesc="Official toolchain for Arch ARM builds via distcc on x86_64 volunteers"
url="https://github.com/graysky2/distccd-alarm"
depends=('distcc')
options=('libtool' 'emptydirs' '!strip')
source=(
"x-tools7h-$_date.tar.xz::$_URL/x-tools7h.tar.xz"
"x-tools8-$_date.tar.xz::$_URL/x-tools8.tar.xz"
'config.in' 'service.in' 'readme.in'
)
noextract=(
"x-tools7h-$_date.tar.xz"
"x-tools8-$_date.tar.xz"
)
#PKGEXT='.pkg.tar'
sha256sums=('0570d1e7a88e211971c54c2347fedfcf060557d4f6a2ee6bd40bcebe32b6581a'
            'ecb69c45c627ea69016bd73d06c38a10863550a687b956fb7170550bf47e3fe4'
            '9267e582cec2c8fad5d3e2945ddd0438a74c3d81f2915c21e6dff854f09d6bd0'
            '0826429ae7faae43fac60202f717da44c05a1246eb50593a19b4b9574a8aab1c'
            'f00bfbd7c767c1a2f4089b08f90880005f76f26c1026869213d3ee4a2b764c52')

build() {
  # setup config and services
  _path=('7h' '8')
  _name=('arm-unknown-linux-gnueabihf' 'aarch64-unknown-linux-gnu')
  _port=('3635' '3636')

  for i in 0 1; do
    # make service units
    sed "s/@VERS@/${_subarchs[$i]}/" <service.in >"distccd-${_subarchs[$i]}.service"

    # make configs
    sed -e "s/@VERS@/${_path[$i]}/" \
      -e "s/@PATH@/${_name[$i]}/" \
      -e "s/@LOG@/${_subarchs[$i]}/" \
      -e "s/@PORT@/${_port[$i]}/" \
      <config.in >"distccd-${_subarchs[$i]}.conf"

    # make readme.install
    sed -e "s/@VERS@/${_subarchs[$i]}/g" \
      -e "s/@PORT@/${_port[$i]}/g" \
      <readme.in >${startdir}/"${_subarchs[$i]}".install
  done
}

_package_subarch() {
  # backup configs
  backup=("etc/conf.d/distccd-$1")
  pkgdesc="A toolchain for Arch ARM $1 builds via distcc"
  install="$1.install"

  # install symlink to distccd
  install -d "${pkgdir}/usr/bin"
  ln -sf /usr/bin/distccd "${pkgdir}/usr/bin/distccd-$1"
  
  # install whitelist for toolchain new for v3.3
  install -d "${pkgdir}/usr/lib/distcc"
  for bin in c++ cc clang clang++ cpp g++ gcc; do
    ln -sf /usr/bin/distcc "${pkgdir}/usr/lib/distcc/$3-$bin"
  done
  
  # install toolchain
  install -d "${pkgdir}/opt"
  bsdtar -x --uid 0 --gid 0 -f "${srcdir}/$2-$_date.tar.xz" -C "${pkgdir}/opt"

  # FS#67629 - since distcc is a dependency there is no need to provide a sysuser.d config

  # install services
  install -Dm644 "${srcdir}/distccd-$1.service" \
    "${pkgdir}/usr/lib/systemd/system/distccd-$1.service"
  
  # install config
  install -Dm644 "${srcdir}/distccd-$1.conf" \
    "${pkgdir}/etc/conf.d/distccd-$1"
}

for i in "${!_subarchs[@]}"; do
  _bins=('armv7l-unknown-linux-gnueabihf' 'aarch64-unknown-linux-gnu')
  _xtoolsdir="${source[i]##*/}"
  _xtoolsdir="${_xtoolsdir%%.*}"
  eval 'package_distccd-alarm-'${_subarchs[i]}'() {
 _package_subarch '${_subarchs[i]}' '${_xtoolsdir}' '${_bins[i]}'
}'
done
