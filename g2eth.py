#!/bin/python3
import requests, re, argparse, os, sys, random;
from time import sleep;
from decimal import Decimal as D;
from platform import platform as getOS;
DB=("\033[01;38;5;21m")
RD=("\033[01;38;5;9m")
PNK=("\033[01;38;5;13m")
PRP=("\033[01;38;5;55m")
GRN=("\033[01;38;5;10m")
DRK=("\033[01;38;5;8m")
WHT=("\033[01;38;5;15m")
GRY=("\033[01;38;5;242m")
NVD=("\033[1;42;97m")
AMD=("\033[1;41;97m")
RESET=("\033[0m")
LOAD=("\033[1;49;32m")
if (os.path.isdir('/data/data/com.termux')):
    OS = ('Termux')
elif ('Linux') in (getOS()):
    OS = ('Linux')
elif ('Windows') in (getOS()):
    OS = ('Windows')
script = (os.path.basename(sys.argv[0]))
counter = [0]
RANDOM = [('/', '-', '\\', '|'),  ('⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏') , ('◜','◠','◝','◞','◡','◟'),('↰','↱','↲','↳')]
def multiply(A, B):
    return (float(A) * float(B))
Agents = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Mozilla/5.0 (X11; U; Linux x86_64; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/531.2+',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.02',
    'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'
]
def loading():	
    CHARS = random.choice(RANDOM)
    for i in range(10):
        counter[0] += 1
        sys.stdout.write('\r')
        sys.stdout.write(f"{LOAD}%s{RESET}" % CHARS[counter[0] % len(CHARS)])
        sys.stdout.flush()
        sleep(.2)
    sys.stdout.write("\b ")
    return()
def loading2(duration):	
    CHARS = random.choice(RANDOM)
    for i in range(10):
        counter[0] += 1
        sys.stdout.write('\r')
        sys.stdout.write(f"{LOAD}%s{RESET}" % CHARS[counter[0] % len(CHARS)])
        sys.stdout.flush()
        sleep(duration)
    sys.stdout.write("\b ")
    return()
def echo(data):
	blank = ' '
	s = ''
	for l in blank:
		sys.stdout.write('\r')
		sys.stdout.write(f"{DRK}[{GRN}-{GRN}♦{GRN}-{DRK}] {GRN}{data}")
		s += (f"{l}")
		sys.stdout.flush()
		sleep(0.3)
	sys.stdout.write("\n")
def icon():
    icon = (f"""
                   ..
                  {WHT},d{GRY}:.
                 {WHT}:dd{GRY}::,
                {WHT}lddd{GRY}:::;
              {WHT}.odddd{GRY}:::::.
             {WHT};dddddd{GRY}::::::'
            {WHT}cddddddo{GRY}:::::::,
           {WHT}oddool{DRK}c::{GRY},,,;;::::
         {WHT}'olcc{DRK}::::::{GRY},,,,,,,;;:.
            {DRK}::::::::{GRY},,,,,,,,
          {WHT}.    '::::{GRY},,,,.    .
           {WHT}'c'.    :{GRY},     .,.
             {WHT}ddo;.  {GRY}  .';::
              {WHT}'ddddc{GRY},::::.
                {WHT}dddd{GRY}::::
                 {WHT}'dd{GRY}::.
                   {WHT}d{GRY}:    """)
    sys.stdout.write(f"{icon}\n")
def usage():
    info = (f"""{PRP}({RD}Doesn't work with {GRN}GTX {WHT}1050{PNK}/{WHT}1050{GRN}ti {RD}\u2639 {PRP}){DRK}
{GRY}Mining {GRN}Ethereum {GRY}requires {RD}>4GB {GRN}VRAM{PNK}. {GRY}Therefore{PNK}, {GRY}you {RD}cannot {GRY}mine {GRN}ETH {GRY}with a {GRN}1050{PNK}. 
{GRY}Formatting the {GRN}GPU {GRY}in your command{PNK}:
      {NVD}NVIDIA{RESET}{DRK} 
{GRN}3060 {WHT}({GRN}NVIDIA RTX 3060 {PNK}({WHT}Non-LHR{PNK}){WHT})
{GRN}3060lhr {WHT}({GRN}NVIDIA RTX 3060 {PNK}({WHT}LHR{PNK}){WHT})
{GRN}3060ti {WHT}({GRN}NVIDIA RTX 3060 Ti {PNK}({WHT}Non-LHR{PNK}){WHT})
{GRN}3060tilhr {WHT}({GRN}NVIDIA RTX 3060 Ti {PNK}({WHT}LHR{PNK}){WHT})
{GRN}2060s {WHT}({GRN}NVIDIA RTX 2060 Super{WHT})
{PNK}& {GRN}Many more{PNK}. . .
        {AMD}AMD{RESET}{DRK}
{RD}580 {WHT}({RD}RX 580{WHT})
{RD}5600xt {WHT}({RD}RX 5600 XT{WHT})
{RD}vega56 {WHT}({RD}AMD VEGA 56{WHT})
{PNK}& {RD}Many more{PNK}. . .
{GRY}Search mining details on a {GRN}GPU
{PNK}./{GRN}{script} {DRK}[{RD}-c{PNK}/{RD}--card {WHT}({GRN}3060 {PNK}| {GRN}3060lhr {PNK}| {GRN}3060ti {PNK}| {GRN}3060tilhr {PNK}| {RD}5600xt {PNK}| {GRN}Etc{WHT}){DRK}]
{PNK}./{GRN}{script} {RD}-c{GRN} 3060
{GRY}List all cards capable of mining {GRN}ETH
{PNK}./{GRN}{script} {RD}-l{PNK}/{RD}--list """)
    info = info.replace('\r','.')
    sys.stdout.write(f"{info}\b")
