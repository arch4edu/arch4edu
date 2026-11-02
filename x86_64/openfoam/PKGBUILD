# SPDX-License-Identifier: 0BSD
# Maintainer: faruq <zhao@faruq.top>
# Contributor: envolution
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Xwang <xwaang1976@gmail.com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Andrew Fischer <andrew_at_apastron.co>
# shellcheck shell=bash disable=SC2034,SC2154

pkgbase=openfoam
pkgname=openfoam-org
pkgver=14.20261008+a4867fc
_pkgver="${pkgver%%.*}"
_subver_and_commit="${pkgver#*.}"
_subver="${_subver_and_commit%+*}"
_commit="${pkgver#*+}"
pkgrel=2
pkgdesc="The open source CFD toolbox (www.openfoam.org)"
_distpkgbase=OpenFOAM
_gitname="$_distpkgbase-$_pkgver"
# wmake uses its own optimisation/link flags and ignores makepkg CFLAGS/CXXFLAGS/LDFLAGS.
# Symbols are kept to simplify debugging of user-compiled solvers.
options=(!strip !buildflags)
arch=('x86_64')
url="https://www.openfoam.org"
license=("GPL-3.0-or-later")
depends=(
  glibc
  gcc-libs
  boost
  zlib
  metis
  parmetis
  scotch
  zoltan
  openmpi
  paraview
  vtk
  qt6-base
  fmt
  freetype2
  jsoncpp
  onetbb
  protobuf
  libglvnd
)
makedepends=(
  git
  cmake
  flex
  cli11
  nlohmann-json
  fast_float
)
optdepends=(
  'gnuplot: for foamMonitor and graph plotting'
  'gcc: for compiling user applications with wmake'
  'make: for compiling user applications with wmake'
)
provides=(openfoam)
source=(
  "$_gitname-$_subver::git+https://github.com/OpenFOAM/OpenFOAM-${_pkgver}.git#commit=${_commit}"
  openfoam.install
)
install="${pkgbase}.install"
sha256sums=('f7c0896107445cbc8c0d9ad805f74ee15d6901965316480b96f30a9e77fee00b'
  'a114fe7db76febbac9a6b37800c96391c0ca18948b4a17f2095f4ae5a2be2fc8')

prepare() {
  cd "$srcdir"

  if [[ -d "${_gitname}-${_subver}" ]]; then
    rm -rf "${_distpkgbase}-${_pkgver}"
    mv "${_gitname}-${_subver}" "${_distpkgbase}-${_pkgver}"
  fi

  local bashrc="${_distpkgbase}-${_pkgver}/etc/bashrc"

  sed -i "s|^export WM_PROJECT_VERSION=.*|export WM_PROJECT_VERSION=${_pkgver}|" "$bashrc"
  cp "$bashrc" "$bashrc.prepared"

  # The build uses bashrc; the installed copy is replaced by bashrc.prepared,
  # so adjust FOAM_INST_DIR for the post-install environment here.
  sed -i 's|^# export FOAM_INST_DIR=.*|export FOAM_INST_DIR=/opt/\$WM_PROJECT|' \
    "$bashrc.prepared"

  # Use system libraries from Arch
  cat <<EOF >"${_distpkgbase}-${_pkgver}/etc/prefs.sh"
# System-wide settings for Arch Linux
export SCOTCH_TYPE=system
export METIS_TYPE=system
export PARMETIS_TYPE=system
export ZOLTAN_TYPE=system
EOF

  # wmkdep only understands -I; CMake emits -isystem, so convert for
  # dependency generation (otherwise vtk/paraview headers are never tracked).
  sed -i 's#CXX_INCLUDES)")#CXX_INCLUDES)" | sed "s/-isystem /-I/g")#' \
    "${_distpkgbase}-${_pkgver}/applications/utilities/postProcessing/graphics/PVReaders/Allwmake"
}

build() {
  cd "${_distpkgbase}-${_pkgver}"

  # Initialise the OpenFOAM build environment
  source etc/bashrc || true
  if [[ -z $WM_OPTIONS || -z $FOAM_LIBBIN || ! -d $WM_PROJECT_DIR ]]; then
    echo "Failed to initialise the OpenFOAM build environment" >&2
    return 1
  fi

  # Extract the parallelism value from MAKEFLAGS
  local _jval=1
  if [[ $MAKEFLAGS =~ -j[[:space:]]*([0-9]+) ]]; then
    _jval="${BASH_REMATCH[1]}"
  elif [[ $MAKEFLAGS =~ --jobs=([0-9]+) ]]; then
    _jval="${BASH_REMATCH[1]}"
  fi

  # The build runs as a recursive make chain; without this flag, the nested
  # `make --eval` calls in PVReaders/Allwmake print "Entering directory"
  # to stdout, which pollutes ParaView_INCLUDES/DEFINES and breaks wmkdep.
  export MAKEFLAGS=--no-print-directory

  export PATH="$PWD/wmake:$PATH"
  wmakeLnIncludeAll
  ./Allwmake -s -q -j "$_jval"
}

package() {
  local installdir="${_distpkgbase}-${_pkgver}"
  local optdir="${pkgdir}/opt/${_distpkgbase}"

  install -d "$optdir" "${pkgdir}/etc/profile.d"

  cp -r "$installdir" "$optdir"

  local baseclean="${optdir}/${installdir}"

  # Remove build artefacts
  rm -rf "$baseclean"/platforms/*/applications "$baseclean"/platforms/*/src
  rm -f "$baseclean"/platforms/*/lib/*.o

  # Remove build metadata
  rm -rf "$baseclean/.git" "$baseclean/.arch_cache" \
    "$baseclean/etc/bashrc.prepared" \
    "$baseclean/applications/utilities/postProcessing/graphics/PVReaders/Make" \
    "$baseclean/applications/utilities/postProcessing/graphics/PVReaders/PVdummy/Make"

  # Configure profile.d
  local profile="${pkgdir}/etc/profile.d/openfoam-${_pkgver}.sh"
  {
    echo "export FOAM_INST_DIR=/opt/${_distpkgbase}"
    echo "alias ofoam=\"source \${FOAM_INST_DIR}/${installdir}/etc/bashrc\""
    echo "alias ofoam${_pkgver}=\"source \${FOAM_INST_DIR}/${installdir}/etc/bashrc\""
  } >"$profile"
  chmod 755 "$profile"

  # Keep an empty ThirdParty directory
  install -d "${optdir}/ThirdParty-${_pkgver}"

  # Install the prepared bashrc
  install -Dm755 "${installdir}/etc/bashrc.prepared" \
    "${baseclean}/etc/bashrc"

  install -Dm644 "${installdir}/COPYING" \
    -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
