#!/bin/bash
script=('fuck.sh')
RD=("\033[01;38;5;9m")
PNK=("\033[01;38;5;13m")
PRP=("\033[01;38;5;55m")
GRN=("\033[01;38;5;10m")
DRK=("\033[01;38;5;8m")
WHT=("\033[01;38;5;15m")
GRY=("\033[01;38;5;242m")
echo -e "${DRK}Making ${GRN}${script} ${DRK}executable $(chmod +x ${script})"
if grep -q "arch" /etc/os-release; then
    export DISTRO="Arch"
elif grep -q "debian" /etc/os-release; then
    export DISTRO="Debian"
fi
install_script() {
    # Where to install
    if [[ -d $HOME/.local/bin/fuck ]]; then
        echo -e "Copying to $HOME/.local/bin"
        #cp ${script} $HOME/.local/bin
    else
        echo -e "Copy file to /bin ? This will require your password."
        read -p ">>> " answer3
        if [[ ${answer3} == [yY] || ${answer3} == [yY][eE][sS] ]]; then
            chmod +x ${script}
            #sudo cp ${script} /bin/
        elif [[ ${answer3} == [nN] || ${answer3} == [nN][oO] ]]; then
            echo -e "${GRN}You can still run the script with${PNK}:\n./${GRN}${script} ${DRK}[${RD}-u${PNK}/${RD}--usage ${PNK}| ${RD}-c${PNK}/${RD}--card ${WHT}(${GRN}3060lhr ${PNK}| ${RD}580${WHT}) ${PNK}| ${RD}-l${PNK}/${RD}--list${DRK}]"
            echo -e "${RD}Or${PNK}:\n${GRN}python3 ${script} ${DRK}[${RD}-u${PNK}/${RD}--usage ${PNK}| ${RD}-c${PNK}/${RD}--card ${PNK}| ${RD}-l${PNK}/${RD}--list${DRK}]"
        fi
    fi
}
get_pip() {
    if [[ ${DISTRO} == "Arch" ]]; then
        echo -e "${GRN}Arch${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python${PNK}-${GRN}pip"
        sudo pacman -S python-pip
        get_requests
    elif [[ ${DISTRO} == "Debian" ]]; then
        echo -e "${GRN}Debian${PNK}-${GRN}based ${DRK}distro detected ${PNK}:: ${DRK}Installing ${GRN}python3${PNK}-${GRN}pip"
        sudo apt install python3-pip
        get_requests
    fi
}
get_requests() {
    command pip help &>/dev/null
    if [[ $? != 0 ]]; then
        echo -e "${RD}pip not found${PNK}. ${GRN}Install now to continue script installation ?"
        read -p ">>> " answer2
        if [[ ${answer2} == [yY] || ${answer2} == [yY][eE][sS] ]]; then
            echo -e "${DRK}Installing ${GRN}pip"
            get_pip
        elif [[ ${answer2} == [nN] || ${answer2} == [nN][oO] ]]; then
            echo -e "Aborting"
        fi
    else
        echo -e "${GRN}pip found"
        pip install requests --user
        command python3 -c "import requests; print(True)" &>/dev/null
        if [[ $? == 0 ]]; then
            install_script
        else
            echo -e "${RD}You're going to have to manually install requests."
        fi
    fi
}


initialize() {
    command python3 -c "import requests; print(True)" &>/dev/null
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