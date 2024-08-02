import datetime
import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from random import randint, uniform, shuffle, choice
from selenium_stealth import stealth
import re
import random
import string
import os
import requests
import platform
import asyncio
import base64
import json
import random
from typing import Dict, Any
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import aiohttp
import requests
from colorama import Fore, Back, Style
# haha funny i dont know how to import only necessary modules so here's a 27 line import for no reason LMFAO
clear = lambda: os.system('cls')
# Set the path to the Chrome driver executable
driver_path = 'C:/chromedriver-win64/chromedriver.exe'

cService = webdriver.ChromeService(executable_path='C:/chromedriver-win64/chromedriver.exe')
service = Service('C:\Program Files\Chrome Driver\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--lang=en')
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False) 
driver = webdriver.Chrome(service=cService, options=options)

webhook_url = 'Webhook URL'

print(Fore.RED + r"""
 ____  __   __ _   _   ____ __        __   _     ____   _____ 
/ ___| \ \ / /| \ | | / ___|\ \      / /  / \   |  _ \ | ____|
\___ \  \ V / |  \| || |     \ \ /\ / /  / _ \  | |_) ||  _|  
 ___) |  | |  | |\  || |___   \ V  V /  / ___ \ |  _ < | |___ 
|____/   |_|  |_| \_| \____|   \_/\_/  /_/   \_\|_| \_\|_____|
                                                               
    """)
print(Style.RESET_ALL)
print(Fore.GREEN + "I do not fucking know how to python")
print(Fore.GREEN + " ")
print(Fore.GREEN + " ")
print(Fore.LIGHTCYAN_EX + "[XGPC Redeemer]")
print(Style.RESET_ALL) 
def get_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()
    
def Type_Me(element: WebElement, text: str):
    for character in text:
        element.send_keys(character)
        sleep(uniform(.08, .12))
wait = WebDriverWait(driver, 1000)

