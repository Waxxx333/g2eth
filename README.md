![Script](https://img.shields.io/badge/WaXxX-G2ETH-BF5B16?style=plastic&logo=Ethereum)
![ETH](https://img.shields.io/badge/Ethereum-3C3C3D?style=plastic&logo=Ethereum&logoColor=orange)
![Python](https://img.shields.io/badge/Python-FFD43B?style=plastic&logo=python&logoColor=darkgreen)
![g](https://img.shields.io/badge/GitHub-%2312100E.svg?&style=plastic&logo=Github&logoColor=BF5B16&?labelColor=BF5B16)
![Blah](https://img.shields.io/badge/Python3-RE-7A297B?style=plastic&logo=Python)
![fff](https://img.shields.io/badge/Python3-Requests-7A297B?style=plastic&logo=Python)

# ***G2ETH***
<p align="center">
  <img width="300" height="300" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg">
  <img width="300" height="300" src="https://imgur.com/KHidht1.png">
</p>

<hr>

### Get ETH mining stats on a given GPU
##### **Returns current Bitcoin price, current ***ETH*** price, ***ETH*** hashrate of the given GPU, daily, weekly and monthly estimated profit, year the GPU was released, ROI(Return of Investment), Power consumption, efficiency and TDP.** 
##### **Lists all cards capable of mining ***ETH*** and their ***ETH*** mining stats.** ***g2eth*** **also has a USD/GBP/CAD/EUR to ETH converter and vice versa.**
##### **Check the current ETH and BTC prices.**
<hr>

##### To install:
```python
git clone --depth 1 https://github.com/Waxxx333/g2eth.git
cd g2eth
chmod +x install.sh
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ ./install.sh
```
##### Or simply run it:
```python
git clone --depth 1 https://github.com/Waxxx333/g2eth
cd g2eth
chmod +x g2eth
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ python3 g2eth -h/--help
g2eth.py GPU ETH mining stats

options:
  -g GPU, --gpu GPU     GPU to search for
  -h, --help            Show this help menu
  -u, --usage           Advanced Usage
  -l, --list            List all cards capable of mining ETH
  -p, --price           Show BTC and ETH price
  -c CONVERT, --convert CONVERT | Currency to conver ETH/USD/GBP
  -i INTO, --into INTO | Currency to convert into ETH/USD/GBP
  -n AMOUNT, --amount AMOUNT | Amount to convert
```
#### Command formatting: 
 - <kbd>g2eth -g 3060ti</kbd> = 3060 Ti Non-LHR
 - <kbd>g2eth -g 3060tilhr</kbd> = 3060 Ti LHR 
 - <kbd>g2eth -g 3060lhr</kbd> = 3060 LHR 
 - <kbd>g2eth -g 3060</kbd> = 3060 Non-LHR 
 - <kbd>g2eth -g 2060s</kbd> Super cards (1660 Super | 2060 Super) 
 - Etc. . .

##### Example output:
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -g 3060tilhr
[■] NVIDIA RTX 3080 LHR [■]
[■] BTC Price: $37,280.0200 .::. ETH Price: $2448 .::. Up: 2.7543
[■] ETH Hashrate(DaggerHashimoto): 71.70 Mh/s
[■] 24h: $2.15 / Weekly: $15.05 / Monthly: $64.50
[■] Released: 2021 .::. MSRP: $999
[■] ROI: 465 days .::. Efficiency 0.316 Mh/w
[■] TDP: 320 watt .::. Power: 227w
``` 
 ##### ***Using the*** <kbd>-l/--list</kbd> ***flag will show all cards capable of mining <kbd>ETH</kbd> and it will also give the name you need to use in the command to search the stats***
###### <kbd>-l/--list</kbd> arg will give something like the following. The name after <kbd>Command name:</kbd> is the name you'll use to search the GPU by.
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ ./g2eth.py -l
[■] Card name: NVIDIA GTX 1080 .:|:. Command name: 1080
[■] Card name: AMD RX 6800 .:|:. Command name: 6800
[■] Card name: NVIDIA CMP 90HX .:|:. Command name: cmp90
[■] Card name: NVIDIA P106-100 .:|:. Command name: p106
```
##### Convert USD/GBP/CAD/EUR to ETH or ETH to USD/GBP/CAD/EUR <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg#gh-light-mode-only" alt="python" align=left width=24><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg#gh-dark-mode-only" alt="python" align=left width=24><br>
```python
g2eth --convert/-c [USD/GBP/CAD/EUR/ETH] --into/-i [USD/GBP/CAD/EUR/ETH] --amount/-n [AMOUNT]
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth.py --convert eth --into usd --amount 20
[■] Converting: ♦20.0 ETH into: $48508.72 USD [■]
```
<hr>

###### Requirements: <kbd>python-requests</kbd> | but the installation script will attempt to install it. 
<!--
|Feature            |Termux | Linux | Windows | WSL
|-------------------|-----|-------|---|------------|
| Installer Compatible with    |    |✓      |  |   ✓-->
###### **For** ***Windows*** and ***Termux*** **you will have to manually install python-requests**. **You will need <kbd>pip</kbd> if you're on Windows or Termux to install <kbd>requests</kbd>.** **I will be fixing this at some point. Right now the installer supports: **openSUSE, Arch-based distros, Debian-based distros and Fedora**
###### **This script doesn't work for ***GTX 1050*** cards as because you need ***<kbd>>4GB</kbd>*** ***VRAM*** to mine ***ETH*****. 

* To Do
- [ ] Add more distros' package managers to the installer
- [ ] Make installer work in Winblows
- [ ] Make installer work with Termux
- [ ] Make STDOUT <kbd>prettier</kbd> on Termux
- [ ] Work on bash and zsh completion
- [ ] Maybe a side-by-side comparison function
  - [x] <strike>***Add current ETH price function***</strike>
  - [x] <strike>***Add Canadian Dollars***</strike>
  - [x] <strike>***Make <kbd>install.sh</kbd>***</strike> 
  - [x] <strike>***Create <kbd>requirements.txt</kbd>***</strike>


<p align="center">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/amd.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/nvidia.svg" width="75" height="75">
</p>

<a href="https://twitter.com/waxxx333"><img src="https://img.shields.io/badge/-WaXxX-E34F26?style=plastic&logo=Windows%2095&logoColor=white"></a>

<hr><hr>
<!--
* <kbd>1.3</kbd>
    * Updated code accordingly to source's code change
-->

<details>
  <summary><kbd>Changes</kbd></summary>
  <ul>
    <li><b>Added function to convert ETH to USD/GBP and vice versa</li>
    <li><b>Added function to list ALL cards and all of their stats</li>
    <li><b>Shows <kbd>+/-</kbd> ETH</li>
    <li>Added price function</li>
    <li>Added CAD and EUR to the converter</li>
    <li>Updated script according to the source's source code change(Source: let me know if there's a problem with this project)</li>
    <li>Fixed conversion decimal problem</li>
    <li>Got rid of redundant "list all and stat" function</li>
    </ul>
</details>
