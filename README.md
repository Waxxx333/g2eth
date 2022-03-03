![Script](https://img.shields.io/badge/WaXxX-G2ETH-BF5B16?style=plastic&logo=Ethereum)
![ETH](https://img.shields.io/badge/Ethereum-3C3C3D?style=plastic&logo=Ethereum&logoColor=orange)
![Python](https://img.shields.io/badge/Python-FFD43B?style=plastic&logo=python&logoColor=darkgreen)
![g](https://img.shields.io/badge/GitHub-%2312100E.svg?&style=plastic&logo=Github&logoColor=BF5B16&?labelColor=BF5B16)
![Blah](https://img.shields.io/badge/Python3-RE-7A297B?style=plastic&logo=Python)
![fff](https://img.shields.io/badge/Python3-Requests-7A297B?style=plastic&logo=Python)
[![BTC Tip Jar](https://img.shields.io/badge/BTC-DONATE%20HERE-orange.svg?logo=bitcoin&style=flat)](https://www.blockchain.com/btc/address/bc1q7057d3g5vp8zrtcttcq6cz8fmqxhl8yt27kqdt)

# ***★G2ETH★*** <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg#gh-light-mode-only" alt="python" align=left width=24><img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg#gh-dark-mode-only" alt="python" align=left width=24><br>
<p align="center">
  <!--⁑<img width="300" height="300" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg">-->
  <img width="300" height="300" src="https://imgur.com/KHidht1.png">
</p>


<hr>

## Get ETH mining stats on GPUs, convert crypto currencies into local currencies or vice versa, get current crypto prices and list GPUs capable of mining Ethereum
###### ⁂ ***All data is estimated***

##### · Functions: 
* <b> Has installation script for Linux-based systems [¶](#install)
* <b> Check the stats on a GPU for mining Ethereum [¶](#gpu)
  * <b> Estimated ROI ***(Return of Investment)***
  * <b> Power consumption
  * <b> Hash rate of a given GPU
  * <b> Estimated earnings
    * Daily
    * Weekly
    * Monthly
  * <b> Efficiency
  * <b> MSRP
  * <b> Release year
  * <b> TDP
* <b> Convert crypto [¶](#convert)
  * <b> Convert a crypto currency to your local currency 
  * <b> Convert your local currency to a crypto currency
  * <b> Convert a crypto currency to another crypto currency
    * **Over 150 currencies supported**
* <b> List GPUs that are capable of mining Ethereum [¶](#list)
* <b> Check crypto prices [¶](#check)
  * Check prices on specified coins 
  * Check prices on 200+ coins all at once </b>

<hr>


<a name="install"></a> 
### ● Installation/Usage
#### ° To install:
```python
git clone --depth 1 https://github.com/Waxxx333/g2eth.git
cd g2eth
chmod +x install.sh
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ ./install.sh
```
#### ° Or simply run it:
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

<a name="gpu"></a>
### ● Get the mining stats on GPUs
#### ° You can get the Ethereum mining statistics on NVIDIA and AMD graphics cards. You can use the <kbd>-l/--list</kbd> flag to retrieve a list of GPUs capable of mining Ethereum.

###### · The command format for GPUs, for example, would look like: LHR 3080 would be <kbd>g2eth -g 3080lhr</kbd>; a non-LHR(FHR) 3080 would be: <kbd>g2eth -g 3080</kbd>; for a Super card,  the syntax would be: <kbd>g2eth -g 2070s</kbd>
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -g 3060tilhr
[■] NVIDIA RTX 3080 LHR [■]
[■] ₿TC Price: $43,461.9767 .::. ΞTH Price: $2953 .::. Up: 13.639
[■] ΞTH Hashrate(DaggerHashimoto): 71.70 Mh/s 
[■] 24h: $2.89 / Weekly: $20.23 / Monthly: $86.70
[■] Released:  2021  .::. MSRP: $999  
[■] ROI: 346 days .::. Efficiency 0.316 Mh/w
[■] TDP: 320 watt .::. Power: 227w :: 5.4 kwh
``` 

<a name="list"></a>
### ● List GPUs capable of mining ETH
#### ° Retrieve a list of GPUs capable of mining Ethereum. The name on the left is the actual name, the name on the right side, or ***Command name*** is the name to use with the script. E.g <kbd>g2eth -g 1080</kbd>
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -l
[■] Card name: NVIDIA GTX 1080 .:|:. Command name: 1080
[■] Card name: AMD RX 6800 .:|:. Command name: 6800
[■] Card name: NVIDIA CMP 90HX .:|:. Command name: cmp90
[■] Card name: NVIDIA P106-100 .:|:. Command name: p106
```

<a name="convert"></a>  
## ● Convert crypto currencies 
#### ° ***Some*** of the currencies supported:
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
* && many more 

```python
g2eth --convert/-c [USD/GBP/CAD/EUR/ETH] --into/-i [USD/GBP/CAD/EUR/ETH] --amount/-n [AMOUNT]
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -c usd -i grc -n 10 
[■] Conversion is courtesy of: cryps.info
[■] 10.0 USD to GRC (US Dollar to Gridcoin)  [■]
[■] 10.0 U$D == 1,132.95960772 GRC [■]
```

<a name="check"></a>
## ● Check current crypto prices
#### ° By default it will retrieve just ETH and BTC prices, but you can specify a currency to check the price on by adding it to the <kbd>--price/-p</kbd> flag
###### · Just check Ethereum and Bitcoin
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -p
[■] ₿TC Price: $37,875.6767
[■] ΞTH Price: $2611 .::. Down: -3.83634
```
###### · Check the price of another coin
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -p Dogecoin
[■] DOGE Price: $0.1228
[■] ₿TC Price: $37,875.6767
[■] ΞTH Price: $2611 .::. Down: -3.83634
```
###### · Check the price of over 200 coins all at once
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<g2eth>
└─⋗ g2eth -p all
[■] Name         Price         Alt                 
[■] Moonriver    $67.57        MOVR                
[■] PancakeSwap  $6.74         CAKE                
[■] Helium       $24.91        HNT                 
[■] Siacoin      $0.009572      SC                  
[■] Polkadot     $18.44        DOT                 
[■] Request      $0.2214       REQ                 
[■] OKB          $17.87        OKB                 
[■] Zilliqa      $0.04461      ZIL                 
[■] Secret       $5.40         SCRT                
[■] GateToken    $6.76         GT 
```  

<hr>

###### · Requirements: <kbd>python-requests</kbd> | but the installation script will attempt to install it in Linux based systems. 


###### · For Windows and Termux you will have to manually install python-requests. You will need pip if you're on Windows or Termux to install requests. **I will be fixing this at some point. Right now the installer supports: openSUSE, Arch-based distros, Debian-based distros and Fedora
###### · This script doesn't work for GTX 1050 cards as because you need >4GB VRAM to mine ETH.
###### · G2ETH now has tab completion if you install it via install.sh. You must be using zsh or bash and you also need to have bash-completion for bash or zsh-completions for zsh. Run the install script, close your shell, reopen a shell and type g2eth -- (two hyphens) and press tab. Has an advanced usage menu for extra hep with its functions.

<hr>

<h1 align="center">Screenshots</h1>

<p align="center">
  <img src="https://i.imgur.com/Dt8Q56c.png" width="710" height="900">
  <img src="https://i.imgur.com/SxDR9aQ.png" width="710" height="500">
   <img src="https://i.imgur.com/CcbfYKE.png" width="710" height="500">
  <img src="https://i.imgur.com/u1ARbmG.png" width="710" height="500">
</p>





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

<details>
  <summary><kbd>Changes</kbd></summary>
  <ul>
    <li><b> · Added function to convert ETH to USD/GBP and vice versa</li>
    <li><b> · Added function to list ALL cards and all of their stats</li>
    <li><b> · Shows <kbd>+/-</kbd> ETH</li>
    <li> · Added price function</li>
    <li> · Added CAD and EUR to the converter</li>
    <li> · Updated script according to the source's source code change(Source: let me know if there's a problem with this project)</li>
    <li> · Fixed conversion decimal problem</li>
    <li> · Got rid of redundant "list all and stat" function</li>
    <li> · Added zsh and bash tab completion</li>
    <li> · Added over 150 currencies to the conversion function</li>
    </ul>
</details>  

##### All data is scraped.

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
  <a href="https://www.blockchain.com/btc/address/bc1q7057d3g5vp8zrtcttcq6cz8fmqxhl8yt27kqdt"><img src="https://img.shields.io/badge/BTC-DONATE%20HERE-orange.svg?logo=bitcoin&style=flat"></a>
  <a href="https://www.blockchain.com/btc/address/bc1q7057d3g5vp8zrtcttcq6cz8fmqxhl8yt27kqdt"><br>bc1q7057d3g5vp8zrtcttcq6cz8fmqxhl8yt27kqdt</a>
</p>
  
<hr>

