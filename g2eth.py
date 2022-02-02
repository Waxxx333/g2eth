#!/bin/python3
import requests, re, argparse, os, sys, random;
from time import sleep;
from decimal import Decimal as D;
DB=("\033[01;38;5;21m")
RD=("\033[01;38;5;9m")
PNK=("\033[01;38;5;201m")
PRP=("\033[01;38;5;55m")
GRN=("\033[01;38;5;10m")
DRK=("\033[01;38;5;242m")
WHT=("\033[01;38;5;15m")
GRY=("\033[01;38;5;242m")
NVD=("\033[1;42;97m")
AMD=("\033[1;41;97m")
RESET=("\033[0m")
LOAD=("\033[1;49;32m")
version = (1.3)
if (os.path.isdir('/data/data/com.termux')):
    OS = ('Termux')
elif ('linux') in (sys.platform):
    OS = ('Linux')
elif ('win') in (sys.platform):
    OS = ('Windows')
script = (os.path.basename(sys.argv[0]))
if ('.py') in script:
    script = (script.split('.')[0])
counter = [0]
currency_options = ['usd', 'gbp', 'cad', 'eur', 'eth']
CHARS = ('/', '-', '\\', '|')
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

def loading(duration):	
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
        if 'Error' in data:
            sys.stdout.write(f"{DRK}[{RD}■{DRK}] {GRN}{data}")
        else:
            sys.stdout.write(f"{DRK}[{GRN}■{DRK}] {GRN}{data}")
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
{PNK}./{GRN}{script} {DRK}[{RD}-g{PNK}/{RD}--gpu {WHT}({GRN}3060 {PNK}| {GRN}3060lhr {PNK}| {GRN}3060ti {PNK}| {GRN}3060tilhr {PNK}| {RD}5600xt {PNK}| {GRN}Etc{WHT}){DRK}]
{PNK}./{GRN}{script} {RD}-c{GRN} 3060
{GRY}List all cards capable of mining {GRN}ETH
{PNK}./{GRN}{script} {RD}-l{PNK}/{RD}--list
{GRY}Now has the ability to convert {GRN}GBP{PNK}, {GRN}CAD {GRY}or {GRN}USD {GRY}to {GRN}ETH {GRY}and vice versa{PNK}.
{GRY}Options{PNK}: 
{GRN}{script} {RD}-c{PNK}/{RD}--currency {WHT}({GRN}eth{PNK}|{GRN}usd{PNK}|{GRN}cad{PNK}|{GRN}gbp{PNK}|{GRN}cad{WHT}) {RD}-i{PNK}/{RD}--into {WHT}({GRN}eth{PNK}|{GRN}usd{PNK}|{GRN}gbp{PNK}|{GRN}cad{PNK}|{GRN}eur{WHT}) {RD}-n{PNK}/{RD}--amount {GRN}10
{GRY}Example syntax to convert {RD}0{PNK}.{RD}2 {GRN}ETH {GRY}into {GRN}GBP{PNK}/{GRN}USD{PNK}/{GRN}CAD{PNK}/{GRN}EUR{PNK}:
{GRN}{script} {RD}-c {GRN}eth {RD}-t {GRN}gbp {RD}-n {GRN}0.2 
{GRY}Or convert {GRN}$175 USD {GRY}into {GRN}ETH{PNK}:
{GRN}{script} {RD}-c {GRN}usd {RD}-t {GRN}eth {RD}-n {GRN}175
 """)
    info = info.replace('\r','.')
    sys.stdout.write(f"{info}\b")
class get():
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':f"{random.choice(Agents)}"})
        parser = argparse.ArgumentParser(description=f'{GRN}{script} ETH mining stats',add_help=False)
        parser.add_argument('-g', '--gpu', required=False, action=('store'),help=(f'{GRN}GPU to search for'))
        parser.add_argument('-h', '--help',action='help', default=argparse.SUPPRESS,help=(f'Show this help menu'))
        parser.add_argument('-u', '--usage' ,required=False, action=('store_true'), help=(f"Advanced Usage"))
        parser.add_argument('-v', '--version' ,required=False, action=('store_true'), help=(f"{script} Version"))
        parser.add_argument('-l', '--list' ,required=False, action=('store_true'), help=(f"List all cards capable of mining ETH"))
        parser.add_argument('-p', '--price' ,required=False, action=('store_true'), help=(f"Show BTC and ETH price"))
        parser.add_argument('-c', '--convert' ,required=False, action=('store'),type=(str.lower), help=(f"Currency to conver ETH/USD/GBP/CAD/EUR"))
        parser.add_argument('-i', '--into' ,required=False, action=('store'),type=(str.lower), help=(f"Currency to convert into ETH/USD/GBP/CAD/EUR"))
        parser.add_argument('-n', '--amount' ,required=False, action=('store'),type=(float), help=(f"Amount to convert"))
        args = (parser.parse_args())
        if args.price:
            loading(0.05)
            self.get_current_price()
        if args.version:
            icon()
            data = (f"{DRK}Version: {GRN}{script} {PNK}{version} {DRK}[{GRN}■{DRK}]")
            echo(data)
            exit(0);
        try:
            if args.convert:
                to_convert = (args.convert)
                if (args.amount) == (0):
                    data = (f"{RD}Error{PNK}: {DRK}Cannot convert {RD}{args.amount} {DRK}[{RD}■{DRK}]")
                    echo(data)
                    exit(0);
                elif (args.amount) > (0):
                    amount = (args.amount)
                else:
                    data = (f"{RD}Error{PNK}: {DRK}You must supply an amount to convert {DRK}[{RD}■{DRK}]")
                    echo(data)
                    exit(0);
                if to_convert not in ['usd'.casefold(), 'gbp'.casefold(), 'cad'.casefold(), 'eur'.casefold(), 'eth'.casefold()]:
                    data = (f"{RD}Error{PNK}: {RD}{to_convert} {DRK}is not a supported currency{PNK}. {DRK}Acceptable currencies are{PNK}: {GRN}USD{PNK},{GRN}GBP{PNK},{GRN}EUR{PNK},{GRN}CAD")
                    echo(data)
                    exit(0);
                if len(args.convert) != (3):
                    data = (f"{RD}Error {PNK}'{RD}{args.convert}{PNK}' {DRK}not recognized{PNK}: {RD}Options are{PNK}: {GRN}eth{PNK}, {GRN}usd{PNK}, {GRN}gbp{PNK},{GRN}cad{PNK},{GRN} eur {DRK}[{RD}■{DRK}]")
                    echo(data)
                if ('eth') in (to_convert):
                    currency = ('ethereum')
                elif 'usd' in (to_convert):
                    currency = ('usd')
                elif ('gbp') in (to_convert):
                    currency = ('gbp')
                elif ('eur') in (to_convert):
                    currency = ('eur')
                elif ('cad') in (to_convert):
                    currency = ('cad')
                if len(args.into) <= (2):
                    data = (f"{RD}Error {PNK}'{RD}{args.into}{PNK}' {DRK}not recognized{PNK}: {RD}Options are{PNK}: {GRN}eth{PNK}, {GRN}usd{PNK}, {GRN}gbp{PNK},{GRN}cad{PNK}, {GRN}eur {DRK}[{RD}■{DRK}]")
                    echo(data)
                else:
                    convert_to = (args.into)
                    if convert_to not in ['usd'.casefold(), 'gbp'.casefold(), 'cad'.casefold(), 'eur'.casefold(), 'eth'.casefold()]:
                        data = (f"{RD}Error{PNK}: {RD}{to_convert} {DRK}is not a supported currency{PNK}. {DRK}Acceptable currencies are{PNK}: {GRN}USD{PNK},{GRN}GBP{PNK},{GRN}EUR{PNK},{GRN}CAD")
                        echo(data)
                        exit(0);
                loading(0.05)
                self.convert(currency,amount,convert_to)
        except:
            pass
        if args.list:
            icon()
            loading(.2)
            self.list_cards()
            exit(0);
        if args.usage:
            usage()
            exit(0);
        else:
            pass
        if args.gpu:
            if args.gpu == ('1050') or args.gpu == ('1050ti'):
                data = (f"{RD}Error{PNK}: {RD}\u2639 {DRK} The {GRN}GTX {GRN}1050{PNK}/{WHT}1050{GRN}ti {DRK}cannot be used to mine {GRN}ETH {RD}\u2639  {DRK}[{RD}■{DRK}]")
                echo(data)
                data = (f"{RD}Error{PNK}: {GRY}Mining {GRN}ETH {GRY}requires {RD}>4GB {GRN}VRAM {DRK}[{RD}■{DRK}]")
                echo(data)
                exit(0)
            else:
                self.card = (args.gpu)
                icon()
                self.get_mhs()
        else:
            pass
    def get_gas_price(self):
        data = (f"Maybe a 'gas price' here ?")
        echo(data)
    def get_current_price(self):
        btc_page = ('https://api.coindesk.com/v1/bpi/currentprice/usd.json')
        page = (f'https://www.hashrate.no/')
        page2 = (f"https://walletinvestor.com/converter/ethereum/usd/1")
        retrieve = (self.session.get(page).text)
        get_btc = (self.session.get(btc_page).text)
        retrieve2 = (self.session.get(page2).text)
        try:
            btc_price = (re.findall('"rate":"(.*?)"',get_btc)[0])
        except:
            btc_price = (f'N/A')
        try:
            eth_price = (re.findall("ETH: <b>(.*?)</", retrieve)[0])
        except:
            eth_price = ('N/A')
        try:
            down = (re.findall('glyphicon-menu-down"></i> (.*?)</',retrieve2)[0])
            down_clean = (down.replace(" ", ""))
        except:
            down = (re.findall('glyphicon-menu-up"></i> (.*?)</',retrieve2)[0])
            down_clean = (down.replace(" ", ""))
        if ('-') in down:
            data = (f"{DRK}BTC Price{PNK}: {GRN}${GRN}{btc_price}")
            echo(data)
            loading(0.01)
            data = (f"{DRK}ETH Price{PNK}: {GRN}{eth_price} {PNK}.::. {DRK}Down{PNK}: {RD}{down_clean}\r")
            echo(data)
        else:
            data = (f"{DRK}BTC Price{PNK}: {GRN}${GRN}{btc_price}")
            echo(data)
            loading(0.01)
            data = (f"{DRK}ETH Price{PNK}: {GRN}{eth_price} {PNK}.::. {DRK}Up{PNK}: {GRN}{down_clean}\r")
            echo(data)
    def convert(self,currency,amount,convert_to):
        if convert_to == 'gbp':
            convert_symbol = ('£')
        elif convert_to == 'usd':
            convert_symbol = ('$')
        elif convert_to == 'cad':
            convert_symbol = ('$')
        elif convert_to == 'eur':
            convert_symbol = ('€')
        elif convert_to == 'eth':
            convert_symbol = ('♦')
        if convert_to == ('eth'):
            convert_to = ('ethereum')
        if currency == ('ethereum'):
            page = (f"https://walletinvestor.com/converter/{currency}/{convert_to}/{amount}")
            retrieve = (self.session.get(page).text)
            raw = (re.findall('converter-title-amount">(.*?)</span>',retrieve)[0])
            converted = (f"{int(float(raw)):.2f}")
            if currency == 'gbp':
                currency_symbol = ('£')
            elif currency == 'usd':
                currency_symbol = ('$')
            elif currency == 'cad':
                currency_symbol = ('$')
            elif currency == 'eur':
                currency_symbol = ('€')
            elif currency == 'ethereum':
                currency_symbol = ('♦')
            loading(0.05)
            data = (f"{GRY}Converting{PNK}: {GRN}{currency_symbol}{amount} {currency.upper()[0:3]} {GRY}into{PNK}: {GRN}{convert_symbol}{converted} {convert_to.upper()} {DRK}[{GRN}■{DRK}]")
            echo(data)
        elif currency == ('usd') or currency == ('gbp') or currency == ('cad') or currency == ('eur'):
            page = (f"https://walletinvestor.com/converter/{currency}/{convert_to}/{amount}")
            retrieve = (self.session.get(page).text)
            raw = (re.findall('converter-title-amount">(.*?)</span>',retrieve)[0])
            converted = (f"{int(float(raw)):.2f}")
            if currency == 'gbp':
                currency_symbol = ('£')
            elif currency == 'usd':
                currency_symbol = ('$')
            elif currency == 'cad':
                currency_symbol = ('$')
            elif currency == 'eur':
                currency_symbol = ('€')
            elif currency == 'ethereum':
                currency_symbol = ('♦')
            loading(0.05)
            data = (f"{GRY}Converting{PNK}: {GRN}{currency_symbol}{amount} {currency.upper()} {GRY}into{PNK}: {GRN}{convert_symbol}{raw} {convert_to.upper()[0:3]} {DRK}[{GRN}■{DRK}]")
            echo(data)
    def get_mhs(self):
        page2 = (f"https://walletinvestor.com/converter/ethereum/usd/1")
        btc_page = ('https://api.coindesk.com/v1/bpi/currentprice/usd.json')
        get_btc = (self.session.get(btc_page).text)
        page = (f'https://www.hashrate.no/{self.card}')
        retrieve = (self.session.get(page).text)
        retrieve2 = (self.session.get(page2).text)
        try:
            btc_price = (re.findall('"rate":"(.*?)"',get_btc)[0])
        except:
            btc_price = (f'N/A')
        try:
            eth_price = (re.findall("ETH: <b>(.*?)</", retrieve)[0])
        except:
            eth_price = ('N/A')
        try:
            gpu = (re.findall("<title>(.*?) -",retrieve)[0])
        except:
            gpu = (f'N/A')
        try:
            eth_rate = (re.findall("ETH</a></font></td><td>(.*?)</", retrieve)[0])
        except:
            eth_rate = ('N/A')
        try:
            power = (re.findall(f"{eth_rate}</td><td><b>(.*?)</", retrieve)[0])
            power2 = (re.findall(f"{power}</b><br />(.*?)</", retrieve)[0])
        except:
            power = ('N/A')
            power2 = ('N/A')
        try:
            efficiency = (re.findall(f"{power}</b><br />{power2}</td><td>(.*?)</", retrieve)[0])
        except:
            efficiency = ('N/A')
        try:
            oneday = (re.findall(f"{power2}</td><td>{efficiency}</td><td><b>(.*?)</", retrieve)[0])
            oned = oneday.rsplit('$')[1]
            weekly = (D(oned) * 7)
            monthly = (D(oned) * 30)
        except:
            oneday = ('N/A')
            weekly = ('N/A')
            monthly = ('N/A')
        try:
            oneday2 = (re.findall(f"{efficiency}</td><td><b>{oneday}</b><br />(.*?)</", retrieve)[0])
        except:
            oneday2 = ('N/A')
        try:
            rvn_rate = (re.findall("RVN</a></font></td><td>(.*?)</", retrieve)[0])
        except:
            rvn_rate = ('N/A')
        try:
            msrp = (re.findall("MSRP: (.*?)Released:", retrieve)[0])
        except:
            msrp = ('N/A')
        try:
            release_date = (re.findall("Released:(.*?)TDP:", retrieve)[0])
        except:
            release_date = ('N/A')
        try:
            tdp = (re.findall("TDP: </td><td>(.*?)</", retrieve)[0])
        except:
            tdp = ('N/A')
        try:
            test = (oneday.split('.')[1])
            roi = (re.findall(f"{test}</b></td><td>(.*?)</td", retrieve)[0])
        except:
            roi = ('N/A')
        try:
            if "NVIDIA" in gpu:
                gpu_name = (f"{NVD}{gpu}{RESET} {DRK}[{GRN}■{DRK}]")
                data = (f"{gpu_name}")
                echo(data)
                loading(.2)
                try:
                    down = (re.findall('glyphicon-menu-down"></i> (.*?)</',retrieve2)[0])
                    down_clean = (down.replace(" ", ""))
                except:
                    down = (re.findall('glyphicon-menu-up"></i> (.*?)</',retrieve2)[0])
                    down_clean = (down.replace(" ", ""))
                if ('-') in down:
                    data = (f"{DRK}BTC Price{PNK}: {GRN}${GRN}{btc_price} {PNK}.::. {DRK}ETH Price{PNK}: {GRN}{eth_price} {PNK}.::. {DRK}Down{PNK}: {RD}{down_clean}\r")
                    echo(data)
                else:
                    data = (f"{DRK}BTC Price{PNK}: {GRN}${GRN}{btc_price} {PNK}.::. {DRK}ETH Price{PNK}: {GRN}{eth_price} {PNK}.::. {DRK}Up{PNK}: {GRN}{down_clean}")
                    echo(data)
                loading(0.05)
                data = (f"{GRN}ETH {DRK}Hashrate{PNK}({GRN}DaggerHashimoto{PNK}){PNK}: {GRN}{eth_rate} {PNK}") 
                echo(data)
                loading(0.05)
                data = (f"{DRK}24h{PNK}: {GRN}{oneday}{PNK} / {DRK}Weekly{PNK}: {GRN}${weekly}{PNK} / {DRK}Monthly{PNK}: {GRN}${monthly}")
                echo(data)
                loading(0.05)
                data = (f"{DRK}Released{PNK}: {GRN}{release_date} {PNK}.::. {DRK}MSRP{PNK}: {GRN}{msrp} ")
                echo(data)
                loading(0.05)
                data = (f"{DRK}ROI{PNK}: {GRN}{roi} {PNK}.::. {DRK}Efficiency{PNK} {GRN}{efficiency}")
                echo(data)
                loading(0.05)
                data = (f"{DRK}TDP{PNK}: {GRN}{tdp} {PNK}.::. {DRK}Power{PNK}: {GRN}{power} {PNK}:: {GRN}{power2}")
                echo(data)          
            elif "AMD" in gpu:
                gpu_name = (f"{AMD}{gpu}{RESET} {DRK}[{GRN}■{DRK}]")
                data = (f"{gpu_name}")
                echo(data)
                loading(.2)
                try:
                    down = (re.findall('glyphicon-menu-down"></i> (.*?)</',retrieve2)[0])
                    down_clean = (down.replace(" ", ""))
                except:
                    down = (re.findall('glyphicon-menu-up"></i> (.*?)</',retrieve2)[0])
                    down_clean = (down.replace(" ", ""))
                if ('-') in down:
                    data = (f"{DRK}BTC Price{PNK}: {GRN}${RD}{btc_price} {PNK}.::. {DRK}ETH Price{PNK}: {RD}{eth_price} {PNK}.::. {DRK}Down{PNK}: {RD}{down_clean}\r")
                    echo(data)
                else:
                    data = (f"{DRK}BTC Price{PNK}: {RD}${btc_price} {PNK}.::. {DRK}ETH Price{PNK}: {RD}{eth_price} {PNK}.::. {DRK}Up{PNK}: {GRN}{down_clean}")
                    echo(data)
                loading(0.05)
                data = (f"{RD}ETH {DRK}Hashrate{PNK}({RD}DaggerHashimoto{PNK}){PNK}: {RD}{eth_rate} {PNK}") 
                echo(data)
                loading(0.05)
                data = (f"{DRK}24h{PNK}: {RD}{oneday}{PNK}/{DRK}Weekly{PNK}: {RD}${weekly}{PNK}/{DRK}Monthly{PNK}: {RD}${monthly}")
                echo(data)
                loading(0.05)
                data = (f"{DRK}Released{PNK}: {RD}{release_date} {PNK}.::. {DRK}MSRP{PNK}: {RD}{msrp} ")
                echo(data)
                loading(0.05)
                data = (f"{DRK}ROI{PNK}: {RD}{roi} {PNK}.::. {DRK}Efficiency{PNK} {RD}{efficiency}")
                echo(data)
                loading(0.05)
                data = (f"{DRK}TDP{PNK}: {RD}{tdp} {PNK}.::. {DRK}Power{PNK}: {RD}{power}")
                echo(data)
        except KeyboardInterrupt:
            data = (f"{RD}Error{PNK}: {DRK}Keyboard Interruption {DRK}[{RD}■{DRK}]")
            echo(data)
            exit(0);
            
    def list_cards(self):
        page = (f'https://www.hashrate.no/')
        retrieve = (self.session.get(page).text)
        all_cards = (list(set(re.findall(f"href=/(.*?)>", retrieve))))
        loading(.2)
        try:
            for a in all_cards:
                all_cards_clean = (list(set(re.findall(f"href=/{a}>(.*?)</a>", retrieve))))
                for card in all_cards_clean:
                    if "NVIDIA" in card:
                        data = (f"{DRK}Card name{PNK}: {NVD}{card}{RESET} {PNK}.:|:. {DRK}Command name{PNK}: {GRN}{a}")
                        echo(data)
                        loading(0.02)
                    elif "AMD" in card:
                        data = (f"{DRK}Card name{PNK}: {AMD}{card}{RESET} {PNK}.:|:. {DRK}Command name{PNK}: {RD}{a}")
                        echo(data)
                        loading(0.02)
                    else:
                        data = (f"{DRK}Card name{PNK}: {GRN}{card} {PNK}.:|:. {DRK}Command name{PNK}: {GRN}{a}")
                        echo(data)
                        loading(0.02)
        except KeyboardInterrupt:
            data = (f"{RD}Error{PNK}: {DRK}Keyboard Interruption {DRK}[{RD}■{DRK}]")
            echo(data)
            exit(0);
get()
