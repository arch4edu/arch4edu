# Maintainer: envolution
# Contributor: Jingbei Li <i@jingbei.li>
# Contributor: Xwang <xwaang1976@gmail.com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Andrew Fischer <andrew_at_apastron.co>
# shellcheck shell=bash disable=SC2034,SC2154

pkgbase=openfoam
pkgname=openfoam-org
pkgver=12.20250102
_pkgver="${pkgver%.*}"
_subver="${pkgver#*.}"
[[ "$pkgver" = "$_subver" ]] && _subver="version-$pkgver"
pkgrel=3
pkgdesc="The open source CFD toolbox (www.openfoam.org)"
_distpkgbase=OpenFOAM
_gitname=$_distpkgbase-$_pkgver
arch=('x86_64')
url="http://www.openfoam.org"
license=("GPL-3.0-or-later")
depends=(
  'bzip2'
  'paraview'
  'parmetis-git' #git until parmetis is fixed
  'scotch'
  'boost'
  'flex'
  'cgal'
  'zoltan' # provided separately from 'trilinos'
)
makedepends=('bash')
provides=('openfoam')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/OpenFOAM/$_gitname/archive/refs/tags/$_subver.tar.gz")
install="${pkgbase}.install"
md5sums=('91df55d65bb132a12fb709aeb37f4b00')

prepare() {
  if [ ! -d $srcdir/$_distpkgbase-$_pkgver ]; then
    mv $srcdir/$_gitname-$_subver $srcdir/$_distpkgbase-$_pkgver
    # Extract the current version and major of paraview and of scotch for use in the system preferences
    #_pversion=`pacman -Q paraview | sed -e 's/.* //; s/-.*//g'`
    _pversion=$(pacman -Q $(pacman -Qqo $(which paraview)) | sed -e 's/.* //; s/-.*//g')
    _pmajor=$(echo $_pversion | cut -d '.' -f1)
    _sversion=$(pacman -Q scotch | sed -e 's/.* //; s/-.*//g')

    # Generate and install the system preferences file
    echo "compilerInstall=system" >${srcdir}/prefs.sh
    echo "export WM_MPLIB=SYSTEMOPENMPI" >>${srcdir}/prefs.sh
    echo "export ParaView_VERSION=${_pversion}" >>${srcdir}/prefs.sh
    echo "export ParaView_MAJOR=${_pmajor}" >>${srcdir}/prefs.sh
    cp ${srcdir}/prefs.sh ${srcdir}/${_distpkgbase}-${_pkgver}/etc

    # Generate the scotch.sh file for arch
    echo "export SCOTCH_VERSION=scotch_${_sversion}" >${srcdir}/scotch.sh
    echo "export SCOTCH_ARCH_PATH=/usr" >>${srcdir}/scotch.sh
    cp ${srcdir}/scotch.sh ${srcdir}/${_distpkgbase}-${_pkgver}/etc/config

    sed -i 's/export SCOTCH_TYPE=.*/export SCOTCH_TYPE=system/' ${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc
    sed -i 's/export METIS_TYPE=.*/export METIS_TYPE=system/' ${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc
    sed -i 's/export PARMETIS_TYPE=.*/export PARMETIS_TYPE=system/' ${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc
    sed -i 's/export ZOLTAN_TYPE=.*/export ZOLTAN_TYPE=system/' ${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc
    cp ${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc ${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc.prepared
    sed -i 's|^# export FOAM_INST_DIR=.*|export FOAM_INST_DIR=/opt/\$WM_PROJECT|' ${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc.prepared
  fi
}

build() {
  # Setup the build environment
  export FOAM_INST_DIR=${srcdir}
  foamDotFile=${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc
  [ -f ${foamDotFile} ] || return 1

  # Enter build directory
  cd ${srcdir}/${_distpkgbase}-${_pkgver}

  # Build and clean up OpenFOAM
  bash -c """
  source ${foamDotFile}
  ./Allwmake
  wclean all
  wmakeLnIncludeAll
  """
}

package() {
  cd ${srcdir}

  # Create destination directories
  install -d "${pkgdir}/opt/${_distpkgbase}" "${pkgdir}/etc/profile.d"

  # Copy package to pkgdir
  cp -r "${srcdir}/${_distpkgbase}-${_pkgver}" "${pkgdir}/opt/${_distpkgbase}"

  # Add source file
  echo "export FOAM_INST_DIR=/opt/${_distpkgbase}" >${pkgdir}/etc/profile.d/openfoam-${_pkgver}.sh
  echo "alias ofoam=\"source \${FOAM_INST_DIR}/${_distpkgbase}-${_pkgver}/etc/bashrc\"" >>${pkgdir}/etc/profile.d/openfoam-${_pkgver}.sh
  chmod 755 "${pkgdir}/etc/profile.d/openfoam-${_pkgver}.sh"

  # Add stub thirdparty directory to keep openfoam happy
  install -d "${pkgdir}/opt/${_distpkgbase}/ThirdParty-${_pkgver}"

  # Permission fixes - for system-wide install and use
  chmod -R go+r "${pkgdir}/opt"
  chmod -R 755 "${pkgdir}/opt/${_distpkgbase}/${_distpkgbase}-${_pkgver}/bin"
  chmod -R 755 "${pkgdir}/opt/${_distpkgbase}/${_distpkgbase}-${_pkgver}/etc"
  rm "${pkgdir}/opt/${_distpkgbase}/${_distpkgbase}-${_pkgver}/etc/bashrc"
  install -Dm 755 "${srcdir}/${_distpkgbase}-${_pkgver}/etc/bashrc.prepared" "${pkgdir}/opt/${_distpkgbase}/${_distpkgbase}-${_pkgver}/etc/bashrc"
}

# vim:set ts=2 sw=2 et:
