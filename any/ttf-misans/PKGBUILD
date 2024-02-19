# Maintainer: taotieren <admin@taotieren.com>

pkgbase=ttf-misans
_Mi=MiSans
_mi=(${_Mi,,})
_MultiLang=(Lao Arabic Devanagari Gujarati Gurmukhi Khmer L3 Latin Myanmar TC Thai Tibetan)
_multilang=(${_MultiLang[@],,})

_mi_ml=()
for mi in "${_mi}"; do
    _mi_ml=(${mi})
  for multilang in "${_multilang[@]}"; do
    _mi_ml+=("${mi}-${multilang}")
  done
done

_ftype=(ttf otf woff woff2)

_pkgbase=()
for ftype in "${_ftype[@]}"; do
  for ml in "${_mi_ml[@]}"; do
    _pkgbase+=("${ftype}-${ml}")
  done
done

pkgname=(misans ${_pkgbase[@]} misans-fontconfig)
pkgver=4.003
pkgrel=2
pkgdesc="MiSans Global is a global language font customization project led by Xiaomi and co-created with Mona font and Han Yi font."
arch=(any)
url='https://hyperos.mi.com/font/download'
license=(custom)
#provides=()
#conflicts=()
depends=(fontconfig)
makedepends=(unzip)
_zipname="MiSansGlobal_ALL"
source=("${_zipname}-${pkgver}.zip::https://hyperos.mi.com/font-download/MiSans_Global_ALL.zip"
"LICENSE.pdf::https://hyperos.mi.com/font-download/MiSans字体知识产权许可协议.pdf")

sha256sums=('2322a01e3138661a3d76980cfd8167f704bbea60445df94a00c79d3d6ae85b57'
            '4a93a27cd2bd81b3b5ecfd0a853144a876fa26938a93a68443c67d74172fcb86')

build() {
    rm -rf ${_zipname}
    mv -f "MiSans Global _ALL" ${_zipname}
    cd ${_zipname}
    unzip -o '*.zip'
    mv " MiSans Lao" "MiSans Lao"
    mv "MiSana Arabic" "MiSans Arabic"
    mv "MiSans Thai " "MiSans Thai"
}

function _package {
    optdepends+=(misans-fontconfig)
    local _pkgname=$1
    pkgdesc+=" - ${_pkgname}"
    local ext="${_pkgname%%-*}"
    local _fml="${_pkgname##*-}"
    _Mi_ML=()
    if [ ${_fml} == tc ];then
      _fml=${_fml^^}
      _Mi_ML="${_Mi} ${_fml}"
    elif [ ${_fml} == ${_mi} ];then
      _Mi_ML=${_Mi}
    else
      _fml=${_fml^}
      _Mi_ML="${_Mi} ${_fml}"
    fi

    cd "${srcdir}/${_zipname}/${_Mi_ML}"
    local fonts=("*.${ext}")
    local installdir="${ext^^}"
    # Prepare destination directory
    install -dm755 "${pkgdir}/usr/share/fonts/${installdir}"
    # Install fonts
    find . -name "*.${ext}" -type f -exec install -Dm644 {} -t "${pkgdir}/usr/share/fonts/${installdir}" \;
    install -Dm644 "${srcdir}/LICENSE.pdf" -t "${pkgdir}/usr/share/licenses/${_pkgname}"
}

for _pkgname in "${_pkgbase[@]}"; do
        eval "function package_${_pkgname}() { _package ${_pkgname}; }"
done

package_misans-fontconfig () {
    pkgdesc+=" - Fontconfig configuration"
    provides=()
    conflicts=()
    depends=(fontconfig)
    install -Dm755 /dev/stdin "${pkgdir}/usr/share/fontconfig/conf.avail/75-misans.conf" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fontconfig SYSTEM "../fonts.dtd">
<fontconfig>
    <alias>
        <family>Mi Sans</family>
        <prefer><family>Mi Sans</family></prefer>
    </alias>
</fontconfig>
EOF
    install -dm755 "${pkgdir}/usr/share/fontconfig/conf.default"
    ln -rs /usr/share/fontconfig/conf.avail/75-misans.conf "${pkgdir}/usr/share/fontconfig/conf.default/75-misans.conf"
}

package_misans () {
    pkgdesc+=" - meta package"
    provides=()
    conflicts=()
    depends=(${_pkgbase[@]} misans-fontconfig)
}
# vim: ts=4 sw=4 et
