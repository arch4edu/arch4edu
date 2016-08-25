# Maintainer: Andrea Fagiani <andfagiani_at_gmail_dot_com>

pkgname=eclim
pkgver=2.6.0
pkgrel=1
pkgdesc="Brings Eclipse functionality to Vim"
url="http://eclim.org/"
license=('GPL3')
arch=(i686 x86_64)
depends=('vim' 'eclipse')
makedepends=('apache-ant' 'python2-sphinx' 'groovy')
optdepends=('eclipse-pdt: Eclipse PHP Development Tools support'
            'eclipse-cdt: Eclipse C/C++ Plugin support'
            'eclipse-dltk-core: Eclipse Dynamic Languagues Toolkit support'
            'eclipse-dltk-ruby: Eclipse Ruby support'
            'eclipse-wtp: Eclipse Web Developer Tools support')
conflicts=('eclim-git')
install=$pkgname.install
source=("https://github.com/ervandew/eclim/releases/download/$pkgver/${pkgname}_$pkgver.tar.gz")
md5sums=('74557a1d0c2fb22ec7ae46e7ad200e49')

prepare() {
  cd $srcdir/${pkgname}_$pkgver

  # fix build, thanks to mikezackles
  sed -e "s/'sphinx-build'/'sphinx-build2'/g" \
    -e 's|${user.home}/\.|${vim.files}/|g' \
    -e "s|File(getVariable('eclipse')|File('/usr/lib/eclipse/'|g" \
    -e '68,88d' \
    -i ant/build.gant

  # Get the ANT_HOME environment variable
  source /etc/profile.d/apache-ant.sh

  chmod +x org.eclim/nailgun/configure bin/sphinx
}

build() {
  cd $srcdir/${pkgname}_$pkgver

  # recompiling nailgun to make sure the executable is compliant with our architecture
  cd org.eclim/nailgun
  ./configure
  make

  cd ../..

  ant -lib /usr/share/groovy/lib \
      -Declipse.home=/usr/lib/eclipse \
      -Dvim.files=/usr/share/vim/vimfiles \
      build

}

package() {
  cd $srcdir/${pkgname}_$pkgver

  mkdir -p $pkgdir/usr/lib/eclipse
  mkdir -p $pkgdir/usr/share/vim/vimfiles

  ant -lib /usr/share/groovy/lib \
      -Declipse.home=/usr/lib/eclipse \
      -Dvim.files=$pkgdir/usr/share/vim/vimfiles \
      docs vimdocs

  ant -lib /usr/share/groovy/lib \
      -Declipse.home=$pkgdir/usr/lib/eclipse \
      -Dvim.files=$pkgdir/usr/share/vim/vimfiles \
      deploy

  # copy eclim docs
  mkdir -p $pkgdir/usr/share/doc/
  cp -r build/doc/site $pkgdir/usr/share/doc/eclim

  # fix eclim paths
  sed -e "s|$pkgdir||g" \
    -i $pkgdir/usr/share/vim/vimfiles/eclim/plugin/eclim.vim \
    -i $pkgdir/usr/lib/eclipse/plugins/org.eclim_$pkgver/bin/eclimd \
    -i $pkgdir/usr/lib/eclipse/plugins/org.eclim_$pkgver/plugin.properties

  # delete doctrees
  rm -fr $pkgdir/usr/share/doc/eclim/.doctrees

  # delete Windows stuff
  for i in $(find $pkgdir -regex ".*bat\|.*cmd\|.*exe"); do  rm -f $i ; done

  rm $pkgdir/usr/lib/eclipse/plugins/org.eclim_${pkgver}/nailgun/config.status
}
