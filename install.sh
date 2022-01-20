#!/bin/bash
script=("g2eth")
RD=("\033[01;38;5;9m")
PNK=("\033[01;38;5;13m")
PRP=("\033[01;38;5;55m")
GRN=("\033[01;38;5;10m")
DRK=("\033[01;38;5;242m")
WHT=("\033[01;38;5;15m")
echo -e "${DRK}Getting ready to install ${GRN}${script}"
echo -e "${DRK}Making ${GRN}${script} ${DRK}executable $(chmod +x ${script})"
if grep -qi "arch" /etc/os-release; then
    export DISTRO="Arch" 
elif grep -qi "debian" /etc/os-release; then
    export DISTRO="Debian" 
elif grep -qi 'fedora' /etc/os-release; then
    export DISTRO="Fedora" 
elif grep -qi "opensuse" /etc/os-release; then
    export DISTRO="openSUSE" 
fi
install_script() {
    if [[ -d $HOME/.local/bin/ ]]; then
        echo -e "${DRK}Copying to ${GRN}$HOME/.local/bin"
        cp ${script} $HOME/.local/bin
    else
        echo -e "Copy file to /bin ? This will require your password."
        read -p ">>> " answer3
        if [[ ${answer3} == [yY] || ${answer3} == [yY][eE][sS] ]]; then
            chmod +x ${script}
            sudo cp ${script} /bin/
        elif [[ ${answer3} == [nN] || ${answer3} == [nN][oO] ]]; then
            echo -e "${GRN}You can still run the script with${PNK}:\n./${GRN}${script} ${DRK}[${RD}-u${PNK}/${RD}--usage ${PNK}| ${RD}-c${PNK}/${RD}--card ${WHT}(${GRN}3060lhr ${PNK}| ${RD}580${WHT}) ${PNK}| ${RD}-l${PNK}/${RD}--list${DRK}]"
            echo -e "${RD}Or${PNK}:\n${GRN}python3 ${script} ${DRK}[${RD}-u${PNK}/${RD}--usage ${PNK}| ${RD}-c${PNK}/${RD}--card ${PNK}| ${RD}-l${PNK}/${RD}--list${DRK}]"
        fi
    fi
}
get_requests() {
    if [[ ${DISTRO} == "Arch" ]]; then
        echo -e "${GRN}Arch${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python${PNK}-${GRN}pip"
        sudo pacman --noconfirm -S python-requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    elif [[ ${DISTRO} == "Debian" ]]; then
        echo -e "${GRN}Debian${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python3${PNK}-${GRN}pip"
        sudo apt-get -y install python3-requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    elif [[ ${DISTRO} == "Fedora" ]]; then
        echo -e "${GRN}Fedora${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python3${PNK}-${GRN}pip"
        sudo dnf install  python3-requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    elif [[ ${DISTRO} == "openSUSE" ]]; then
        echo -e "${GRN}Fedora${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python3${PNK}-${GRN}pip"
        sudo zypper install python3-requests
        command python3 -c "import requests;" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    fi
}

initialize() {
    command python3 -c "import requests;" &>/dev/null
    if [[ $? == 0 ]]; then
        echo -e "${GRN}requests found ${PNK}. . . ${GRN}Continuing installation"
        install_script
    elif [[ $? != 0 ]]; then
        echo -e "${RD}requests not found. Install now to continue script installation ?"
        read -p ">>> " answer1
        if [[ ${answer1} == [yY] || ${answer1} == [yY][eE][sS] ]]; then
            echo -e "${GRN}Attempting to install requests"
            get_requests
        elif [[ ${answer1} == [nN] || ${answer1} == [nN][oO] ]]; then
            echo -e "Aborting"
        fi
    fi
}
initialize