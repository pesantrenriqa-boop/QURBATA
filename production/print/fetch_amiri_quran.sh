#!/usr/bin/env bash
set -euo pipefail

font_dir="production/print/fonts"
font_path="${font_dir}/AmiriQuran.ttf"
license_path="${font_dir}/OFL-Amiri.txt"
font_url="https://raw.githubusercontent.com/aliftype/amiri/1.003/fonts/AmiriQuran.ttf"
license_url="https://raw.githubusercontent.com/aliftype/amiri/1.003/OFL.txt"
font_sha256="5594121cfcd33d05ea4635b7908d15c0eced0c91aa06469a95354b3369ca2949"

mkdir -p "${font_dir}"
curl --fail --location --silent --show-error "${font_url}" --output "${font_path}"
curl --fail --location --silent --show-error "${license_url}" --output "${license_path}"
printf '%s  %s\n' "${font_sha256}" "${font_path}" | sha256sum --check --status

echo "Amiri Quran 1.003 downloaded and verified at ${font_path}"
