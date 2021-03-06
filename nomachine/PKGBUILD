# Maintainer: Runnytu < runnytu at gmail dot com >
# OldMaintainer: FreeK <stephan@confidr.me>
# Contributor: olav-st <olav.s.th@gmail.com>
# Contributor: David Manouchehri <manouchehri@riseup.net>

### BUILD OPTIONS
# Set to y to enable nomachine service autostart
_autoservice=n
# Set to y to enable firewall autorules
_autofirewall=n
### END BUILD OPTIONS

pkgname=nomachine
pkgver=7.2.3
_pkgvermain=7.2
_pkgrel_i686=8
_pkgrel_x86_64=8
_pkgrel_armv6h=3
_pkgrel_armv7h=3
_pkgrel_armv8h=3
_pkgrel_aarch64=${_pkgrel_armv8h}
_pkgrel_pentium4=${_pkgrel_i686}
pkgrel=1
pkgdesc="Remote desktop application"
groups=('network')
url="http://www.nomachine.com"
license=('custom:"NoMachine EULA"')
arch=('x86_64' 'i686' 'armv6h' 'armv7h' 'armv8h' 'aarch64' 'pentium4')
options=('!strip')
conflicts=('nxmanager' 'nxwebplayer' 'nxserver' 'nxnode' 'nxclient')
depends=('bash' 'openssh' 'nawk')
optdepends=('xorg-xauth: allows logging into a headless machine')
sha512sums_x86_64=('7d63351fc66b19ca16b0fcc5318ce497b7c5912188fda3b7b6e34bc872cd3dee0dcd8d47583ab0de9151cbc96439146143c050e671cb88fd33550b9689092223')
sha512sums_i686=('745a7c786c9d87e5a8fcd9c85fecbe87deb4220e9b661e00a60c54f851729194d274bd320f88d6c147634488668630994abb10e04dfe77522d9f1af4b7cf379b')
sha512sums_armv6h=('9731798cb20eb648048e38e74ea9bfedf78c025fda40f9815325d968d403067bc8ec030b202dbd948ad6349206f83d160460c6da0dc29195d8d8f7528195f24f')
sha512sums_armv7h=('8667b1868b36a205c0c5a575080073e8f26e98ac75d300a81e058a5307fac417f4f6afe31b15802aec6fa4c6c7c01cdddf111e99b4367b3eac82071b05fb5eed')
sha512sums_armv8h=('faac374c3a2602c40154e1c6bc63b7dbedef7230b821842ca5b3361dde2d877f0eafc9a5d52102ef0e3e01ed3d9b6020af793238eaad3d675e3098e96ba79748')
sha512sums_aarch64=('faac374c3a2602c40154e1c6bc63b7dbedef7230b821842ca5b3361dde2d877f0eafc9a5d52102ef0e3e01ed3d9b6020af793238eaad3d675e3098e96ba79748')
sha512sums_pentium4=('745a7c786c9d87e5a8fcd9c85fecbe87deb4220e9b661e00a60c54f851729194d274bd320f88d6c147634488668630994abb10e04dfe77522d9f1af4b7cf379b')
source_x86_64=("http://download.nomachine.com/download/${_pkgvermain}/Linux/${pkgname}_${pkgver}_${_pkgrel_x86_64}_x86_64.tar.gz")
source_i686=("http://download.nomachine.com/download/${_pkgvermain}/Linux/${pkgname}_${pkgver}_${_pkgrel_i686}_i686.tar.gz")
source_armv6h=("http://download.nomachine.com/download/${_pkgvermain}/Raspberry/${pkgname}_${pkgver}_${_pkgrel_armv6h}_armv6hl.tar.gz")
source_armv7h=("http://download.nomachine.com/download/${_pkgvermain}/Raspberry/${pkgname}_${pkgver}_${_pkgrel_armv7h}_armv7hl.tar.gz")
source_armv8h=("http://download.nomachine.com/download/${_pkgvermain}/Raspberry/${pkgname}_${pkgver}_${_pkgrel_armv8h}_aarch64.tar.gz")
source_aarch64=("${source_armv8h[@]}")
source_pentium4=("${source_i686[@]}")
install=nomachine.install

