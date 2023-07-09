# Maintainer: Norbert Weber <norbert.weber_at_hzdr.de>
# Contributor: Marc Olesen
# Contributor: Xwang <xwaang1976@gmail.com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Andrew Fischer <andrew_at_apastron.co>
# Contributor: <gucong43216@gmail.com>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>

# Installs as (for example)
# /opt/OpenFOAM/OpenFOAM-v2306

pkgname=openfoam-com
pkgver=v2306
_distname=OpenFOAM
_dist=$_distname-$pkgver
pkgrel=1
pkgdesc="The open source CFD toolbox (www.openfoam.com)"
arch=('i686' 'x86_64')
url="http://www.openfoam.com"
license=('GPL3')
install="${pkgname}.install"
depends=('gcc' 'cgal' 'fftw' 'boost' 'openmpi' 'paraview' 'utf8cpp' 'scotch' 'parmetis')

source=('https://dl.openfoam.com/source/v2306/OpenFOAM-v2306.tgz')

md5sums=('236c87f9ba7640a0b3fd78171f50158a')

prepare() {
  if [ -n "$WM_PROJECT_DIR" ]
  then
    echo
    echo -e "\e[1m\e[5m\e[31mPlease make sure that no OpenFOAM version is sourced in bashrc.\e[0m"
    echo
    return 1
  fi

  projectDir="${srcdir}/${_dist}"

  # Generate and install the system preferences file
  echo "# Preferences for arch-linux
export WM_COMPILER_TYPE=system
export WM_MPLIB=SYSTEMOPENMPI
# End" \
  > "${projectDir}"/etc/prefs.sh


  # Configure components.
  # Use system values for boost/cgal, fftw, scotch, paraview

  "${projectDir}"/bin/tools/foamConfigurePaths \
    -boost boost-system \
    -cgal  cgal-system \
    -fftw  fftw-system \
    -kahip kahip-system \
    -scotch scotch-system \
    -paraview paraview-system \
    ;
}

build() {
  if [ -n "$WM_PROJECT_DIR" ]
  then
    echo
    echo -e "\e[1m\e[5m\e[31mPlease make sure that no OpenFOAM version is sourced in bashrc.\e[0m"
    echo
    return 1
  fi

  projectDir="${srcdir}/${_dist}"
  [ -f "$projectDir/etc/bashrc" ] || {
      echo "No $projectDir/etc/bashrc found"
      return 1
  }

  # changes to avoid linking problems related to gcc 11
  # check this for the next upgrade!
  pwd
  sed -i 's/g++$(COMPILER_VERSION) -std=c++11/g++$(COMPILER_VERSION) -std=c++14 -D_GLIBCXX_USE_CXX14_ABI=0/g' $projectDir/wmake/rules/General/Gcc/c++

  # Avoid external influence on the environment
  export FOAM_CONFIG_MODE="o"
  unset FOAM_SETTINGS

  set +e  # Turn errexit off

  source "$projectDir"/etc/bashrc '' || \
    echo "Ignore spurious sourcing error"

  # it seems, the bashrc file destroys 'projectDir'
  projectDir="${srcdir}/${_dist}"

  set -e  # Turn errexit back on
  cd "$projectDir" || exit

  # Dummy application for testing
  #./applications/test/00-dummy/Allwmake

  ./Allwmake -j -log=log.build

  # Check log for this type of content:
  #
  #   api   = 2006
  #   patch = 1
  #   bin   = 283 entries
  #   lib   = 139 entries

  [ -f log.build ] || {
      echo "No log.build file - build failed entirely"
      exit 1
  }

  bins="$( cat log.build | sed -ne 's/.*bin *= *\([0-9][0-9]*\).*/\1/p;' | sed -ne '$p' )"
  libs="$( cat log.build | sed -ne 's/.*lib *= *\([0-9][0-9]*\).*/\1/p;' | sed -ne '$p' )"

  if [ "${bins:=0}" = 0 ] || [ "${libs:=0}" = 0 ]
  then
      echo
      echo "Build failed with $bins executables and $libs libraries"
      echo "Check the log.build file"
      echo
      exit 1
  fi

  # Remove intermediate build artifacts
  rm -rf "${projectDir}/build"
}


package() {
  cd ${srcdir}

  # Installation directories
  parentDir="${pkgdir}/opt/${_distname}"
  projectDir="${parentDir}/${_dist}"

  # Create destination directories
  install -d "${parentDir}" "${pkgdir}"/etc/profile.d || return 1

  # Copy package to pkgdir
  cp -r "${srcdir}/${_dist}" "${parentDir}" || return 1

  # Permission fixes - for system-wide install and use
  chmod -R go+r "${pkgdir}"/opt
  chmod -R 755 "${projectDir}"/bin
  chmod -R 755 "${projectDir}"/etc

  [ -e "${projectDir}"/ThirdParty ] || \
      echo "system dependencies" >| "${projectDir}"/ThirdParty

  # create aliases
  echo "alias of='source /opt/${_distname}/${_dist}/etc/bashrc'" >> "${pkgdir}/etc/profile.d/openfoam-com.sh"
  echo "alias paraFoam='paraFoam -builtin'" >> "${pkgdir}/etc/profile.d/openfoam-com.sh"
}

# ---------------------------------------------------------------------------
