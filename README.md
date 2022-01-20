![fff](https://img.shields.io/badge/Python-Requests-ff69b4.svg)
![Python3](https://img.shields.io/badge/Python-ETH-orange.svg)
![G2ETH](https://img.shields.io/badge/Python-G2ETH-8300FF.svg)
![Blah](https://img.shields.io/badge/Python-RE-FF5100.svg)
# ***G2ETH***
#### ***Get mining stats on given GPUs***
<p align="center">
  <img width="300" height="300" src="https://imgur.com/KHidht1.png">
</p>
<!--
<p align="center">
  <img src="https://imgur.com/5KxT8pi.png" width="600" height="500">
</p><hr>-->
<hr>

### Get ETH mining stats on a given GPU
##### **Returns current Bitcoin price, current ***ETH*** price, ***ETH*** hashrate of the given GPU, daily, weekly and monthly estimated profit, year the GPU was released, ROI(Return of Investment), Power consumption, efficiency and TDP. Also lists all 54 cards capable of mining ***ETH*** and their ***ETH*** mining stats.**
<hr>

##### To install:
```shell
git clone https://github.com/Waxxx333/g2eth
cd g2eth
chmod +x install.sh
./install.sh
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -h
g2eth.py GPU ETH mining stats

options:
  -c CARD, --card CARD  GPU to search for
  -h, --help            Show this help menu
  -u, --usage           Advanced Usage
  -l, --list            List all cards capable of mining ETH

```
##### Or simply run it:
```bash
https://github.com/Waxxx333/g2eth
cd g2eth
chmod +x g2eth
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ python3 g2eth -h/--help
g2eth.py GPU ETH mining stats

options:
  -c CARD, --card CARD  GPU to search for
  -h, --help            Show this help menu
  -u, --usage           Advanced Usage
  -l, --list            List all cards capable of mining ETH
```
#### Command formatting: 
 - `g2eth -c 3060ti` = 3060 Ti Non-LHR
 - `g2eth -c 3060tilhr` = 3060 Ti LHR 
 - `g2eth -c 3060lhr` = 3060 LHR 
 - `g2eth -c 3060` = 3060 Non-LHR 
 - `g2eth -c 2060s` Super cards (1660 Super | 2060 Super) 
 - Etc. . .
 ##### ***Using the*** `-l/--list` ***flag will show all cards capable of mining `ETH` and it will also give the name you need to use in the command to search the stats***

##### Example output:
```bash
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -c 3060tilhr
[-*-] NVIDIA RTX 3060 Ti LHR [-*-]
[-*-] BTC Price: $42,048.8317 :: ETH Price: $3127
[-*-] ETH Hashrate: 45.05 Mh/s
[-*-] 24h: $2.16 / Weekly: $15.12 / Monthly: $64.80
[-*-] Released: 2021 :: MSRP: $499
[-*-] ROI: 232 days :: Efficiency 0.309 Mh/w
[-*-] TDP: 220 watt :: Power: 146w
```
###### Requirements: `python-requests` | but the installation script will attempt to install it. 
|Feature            |Termux | Linux | Windows | WSL
|-------------------|-----|-------|---|------------|
| Installer Compatible with    |    |✓      |  |   ✓
###### **For** ***Windows*** and ***Termux*** **you will have to manually install python-requests**. **You will need** `pip`. **I will be fixing this at some point.**

> Todos
- [ ] Add more distros' package managers to the installer
- [ ] Make installer work in Winblows
- [ ] Make installer work with Termux
  - [x] <strike>***Make `install.sh`***</strike> 
  - [x] <strike>***Create `requirements.txt`***</strike>

<hr><hr>

