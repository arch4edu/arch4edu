# Maintainer: Rafael Dominiquini <rafaeldominiquini at gmail dot com>
# Co-maintainer: edu4rdshl <edu4rdshl at protonmail dot com>

_npmmodule=@github/copilot

pkgname=github-copilot-cli
_pkgexec=copilot

pkgver=1.0.61
pkgrel=1

pkgdesc="GitHub Copilot CLI brings the power of Copilot coding agent directly to your terminal."

url="https://github.com/github/copilot-cli"
_urlraw="https://raw.githubusercontent.com/github/copilot-cli/v${pkgver}"

arch=("x86_64")

license=("LicenseRef-GitHub-Copilot")

conflicts=("${pkgname%%-cli}" "${pkgname}-legacy")
depends=("glibc" "gcc-libs" "nodejs" "glib2" "libsecret")
replaces=("${pkgname%%-cli}")
makedepends=("npm" "jq")
provides=("${_pkgexec}")

options=(!strip emptydirs staticlibs zipman)

source=("https://registry.npmjs.org/${_npmmodule}/-/copilot-${pkgver}.tgz"
		"CHANGELOG-${pkgver}.md::${_urlraw}/changelog.md")
noextract=("copilot-${pkgver}.tgz")

b2sums=('81d2c26f994fea03f3f76639e0457703824019419ee78b770b5e5c64c75ce0cdbc3d09dc0850a80b37ecaa25d9e08dcf936876770a6816483e4a93dcb6c697eb'
        '809200436c925a4e8cd14d5a7296eef22fa47ec1b9482b8ed2c2cc98c365f808d277e009a372502d40ef7918638abb85023eab6382f9f4f4fe1c079dd42d2ce3')

# Document: https://wiki.archlinux.org/title/Node.js_package_guidelines
package() {
	msg2 "Install using Using NPM"
	npm install -s -g \
		--cache "${srcdir}/npm-cache" \
		--prefix "${pkgdir}/usr" \
		"${srcdir}/copilot-${pkgver}.tgz"

	msg2 "Remove prebuilds and binaries for other platforms"
	local _moddir="${pkgdir}/usr/lib/node_modules/${_npmmodule}"

	local _arch
	case "$CARCH" in
		x86_64)  _arch="x64" ;;
		aarch64) _arch="arm64" ;;
		*)       error "Unsupported architecture: $CARCH"; exit 1 ;;
	esac

	msg2 "Cleaning non-native prebuilds for ${_arch}"
	if [ -d "${_moddir}/prebuilds" ]; then
		find "${_moddir}/prebuilds" -mindepth 1 -maxdepth 1 -type d ! -name "linux-${_arch}" -exec rm -rf {} +
	fi
	if [ -d "${_moddir}/mxc-bin" ]; then
		find "${_moddir}/mxc-bin" -mindepth 1 -maxdepth 1 -type d ! -name "${_arch}" -exec rm -rf {} +
	fi
	if [ -d "${_moddir}/ripgrep/bin" ]; then
		find "${_moddir}/ripgrep/bin" -mindepth 1 -maxdepth 1 -type d ! -name "linux-${_arch}" -exec rm -rf {} +
	fi
	if [ -d "${_moddir}/clipboard/node_modules/@teddyzhu" ]; then
		find "${_moddir}/clipboard/node_modules/@teddyzhu" -mindepth 1 -maxdepth 1 -type d ! -name "clipboard-linux-${_arch}-gnu" -exec rm -rf {} +
	fi
	if [ -d "${_moddir}/foundry-local-sdk/node_modules/foundry-local-sdk/prebuilds" ]; then
		find "${_moddir}/foundry-local-sdk/node_modules/foundry-local-sdk/prebuilds" -mindepth 1 -maxdepth 1 -type d ! -name "linux-${_arch}" -exec rm -rf {} +
	fi

	# pvrecorder only ships linux/x86_64; remove other OSes and non-native Linux archs
	if [ -d "${_moddir}/pvrecorder/node_modules/@picovoice/pvrecorder-node/lib" ]; then
		find "${_moddir}/pvrecorder/node_modules/@picovoice/pvrecorder-node/lib" -mindepth 1 -maxdepth 1 -type d ! -name 'linux' -exec rm -rf {} +
		if [ "$CARCH" = "x86_64" ]; then
			find "${_moddir}/pvrecorder/node_modules/@picovoice/pvrecorder-node/lib/linux" -mindepth 1 -maxdepth 1 -type d ! -name 'x86_64' -exec rm -rf {} +
		else
			rm -rf "${_moddir}/pvrecorder/node_modules/@picovoice/pvrecorder-node/lib/linux"
		fi
	fi

	msg2 "Fix ownership of ALL FILES"
	find "${pkgdir}/usr" -type d -exec chmod 755 {} +
	chown -R root:root "${pkgdir}"

	msg2 "Remove references to PKGDIR"
	find "${pkgdir}" -name package.json -print0 | xargs -r -0 sed -i '/_where/d'

	msg2 "Fixing 'package.json'"
	local tmppackage="$(mktemp)"
	local pkgjson="${pkgdir}/usr/lib/node_modules/${_npmmodule}/package.json"
	jq '.|=with_entries(select(.key|test("_.+")|not))' "${pkgjson}" > "${tmppackage}"
	mv "${tmppackage}" "${pkgjson}"
	chmod 644 "${pkgjson}"

	msg2 "More fixes for 'package.json'"
	find "${pkgdir}" -type f -name package.json | while read pkgjson; do
		local tmppackage="$(mktemp)"
		jq 'del(.man)' "${pkgjson}" > "${tmppackage}"
		mv "${tmppackage}" "${pkgjson}"
		chmod 644 "${pkgjson}"
	done

	msg2 "Generating autocompletions for Bash"
	"${pkgdir}/usr/bin/copilot" completion bash > copilot
	install -Dm644 copilot "${pkgdir}/usr/share/bash-completion/completions/copilot"

	msg2 "Generating autocompletions for Zsh"
	"${pkgdir}/usr/bin/copilot" completion zsh > _copilot
	install -Dm644 _copilot "${pkgdir}/usr/share/zsh/site-functions/_copilot"

	msg2 "Generating autocompletions for Fish"
	"${pkgdir}/usr/bin/copilot" completion fish > copilot.fish
	install -Dm644 copilot.fish "${pkgdir}/usr/share/fish/vendor_completions.d/copilot.fish"

	msg2 "Install README file"
	install -dm755 "${pkgdir}/usr/share/doc/${pkgname}/"
	ln -sf "/usr/lib/node_modules/${_npmmodule}/README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"
	
	msg2 "Install CHANGELOG file"
	install -Dm755 "${srcdir}/CHANGELOG-${pkgver}.md" "${pkgdir}/usr/share/doc/${pkgname}/CHANGELOG.md"

	msg2 "Install LICENSE file"
	install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}/"
	ln -sf "/usr/lib/node_modules/${_npmmodule}/LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

}

