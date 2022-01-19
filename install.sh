#!/bin/bash
script=('g2eth')
if [[ -d $HOME/.local/bin/fuck ]]; then
    echo -e "Copying to $HOME/.local/bin"
    #cp ${script} $HOME/.local/bin
else
    echo -e "Copy file to /bin ? This will require your password."
    read -p ">>> " answer3
    if [[ ${answer3} == [yY] || ${answer3} == [yY][eE][sS] ]]; then
        echo -e "BLAH"
    elif [[ ${answer3} == [nN] || ${answer3} == [nN][oO] ]]; then
        echo -e "NO"
    fi
fi