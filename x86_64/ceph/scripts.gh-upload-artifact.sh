#!/usr/bin/env bash

usage() {
cat <<EOF
$0 --repo=<owner/repo> --tag=<release tag | @> --file=<artifact path> --token=<github api token>

Usage:

  This script uploads the given artifact to a GitHub release.

  It takes 4 required options:

  --repo        | The <org>/<repo> combo to upload the artifact to      env:\$GITHUB_REPO     =${repo:-<unset>}
  --tag         | The tag / release name to upload the artifact to      env:\$GITHUB_RELEASE  =${tag:-<unset>}
  --file        | The file path to the artifact to upload               env:\$GITHUB_ARTIFACT =${artifact:-<unset>}
  --token       | The API token to use when authenticating with GitHub  env:\$GITHUB_TOKEN    =$([[-n "$token" ]] && printf '<*****>' || printf '<unset>')
  --dry-run     | Don't actually upload the artifact                    env:\$GITHUB_DRYRUN   =$([[-n "$dry" ]] && printf 'true' || printf 'false')
  --help        | Print this help

  Each option may also be set via the associated environment variable, with the command line taking precedence.

  You may optionally force the uploaded artifact to have a different name from the given file, by suffixing --file
  with a ':<name-override>'. For example, '/path/to/artifact_with.dirty+name.tar.gz:artifact.tar.gz' will resolve
  the uploaded artifact's filename to 'artifact.tar.gz'.

  To select the most recent tag on the remote, you can use the special value '@' when setting --tag.

Examples:

  1. $(basename $0) --tag=v1.0.0 --repo github/octocat --file ./cute-kat.jpg --token=dae3re34...

  2. GITHUB_TOKEN=4wf4dec... GITHUB_ARTIFACT=/assets/cats.json $(basename $0) --repo=github/octocat --tag=v2.0.0

  3. $(basename $0) --tag=@ --repo github/octocat --file ./dirty_m3sszy.kitty.tar.xz:kitty.tar.xz --token f43rffe...

EOF
}

requires() {
  local t v efails xfails emsg
  for t in "$@"; do
    v=${t#*:}

    case $t in
      e:*)
        [[ -n "${!v}" ]] || efails+=("$v")
      ;;
      x:*|*)
        command -v "${v}" &>/dev/null || xfails+=("$v")
      ;;
    esac
  done

  [[ -n "${efails}" ]] && emsg=$(printf 'Missing required variable(s): %s' "${efails[*]}")
  [[ -n "${xfails}" ]] && emsg=$(printf '%s\nMissing required executable(s): %s' "$emsg" "${xfails[*]}")
  [[ -n "$emsg" ]] && die 3 "$(printf '%s\n[INFO]: Use --help for more information' "$emsg")"
}

cli() {
  local GOPTS=$(getopt -o hd --long help,dry-run,repo:,tag:,file:,token: -n "gh-upload-artifact" -- "$@")
  eval set -- "$GOPTS"

  while (( $# > 0 )); do
    case "$1" in
      --repo)         repo="$2";        shift 2 ;;
      --tag)          tag="$2";         shift 2 ;;
      --file)         artifact="$2";    shift 2 ;;
      --token)        token="$2";       shift 2 ;;
      -h|--help)      help=1;           shift   ;;
      -d|--dry-run)   dry=1;            shift   ;;
      --)             shift;            break   ;;
      *) die 1 "Unknown option: $1" 1           ;;
    esac
  done
}

set_filename() {
  artifact=${1%:*}
  filename=${1##*:}
  [[ -n "$filename" ]] || filename=$(basename $artifact)
}

die() {
  echo "[ERROR]: $2" >&2
  [ -n "$3" ] && usage >&2
  exit $1
}

setup() {
  requires x:getopt x:curl x:jq

  # Script inputs
  repo=${GITHUB_REPO}
  tag=${GITHUB_RELEASE}
  artifact=${GITHUB_ARTIFACT}
  token=${GITHUB_TOKEN}
  dry=${GITHUB_DRYRUN:+1}
  filename=""
  help=-1

  cli "$@"
  (( help > 0 )) && usage && exit 0

  requires e:repo e:tag e:artifact e:token

  set_filename "$artifact"

  # Constants
  GH_RESPONSE=$(mktemp)
  GH_AUTH="Authorization: token $token"
  CURL_ARGS="-sSL"
  [[ "$tag" == '@' ]] \
    && GH_TAG="latest" \
    || GH_TAG="tags/$tag"
}

main() {
  setup "$@"
  trap 'rm -f $GH_RESPONSE' EXIT

  # Fetch release JSON blob
  curl "$CURL_ARGS" -o "$GH_RESPONSE" -H "$GH_AUTH" "https://api.github.com/repos/$repo/releases/$GH_TAG"
  (( $? > 0 )) && die 1 "$(cat <(printf "Invalid repo, token or network issue!\n") $GH_RESPONSE)"

  # Get ID of the asset based on given filename.
  id=$(jq -r '.id' "$GH_RESPONSE")
  (( $? > 0 )) && die 1 "$(cat <(printf "Failed to get release id for tag '%s' from response:\n" "$tag") $GH_RESPONSE)"

  # Construct url
  upload_uri="https://uploads.github.com/repos/$repo/releases/$id/assets?name=$filename"

  # Upload artifact
  if [[ -n "$dry" ]]; then
    echo "[INFO]: Would upload $artifact to $upload_uri" >&2
  else
    curl "$CURL_ARGS" \
      -H "$GH_AUTH" \
      -H "Content-Type: $(file -b --mime-type $artifact)" \
      --data-binary @"$artifact" \
      $upload_uri
  fi
}

[[ -n "$Debug" ]] && set -x
main "$@"
