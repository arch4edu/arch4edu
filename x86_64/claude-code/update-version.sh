#!/bin/bash
set -e

GCS_BUCKET="https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases"
PKGBUILD="PKGBUILD"

# Get current version from PKGBUILD
current_version=$(grep -Po '^pkgver=\K.*' "$PKGBUILD")

# Fetch latest version
new_version=$(curl -fsSL "$GCS_BUCKET/latest")
echo "Current version: $current_version"
echo "New version: $new_version"

if [ "$current_version" = "$new_version" ]; then
    echo "Already up to date!"
    exit 1
fi

# Download manifest
manifest=$(curl -fsSL "$GCS_BUCKET/$new_version/manifest.json")

# Extract checksums using jq
linux_x64=$(echo "$manifest" | jq -r '.platforms["linux-x64"].checksum')
linux_arm64=$(echo "$manifest" | jq -r '.platforms["linux-arm64"].checksum')

echo ""
echo "Checksums (SHA256):"
echo "  linux-x64:   $linux_x64"
echo "  linux-arm64: $linux_arm64"
echo ""

# Update PKGBUILD
echo "Updating PKGBUILD..."
sed -i "s/^pkgver=.*/pkgver=$new_version/" "$PKGBUILD"
sed -i "s/^pkgrel=.*/pkgrel=1/" "$PKGBUILD"
sed -i "s/^sha256sums_x86_64=.*/sha256sums_x86_64=('$linux_x64')/" "$PKGBUILD"
sed -i "s/^sha256sums_aarch64=.*/sha256sums_aarch64=('$linux_arm64')/" "$PKGBUILD"

echo "Regenerating .SRCINFO..."
makepkg --printsrcinfo > .SRCINFO

echo ""
echo "Done! Updated from $current_version to $new_version"
