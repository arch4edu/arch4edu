# Maintainer: Christopher Cooper <christopher@cg505.com>
# Maintainer: Jérôme Poulin <jeromepoulin@gmail.com>
# Maintainer: Fabio Fontana (fabifont) <me@fabifont.dev>
# Automation repository: https://github.com/fabifont/claude-code-aur

pkgname=claude-code
pkgver=2.1.328
pkgrel=1
pkgdesc="An agentic coding tool that lives in your terminal"
arch=('x86_64' 'aarch64')
url="https://github.com/anthropics/claude-code"
license=('LicenseRef-claude-code')
depends=('bash')
# Binary is a self-contained Bun executable with embedded JS/resources - stripping breaks it
options=('!strip')

optdepends=(
	'git: allow Claude to use git'
	'github-cli: interact with GitHub'
	'glab: interact with GitLab'
	'ripgrep: enhanced file search'
	'tmux: agent team split panes'
	'bubblewrap: sandboxing'
	'socat: sandboxing'
)

source=("cc-legal::https://code.claude.com/docs/en/legal-and-compliance.md")
source_x86_64=("claude-${pkgver}-x86_64::https://downloads.claude.ai/claude-code-releases/${pkgver}/linux-x64/claude")
source_aarch64=("claude-${pkgver}-aarch64::https://downloads.claude.ai/claude-code-releases/${pkgver}/linux-arm64/claude")

sha256sums=('SKIP')
sha256sums_x86_64=('a982d38030b97e750848add2cbb2df6d9a70d5544a22ca9b216a349ba25865e8')
sha256sums_aarch64=('307f8bada27b37db7553fac75e86004e3dbff5a931ffc611b54fe710ce1eb521')

package() {
	install -Dm755 "${srcdir}/claude-${pkgver}-${CARCH}" "${pkgdir}/opt/claude-code/bin/claude"

	# Create wrapper script to disable upstream update paths, and to suppress the
	# native-install health check. Claude Code expects the native installer layout
	# (~/.local/bin/claude); since we install to /opt + /usr/bin it would otherwise
	# warn on every startup: "claude command at ~/.local/bin/claude missing or broken".
	install -dm755 "${pkgdir}/usr/bin"
	cat > "${pkgdir}/usr/bin/claude" << 'EOF'
#!/bin/sh
export DISABLE_UPDATES=1
export DISABLE_INSTALLATION_CHECKS=1
exec /opt/claude-code/bin/claude "$@"
EOF
	chmod 755 "${pkgdir}/usr/bin/claude"

	install -Dm644 "${srcdir}/cc-legal" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