class get():
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':f"{random.choice(Agents)}"})
        parser = argparse.ArgumentParser(description=f'{GRN}{script} GPU ETH mining stats',add_help=False)
        parser.add_argument('-c', '--card', required=False, action='store',help=f'{GRN}GPU to search for')
        parser.add_argument('-h', '--help',action='help', default=argparse.SUPPRESS,help='Show this help menu')
        parser.add_argument('-u', '--usage' ,required=False, action='store_true', help=f"Advanced Usage")
        parser.add_argument('-l', '--list' ,required=False, action='store_true', help=f"List all cards capable of mining ETH")
        args = parser.parse_args()
        if args.list:
            icon()
            loading()
            self.list_cards()
            exit(0)
        if args.usage:
            usage()
            exit(0)
        else:
            pass
        if args.card:
            if args.card == ('1050') or args.card == ('1050ti'):
                data = (f"{RD}\u2639 {RD} The {GRN}GTX {WHT}1050{PNK}/{WHT}1050{GRN}ti {RD}cannot be used to mine {GRN}ETH {RD}\u2639  {DRK}[{GRN}-{GRN}♦{GRN}-{DRK}]")
                echo(data)
                data = (f"{GRY}Mining {GRN}ETH {GRY}requires {RD}>4GB {GRN}VRAM")
                echo(data)
                exit(0)
            else:
                self.card = args.card
                icon()
                self.get_mhs()
        else:
            pass
    def get_mhs(self):
        btc_page = ('https://api.coindesk.com/v1/bpi/currentprice/usd.json')
        get_btc = (self.session.get(btc_page).text)
        page = (f'https://www.hashrate.no/{self.card}')
        retrieve = (self.session.get(page).text)
        # Get BTC price
        try:
            btc_price = (re.findall('"rate":"(.*?)"',get_btc)[0])
        except:
            btc_price = (f'N/A')
        # Get ETH Price
        try:
            eth_price = (re.findall("ETH: <b>(.*?)</", retrieve)[0])
        except:
            eth_price = ('N/A')
        # GPU Name
        try:
            gpu = (re.findall("<title>(.*?) -",retrieve)[0])
        except:
            gpu = (f'N/A')
        # Eth hashrate
        try:
            eth_rate = (re.findall("ETH</a></font></td><td>(.*?)</", retrieve)[0])
        except:
            eth_rate = ('N/A')
        # Ravencoin hashrate 
        try:
            rvn_rate = (re.findall("RVN</a></font></td><td>(.*?)</", retrieve)[0])
        except:
            rvn_rate = ('N/A')
        # MSRP
        try:
            msrp = (re.findall("<tr><td>MSRP: </td><td>(.*?)</", retrieve)[0])
        except:
            msrp = ('N/A')
        # Release date
        try:
            release_date = (re.findall("Released: </td><td>(.*?)</", retrieve)[0])
        except:
            release_date = ('N/A')
        # TDP
        try:
            tdp = (re.findall("TDP: </td><td>(.*?)</", retrieve)[0])
        except:
            tdp = ('N/A')
        # Power consumption
        try:
            power = (re.findall(f"ETH</a></th></tr><tr><td>Hashrate:</td><td>{eth_rate}</td></tr><tr><td>Power:</td><td>(.*?)</", retrieve)[0])
        except:
            power = ('N/A')
        # Efficiency
        try:
            efficiency = (re.findall(f"ETH</a></font></td><td>{eth_rate}</td><td>{power}</td><td>(.*?)</", retrieve)[0])
        except:
            efficiency = ('N/A')
        # 24h Est.
        try:
            oneday = (re.findall(f"ETH</a></font></td><td>{eth_rate}</td><td>{power}</td><td>{efficiency}</td><td><b>(.*?)</", retrieve)[0])
            # Daily/weekly/monthly
            oned = oneday.rsplit('$')[1]
            weekly = (D(oned) * 7)
            monthly = (D(oned) * 30)
        except:
            oneday = ('N/A')
        # Return of investment
        try:
            test = (oneday.split('.')[1])
            roi = (re.findall(f"{test}</b></td><td>(.*?)</td", retrieve)[0])
        except:
            roi = ('N/A')
        if "NVIDIA" in gpu:
            gpu_name = (f"{NVD}{gpu}{RESET} {DRK}[{GRN}-{GRN}♦{GRN}-{DRK}]")
            data = (f"{gpu_name}")
            echo(data)
            loading()
            data = (f"{DRK}BTC Price{PNK}: {GRN}${GRN}{btc_price} {PNK}:: {DRK}ETH Price{PNK}: {GRN}{eth_price}")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}ETH Hashrate{PNK}: {GRN}{eth_rate} {PNK}") #{PNK}:: {DRK}RVN Hashrate{PNK}: {GRN}{rvn_rate}")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}24h{PNK}: {GRN}{oneday}{PNK} / {DRK}Weekly{PNK}: {GRN}${weekly}{PNK} / {DRK}Monthly{PNK}: {GRN}${monthly}")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}Released{PNK}: {GRN}{release_date} {PNK}:: {DRK}MSRP{PNK}: {GRN}{msrp} ")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}ROI{PNK}: {GRN}{roi} {PNK}:: {DRK}Efficiency{PNK} {GRN}{efficiency}")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}TDP{PNK}: {GRN}{tdp} {PNK}:: {DRK}Power{PNK}: {GRN}{power}")
            echo(data)          
        elif "AMD" in gpu:
            gpu_name = (f"{AMD}{gpu}{RESET} {DRK}[{GRN}-{GRN}♦{GRN}-{DRK}]")
            data = (f"{gpu_name}")
            echo(data)
            loading()
            data = (f"{DRK}BTC Price{PNK}: {RD}${btc_price} {PNK}:: {DRK}ETH Price{PNK}: {RD}{eth_price}")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}ETH Hashrate{PNK}: {RD}{eth_rate} {PNK}") #{PNK}:: {DRK}RVN Hashrate{PNK}: {GRN}{rvn_rate}")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}24h{PNK}: {RD}{oneday}{PNK}/{DRK}Weekly{PNK}: {RD}${weekly}{PNK}/{DRK}Monthly{PNK}: {RD}${monthly}")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}Released{PNK}: {RD}{release_date} {PNK}:: {DRK}MSRP{PNK}: {RD}{msrp} ")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}ROI{PNK}: {RD}{roi} {PNK}:: {DRK}Efficiency{PNK} {RD}{efficiency}")
            echo(data)
            loading2(0.05)
            data = (f"{DRK}TDP{PNK}: {RD}{tdp} {PNK}:: {DRK}Power{PNK}: {RD}{power}")
            echo(data)
            
    def list_cards(self):
        page = (f'https://www.hashrate.no/')
        retrieve = (self.session.get(page).text)
        all_cards = (list(set(re.findall(f"href=/(.*?)>", retrieve))))
        loading()
        for a in all_cards:
            all_cards_clean = (list(set(re.findall(f"href=/{a}>(.*?)</a>", retrieve))))
            for card in all_cards_clean:
                if "NVIDIA" in card:
                    data = (f"{DRK}Card name{PNK}: {GRN}{card} {PNK}| {DRK}Search name{PNK}: {GRN}{a}")
                    echo(data)
                    loading2(0.02)
                elif "AMD" in card:
                    data = (f"{DRK}Card name{PNK}: {RD}{card} {PNK}| {DRK}Search name{PNK}: {RD}{a}")
                    echo(data)
                    loading2(0.02)
                else:
                    data = (f"{DRK}Card name{PNK}: {GRN}{card} {PNK}| {DRK}Search name{PNK}: {GRN}{a}")
                    echo(data)
                    loading2(0.02)
get()