prepare()
{
#Fix Fedora Version Var And Libstdc++ Rename
tar -zxf "$srcdir/NX/etc/NX/server/packages/nxclient.tar.gz" NX/scripts/setup/nxclient
sed -i 's/    majorFedoraVersion.*/    majorFedoraVersion=23/' "$srcdir/NX/scripts/setup/nxclient"
tar -zxf "$srcdir/NX/etc/NX/server/packages/nxclient.tar.gz" "NX/lib/"
for _libstdc in "$srcdir/NX/lib/"libstdc++.*; do
mv "${_libstdc}" ${_libstdc}.nomachine
done
gzip -d "$srcdir/NX/etc/NX/server/packages/nxclient.tar.gz"
tar -rf "$srcdir/NX/etc/NX/server/packages/nxclient.tar" NX/scripts/setup/nxclient -C "$srcdir/NX/scripts/setup/nxclient"
tar --delete -f "$srcdir/NX/etc/NX/server/packages/nxclient.tar" "NX/lib/"
tar -rf "$srcdir/NX/etc/NX/server/packages/nxclient.tar" "NX/lib/" -C "$srcdir/NX/lib/"
gzip "$srcdir/NX/etc/NX/server/packages/nxclient.tar"
rm -fr "$srcdir/NX/scripts"*
rm -fr "$srcdir/NX/lib"*
#Change Automatic Service Start And/Or Firewall Automatic Rules If Apply
if [ $_autoservice = y ] && [ $_autofirewall = y ]; then
echo "##################################################################"
echo "#Enabling Automatic Service Start And Firewall Automatic Rules#"
echo "##################################################################"
elif [ $_autoservice = y ] && [ $_autofirewall = n ]; then
echo "#####################################"
echo "#Enabling Automatic Service Start#"
echo "#####################################"
tar -zxf "$srcdir/NX/etc/NX/server/packages/nxserver.tar.gz" NX/etc/server-fedora.cfg.sample
sed -i 's/#EnableFirewallConfiguration 1/EnableFirewallConfiguration 0/' NX/etc/server-fedora.cfg.sample
gzip -d "$srcdir/NX/etc/NX/server/packages/nxserver.tar.gz"
tar -rf "$srcdir/NX/etc/NX/server/packages/nxserver.tar" NX/etc/server-fedora.cfg.sample -C "$srcdir/NX/etc/server-fedora.cfg.sample"
gzip "$srcdir/NX/etc/NX/server/packages/nxserver.tar"
rm -fr "$srcdir/NX/etc/server-fedora.cfg.sample"
elif [ $_autoservice = n ] && [ $_autofirewall = y ]; then
echo "######################################"
echo "#Enabling Firewall Automatic Rules#"
echo "######################################"
tar -zxf "$srcdir/NX/etc/NX/server/packages/nxserver.tar.gz" NX/etc/server-fedora.cfg.sample
sed -i 's/#StartNXDaemon Automatic/StartNXDaemon Manual/' NX/etc/server-fedora.cfg.sample
gzip -d "$srcdir/NX/etc/NX/server/packages/nxserver.tar.gz"
tar -rf "$srcdir/NX/etc/NX/server/packages/nxserver.tar" NX/etc/server-fedora.cfg.sample -C "$srcdir/NX/etc/server-fedora.cfg.sample"
gzip "$srcdir/NX/etc/NX/server/packages/nxserver.tar"
rm -fr "$srcdir/NX/etc/server-fedora.cfg.sample"
elif [ $_autoservice = n ] && [ $_autofirewall = n ]; then
echo "###################################################################"
echo "#Disabling Automatic Service Start And Firewall Automatic Rules#"
echo "###################################################################"
tar -zxf "$srcdir/NX/etc/NX/server/packages/nxserver.tar.gz" NX/etc/server-fedora.cfg.sample
sed -i 's/#EnableFirewallConfiguration 1/EnableFirewallConfiguration 0/' NX/etc/server-fedora.cfg.sample
sed -i 's/#StartNXDaemon Automatic/StartNXDaemon Manual/' NX/etc/server-fedora.cfg.sample
gzip -d "$srcdir/NX/etc/NX/server/packages/nxserver.tar.gz"
tar -rf "$srcdir/NX/etc/NX/server/packages/nxserver.tar" NX/etc/server-fedora.cfg.sample -C "$srcdir/NX/etc/server-fedora.cfg.sample"
gzip "$srcdir/NX/etc/NX/server/packages/nxserver.tar"
rm -fr "$srcdir/NX/etc/server-fedora.cfg.sample"
fi
}

package()
{
cd "$srcdir"
mkdir "$srcdir/NX/etc" -p
install -d "$pkgdir/usr/"
cp -a NX "$pkgdir/usr/NX"
}

