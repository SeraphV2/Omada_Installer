import os
import time
from pystyle import Colorate, Colors, Write, Add, Center, Box
import webbrowser

class Main():
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        os.system('clear')
        self.warn()
        time.sleep(2)
        os.system('clear')
        self.banner()
        self.options()
        while self.gg == True:
            print()
            choose = Write.Input("            Choose Number -> ", Colors.yellow_to_red, interval=0.0025)
            if (choose == '1'):
                os.system('clear')
                self.banner()
                self.rs()
            elif (choose == '2'):
                os.system('clear')
                self.banner2()
                self.zp()
            
    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
        
    def warn(self):
        Banner1= """
            .____    ._______   ________ ____________  
            |    |   |   \   \ /   /    |   \_   ___ \    EST. 2016-2023
            |    |   |   |\   Y   /|    |   /    \  \/    © LIV Unified Comms. 
            |    |___|   | \     / |    |  /\     \____   All rights reserved
            |_______ \___|  \___/  |______/  \______  /   https://livuc.co.uk/
                    \/                              \/ 
            --------------------- TP-Link Omada Toolset ----------------------
            ==================================================================
            + Please use this tool on a debian based system for best results +
            ==================================================================    
            + Please Use this tool on a root user + Root check Starting..... +
            ==================================================================
        """
        Banner2 = """
              """
        print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2)))
 
    def banner(self):
        Banner1= """
            .____    ._______   ________ ____________  
            |    |   |   \   \ /   /    |   \_   ___ \    EST. 2016-2023
            |    |   |   |\   Y   /|    |   /    \  \/    © LIV Unified Comms. 
            |    |___|   | \     / |    |  /\     \____   All rights reserved
            |_______ \___|  \___/  |______/  \______  /   https://livuc.co.uk/
                    \/                              \/ 
            --------------------- TP-Link Omada Toolset ----------------------
                              
        """
        Banner2 = """
              """
        print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2)))
    
    def banner2(self):
        Banner1= """
            .____    ._______   ________ ____________  
            |    |   |   \   \ /   /    |   \_   ___ \    EST. 2016-2023
            |    |   |   |\   Y   /|    |   /    \  \/    © LIV Unified Comms. 
            |    |___|   | \     / |    |  /\     \____   All rights reserved
            |_______ \___|  \___/  |______/  \______  /   https://livuc.co.uk/
                    \/                              \/ 
            --------------------- TP-Link Omada Toolset ----------------------
            ==================================================================
            Please verify latest omada upgrade version when web page loads up
            ================================================================== 
                              
        """
        Banner2 = """
              """
        print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2)))
    
    
    def options(self):
        Banner1 ="""            [1]  Install Omada
            [2]  Update Omada
            [3]  Exit """
        Banner2 = """
              """
        print(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2))
               
    
    def irtb(self):
        Banner1 = """            [1] Install MongoDB Dependencies
            [2] Install MongoDB 
            [3] Install Omada Dependencies
            [4] Install Omada Controller
            [99] Back"""
        Banner2 = """
              """
        print(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2))

    def upgrade(self):
        Banner1 = """            [1] Install Omada Update
            [99] Back"""
        Banner2 = """
              """
        print(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2))

    def comp(self):
        Banner1 = """            Install Complete!!!"""
        Banner2 = """
              """
        print(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2))    
        
    def check(self):
        Banner1 = """            Double check you have verified latest update!!!!!"""
        Banner2 = """
              """
        print(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2))   

    def wait(self):
        Banner1 = """            Please wait......"""
        Banner2 = """
              """
        print(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner1,Banner2, center=True), 2))  


    def rs(self):
        self.irtb()
        while self.gg == True:
            print('')
            choose = Write.Input("            Choose Number -> ", Colors.yellow_to_red, interval=0.0025)
            if (choose == '1'):
               os.system('clear')
               self.banner() 
               os.system('wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb')           
               os.system('sudo dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb ')
               self.comp()
               time.sleep(2)
               self.rs()
            elif (choose == '2'):
               os.system('sudo apt install -y software-properties-common')
               os.system('wget -qO- https://www.mongodb.org/static/pgp/server-4.4.asc && sudo tee /etc/apt/trusted.gpg.d/mongodb-org-4.4.asc')
               os.system('sudo add-apt-repository -y "deb [arch=amd64] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse"')
               os.system('sudo apt install -y mongodb-org')
               self.comp()
               time.sleep(2)
               self.rs()
            elif (choose == '3'):
               os.system('sudo apt install -y openjdk-8-jre-headless jsvc curl')
               self.comp()
               time.sleep(2)
               self.rs()
            elif (choose == '4'):
               os.system('wget https://static.tp-link.com/upload/software/2024/202411/20241101/Omada_SDN_Controller_v5.14.32.3_linux_x64.deb')
               os.system('sudo apt install -y ./Omada_SDN_Controller_v5.14.32.3_linux_x64.deb')
               self.comp()
               time.sleep(2)
               self.rs()
            elif (choose == '99'):
               os.system('clear')
               self.banner()
               self.options()
               
       
    def zp(self):
        while self.gg == True:
            os.system('clear')
            self.banner2()
            self.check()
            webbrowser.open('https://www.tp-link.com/uk/support/download/omada-software-controller/#Controller_Software', new=2)
            print("")
            self.wait()
            time.sleep(10)
            os.system('clear')
            self.banner2()
            self.upgrade()
            print("")
            choose2 = Write.Input("            Choose Number -> ", Colors.yellow_to_red, interval=0.0025)
            if (choose2 == '1'):
                link = Write.Input("            Input Update Link -> ", Colors.yellow_to_red, interval=0.0025)
                version = Write.Input("            Input Version Number -> ", Colors.yellow_to_red, interval=0.0025)
                os.system(f'wget {link}')           
                os.system(f'dpkg -i Omada_SDN_Controller_v{version}_linux_x64.deb')
                self.comp()
                self.rs()
            elif (choose2 == '99'):
                os.system('clear')
                self.banner()
                self.options()
               

Main()
