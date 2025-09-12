# Maintainer: envolution
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Xwang <xwaang1976@gmail.com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Andrew Fischer <andrew_at_apastron.co>
# shellcheck shell=bash disable=SC2034,SC2154

pkgbase=openfoam
pkgname=openfoam-org
pkgver=13.20250911+cde978a
_pkgver="${pkgver%%.*}"
_subver_and_commit="${pkgver#*.}"
_subver="${_subver_and_commit%+*}"
_commit="${pkgver#*+}"
pkgrel=1
pkgdesc="The open source CFD toolbox (www.openfoam.org)"
_distpkgbase=OpenFOAM
_gitname=$_distpkgbase-$_pkgver
options=(!strip)
arch=('x86_64')
url="http://www.openfoam.org"
license=("GPL-3.0-or-later")
depends=(
  glibc
  qt6-base
  gcc-libs
  metis
  vtk
  bzip2
  paraview
  parmetis
  scotch
  boost
  cgal
  zoltan
  openmpi
  gnuplot
  libxt
  libxml2
  freetype2
  double-conversion
  glew
  utf8cpp
  gl2ps
  python
  hdf5
  zlib
)
makedepends=(
  git
  cmake
  cli11 
  nlohmann-json 
  fast_float 
  flex
)
provides=(openfoam)
source=(
  "$_gitname-$_subver::git+https://github.com/OpenFOAM/OpenFOAM-${_pkgver}.git#commit=${_commit}"
  paraview.arch
  openfoam.install
)
install="${pkgbase}.install"
sha256sums=('c7371730f61b12147e5ae85561b2d0d25747dd310ab0a11ef5f598ace0c61ab3'
            'bbec057b1153a616ea388dc80fdaeb6337edc6150e0601f140a1304f82a10ddb'
            'a94080d4e5bc4736868269d66f61f5430dec961c70bdcdaa1c9a402dba5203d2')

_cache_notify() {
  local yellow='\033[1;33m'
  local red='\033[1;31m'
  local nc='\033[0m'
  echo -e "${yellow}==> Using build cache:${nc}"
  echo "    ${srcdir}/${_distpkgbase}-${_pkgver}"
  echo
  echo -e "${yellow}==> To build from scratch, run:${nc}"
  echo -e "    ${red}rm -rf ${srcdir}/${_distpkgbase}-${_pkgver}${nc}"
}

prepare() {
  _cachefile=${_distpkgbase}-${_pkgver}/.arch_cache
  if [[ -f "$_cachefile" ]] && grep -q "$pkgver" "$_cachefile"; then
    _cache_notify
  else
    rm -rf $_distpkgbase-$_pkgver
    mv $_gitname-$_subver $_distpkgbase-$_pkgver

    _bashrc=${_distpkgbase}-${_pkgver}/etc/bashrc
    sed -i "s|^export WM_PROJECT_VERSION=.*|export WM_PROJECT_VERSION=${_pkgver}|" "$_bashrc"
    cp ${_bashrc} ${_bashrc}.prepared

    # we'll be using $bashrc while building, and replace it with $bashrc.prepared
    # (below) during install - so we have to modify the FOAM_INST_DIR for post-install use
    sed -i 's|^# export FOAM_INST_DIR=.*|export FOAM_INST_DIR=/opt/\$WM_PROJECT|' \
      ${_bashrc}.prepared

    # Add system library settings to prefs.sh
    cat <<EOF >"${_distpkgbase}-${_pkgver}/etc/prefs.sh"
# System-wide settings for Arch Linux
export SCOTCH_TYPE=system
export METIS_TYPE=system
export PARMETIS_TYPE=system
export ZOLTAN_TYPE=system
EOF

    echo $pkgver >$_cachefile
  fi

  # Drop in Arch paraview environment script
  cd ${_distpkgbase}-${_pkgver}
  cp ${srcdir}/paraview.arch etc/config.sh/paraview
}

build() {
  cd ${_distpkgbase}-${_pkgver}
  # export FOAM_VERBOSE=1
  # export PS1='~' # required for verbosity checks
  # Setup the build environment
  source etc/bashrc || true

  # see if we have extra threads available in /etc/makepkg.conf MAKEFLAGS
  [[ $MAKEFLAGS =~ -j[[:space:]]*([0-9]+) ]] &&
    _jval="${BASH_REMATCH[1]}" || _jval=1
  
  export PATH="$PWD/wmake:$PATH" 
  wmakeLnIncludeAll
  ./Allwmake -s -q -j ${_jval:=1}
}

package() {
  # Create destination directories
  install -d "${pkgdir}/opt/${_distpkgbase}" "${pkgdir}/etc/profile.d"

  # Copy package to pkgdir
  cp -r "${_distpkgbase}-${_pkgver}" "${pkgdir}/opt/${_distpkgbase}"

  # Clean up build files
  # https://openfoamwiki.net/index.php/Installation/Delete_intermediate_files#OpenFOAM_v1706_and_newer
  _baseclean="${pkgdir}/opt/${_distpkgbase}/${_distpkgbase}-${_pkgver}"
  rm -rf ${_baseclean}/platforms/*/applications ${_baseclean}/platforms/*/src

  # Add bash profile
  _bash_profile=${pkgdir}/etc/profile.d/openfoam-${_pkgver}.sh
  echo "export FOAM_INST_DIR=/opt/${_distpkgbase}" >$_bash_profile
  echo "alias ofoam=\"source \${FOAM_INST_DIR}/${_distpkgbase}-${_pkgver}/etc/bashrc\"" \
    >>$_bash_profile
  echo "alias ofoam${_pkgver}=\"source \${FOAM_INST_DIR}/${_distpkgbase}-${_pkgver}/etc/bashrc\"" \
    >>$_bash_profile
  chmod 755 $_bash_profile

  # Add stub thirdparty directory to keep openfoam happy
  install -d "${pkgdir}/opt/${_distpkgbase}/ThirdParty-${_pkgver}"

  install -Dm755 "${_distpkgbase}-${_pkgver}/etc/bashrc.prepared" \
    "${pkgdir}/opt/${_distpkgbase}/${_distpkgbase}-${_pkgver}/etc/bashrc"
  install -Dm644 ${_distpkgbase}-${_pkgver}/COPYING -t $pkgdir/usr/share/licenses/$pkgname
}

# vim:set ts=2 sw=2 et:
