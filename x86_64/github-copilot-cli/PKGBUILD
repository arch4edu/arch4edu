# Maintainer: Rafael Dominiquini <rafaeldominiquini at gmail dot com>
# Co-maintainer: edu4rdshl <edu4rdshl at protonmail dot com>

_npmmodule=@github/copilot

pkgname=github-copilot-cli
_pkgexec=copilot

pkgver=1.0.9
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

b2sums=('07ad6f541e1cecebab68022eeb26c2f540715373ee661ebf179e3b558c570731893e2ace9a67b05547c21c4ac5ccd0d6bcfaa629a50f7bac8c7128ff30627b7c'
        'd5bc433fbcaf4ad0c17f9d741044dd6d1167bc53699dee49edc3929192bab551be987bea1272d98cba9006a569326abb2083f16dfcf388e73f60204b1212e36e')

# Document: https://wiki.archlinux.org/title/Node.js_package_guidelines
package() {
	msg2 "Install using Using NPM"
	npm install -s -g \
		--cache "${srcdir}/npm-cache" \
		--prefix "${pkgdir}/usr" \
		"${srcdir}/copilot-${pkgver}.tgz"

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

	msg2 "Install README file"
	install -dm755 "${pkgdir}/usr/share/doc/${pkgname}/"
	ln -sf "/usr/lib/node_modules/${_npmmodule}/README.md" "${pkgdir}/usr/share/doc/${pkgname}/README.md"
	
	msg2 "Install CHANGELOG file"
	install -Dm755 "${srcdir}/CHANGELOG-${pkgver}.md" "${pkgdir}/usr/share/doc/${pkgname}/CHANGELOG.md"

	msg2 "Install LICENSE file"
	install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}/"
	ln -sf "/usr/lib/node_modules/${_npmmodule}/LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

}

