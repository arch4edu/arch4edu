#! /bin/bash

service_url="https://cef-builds.spotifycdn.com"

versions=$(curl -s "$service_url/index.json")

stripQuotes() {
  sed -e 's/^"//' -e 's/"$//' <<<$1
}

replace_line() {
  sed -i "$2s#.*#$1#" $3
}

update_version() {
  local arch=$1;

  stable=$(echo $versions | jq ".$arch.versions | map(select(.channel == \"stable\" )) | .[0]");
  # versions
  version_arr=$(echo $stable | jq '.cef_version | split("+")');

  version=$(stripQuotes $(echo $version_arr | jq '.[0]'));
  build_hash=$(stripQuotes $(echo $version_arr | jq '.[1]'));
  chromium_version=$(stripQuotes $(echo $version_arr | jq '.[2] | split("-") | .[1]'));

  echo $version

  minimal=$(echo $stable | jq '.files | map(select(.type == "minimal" )) | .[0]');

  filename=$(stripQuotes $(echo $minimal | jq '.name' ))
  sha_hash=$(stripQuotes $(echo $minimal | jq '.sha1' ))

  file_url=$service_url/$filename

  # update PKGBUILD
  replace_line "pkgver=\"$version\"" 5 PKGBUILD
  replace_line "_pkgcommit=\"$build_hash\"" 6 PKGBUILD
  replace_line "_chromiumver=\"$chromium_version\"" 7 PKGBUILD

  # update .SRCINFO
  replace_line "	pkgver = $version" 3 .SRCINFO

  if [ $arch = "linux64" ]; then
    replace_line "sha1sums_x86_64=(\"$sha_hash\")" 29 PKGBUILD

    replace_line "  source_x86_64 = $file_url" 27 .SRCINFO
    replace_line "  sha1sums_x86_64 = $sha_hash" 28 .SRCINFO
  else
    replace_line "sha1sums_i686=(\"$sha_hash\")" 28 PKGBUILD

    replace_line "  source_i686 = $file_url" 25 .SRCINFO
	  replace_line "  sha1sums_i686 = $sha_hash" 26 .SRCINFO
  fi
}

echo "UPDATING "
git pull > /dev/null

echo "- Patching i686..."
update_version linux32

echo "- Patching x86_64..."
update_version linux64


echo $version
echo "- Rebuilding(makepkg)..."
makepkg > /dev/null

if [ -z ${SKIP_PUSH+x} ]; then
  echo "- Uploading to AUR"
  git add .SRCINFO PKGBUILD > /dev/null
  git commit  -m "[AUTO] Version $version" > /dev/null
  git push > /dev/null
fi

echo "Cleanup"
rm -r src/* > /dev/null
rm -r pkg/* > /dev/null

echo "DONE"
