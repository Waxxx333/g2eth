![Script](https://img.shields.io/badge/WaXxX-G2ETH-BF5B16?style=plastic&logo=Ethereum)
![ETH](https://img.shields.io/badge/Ethereum-3C3C3D?style=plastic&logo=Ethereum&logoColor=orange)
![Python](https://img.shields.io/badge/Python-FFD43B?style=plastic&logo=python&logoColor=darkgreen)
![g](https://img.shields.io/badge/GitHub-%2312100E.svg?&style=plastic&logo=Github&logoColor=BF5B16&?labelColor=BF5B16)
![Blah](https://img.shields.io/badge/Python3-RE-7A297B?style=plastic&logo=Python)
![fff](https://img.shields.io/badge/Python3-Requests-7A297B?style=plastic&logo=Python)



# ***G2ETH***
<p align="center">
  <!--<img width="300" height="300" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg">-->
  <img width="300" height="300" src="https://imgur.com/KHidht1.png">
</p>

<hr>

### Get ETH mining stats on a given GPU
##### **Returns current Bitcoin price, current ***ETH*** price, ***ETH*** hashrate of the given GPU, daily, weekly and monthly estimated profit, year the GPU was released, ROI(Return of Investment), Power consumption, efficiency and TDP.**  **Lists all cards capable of mining ***ETH*** and their ***ETH*** mining stats.** ***g2eth*** <strike>**also has a USD/GBP/CAD/EUR to ETH converter and vice versa.**</strike>. Over 150 currencies have been added to the conversion function. 

**Check the current ETH and BTC prices.**
##### 

##### Available statistics:
* Get mining stats on GPUs
  *  Get ETH hash rate on a supplied GPU
  *  Get current ETH price
  *  Get current BTC price
  *  Daily, weekly and monthly estimated earnings
  *  MSRP, Release year, projected ROI, TDP, Efficiency, Power consumption
* List all GPUs capable of mining ETH
* Convert over 150 currencies
* Get current ETH and BTC price and status
  * You can now also specify other coins to get a current price on

### ***Some*** of the currencies supported:
* AUR - Auroracoin
* BCC - BitConnect (inactive)
* BCH - Bitcoin Cash
* BTC or XBT - Bitcoin
* DASH - Dash
* DOGE or XDG - Dogecoin
* EOS - EOS.IO
* ETC - Ethereum Classic
* ETH - Ether (also known as Ethereum)
* GRC - Gridcoin
* LTC - Litecoin
* KOI or COYE - Coinye (inactive)
* And so many more 


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
└─⋗ g2eth -l
[■] Card name: NVIDIA GTX 1080 .:|:. Command name: 1080
[■] Card name: AMD RX 6800 .:|:. Command name: 6800
[■] Card name: NVIDIA CMP 90HX .:|:. Command name: cmp90
[■] Card name: NVIDIA P106-100 .:|:. Command name: p106
```
##### Convert over 150 currencies from a local currency to crypto or vice versa <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg#gh-light-mode-only" alt="python" align=left width=24><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg#gh-dark-mode-only" alt="python" align=left width=24><br>
```python
g2eth --convert/-c [USD/GBP/CAD/EUR/ETH] --into/-i [USD/GBP/CAD/EUR/ETH] --amount/-n [AMOUNT]
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -c usd -i grc -n 10 
[■] Conversion is courtesy of: cryps.info
[■] 10.0 USD to GRC (US Dollar to Gridcoin)  [■]
[■] 10.0 U$D == 1,132.95960772 GRC [■]
```

#### Now you can get current prices on more coins than ETH and BTC. Usage is as follows:
###### <kbd>Just check Bitcoin and Ethereum</kbd>
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -p
[■] ₿TC Price: $37,875.6767
[■] ΞTH Price: $2611 .::. Down: -3.83634
```
##### <kbd>Get price of a custom coin:</kbd>
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -p Dogecoin
[■] DOGE Price: $0.1228
[■] ₿TC Price: $37,875.6767
[■] ΞTH Price: $2611 .::. Down: -3.83634
```
<hr>

###### Requirements: <kbd>python-requests</kbd> | but the installation script will attempt to install it. 
<!--
|Feature            |Termux | Linux | Windows | WSL
|-------------------|-----|-------|---|------------|
| Installer Compatible with    |    |✓      |  |   ✓-->
###### **For** ***Windows*** and ***Termux*** **you will have to manually install python-requests**. **You will need <kbd>pip</kbd> if you're on Windows or Termux to install <kbd>requests</kbd>.** **I will be fixing this at some point. Right now the installer supports: **openSUSE, Arch-based distros, Debian-based distros and Fedora**
###### **This script doesn't work for ***GTX 1050*** cards as because you need ***<kbd>>4GB</kbd>*** ***VRAM*** to mine ***ETH*****. 

###### G2ETH now has tab completion if you install it via <kbd>install.sh</kbd>. You must be using <kbd>zsh</kbd> or <kbd>bash</kbd> and you also need to have <kbd>bash-completion</kbd> for <kbd>bash</kbd> or <kbd>zsh-completions</kbd> for <kbd>zsh</kbd>. Run the install script, close your shell, reopen a shell and type <kbd>g2eth --</kbd> (***two hyphens***) and press ***tab***.


<hr>

<h1 align="center">Screenshots</h1>

<p align="center">
  <img src="https://i.imgur.com/Dt8Q56c.png" width="710" height="900">
  <img src="https://i.imgur.com/SxDR9aQ.png" width="710" height="500">
   <img src="https://i.imgur.com/CcbfYKE.png" width="710" height="500">
</p>


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
    <li>Added zsh and bash tab completion</li>
    <li>Added over 150 currencies to the conversion function</li>
    </ul>
</details>

> To Do
- [ ] Add more distros' package managers to the installer
- [ ] Make installer work in Winblows
- [ ] Make installer work with Termux
- [ ] Make STDOUT <kbd>prettier</kbd> on Termux
- [ ] Maybe a side-by-side comparison function
  - [x] Make the ***price check*** function have more currencies
  - [x] <strike>***Add current ETH price function***</strike>
  - [x] <strike>***Add Canadian Dollars***</strike>
  - [x] <strike>***Make <kbd>install.sh</kbd>***</strike> 
  - [x] <strike>***Create <kbd>requirements.txt</kbd>***</strike>
  - [x] Work on bash and zsh completion
  - [x] Add more currencies to the conversion function

##### All information is scraped, no APIs are being used.

GPU stats are from [hashrate.no](https://hashrate.no)

Price conversions are from [cryps.info](https://www.cryps.info/)

Price checks are from: [coinmarketcap](https://coinmarketcap.com), [hashrate.io](https://www.hashrate.no/), and [walletinvestor](https://walletinvestor.com)
  
<hr>

<p align="center">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/amd.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/nvidia.svg" width="75" height="75">
</p>
<p align="center">
  <a href="https://twitter.com/waxxx333"><img src="https://img.shields.io/badge/-WaXxX-E34F26?style=plastic&logo=Windows%2095&logoColor=white"></a>
</p>

<hr>
