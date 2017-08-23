# Original Contributor: aquavitae <aquavitae69: gmail>
# Current Maintainer: Andrew Fischer <andrew_at_ltengsoft.com>
# Packager: Heavysink

pkgname=openfoam3.0-git

# The distributors package name
_distpkgname=OpenFOAM
_distpkgver=3.0.x
_gitname=$_distpkgname-$_distpkgver
pkgver=20170710.221b8ab7
pkgrel=4
pkgdesc="The open source CFD toolbox"
arch=('i686' 'x86_64')
url="http://www.openfoam.com"
license=('GPL')
groups=()
depends=('cgal' 'paraview' 'parmetis' 'scotch' 'boost')
makedepends=('git' 'flex')
optdepends=()
replaces=()
backup=()
options=()
source=(git+https://github.com/OpenFOAM/OpenFOAM-3.0.x.git
	 'decomp-options.patch'
	 'paraFoam.patch'
	 'scotch-options.patch'
	 'boost.patch'
	 'prefs.sh'
	 'scotch.sh'
   'paraview.sh')
noextract=()
install=openfoam.install
md5sums=('SKIP'
         'dcb09c65c450601203f48f7d5177ced2'
         'fb84ecc41b63304064b88ee3291513be'
         '905fbd21aa780a57530d65818425ec6c'
	   'e0bc9bb43c48acbe06fc834cb93ce949'
         'SKIP'
         'SKIP'
         'SKIP')

pkgver() {
	cd "$srcdir/$_gitname"
	git log -1 --date=short --format="%cd.%h" | tr -d '-'
}


build() {
  # Extract the current version and major of paraview and of scotch for use in the system preferences
  _pversion1=`pacman -Q {paraview,paraview-manta,paraview-git} | sed -e 's/.* //; s/-.*//g'`
  _pversion=`echo $_pversion1 | grep .`
  _pmajor=`echo $_pversion | cut -d '.' -f1`
  _sversion=`pacman -Q scotch | sed -e 's/.* //; s/-.*//g'`

  # Generate and install the system preferences file
  echo "compilerInstall=system" > $startdir/prefs.sh
  echo "export WM_MPLIB=SYSTEMOPENMPI" >> $startdir/prefs.sh
  echo "export ParaView_VERSION=$_pversion" >> $startdir/prefs.sh
  echo "export ParaView_MAJOR=$_pmajor" >> $startdir/prefs.sh
  cp $startdir/prefs.sh $srcdir/$_gitname/etc || return 1

  # Generate the scotch.sh file for arch
  echo "export SCOTCH_VERSION=scotch_$_sversion" > $startdir/scotch.sh
  echo "export SCOTCH_ARCH_PATH=/usr" >> $startdir/scotch.sh
  cp $startdir/scotch.sh $srcdir/$_gitname/etc/config || return 1

  # Generate the paraview.sh file for Paraview plugin
  sed -i -e "s|paraviewversion|ParaView_VERSION=${_pversion}|g" ${srcdir}/paraview.sh
  sed -i -e "s|paraviewmajor|ParaView_MAJOR=${_pmajor}|g" ${srcdir}/paraview.sh
  cp ${srcdir}/paraview.sh ${srcdir}/${_distpkgname}-3.0.x/etc/config #|| return 1

  # Patch for archlinux parmetis, paraview and openmpi paths, and ptscotch link lines
  patch -p1 < $startdir/decomp-options.patch
  patch -p1 < $startdir/paraFoam.patch
  patch -p1 < $startdir/scotch-options.patch
  patch -p1 < $startdir/boost.patch

  # Setup the build environment
  export FOAM_INST_DIR=$srcdir 
  foamDotFile=$srcdir/$_gitname/etc/bashrc
  [ -f $foamDotFile ] && . $foamDotFile || return 1

  #Fix flex version
  cd ${srcdir}/$_gitname  
  find . -name '*.L' -print -exec sed -i -e 's|YY_FLEX_SUBMINOR_VERSION < 34|YY_FLEX_SUBMINOR_VERSION < 34 \&\& YY_FLEX_MINOR_VERSION < 6|g' {} \;

  # Enter build directory
  cd "$srcdir/$_gitname" || return 1

  # Build and clean up OpenFOAM
  ./Allwmake || return 1
  wclean all || return 1
  wmakeLnIncludeAll || return 1

}
package() {
  cd "$startdir"

  # Create destination directories
  install -d "$pkgdir/opt/$_distpkgname" "$pkgdir/etc/profile.d" || return 1

  # Move package to pkgdir
  mv "$srcdir/$_gitname" "$pkgdir/opt/$_distpkgname/$_gitname" || return 1

  mkdir -p "$pkgdir/usr/bin"

  # Add source file
  echo "export FOAM_INST_DIR=/opt/$_distpkgname" > "$pkgdir/usr/bin/ofoam-3.0" || return 1
  echo ".\$FOAM_INST_DIR/$_gitname/etc/bashrc" >> "$pkgdir/usr/bin/ofoam-3.0" || return 1

  # Add stub thirdparty directory to keep openfoam happy
  install -d "$pkgdir/opt/$_distpkgname/ThirdParty-$_distpkgver" || return 1

  # Permission fixes - for system-wide install and use
  chmod -R go+r "$pkgdir/opt"
  chmod -R 755 "$pkgdir/opt/$_distpkgname/$_gitname/bin"
  chmod -R 755 "$pkgdir/opt/$_distpkgname/$_gitname/etc"
  chmod -R 755 "$pkgdir/usr/bin/ofoam-3.0"
}



