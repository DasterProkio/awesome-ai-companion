#!/bin/sh
# Downloads what scene.html needs but the repo doesn't ship (both git-ignored):
#   fonts/    OFL fonts (Noto Serif/Sans SC, Fraunces, JetBrains Mono)
#   avatars/  GitHub avatars of the authors listed in timeline.json
set -e
cd "$(dirname "$0")"; mkdir -p fonts avatars
base=https://raw.githubusercontent.com/google/fonts/main/ofl
get() { [ -s "fonts/$2" ] || curl -fsSL -o "fonts/$2" "$base/$1"; }
get "notoserifsc/NotoSerifSC%5Bwght%5D.ttf" NotoSerifSC.ttf
get "notosanssc/NotoSansSC%5Bwght%5D.ttf" NotoSansSC.ttf
get "fraunces/Fraunces%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf" Fraunces.ttf
get "fraunces/Fraunces-Italic%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf" Fraunces-Italic.ttf
get "jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf" JetBrainsMono.ttf
for u in $(python3 -c "import json; print(' '.join(a['login'] for a in json.load(open('timeline.json'))['authors']))"); do
  [ -s "avatars/$u.png" ] || curl -fsSL -o "avatars/$u.png" "https://avatars.githubusercontent.com/$u?s=240"
done
ls fonts avatars
