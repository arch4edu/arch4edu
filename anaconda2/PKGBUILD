# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>
# Contributor : Jingbei Li <i@jingbei.li>

pkgname=anaconda2
pkgver=4.4.0
pkgrel=2
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=('x86' 'x86_64')
url="https://store.continuum.io/cshop/anaconda/"
license=("custom")
makedepends=('patch')
source=("http://repo.continuum.io/archive/Anaconda2-${pkgver}-Linux-x86_64.sh"
        "install.py.patch"
        "$pkgname.install")
options=(!strip libtool staticlibs)
sha256sums=('2d30b91ed4d215b6b4a15162a3389e9057b15445a0c02da71bd7bd272e7b824e'
            '04b4ea775ba805ff24e93162b6679e65d00b997a46cde11fd76602db4e824dc7'
            'c491735df1753335c6aa5b3b71bd936ccb4ff5622fedbf22d1d6d9da5bd45fbc')
_pythonver='2.7.13-0'
install="$pkgname.install"

_pkgarch=`uname -m`
if [ "$CARCH" == "x86" ]; then
    _pkgarch="x86"
    sha256sums[0]='7764093f337a43e4962b12d01508c1a385f0f62c1ddc006b69af95ae763fc4c2'
    source[0]="http://repo.continuum.io/archive/Anaconda2-${pkgver}-Linux-x86.sh"
fi

prepare() {
    cd ${srcdir}
    msg2 "Patching Anaconda2-${pkgver}-Linux-x86_64.sh"
    sed \
        -e '/^wc -c "\$THIS_PATH" | grep/s/^/#/' \
        -e '/^mkdir \$HOME\/\.continuum/s/^/#/' \
        -e '/^echo "creating default environment..."$/s/^/exit 0 || /' \
        -i Anaconda2-${pkgver}-Linux-x86_64.sh
}

package() {
    prefix=${pkgdir}/opt/${pkgname}
    LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

    msg2 "Extracting default libraries"
    bash ${srcdir}/Anaconda2-${pkgver}-Linux-${_pkgarch}.sh -b -p $prefix
    [ "$BREAK_EARLY" = 1 ] && exit 1

    msg2 "Patching .install.py"
    cd $prefix
    CONDA_INSTALL="$prefix/pkgs/.install.py"
    patch -p1 < $srcdir/install.py.patch

    msg2 "Installing anaconda to /opt/${pkgname}"
    $prefix/pkgs/python-${_pythonver}/bin/python -E -s $CONDA_INSTALL --root-prefix=$prefix --instdir=/opt/${pkgname} || exit 1

    msg2 "Correcting permissions"
    chmod a+r -R $prefix/pkgs

    msg2 "Stripping \$pkgdir from default meta"
    find conda-meta -name '*.json' -exec sed -e "s/${pkgdir//\//\\\/}//g" -i {} \;

    msg2 "Installing license"
    install -D -m644 $prefix/LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
