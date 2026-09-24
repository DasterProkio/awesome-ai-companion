#!/bin/sh
# Downloads the OFL fonts used by scene.html into ./fonts (git-ignored).
set -e
cd "$(dirname "$0")"; mkdir -p fonts
base=https://raw.githubusercontent.com/google/fonts/main/ofl
get() { [ -s "fonts/$2" ] || curl -fsSL -o "fonts/$2" "$base/$1"; }
get "notoserifsc/NotoSerifSC%5Bwght%5D.ttf" NotoSerifSC.ttf
get "notosanssc/NotoSansSC%5Bwght%5D.ttf" NotoSansSC.ttf
get "fraunces/Fraunces%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf" Fraunces.ttf
get "fraunces/Fraunces-Italic%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf" Fraunces-Italic.ttf
get "jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf" JetBrainsMono.ttf
ls -la fonts
