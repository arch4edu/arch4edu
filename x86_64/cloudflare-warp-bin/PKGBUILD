# Maintainer: Leon Mergen <leon@solatis.com>
# Maintainer: unlogicalcode <jearsmail99@gmail.com>
# Maintainer: Noah Kennedy <nomaxx117@gmail.com>
# Maintainer: Arsalan Rezazadeh <arsalanrezazadeh4@gmail.com>
# Maintainer: Jongsik Kim <jjong84@gmail.com>
# Maintainer: <memoryshadow@outlook.com>
# Maintainer: Daffa Haj Tsaqif <narutohaj00@gmail.com>

pkgname=cloudflare-warp-bin
pkgver=2024.2
pkgrel=1
pkgdesc="Cloudflare Warp Client"
url="https://1.1.1.1"
license=("unknown")
depends=("glibc" "dbus" "lz4" "zstd" "xz" "nftables" "libgpg-error")
checkdepends=("coreutils")
arch=('x86_64')
provides=('warp-cli' 'warp-diag' 'warp-svc')
conflicts=('cloudflare-warp')

# Function to get latest version from repository
get_latest_version() {
    curl -s https://pkg.cloudflareclient.com/dists/focal/main/binary-amd64/Packages \
    | grep -E -o 'Version: [0-9]+\.[0-9]+\.[0-9]+' \
    | head -n1 \
    | grep -E -o '[0-9]+\.[0-9]+\.[0-9]+'
}

latest_version=$(get_latest_version)

# Compare latest version with current version
if [[ "$pkgver" != "$latest_version" ]]; then
    pkgver=$latest_version
    pkgrel=1
fi

source=(
    "${pkgname}-${pkgver}-x86_64.deb::https://pkg.cloudflareclient.com/pool/focal/main/c/cloudflare-warp/cloudflare-warp_${pkgver//-/_}-1_amd64.deb"
    "${pkgname}-${pkgver}-${pkgrel}-Release::https://pkg.cloudflareclient.com/dists/focal/Release"
    "${pkgname}-${pkgver}-${pkgrel}-x86_64-Packages::https://pkg.cloudflareclient.com/dists/focal/main/binary-amd64/Packages"
)

md5sums=('SKIP'
         'SKIP'
         'SKIP')
sha256sums=('SKIP'
            'SKIP'
            'SKIP')

prepare() {
    tar -xzOf control.tar.gz ./md5sums \
        | awk '{print $1, "'"${srcdir}"'/build/" $2}' \
        > "${srcdir}/md5sums"
}

build() {
    if [[ -d "${srcdir}/build/" ]]; then
        rm -rf "${srcdir}/build/"
    fi

    mkdir -p "${srcdir}/build/" \
        && tar --extract \
               --gzip \
               --file=data.tar.gz \
               -C "${srcdir}/build/"
}


package() {
    mkdir -p "${pkgdir}/usr/" || true

    cp -R -v "${srcdir}/build/usr/" "${pkgdir}/"

    cp -R -v "${srcdir}/build/"{bin,lib} "${pkgdir}/usr/"

    sed -i \
        -e "s%ExecStart=/bin/warp-svc%ExecStart=/usr/bin/warp-svc%" \
        "${pkgdir}"/usr/lib/systemd/system/warp-svc.service
    sed -i \
        -e "s%ExecStart=/bin/warp-taskbar%ExecStart=/usr/bin/warp-taskbar%" \
        "${pkgdir}"/usr/lib/systemd/user/warp-taskbar.service
}