def generateAccount():
 driver.get('https://www.xbox.com/tr-TR/auth/msa?action=logIn')
 button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signup"]')))
 sleep(0.4)
 button.click()
 wait.until(EC.title_contains('Create account'))
 sleep(1.4)
 button2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="liveSwitch"]')))
 button2.click()

 random_number1 = str(randint(1000, 9999))
 random_number2 = str(randint(1000, 9999))
 years = ["2002","2003", "2004", "2005"]
 words1 = ["sludgy","estral","tauted","fierce","scaped","taxmen","review","jokily","bagged","unfond","scraps","sended","select","amigos","thanes","mouths","sighed","missus","trifid","punily","chilly","drawee","oilcup","nostoc","agouti","stayed","sordid","towels","slacks","oblige","sartor","sporal","trapan","oxeyes","grisly","slayer","lawing","smerks","hostly","milker","citric","selles","hijabs","comedo","dreamt","hoised","oaters","fuzzes","custos","pardon","flying","tipple","unbusy","clothe","ureter","grands","tartar","carets","hereon","shotts","griffe","humvee","espies","hostas","polers","purlin","parley","sasses","toledo","skelms","lawyer","snoopy","winery","codein","arshin","gamely","recoat","poxing","binned","cedarn","larval","whimsy","unpack","dibber","pierce","hocked","others","niggly","moulin","expand","secret","cleans","voyeur","favism","choice","slaggy","sabirs","todies","uremic","hexose","parget","hooeys","curule","pargos","nautch","tocsin","grower","treads","cyprus","shazam","jewing","pechan","yellow","kerbed","robing","burrow","wifely","techie","imbrue","viroid","impark","comedy","gingko","caulis","bemata","patens","aroids","zocalo","sugary","joking","tented","nicker","roosts","natant","resows","wiccas","engulf","plumps","subbed","editor","champs","hyenas","kimono","enolic","mailer","blunts","hyssop","mixers","bitted","gusted","cursed","tmeses","sayids","fleers","inturn","cuisse","corrie","uranyl","yapoks","masque","jersey","eerier","sughed","raptor","lambed","devise","pinned","lieges","mining","kayoes","enures","gadfly","jacker","babble","lisles","burqas","deaves","zonule","hiatus","eating","glaces","unshod","darked","dormin","dhotis","bleach","fellow","retral","nights","fudged","fillip","rifled","fadein","silkie","jasper","allium","odists","iterum","cranky","jubbah","unties","format","fennec","pyrene","gauges","uglies","civism","caners","gieing","cabman","telnet","dulled","plucks","glairy","elater","kaftan","deathy","vaward","vowers","bannet","blames","batter","nandin","ending","incise","phenyl","rebbes","lassie","forgat","curled","ockers","locate","runnel","blared","cozens","walrus","welkin","rustic","planed","rubier","thorns","stanes","dipnet","drawly","noises","sepals","fathom","wanker","kerfed","railer","mensas","scorer","mammae","zanana","ponces","bopper","primps","gyving","habits","burnet","theism","broths","smoosh","bushwa","deicer","oohing","frizer","doodad","clucks","arriba","cyeses","cloots","grange","pignut","doodoo","animus","dangly","fluter","branks","sextos","dicier","muting","edging","retial","hacked","lankly","halons","unfree","womans","fatsos","blithe","methyl","orangs","tazzas","anemia","alarms","oilily","sleaze","gusset","intime","poppet","slices","conies","illite","scubas","basify","sawney","megohm","platys","praise","resold","moguls","chicas","medick","raters","thrums","quaigh","jorams","regnal","racily","pelted","unopen","vaunty","reshot","stella","legist","hanker","gleets","pablum","girdle","flange","petnap","clerid","corona","coiled","locoed","rebate","hakims","paulin","clouts","tythed","frowsy","almugs","retook","hilled","pinata","sundew","steeps","audits","hazily","bravas","cartop","haggis","pleiad","yoking","vagrom","cadges","ninons","chorus","chotts","tweedy","sapour","sobber","fimble","butted","twists","colors","verify","putsch","bosons","greeny","storer","mascot","duomos","outwar","ropily","seeped","wiener","unsnap","quacks","lovats","smalts","chinas","prides","rapier","adhere","defect","redans","algors","rhythm","glared","famuli","cooing","tidbit","ragmen","grieve","fetors","almond","taxols","huffed","bhakta","corban","choosy","queens","exogen","action","nooses","tagged","jiminy","azures","foleys","denars","chicly","basely","pitchy","zoster","reword","axenic","feists","hiding","faqirs","stuffs","upleap","palais","menads","uproar","outrig","angles","droops","covins","stride","troops","spacey","pouffs","kalmia","larees","costar","surety","socman","menhir","yelper","bromic","dibbuk","ticals","sowers","splosh","neared","clavus","repoll","cypres","rotten","bredes","seamed","smoggy","arcked","elated","layoff","popped","cutoff","guider","medals","kombus","punkey","gizmos","dirndl","gaging","reseat","phased","verite","ebbing","heaped","glints","vinous","encina","decoys","bathos","switch","paseos","shamus","fleecy","poohed","speedo","yeoman","dinars","muscle","gipons","spathe","cheder","squish","ashier","ingles","parkas","hunted","byroad","rhetor","lammed","shield","hammal","volost","cusecs"]
 words2 = ["arriviste","ignescent","beshouted","pneumonic","kilogauss","misadapts","ethephons","bairnlier","myomatous","valorises","preachify","leafworms","liposomes","waitlists","madnesses","gallivant","unscrewed","impellors","pestilent","overswung","predeaths","amputates","friskiest","spaldeens","cloyingly","squallers","narration","bearskins","mobilised","multipath","catalatic","saddening","cognizers","isometric","underlaps","prelusive","catalogue","triangles","fulgently","flagrance","nonproven","amassment","fruitions","enamelers","bigarreau","academism","grandsirs","awfulness","lionisers","clafoutis","missileer","mistiness","dullishly","antialien","directing","sculpting","automatic","ciliately","oolachans","neustonic","prorogate","mujahedin","imageable","allotypic","sunscreen","cryometer","pyrogenic","disclaims","nucleates","tipsheets","nonbodies","royalisms","brutifies","flagstaff","splashing","distorter","nonpapist","maccaboys","quadricep","parvenues","xenoblast","sinkholes","sneeziest","renatures","weaselled","vulgarise","groomsman","kingships","ostinatos","ketonuria","reachable","cruzadoes","recession","misspoken","validates","lacerated","developpe","embargoed","prolactin","infancies","antiunion","squinnies","pyorrhoea","dissipate","atonalism","redefeats","suppliant","dimension","ruddiness","subsister","levellers","dizziness","gossipped","catrigged","uncrowned","hypotaxis","declining","aforetime","primroses","besmearer","parodical","wuthering","gradeless","outranges","assegaied","champerty","exquisite","brevities","octupling","sphincter","spaceband","heathiest","anelastic","inhesions","mythmaker","pirarucus","feedbacks","protrudes","laminable","ordinally","producing","tunnelled","blowtubes","impudency","exosmosis","analgetic","partridge","kvetchier","deafening","spoonfuls","nepotists","naggingly","poulardes","revertant","yattering","pyralidid","advantage","sleddings","enjoinder","pachalics","anatomise","hexagrams","ionizable","zarzuelas","stinkpots","toluidine","calamatas","harlequin","airlifted","trifocals","carangids","iseikonia","quackisms","respelled","snowsuits","vowelized","cytoplast","absterges","newsgirls","nullipore","breachers","iodopsins","breastpin","analysers","splurgier","underbuys","lanthanon","repertory","welcoming","herbivore","deselects","ephedrine","plumipeds","obsidians","brierroot","parachors","sclerotin","bastardly","mentalist","bespouses","wellaways","scaraboid","cupbearer","placement","anchorets","randiness","packboard","multibank","perilunes","eurythmic","redbricks","calculous","recooking","chapattis","upraisers","fatiguing","blindness","soulfully","threnodes","hyperpure","caboodles","landaulet","trademark","natations","glistened","scaphopod","antidoted","matambala","workmates","indorsers","spearwort","remittent","hurtfully","moralized","schmooses","lysosomal","synagogue","parvolins","phosphene","hamadryad","napalming","shabbiest","nabobisms","unharried","marceller","milliares","alternate","gyropilot","earliness","phenytoin","foliating","overplays","relatives","deflation","bottleful","lemuroids","crampoons","angiogram","engrosser","evacuator","broadened","millirems","rattlings","guidebook","weanlings","decrypted","bewitcher","phosphors","symbology","nonrandom","planisher","unnailing","mesosomes","gaynesses","bushelman","womanlike","salicines","beheaders","saucepots","turnovers","lunisolar","sasswoods","glowflies","nonrioter","eutherian","transacts","phytology","inletting","imbrowned","roistered","emanative","crustiest","rancidity","unstepped","tenanting","talkiness","halakhist","prelature","misspaced","breakdown","droopiest","barhopped","thermites","relevance","coreopsis","paleosols","feignedly","catenoids","skylarked","shillings","vocalizer","mortgaged","manifolds","actresses","layperson","milliwatt","blackfins","unshelled","sidehills","annulment","crapshoot","treasures","spiritual","undrilled","pliotrons","precocial","impudence","seascouts","prudences","bicyclers","leptophos","intrigued","aeroducts","strongyls","grassroot","imbroglio","privacies","godlessly","flockiest","studworks","stenokies","carroches","carousels","minimills","herbalism","springing","fructoses","grandpapa","mirabelle","heliogram","asymmetry","haplontic","fettering","enervator","monkshood","brooklime","charlocks","boneyards","acquirers","gauzelike","chitchats","refunders","unpackers","slavishly","dionysiac","saponines","fisheries","osteomata","antepasts","cotillons","fumigants","redargued","irriguous","aqualungs","enceintes","hemateins","destained","bluestone","uredinial","cribbages","adulthood","avadavats","anaphoric","eyepoints","gearwheel","backseats","potboiled","bunkering","draftiest","truanting","outgazing","balloters","tentmaker","decurions","exhauster","fluorides","cellulose","beeriness","wallowers","devoicing","astonying","strainers","orangutan","entangled","idealists","apheretic","negligees","bemedaled","myoclonic","disjoints","profiters","misformed","saphenous","analyzers","roundwood","carjacker","contained","revolting","spoutless","teentsier","humouring","prereform","colcannon","disinvest","cymogenes","windrowed","cutthroat","preshrunk","carrotier","cleveites","sensately","bodycheck","canneries","beclamors","sleighing","hosannahs","magnifico","misoneist","aceldamas","dickering","blacklegs","coleworts","churchier","calculate","unwrinkle","preaudits","hemstitch","spiccatos","bluecoats","profferer","dissected","anciently","safeguard","colonized","surprised","clickable","crushable","precisely","rebbetzin","reignited","diemakers","fluidised","sesspools","estoppels","graperies","driveller","paludisms","lineament","neurotomy","pesticide","charwomen","untenable","allantoic","caucusing","certainer","rosaceous","antipasto","equivocal","sideritic","gasolenes","peppering","bedsteads","custodies","theorised","overfrank","hooknoses","vulviform","begetters","insolates","dosshouse","modernity","deplorers","gravamina","concluder","autoecism","tenacious","pulsators","shvartzes","uropodous","homunculi"]
 global email1
 global password1
 email1 = random.choice(words1) + random.choice(words2) + random_number1
 password1 = random.choice(words1) + random.choice(words2) + random_number2
 file_path = "names.txt"
 name = get_random_line(file_path)
 surname = get_random_line(file_path)
 email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="usernameInput"]'))) # email
 sleep(1.2)
 Type_Me(email, email1)
 button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nextButton"]')))
 sleep(1.3)
 button.click()
 field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Password"]')))
 sleep(1.1)
 Type_Me(field, password1)
 button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nextButton"]')))
 
 button.click()
 field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="firstNameInput"]')))
 sleep(0.7)
 Type_Me(field, name)
 field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lastNameInput"]')))
 sleep(0.9)
 Type_Me(field, surname)
 sleep(1.6)
 sleep(0.7)
 button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nextButton"]')))
 button.click()
 WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="countryRegionDropdown"]')))
 country = driver.find_element(By.ID, "countryRegionDropdown")
 Type_Me(country, "United States")
 sleep(2.1)
 sleep(0.7)

 WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BirthMonth"]')))
 month = driver.find_element(By.ID, "BirthMonth")
 month.click()
 sleep(1.2)
 Type_Me(month, "Jan")

 
 WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BirthDay"]')))
 day = driver.find_element(By.ID, "BirthDay")
 day.click()
 sleep(0.8)
 day.send_keys(str(randint(1, 12)))

 WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BirthYear"]')))

 yr = driver.find_element(By.ID, "BirthYear")
 yr.click()
 sleep(0.2)
 yr.send_keys(str(random.choice(years)))
 sleep(0.7)
 sleep(0.7)
 button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nextButton"]')))
 button.click()
     
 WebDriverWait(driver, 600000).until(EC.title_contains('Welcome to Xbox'))
 sleep(2)
 button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-account-gamertag-suggestion-1"]')))
 button.click()
 sleep(2)
 button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
 button.click()

 wait.until(EC.title_contains('Consent'))
 sleep(2)
 button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
 button.click()
 print(Fore.YELLOW + '+ Account created ' + email1 + '@outlook.com:' + password1)
 sleep(3)


