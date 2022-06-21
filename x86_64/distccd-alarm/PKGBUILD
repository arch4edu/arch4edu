# Maintainer: graysky <therealgraysky AT protonmail DOT com>
# Contributor: Jason Plum <jplum@archlinuxarm.org>
# Contributor: Kevin Mihelich <kevin@archlinuxarm.org>

pkgbase='distccd-alarm'
_subarchs=(armv7h armv8)
pkgname=("${_subarchs[@]/#/$pkgbase-}")
_date=20220530
pkgver=12.1.0.$_date
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
md5sums=('18ae923647b6d543a8b2a446a07d910c'
         '368d04d810f15aa42d7cefe20ae910f7'
         '6bd0313f391b8c21d9ba1eae88026bf7'
         '26741c886597e3fd8d8fc0a61aa8a49a'
         '9219b50ec9dce99aed3cca88a584c835')

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
