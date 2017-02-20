# This package is inspired from https://github.com/WarheadsSE/PKGs/blob/master/distccd-alarm/PKGBUILD 
# Maintainer: Jacky Ren <i@jacky.ren>
# Maintainer: Jingbei Li <i@jingbei.li>

_subarchs=(armv6h armv7h armv8h)
pkgbase='distccd-arm'
pkgname=("${_subarchs[@]/#/$pkgbase-}")
pkgver=1.0
pkgrel=1
pkgdesc="Distcc services package for ARM"
arch=('x86_64')
license=('GPL' )
depends=('distcc')
options=('libtool' 'emptydirs' '!strip')
source=(
'distccd.conf.d::https://git.archlinux.org/svntogit/community.git/plain/trunk/distccd.conf.d?h=packages/distcc'
'distccd.service::https://git.archlinux.org/svntogit/community.git/plain/trunk/distccd.service?h=packages/distcc'
)
md5sums=(
'239aae53250e3e35288cba566bc0bbf1'
'09f0688da9c1840e518d2593bd5c3830'
)

_package_subarch() {
  arch_tag=${1%h}
  depends+=("x-tools-$arch_tag-bin")

  config_file_path="etc/conf.d/distccd-$arch_tag"

  # backup original configs
  backup=("$config_file_path")

  # install corresponding services
  installed_service_path="${pkgdir}/usr/lib/systemd/system/distccd-$1.service"
  install -Dm0644 "${srcdir}/distccd.service" $installed_service_path
  echo "/\(EnvironmentFile=.*\)/\1-$arch_tag/" 
  # Append for armv* in Description
  sed -i -e "s/\(Description=.*\)/\1 for $arch_tag/" $installed_service_path
  # Update enviroment file to corresponding arch
  sed -i -e "s/\(EnvironmentFile=.*\)/\1-$arch_tag/" $installed_service_path

  # install config
  installed_config_path="${pkgdir}/$config_file_path"
  install -Dm0644 "${srcdir}/distccd.conf.d" "$installed_config_path"
  echo "PATH=/usr/x-tools/x-tools${1##armv}/arm-unknown-linux-gnueabihf/bin:\$PATH" \
    >> "$installed_config_path"
}

# Loop over all supporting subarchs to make pakcages
for i in "${!_subarchs[@]}"; do   
   eval 'package_distccd-arm-'${_subarchs[i]}'() {
     _package_subarch '${_subarchs[i]}'
   }'
done