start = input("Type 'start' to begin checking codes: ")
if start == 'start':
        generateAccount()
        
                    
        # List of codes to check
        codes = []
        with open('codes.txt', 'r') as file:
            for line in file:
                code = line.strip()
                codes.append(code)
        valid_count = 0
        invalid_count = 0

        for code in codes:
            
            url = f'https://www.xbox.com/en-US/xbox-game-pass/invite-your-friends/redeem?offerId={code}' 
           
            driver.get(url)
           
            sleep(4)
            page_source2 = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', driver.page_source)
            

            if 'Redeem your 14-day trial, then install the Xbox app to start playing.' in str(page_source2):
                print(f'Code {code} is eligible')
                payload = {
                            'content': f'Code {code} is eligible'
                        }
                
                response = requests.post(webhook_url, json=payload)
                valid_count += 1
                redeem_button = driver.find_element(By.XPATH, "//button[text()='REDEEM NOW']")
                redeem_button.click()
                sleep(3)
                WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME ,'redeem-sdk-hosted-iframe')))
                element = driver.find_element(By.XPATH, "//button[text()='Get Started! Add a way to pay.']")
                element.click()
                WebDriverWait(driver, 2000).until(EC.presence_of_element_located((By.ID, 'displayId_credit_card_visa_amex_mc_discover')))
                credit_card = driver.find_element(By.ID,"displayId_credit_card_visa_amex_mc_discover")
                credit_card.click()

                WebDriverWait(driver, 2000).until(EC.presence_of_element_located((By.ID, 'accountToken')))
                account_token = driver.find_element(By.ID,"accountToken")
                account_token.click()
                def get_random_cc_info():
                    with open('ccs.txt', 'r') as file:
                        lines = file.readlines()
                        random_line = random.choice(lines)
                        cc_info = random_line.split("|")
                        cc_date1 = cc_info[1]
                        cc_date2 = cc_info[2]
                        cc_cvv = cc_info[3]
                    return cc_info, cc_date1, cc_date2, cc_cvv
                def do_payment():
                 cc_info, cc_date1, cc_date2, cc_cvv = get_random_cc_info()
                 account_token.send_keys(cc_info[0])
                 name = driver.find_element(By.ID,"accountHolderName")
                 name.click()
                 name.send_keys('Alex')
                 expiry_month = driver.find_element(By.ID, "input_expiryMonth")
                 
                 expiry_month.send_keys(cc_date1)

                 expiry_year = driver.find_element(By.ID, "input_expiryYear")
                 expiry_year.send_keys('27')

                 cvv = driver.find_element(By.ID,"cvvToken")
                 cvv.click()
                 cvv.send_keys(cc_cvv)
                 address_line1 = driver.find_element(By.ID,"address_line1")
                 address_line1.click()
                 address_line1.send_keys('9027 Fairground Circle')

                 address_line2 = driver.find_element(By.ID,"city")
                 address_line2.click()
                 address_line2.send_keys('Oceanside')
                
                 region = driver.find_element(By.ID,"input_region")
                
                 region.send_keys('New York')

                 postal = driver.find_element(By.ID,"postal_code")
                 postal.click()
                 postal.send_keys('11572')

                 save1 = driver.find_element(By.ID,"pidlddc-button-saveButton")
                 save1.click()
                 WebDriverWait(driver, 5000).until(EC.presence_of_element_located((By.CLASS_NAME, "lightweight--_B359BGN.base--goua8jma")))
                try:
                    get_random_cc_info()
                    do_payment()
                except:
                    get_random_cc_info()
                    do_payment()
                sleep(3)
                txt = driver.find_element(By.CLASS_NAME, 'lightweight--_B359BGN.base--goua8jma')
                txt.click()

                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'pidlddc-text-profileAddressPageSubheading')))
                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'pidlddc-text-profileAddressPageSubheading')))
               
                address_line1 = driver.find_element(By.ID,"address_line1")
                address_line1.click()
                address_line1.send_keys('9027 Fairground Circle')

                address_line2 = driver.find_element(By.ID,"city")
                address_line2.click()
                address_line2.send_keys('Oceanside')
                
                region = driver.find_element(By.ID,"input_region")
                
                region.send_keys('New York')

                postal = driver.find_element(By.ID,"postal_code")
                postal.click()
                postal.send_keys('11572')
                save1 = driver.find_element(By.ID,"pidlddc-button-saveButton")
                save1.click()
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'pidlddc-button-addressUseButton')))


                sleep(1)
                save2 = driver.find_element(By.ID,"pidlddc-button-addressUseButton")
                save2.click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "primary--kLopxQTl.base--goua8jma")))
                sleep(1)
                cbf = driver.find_element(By.CLASS_NAME, 'primary--kLopxQTl.base--goua8jma')
                cbf.click()
                sleep(23)

                

                
                global current_day
                global current_month
                current_day = datetime.datetime.now().day
                current_month = datetime.datetime.now().strftime("%b")
                print(Fore.GREEN + '+ Redeemed ' + email1 + '@outlook.com:' + password1 + ' | ' + str(current_month) + ' ' + str(current_day))
                print(Style.RESET_ALL)
                sleep(2)
                driver.get('https://www.xbox.com/en-US/auth/msa?action=logOut')
                sleep(3)
                driver.delete_all_cookies()
                sleep(1)
                generateAccount()
                # pls god strike this nigga down
                
           
                

                
            

driver.quit()
print(Fore.GREEN + '+ end | ' + str(valid_count))
print(Style.RESET_ALL)


