from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from chardet import detect
import json
import os
import zipfile
import shutil
import sys
import tkinter as tk
import re
import glob
import logging
import webbrowser
import xml.etree.ElementTree as ET
import subprocess
import configparser
import stat
import datetime

#remove_readonly - shutil.rmtree
def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


version = "v2.1.0"
faq_url = "https://github.com/Kurorin-fs/Kuro_B787-8_Installer/blob/main/index.md"
fsto_url = "https://flightsim.to/file/45062/boeing-787-8"
chglog_url= "https://github.com/Kurorin-fs/Kuro_B787-8_Installer/blob/main/changelog.md"
sb_url = "https://dispatch.simbrief.com/airframes/share/eyJiYXNldHlwZSI6IkI3ODgiLCJpY2FvIjoiQjc4OCIsInJlZyI6IkctWkJKSCIsImZpbiI6IjExMjMiLCJzZWxjYWwiOiJLUldUIiwiaGV4Y29kZSI6IiIsIm5hbWUiOiJCNzg3LTgiLCJlbmdpbmVzIjoiIiwiY29tbWVudHMiOiJLUkI3ODggdjIuMS4wLCBCQVcgTGF5b3V0LCBHRU5YLTFCNjQvVFJFTlQxMDAwLUgyIiwicGxhbnVuaXRzIjoiMCIsInBlciI6IkQiLCJjYXQiOiJIIiwiZXF1aXAiOiJTREUxRTJFM0ZHSElKMkozSjRKNU0xUldYWVoiLCJ0cmFuc3BvbmRlciI6IkxCMUQxIiwicGJuIjoiQTFCMUMxRDFMMU8xUzIiLCJldG9wc3JhbmdlIjoiIiwiZXh0cmFybWsiOiIiLCJ3Z3R1bml0cyI6IktHUyIsIm1heHBheCI6IjIyNSIsInBheHdndCI6Ijg0IiwiYmFnd2d0IjoiMzEiLCJvZXciOiIxMTk5NzUiLCJtemZ3IjoiMTYxMDI1IiwibXRvdyI6IjIyNzkzMCIsIm1sdyI6IjE3MjM2NSIsIm1heGZ1ZWwiOiIxMDE0NTYiLCJtYXhjYXJnbyI6IjIyMDg3IiwiY2FyZ29tb2RlIjoiIiwiZGVmYXVsdGNpIjoiMjUiLCJmdWVsZmFjdG9yIjoiUDAwIiwiY2VpbGluZyI6IjQzMTAwIiwiY3J1aXNlb2Zmc2V0IjoiUDAwMDAifQ--"
logging.basicConfig(level=logging.DEBUG, filename="..\installer.log", format="%(asctime)s %(levelname)s: %(funcName)s: %(message)s")

#icon
root = tk.Tk()
root.withdraw()
data = '''R0lGODlhgACAAOfJAABZnwBbnQtZlwBkoBJfnBNjmhlioCBilCdjnB5ooCtmnyRo
pzNmmippmzJplzFqpCpsqyhvpzlrnx1zqzVtpydypDJvojxtojB0rTdzpzh0qCt4
qjx2pCp7szJ6rDZ5sj14rCGCuUZ6qTh+sTCAuD59qi2CszuBtEx9pj2BrjKFtzaE
vFV+ozyGskCFuUiHrzqLvVqDqDaNuEKLuFmFsjWTxE+Muz6TvkGTx1KPviyaylCS
umWOsz+ZvlqRuj2Zy02VwjmbxVeTtmOQu0WZxS6gyVyUvTWfz0OdwmSUtT6fynGS
rS2lx0Oe0EqdyT2jxy2n1jin0D2l1nKYslifwESkz2Gdv0ujyXSYu1Kjwy2t1Uem
0TWs3EKtykCt1lqmzTyv0kes0FeoyEur1zez2z2x4UWw2n+hvE2w1Fqt0zu23y67
4nenyUq03kW22UO25XKqx3SrwkG64nGt0Fe04Em53DW/51q221u31ZKowEW95ijG
7FO72ULA4k694Gq13D3D3We31yTL6knA6FG/4j7F7Y6wy0fE5ne31DvJ6V6/5Jew
x07E7UrG6FXD5j7L7ETJ8UDM34+2ykHM5k3J60/K7FXJ5VvI3m7D3Ym+1njD3WrI
3HrF2WXL6aG8zZXA2njI6JnA1Ki8zmbP4pHE3ZTE1ojJ5X7N42rW4KPH1prK3bbC
1oDT65XP4rTH147U6sXHxJTW5r7M06DU7bbS48jQ2LrU3sHS3s3QzLDY7KPd7sjX
3s7W3rLf7MDb6rre7bze59bY1cnb59rc2bjl8s7f7L/k8sji7OHc2tne4dze293g
3N3i5ODi373r+Mfp67/r8tbl69Dn7M7o8svt9uDn8OXn5NHt6tvq8d3q69Pt+OXp
7Ofp5uro7Nfu8u/q6d/u9ers6db1+e7w7d71+uX0++j19fHz8Oz0/Of2/fL0+PP2
8uP6/+z5+vX49Pb59uj9/Pb7/vD9/fn7+P36///6 +fr8+fL/+fP///X/+v/8+/7+
9f/9//r///z/+/3//CwAAAAAgACAAAAI/gDdCRxIsKDBgwgTKlzIsKHDhxAjSpxI
saLFixgzatzIsaPHjyBDihxJsqTJkyhTqlzJsqXLlzBjypxJs6bNmzhz6tzJs6fP
n0CDCh1KtKjRo0iTKl3KtKnTp1CjSp1KtarVq1izat3KtavXr2DDih1LtqzZs2jT
qkU7b+3EdefGcZtLt67du3jphht3bh3cceHyCs67t6/fuIEHKxbMdx3EdeGWLUNG
d5vly5gza9bMzVoyZsOSSbbWbbPpzXSRKQs2bNiyYZVPy+Y8V9kya44bruO2bJ2/
38CDCx9OfHi/fvPm2SvOvHi/38/djfPdvLr1451zL4w8z7r378Dp/omn9xw88HrN
0Zv/bm/ZubYKxyWj/lv9+url7+vfj7++v2XhLHSOMueEF08tsiSo4IIMNuhggrz4
50881ezy4IUO8iKPcPhg6CGGtcTzXGAKrdMMN9ChJ8oBBhiAgAIJKIAAAgQYkEAD
MM5IIwEFIBCjjDMqYEABxQBnjicoHPCiAkIawCMBNbbo4oxDDgBlAQYIIEAM6vhT
nisCGDCAAQpI8MCOAdSIwAAFQBmAAAHEGeeQLva4Sz0jcpPQbs0s588+9ezCwAOE
SmDooYgmquihhDLgij/0+HOLBAgUiugDZlq6KKOFKiBKecU4gOmmpCZKqKgPFPBp
eQAmdM4y/t3VB44IEVBAwQUXWKDrrrz26quuETSQRzz07LMKAAvYakGuv0awq7O/
5nqBrVj4Uw84KEQQwbS/dusrsxckcEY8eP7mXkLWoFhfOzxEkMG78MYr77z0VrBE
l5IOAAG971bgLwoosIACB/zKi8EiE05RAbwYFOywvBDwYE5wr2pXkInr1BOpPYZM
4AEIHoQMcsgkiyzyByCkDALKImNAAzq/YSMCBiSn/DEIHHgwwSLYtNOOOvIIw4HK
RK+cMwgiYOPPIh6PPHLJItv8AcpEm+wBDUoDN48y4+ypzDrk9ePKBiOUbfbZaJud
Qtpnv5C1OVN4wLbZHhiyYXDalDD3/ggkjODBLf7Y0sEIeu9ddgklmGAC4Yin3cEL
0eT3H257wuplNj7Y4EMOnPtgxOef++C56EYMkQQWNqigugotqLDCCZBbG48kJqxu
O+snmIBFOxLGE8cJt69+wgoheOIPOEKIvoMNNrigwgzMa+556Tv4YPoOKaje+gnO
n1BkcLxZbNA6w4Ddj4jGASd5cOnAMcP778MAgxDSHNcPLTLIPwMM8O+//w7g4FAo
WsC//sEPBi1gQ3f6YQ/yfKc88pjD/goIA9YdQzjjONdCmAG2SNHDPsIRD3HAAYca
3KAGJrzBDaygtGJhAwg3wIEKZajCGtYgFByiRQxryEMV1oAK/uXwz/rq40ERAgcc
cThhCm+ggx1Mw0vAGVDXGNIZ8IwHT+AoxQmJEAQiEOEHQYBDAIFDiy568Yxn7AEO
fpAFWhzjjcLIRA9+8AM01rGLdZSGl0AYnEhB0Vr1QA84UtEDM3oxCDpgwxijOIyu
wadEzbDGOdzBHD96qR3HyEQQjnAEJXjSk0T4RDv2cR5sXKGTn0ylEpzAyR/o4JVK
QKUqPXkEHVDhGP3QWCUtSUp5HOMTSCiCEpqQyiBkwhwgPEcwpugQyCwDF7CwRnHo
gY5fkEIMT4hCFbbJTSl84YIpisczVJEGKXDznNy8gjqjwE5tqhOdVWDCE1QRRC8N
UTh4/jKHL0jxhSIcoQpNcEIVpCAFJYjBF3crjzKZ+ZBzNKN8w6lHPDKpzSh4QQpb
yGhGtamKdKgHPd5ABEHDoNGSatQLUTDpFjCa0pLe4Rr44GNz8DENUmQzChjdKDu1
UARSTAxSjGSoQ8YRDBRZ8jf4+AUeoOCFpoYhDF4YQ1O9AIZAeKMflqyHNNDQVKlO
9atODUMXoArWsoYBDORAjxH7CMh64AMYgWCCFrxAVq9CFQqBoEYfn8MNrkUEMsEo
0G/8mA9gpIELZkisYs2AhsaCoQ25EBFWoUgOOnhhsYtFAxjG0Apv+Kwd6cjFZTGL
WS48o1wRhVQ98mGMP3ABDYpt/mxiyWAGL6AhF3cLjjuW0YxJPoY3lBQONRTBBTWo
oQ3IRe5xjVuGVkxMPLr0Rzs48QY3JPe6bTDuLPJxnnpQQw1uMC523RBeN3iDPDIF
jjY0QYbkije75FUDGUxBDuIQlRviawhvYgUcecSCDG+oAx/k8AY5GFgOdWiDHPBg
jHviIxZtqMOBJ2zgOnAiHtCxFjw4IWEEU7gOEm5FeY7qR3zoQg1rAHGFO4xgNdzB
GOh5znPqsQ5mLEOoDuHOUcmxCTnooQ96GIQfhuwHOQxZDpoQh4SC04s66EEPRD5y
kf2ACXb8cR/5aEUfolxkA/uhD3YABe/UN1hr8XgNQx4E/pSJrAc59GENmKjvZH9j
j24wA78TGccwgjtYaPABEIMYRB8IQWhCCDrQfXiFlfmIp2cU+tGEPvQgiNFWf9ij
F4OA9KARPQhF1Hc40KXGJeQg6Edn2tB2sMMprIzBYUiSIutwTx+JYYdENGIQjjiE
rnXNiEMUYhCv2FAuh5OOURRi18g+RK5x/QpyOJsc1IiFIwaR7Fzz+hBPPGpwjNGH
QzDC2sguBCMYsYdTbMg+82jGjS2SQfX1Axp2EPe4G9GIXTeCEvV+BYat9ZtxjCPG
1GhEr5Ota0c0ohC2DvchLJHwXTOC3o1wRC/+GJ7fQOPYh2iEJeptb3GHmbvBIR/l
/ixijW/kBxrepgS+VX5vlaucEayAxx/7YQ1YLMNa9IDGyl3Oc0o8ghGUYAQkhg4J
Sgy95T2nhCN0gWHUnocalCiEzxtR9J5DQuP34He/hxGO/EqkGeooDzkuMQlKVOLs
aE87JDqRVv9s4zbShNTYqz70tNv97mh/xCNUnohEdMIZI7Z0cMrRCaPjHe2QiMSn
B2sNDV4k1hmjBzxOMQlBFGIPe+i75jfvDED5sfHr0LP6qDGKSiRC74/QPOpXr3LU
JwLf9HYEK5yR29/MAxbUiQcqBGHrvq8+9YnAPKWD04zeuuORFYG87c1RjnKYg/nN
j37zyWEOPz4H9O44xzDm/uFHesgj+uSQvvjHD37qn9uBtlcGLgRbD/CT3/nP/xNw
IuP1ipQ8P+klTnky6Nt1WGMc9gRI/CEeWMVH5MMNzRAOFUdxlYQe5ONbGzEOzQAp
JDZNzyEe7uBXAzEgBYJ+/KF/88ANXOcO4TCBOFdm3kE+OIYRJhIOyaF/9hMcyTEO
ytB1BZFB1nB85nEc0CE59dAWEngb/bcM3PCCziE5yfEqAfIR59B4riEZymAbUBiF
Uvgat+FIBnEOvPGEthGFUDgMVTiFUCgZZGiFCQiBAqGFq/EarVGGrdEaXugazbCC
HAEXceFveJiHeHgOhrEQh6GHgBiIgWgY9XcYdyiISnvYh26xiIzYiI74iJAYiZI4
iZRYiZZ4iZiYiZq4iZzYiZ74iaAYiqI4iqRYiqZ4iqiYiqq4iqzYiq74irAYi7I4
i7RYi7ZIFAEBADs=
     ''' 
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=data))

#zip Path
pydir = os.getcwd()
zippath = os.path.join(os.getcwd(), 'main.zip')
logging.debug("path ok")


#check if lists exist
oldlistpath = os.path.join(os.getcwd(), 'old.list')
newlistpath = os.path.join(os.getcwd(), 'new.list')
logging.debug("list ok")


#Intro
def intro():
    logging.debug("Intro")
    print("\nThis program is the installer/updater of Kuro_B787-8 for Microsoft Flight Simulator.    Creator:Kurorin(@kuro_x#4595)\nRequired Contents : MSFS Premium Delux Version (B787-10)")
    messagebox.showinfo("Kuro_B787-8 Installer " + version, "This program is the installer/updater of Kuro_B787-8 for Microsoft Flight Simulator.\n\nRequired Contents :\nMSFS Premium Delux Version (B787-10)\n\nCreator : Kurorin(@kuro_x#4595)\nhttps://flightsim.to/profile/Kurorin\n\nPress OK to Continue")


def close():
    logging.debug("close")
    sys.exit()

#open Usercfg.opt
def OpenOpt():
    f = open('usercfg.opt', 'r') 
    alltxt = f.readlines()
    f.close()
    MSFSpathL = len(alltxt) 
    MSFSpathF  = alltxt[MSFSpathL-1].strip()
    MSFSpathH = MSFSpathF.replace('InstalledPackagesPath ', '') 
    MSFSpath=MSFSpathH.strip('"')
    return MSFSpath
    logging.info("MSFSpath =" + MSFSpath)

def AskCom():
    #MS Store Path
    USERCFGpathM = os.path.join((os.environ['USERPROFILE']), 'AppData\Local\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalCache')
    #Steam Path
    USERCFGpathS = os.path.join((os.environ['USERPROFILE']), 'AppData\Roaming\Microsoft Flight Simulator')
    if os.path.exists(os.path.join(USERCFGpathM, 'usercfg.opt')):
        os.chdir(USERCFGpathM)
        MSFSpath = OpenOpt()
    elif os.path.exists(os.path.join(USERCFGpathS, 'usercfg.opt')):
        os.chdir(USERCFGpathS)
        MSFSpath = OpenOpt()
    else:
        MSFSpath = os.environ['USERPROFILE']
    #ask users where Community is
    Community = filedialog.askdirectory(initialdir = MSFSpath, title='Kuro_B787-8 Installer - >>>Select Community Folder<<<') 
    return Community

#settings - window topmost
def AskCom1(sub_set):
    #MS Store Path
    USERCFGpathM = os.path.join((os.environ['USERPROFILE']), 'AppData\Local\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalCache')
    #Steam Path
    USERCFGpathS = os.path.join((os.environ['USERPROFILE']), 'AppData\Roaming\Microsoft Flight Simulator')
    if os.path.exists(os.path.join(USERCFGpathM, 'usercfg.opt')):
        os.chdir(USERCFGpathM)
        MSFSpath = OpenOpt()
    elif os.path.exists(os.path.join(USERCFGpathS, 'usercfg.opt')):
        os.chdir(USERCFGpathS)
        MSFSpath = OpenOpt()
    else:
        MSFSpath = os.environ['USERPROFILE']
    #ask users where Community is
    Community = filedialog.askdirectory(parent=sub_set, initialdir = MSFSpath, title='Kuro_B787-8 Installer - >>>Select Community Folder<<<') 
    return Community
'''def AskGESp(sub_set, pydir, Sp1):
    GESpPath = filedialog.askopenfilename(parent=sub_set, filetypes = [('GE Sp Sound.xml', '*.xml')], initialdir = os.environ['USERPROFILE'], title='Kuro_B787-8 Installer - >>>Select GE SoundPack sound.xml<<<')
    if not GESpPath =="":
        OrgGESp = os.path.dirname(GESpPath)
        print(OrgGESp)
        TempGE = os.path.join(pydir, 'Sp/GE')
        if not os.path.exists(OrgGESp):
            print("GE Sp not found in the folder you specified. GE Sp setting is disabled.")
            messagebox.showwarning("Kuro_B787-8 Installer ", "GE Sp not found in the folder you specified. GE Sp setting is disabled.")
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["GESpDate"] = ""
                config_L["UseGESp"] = bool(0)
                json.dump(config_L, config_json)
            return
        else:
            shutil.rmtree(TempGE, onerror=remove_readonly)
            shutil.copytree(OrgGESp , TempGE, dirs_exist_ok=True)
            Sp1.set(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        sub_set.attributes("-topmost", True)
    return Community'''

def AskGESp(sub_set, pydir, Sp1):
    GESpPath = filedialog.askopenfilename(parent=sub_set, filetypes = [('GE Sp Sound.xml', '*.xml')], initialdir = os.environ['USERPROFILE'], title='Kuro_B787-8 Installer - >>>Select GE SoundPack sound.xml<<<')
    if not GESpPath =="":
        OrgGESp = os.path.dirname(GESpPath)
        SpFiles = []
        SpFiles.append(GESpPath)
        #add Sp files
        with open(GESpPath, "r", encoding="utf-8") as f:
            for line in f:
                if re.search("MainPackage", line):
                    linexml = ET.fromstring(line)
                    Filename=linexml.attrib.get('Name')+".PC.pck"
                    SpFiles.append(os.path.join(OrgGESp, Filename))
                if re.search("AdditionalPackage", line):
                    linexml = ET.fromstring(line)
                    Filename=linexml.attrib.get('Name')+".PC.pck"
                    SpFiles.append(os.path.join(OrgGESp, Filename))
        print(SpFiles)
        TempGE = os.path.join(pydir, 'Sp/GE')
        if not os.path.exists(OrgGESp):
            print("GE Sp not found in the folder you specified. GE Sp setting is disabled.")
            messagebox.showwarning("Kuro_B787-8 Installer ", "GE Sp not found in the folder you specified. GE Sp setting is disabled.")
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["GESpDate"] = ""
                config_L["UseGESp"] = bool(0)
                json.dump(config_L, config_json)
            return
        else:
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["GESpDate"] = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                json.dump(config_L, config_json)
            shutil.rmtree(TempGE, onerror=remove_readonly)
            os.mkdir(TempGE)
            for SpFile in SpFiles:
                shutil.copy(SpFile , TempGE)
            Sp1.set(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        sub_set.attributes("-topmost", True)
    return Community

def AskRRSp(sub_set, pydir, Sp2):
    RRSpPath = filedialog.askopenfilename(parent=sub_set, filetypes = [('RR Sp Sound.xml', '*.xml')], initialdir = os.environ['USERPROFILE'], title='Kuro_B787-8 Installer - >>>Select RR SoundPack sound.xml<<<') 
    if not RRSpPath =="":
        OrgRRSp = os.path.dirname(RRSpPath)
        SpFiles = []
        SpFiles.append(RRSpPath)
        #add Sp files
        with open(RRSpPath, "r", encoding="utf-8") as f:
            for line in f:
                if re.search("MainPackage", line):
                    linexml = ET.fromstring(line)
                    Filename=linexml.attrib.get('Name')+".PC.pck"
                    SpFiles.append(os.path.join(OrgRRSp, Filename))
                if re.search("AdditionalPackage", line):
                    linexml = ET.fromstring(line)
                    Filename=linexml.attrib.get('Name')+".PC.pck"
                    SpFiles.append(os.path.join(OrgRRSp, Filename))
        print(SpFiles)
        TempRR = os.path.join(pydir, 'Sp/RR')
        if not os.path.exists(OrgRRSp):
            print("RR Sp not found in the folder you specified. RR Sp setting is disabled.")
            messaRRbox.showwarning("Kuro_B787-8 Installer ", "RR Sp not found in the folder you specified. RR Sp setting is disabled.")
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["RRSpDate"] = ""
                config_L["UseRRSp"] = bool(0)
                json.dump(config_L, config_json)
            return
        else:
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["RRSpDate"] = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                json.dump(config_L, config_json)
            shutil.rmtree(TempRR, onerror=remove_readonly)
            os.mkdir(TempRR)
            for SpFile in SpFiles:
                shutil.copy(SpFile , TempRR)
            Sp2.set(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        sub_set.attributes("-topmost", True)
    return Community

#open config
with open(os.path.join(pydir, 'settings.jsonc'), mode='r', encoding='utf-8') as config_json:
    config_L=json.load(config_json)
    Community = config_L["CommunityPath"]
    UseGESp = config_L["UseGESp"]
    GESpDate = config_L["GESpDate"]
    UseRRSp = config_L["UseRRSp"]
    RRSpDate = config_L["RRSpDate"]
    isFirstInstall = config_L["isFirstInstall"]
    logging.debug("read Community from cfg")
    print("Community Path = " + Community)

#Find Camera
def chkCam(Community):
    logging.debug("chkCam")
    os.chdir(Community)
    Campath0 = os.path.join(Community, 'z_knusprigvej-b788-fixed-cam')
    #Campath1 = os.path.join(Community, '')
    if os.path.exists(Campath0):
        isCam = True
        Campath = Campath0
        logging.info("Custom Views found")
        print("Custom Views found")
    else:
        isCam = False
        Campath = ""
    return isCam, Campath

#Find HD78XH
def chkB78XH(Community):
    logging.debug("chkB78XH")
    os.chdir(Community)
    HDpathS = os.path.join(Community, 'B78XH')
    HDpathD = os.path.join(Community, 'B78XH-main')
    HDpathD2 = os.path.join(Community, 'B78XH-dev')
    HDpathE = os.path.join(Community, 'B78XH-experimental')
    #check if HD78XH exists and HD78XH is separated new one -v1.1.0
    if os.path.exists(HDpathS):
        HDname = "B78XH"
        HDPath = HDpathS
        logging.info("HD78XH(Stable) found")
        print("HD78XH(Stable) found")
    elif os.path.exists(HDpathD):
        HDname = "B78XH-main"
        HDPath = HDpathD
        logging.info("HD78XH(Development) found")
        print("HD78XH(Development) found")
    elif os.path.exists(HDpathD2):
        HDname = "B78XH-dev"
        HDPath = HDpathD2
        logging.info("HD78XH(Development) found")
        print("HD78XH(Development) found")
    elif os.path.exists(HDpathE):
        HDname = "B78XH-experimental"
        HDPath = HDpathE
        logging.info("HD78XH(Experimental) found")
        print("HD78XH(Experimental) found")
    else:
        HDname = "NaN"
        HDPath = "NaN"
        logging.error("HD78XH not found.")
        print("HD78XH not found.")
        return
    return HDname, HDPath



#def - extract and copy 787-8
def Copy788(pydir, Community):
    with open(os.path.join(pydir, 'settings.jsonc'), mode='r', encoding='utf-8') as config_json:
        UseGESp = config_L["UseGESp"]
        UseRRSp = config_L["UseRRSp"]
    logging.info("Extracting Kuro_B787-8")
    print("Extracting Kuro_B787-8")
    zip_f = zipfile.ZipFile(zippath, "r")
    zip_f.extractall(os.path.join(pydir, 'Temp'))
    zip_f.close()
    logging.info("Extracted Kuro_B787-8")
    print("Extracted Kuro_B787-8")
    if UseGESp:
        logging.info("Copying GE Sp to Temp")
        print("Copying GE Sp to Temp")
        KuroGE = os.path.join(pydir, 'Temp/Kuro_B787-8/SimObjects/Airplanes/Kuro_B787_8/soundGE')
        shutil.rmtree(KuroGE, onerror=remove_readonly)
        shutil.copytree(os.path.join(pydir, 'Sp/GE'), KuroGE, dirs_exist_ok=True)
        logging.info("Copyied GE Sp to Temp")
        print("Copyied GE Sp to Temp")
    if UseRRSp:
        logging.info("Copying RR Sp to Temp")
        print("Copying RR Sp to Temp")
        KuroRR = os.path.join(pydir, 'Temp/Kuro_B787-8/SimObjects/Airplanes/Kuro_B787_8/soundRR')
        shutil.rmtree(KuroRR, onerror=remove_readonly)
        shutil.copytree(os.path.join(pydir, 'Sp/RR'), KuroRR, dirs_exist_ok=True)
        logging.info("Copied RR Sp to Temp")
        print("Copied RR Sp to Temp")
    #rewriteJson
    subprocess.run([os.path.join(pydir, 'MSFSLayoutGenerator.exe'), os.path.join(pydir, 'Temp/Kuro_B787-8/layout.json')])
    logging.info("Rewrote json")
    print("Rewrote json")
    logging.info("Copying Kuro_B787-8 to Community")
    print("Copying Kuro_B787-8 to Community")
    shutil.copytree(os.path.join(pydir, 'Temp'), Community, dirs_exist_ok=True)
    logging.info("Copied Kuro_B787-8 to Community")
    print("Copied Kuro_B787-8 to Community")


#check if 787-8 exists and install
def check788exist(Community, zippath, KuroPath):
    if os.path.exists(KuroPath):
        logging.info("Kuro_B787-8 found in Community folder")
        print("Kuro_B787-8 found in Community folder")
        isUpdate = 1
        if messagebox.askyesno("Kuro_B787-8 Installer", "Kuro_B787-8 found in Community folder.\nDo you want to replace the current one?\n\nSelect Yes to continue.\nSelect No to abort install"):
            willInstall = 1
        else:
            willInstall = 0
    else:
        isUpdate = 0
        willInstall = 1#for temp
    return willInstall, isUpdate

def install788(Community, zippath, isUpdate, KuroPath, pydir):
    #check if zip exist
    if not os.path.exists(zippath):
        logging.error("Required Installer Component(main.zip) not found.")
        print("Required Installer Component(main.zip) not found. Download and Extract the installer again.")
        messagebox.showerror("Kuro_B787-8 Installer - Installation Failed", "Required Installer Component(main.zip) not found.\n(The file is required to install)\n\nDownload and Extract the installer again.")
        isInstallperformed = 0
    elif not isUpdate:#install
        #copy 787-8
        Copy788(pydir, Community)
        isInstallperformed = 1
    else:#update
        #delete 787-8
        logging.info("Deleting Kuro_B787-8 in Community")
        print("Deleting Kuro_B787-8 in Community")
        shutil.rmtree(KuroPath, onerror=remove_readonly)
        logging.info("Deleted Kuro_B787-8 in Community")
        print("Deleted Kuro_B787-8 in Community")
        #copy 787-8
        Copy788(pydir, Community)
        isInstallperformed = 1
    return isInstallperformed

'''def CopyGESp(Sp1, val_UseGESp):
    OrgGESpPath = Sp1.get()
    OrgGESp = os.path.dirname(OrgGESpPath)
    print(OrgGESpPath)
    TempGE = os.path.join(pydir, 'Sp/GE')
    if not os.path.exists(OrgGESpPath):
        print("GE Sp not found in the folder you specified. GE Sp setting is disabled.")
        messagebox.showwarning("Kuro_B787-8 Installer ", "GE Sp not found in the folder you specified. GE Sp setting is disabled.")
        with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
            config_L["GESpDate"] = ""
            config_L["UseGESp"] = bool(0)
            json.dump(config_L, config_json)
        val_UseGESp.set(False)
        return
    else:
        shutil.rmtree(TempGE, onerror=remove_readonly)
        shutil.copytree(OrgGESp , TempGE, dirs_exist_ok=True)
    return

def CopyRRSp(Sp2, val_UseRRSp):
    OrgRRSpPath = Sp2.get()
    OrgRRSp = os.path.dirname(OrgRRSpPath)
    print(OrgRRSpPath)
    TempRR = os.path.join(pydir, 'Sp/RR')
    if not os.path.exists(OrgRRSpPath):
        print("RR Sp not found in the folder you specified. RR Sp setting is disabled.")
        messagebox.showwarning("Kuro_B787-8 Installer ", "RR Sp not found in the folder you specified. RR Sp setting is disabled.")
        with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
            config_L["RRSpDate"] = ""
            config_L["UseRRSp"] = bool(0)
            json.dump(config_L, config_json)
        val_UseRRSp.set(False)
        return
    else:
        shutil.rmtree(TempRR, onerror=remove_readonly)
        shutil.copytree(OrgRRSp , TempRR, dirs_exist_ok=True)
    return'''


def CloseSpSetting(sub_set1, val_UseGESp, val_UseRRSp, Sp1, Sp2):
    sub_set1.destroy()
    sub_set1.quit()
    with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
        config_L["UseGESp"] = bool(val_UseGESp.get())
        config_L["UseRRSp"] = bool(val_UseRRSp.get())
        json.dump(config_L, config_json)
    
    if not Sp1.get() =="" and not Sp2.get() =="":
        with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
            config_L["GESpDate"] = Sp1.get()
            config_L["RRSpDate"] = Sp2.get()
            config_L["UseGESp"] = bool(val_UseGESp.get())
            config_L["UseRRSp"] = bool(val_UseRRSp.get())
            json.dump(config_L, config_json)
    if bool(val_UseGESp.get()):
        if Sp1.get() == "":
            print("GE Sp is not specified. Sp setting is disabled.")
            messagebox.showwarning("Kuro_B787-8 Installer ", "GE Sp is not specified. GE Sp setting is disabled.")
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["UseGESp"] = bool(0)
                json.dump(config_L, config_json)
            val_UseGESp.set(False)
    if bool(val_UseRRSp.get()):
        if Sp2.get() == "":
            print("RR Sp is not specified. Sp setting is disabled.")
            messagebox.showwarning("Kuro_B787-8 Installer ", "RR Sp is not specified. RR Sp setting is disabled.")
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["UseRRSp"] = bool(0)
                json.dump(config_L, config_json)
            val_UseRRSp.set(False)


def closesettings(sub_set, val_UseGESp, val_UseRRSp, entry1, Sp1, Sp2):
    com = tk.StringVar()
    sub_set.destroy()
    com.set(entry1.get())
    logging.debug("override Sp Setting")
    
    if not Sp1.get() =="" and not Sp2.get() =="":
        with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
            config_L["GESpDate"] = Sp1.get()
            config_L["RRSpDate"] = Sp2.get()
            config_L["UseGESp"] = bool(val_UseGESp.get())
            config_L["UseRRSp"] = bool(val_UseRRSp.get())
            json.dump(config_L, config_json)
    if bool(val_UseGESp.get()):
        if Sp1.get() == "":
            print("GE Sp is not specified. Sp setting is disabled.")
            messagebox.showwarning("Kuro_B787-8 Installer ", "GE Sp is not specified. GE Sp setting is disabled.")
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["UseGESp"] = bool(0)
                json.dump(config_L, config_json)
            val_UseGESp.set(False)
    if bool(val_UseRRSp.get()):
        if Sp2.get() == "":
            print("RR Sp is not specified. Sp setting is disabled.")
            messagebox.showwarning("Kuro_B787-8 Installer ", "RR Sp is not specified. RR Sp setting is disabled.")
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                config_L["UseRRSp"] = bool(0)
                json.dump(config_L, config_json)
            val_UseRRSp.set(False)
    
    #Community
    logging.debug("override Community from entry1")
    if not com =="":
        with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
            config_L["CommunityPath"] = com.get()
            json.dump(config_L, config_json)

#writeSpsetting to json (v2.0.0)
def writeGESpsetting(val_UseGESp, pydir):
    with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
        config_L["UseGESp"] = bool(val_UseGESp.get())
        json.dump(config_L, config_json)

#writeSpsetting to json (v2.0.0)
def writeRRSpsetting(val_UseRRSp, pydir):
    with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
        config_L["UseRRSp"] = bool(val_UseRRSp.get())
        json.dump(config_L, config_json)



def SpSet(Community, pydir, UseGESp, UseRRSp):
    ww = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    logging.debug("SpSet")
    sub_set1 = tk.Toplevel()
    lw1 = 300
    lh1 = 175
    sub_set1.geometry(str(lw1)+"x"+str(lh1)+"+"+str(int(ww/2-lw1/2))+"+"+str(int(wh/2-lh1/2)) )
    sub_set1.protocol('WM_DELETE_WINDOW', lambda:CloseSpSetting(sub_set1, val_UseGESp, val_UseRRSp, Sp1, Sp2))
    sub_set1.tk.call('wm', 'iconphoto', sub_set1._w, tk.PhotoImage(data=data))
    sub_set1.title("Kuro_B787-8 Installer " + version)
    sub_set1.resizable(0,0)
    #sub_set1.transient(root)
    sub_set1.attributes("-topmost", True)
    sub_set1.lift()
    sub_set1.focus_force()
    sub_set1.grab_set()
    Sp1 = tk.StringVar()
    Sp2 = tk.StringVar()
    Sp1.set(GESpDate)
    Sp2.set(RRSpDate)
    '''entrySp1 = tk.StringVar()
    entrySp1.set(Sp1.get())
    entrySp2 = tk.StringVar()
    entrySp2.set(Sp2.get())'''
    val_UseGESp = tk.BooleanVar()
    val_UseGESp.set(UseGESp)
    val_UseRRSp = tk.BooleanVar()
    val_UseRRSp.set(UseRRSp)
    label_sub = tk.Label(sub_set1, text="Third Party SoundPack settings")
    label_sub.place(relx = 0.5, rely = 0.1, relwidth = 0.9, anchor = tk.CENTER)
    def change_state(bool_check, button, date, label):
        if bool_check.get():
            date.config(state='normal')
            button.config(state='normal')
            label.config(state='normal')
        else:
            date.config(state='disabled')
            button.config(state='disabled')
            label.config(state='disabled')
    label_sub1 = ttk.Label(sub_set1, textvariable=Sp1)
    label_sub1.place(relx = 0.74, rely = 0.375, relwidth = 0.7, anchor = tk.CENTER)
    label_sub1_2 = ttk.Label(sub_set1, text="GE Latest Loaded:")
    label_sub1_2.place(relx = 0.25, rely = 0.375, relwidth = 0.3, anchor = tk.CENTER)

    label_sub2 = ttk.Label(sub_set1, textvariable=Sp2)
    label_sub2.place(relx = 0.74, rely = 0.7, relwidth = 0.7, anchor = tk.CENTER)
    label_sub2_2 = ttk.Label(sub_set1, text="RR Latest Loaded:")
    label_sub2_2.place(relx = 0.25, rely = 0.7, relwidth = 0.3, anchor = tk.CENTER)

    IDirButton = ttk.Button(sub_set1, text="Select", command=lambda:AskGESp(sub_set1, pydir, Sp1))
    IDirButton.place(relx = 0.85, rely = 0.375, relwidth = 0.2, anchor = tk.CENTER)

    IDirButton1 = ttk.Button(sub_set1, text="Select", command=lambda:AskRRSp(sub_set1, pydir, Sp2))
    IDirButton1.place(relx = 0.85, rely = 0.7, relwidth = 0.2, anchor = tk.CENTER)
    if not val_UseGESp.get():
        label_sub1.config(state='disabled')
        IDirButton.config(state='disabled')
        label_sub1_2.config(state='disabled')
    
    if not val_UseRRSp.get():
        label_sub2.config(state='disabled')
        IDirButton1.config(state='disabled')
        label_sub2_2.config(state='disabled')

    rdo1 = ttk.Checkbutton(sub_set1, variable=val_UseGESp, text='Use GE SoundPack', command=lambda:[writeGESpsetting(val_UseGESp, pydir), change_state(val_UseGESp, IDirButton, label_sub1, label_sub1_2)])
    rdo1.place(relx = 0.05, rely = 0.225, anchor = tk.W)
    rdo2 = ttk.Checkbutton(sub_set1, variable=val_UseRRSp, text='Use RR SoundPack', command=lambda:[writeRRSpsetting(val_UseRRSp, pydir), change_state(val_UseRRSp, IDirButton1, label_sub2, label_sub2_2)])
    rdo2.place(relx = 0.05, rely = 0.55, anchor = tk.W)

    IDirButton2 = ttk.Button(sub_set1, text="Close", command=lambda:CloseSpSetting(sub_set1, val_UseGESp, val_UseRRSp, Sp1, Sp2))
    IDirButton2.place(relx = 0.85, rely = 0.875, relwidth = 0.2, anchor = tk.CENTER)
    sub_set1.mainloop()
    return val_UseGESp, val_UseRRSp

#FirstInstall-----------------------------------------------------------------------
#FirstInstall-----------------------------------------------------------------------
def FirstInstallFunc(Community, zippath, pydir, UseGESp, UseRRSp, config_L):
    #message
    print("Welcome to Kuro_B787-8 Installer")
    messagebox.showwarning("Kuro_B787-8 Installer - IMPORTANT", """All Non-livery/Non-camera Mods for B787-8 (Lights, Systems, Wingflex, etc.) are Incompatible and Cause CTD/Behavior Problems.\nRemove them before the first flight.\n\n---\n@Livery Creator\nIf you modify and upload liveries which are included by default(ANA/ACA/etc...), write a credit "Based on livery by Kurorin" in their description.""")
    messagebox.showinfo("Welcome to Kuro_B787-8 Installer", "You have 6 steps to go.\n\n1.Select Community Folder\n2.Delete Older Kuro_B787-8 (if exists)\n3.Delete incompatible Camera Mods and B78XH (if exists)\n4.Setting up Custom SoundPack\n5.Install Kuro_B787-8\n6.Convert Liveries (if exists)")
    '''#com written in cfg or not
    if Community == "" or not os.path.exists(Community): 
        #message
        print("Select your MSFS Community folder in the next pop-up")
        messagebox.showinfo("Kuro_B787-8 Installer", "Select your MSFS Community folder in the next pop-up")
        while True:
            Community = AskCom()
            if not Community == "":
                break
        #write config
        logging.info("Community Path = " + Community)
        print("Community Path = " + Community)'''
    #Always ask Community if it's the first install
    #message
    print("Select your MSFS Community folder in the next pop-up")
    messagebox.showinfo("Kuro_B787-8 Installer", "Select your MSFS Community folder in the next pop-up")
    while True:
        Community = AskCom()
        if not Community == "":
            break
    #write config
    logging.info("Community Path = " + Community)
    print("Community Path = " + Community)
    
    with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
        config_L["CommunityPath"] = Community
        json.dump(config_L, config_json)
        logging.debug("set Community (1)")
    KuroPath = os.path.join(Community, 'Kuro_B787-8')
    checker788 = check788exist(Community, zippath, KuroPath)
    willInstall = checker788[0]
    isUpdate = checker788[1]
    isDelB788 = 1
    if willInstall:
        isDelB788 = 1
        if os.path.isdir(KuroPath):
            #delete 787-8
            logging.info("Deleting Kuro_B787-8 in Community")
            print("Deleting Kuro_B787-8 in Community")
            shutil.rmtree(KuroPath, onerror=remove_readonly)
            logging.info("Deleted Kuro_B787-8 in Community")
            print("Deleted Kuro_B787-8 in Community")
    else:
        isDelB788 = 0

    if not isDelB788:
        isSetUpDone = 0
        return isSetUpDone
    #delete camera mods
    Cam = chkCam(Community)
    isCam = Cam[0]
    Campath = Cam[1]
    if isCam:
        if messagebox.askyesno("Kuro_B787-8 Installer", "Unsupported Camera Mod found in Community folder.\nDo you want to delete it?\n\nSelect Yes to continue.\nSelect No to abort install"):
            #delete Cam Mod
            logging.info("Deleting Camera Mod in Community")
            print("Deleting Camera Mod in Community")
            shutil.rmtree(Campath, onerror=remove_readonly)
            logging.info("Deleted Camera Mod in Community")
            print("Deleted Camera Mod in Community")
        else:
            isSetUpDone = 0
            return isSetUpDone

    #delete older B78XH
    cB78XH = chkB78XH(Community)
    if cB78XH:
        HDname = cB78XH[0]
        HDPath = cB78XH[1]
        print(HDname)
        isDelB78XH = 1
        #chk Stable/Dev or Exp/NaN
        if HDname == "B78XH" or HDname == "B78XH-main" or HDname == "B78XH-dev":
            if messagebox.askyesno("Kuro_B787-8 Installer", "Unsupported B78XH found in Community folder.\nDo you want to delete it?\n\nSelect Yes to continue.\nSelect No to abort install"):
                #delete B78XH
                logging.info("Deleting B78XH in Community")
                print("Deleting B78XH in Community")
                shutil.rmtree(HDPath, onerror=remove_readonly)
                logging.info("Deleted B78XH in Community")
                print("Deleted B78XH in Community")
                isDelB78XH = 1
            else:
                isDelB78XH = 0
                isSetUpDone = 0
                return isSetUpDone
        if not isDelB78XH:
            isSetUpDone = 0
            return isSetUpDone
    
    #Setup Sp
    SpF = SpSet(Community, pydir, UseGESp, UseRRSp)
    val_UseGESp = SpF[0]
    val_UseRRSp = SpF[1]
    '''
    #Install 788
    logging.debug("Install")
    print("Although the process may appear inactive at times, it is still running. Please wait until the window appears.")
    with open(os.path.join(pydir, 'settings.jsonc'), mode='r', encoding='utf-8') as config_json:
        config_L=json.load(config_json)
        Community = config_L["CommunityPath"]
        if not Community and not os.path.exists(Community):
            Community = AskCom()
            config_L["CommunityPath"] = Community
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                json.dump(config_L, config_json)
            print("Community Path = " + Community)
    if not Community:
        return
    KuroPath = os.path.join(Community, 'Kuro_B787-8')
    checker788 = check788exist(Community, zippath, KuroPath)
    willInstall = checker788[0]
    isUpdate = checker788[1]
    if not willInstall:
        logging.error("Installation canceled")
        print("Installation canceled")
        return
    #install
    isInstallperformed = install788(Community, zippath, isUpdate, KuroPath, pydir)
    if not isInstallperformed:
        logging.error("Update canceled")
        print("Update canceled")
        return
    #clear Temp folder v2.0.0-
    logging.debug("clear temp")
    TempF = os.path.join(pydir, 'Temp')
    shutil.rmtree(TempF, ignore_errors=True)
    os.mkdir(TempF)
    #endI
    logging.info('Installation/Update has been completed')
    print('Installation/Update has been completed')
    messagebox.showinfo("Kuro_B787-8 Installer", "Installation/Update has been completed.")
    os.chdir(pydir)
    #Convert Liveries
    logging.debug("livery")
    with open(os.path.join(pydir, 'settings.jsonc'), mode='r', encoding='utf-8') as config_json:
        config_L=json.load(config_json)
        Community = config_L["CommunityPath"]
        if not Community and not os.path.exists(Community):
            Community = AskCom()
            config_L["CommunityPath"] = Community
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                json.dump(config_L, config_json)
            print("Community Path = " + Community)
    if not Community:
        return
    isConvertOnly = 1
    isUpdate = 0
    isConverted = liveryconv(Community, isUpdate, root)
    if not isConverted:
        return
    else:
        endL()
    '''
    #write FirstInstall is done
    with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
        config_L["isFirstInstall"] = False
        json.dump(config_L, config_json)
    
    isSetUpDone = 1
    isFirstInstallT = 1
    return isSetUpDone, isFirstInstallT

isFirstInstallT=0
if isFirstInstall:
    FirstInstallFuncT = FirstInstallFunc(Community, zippath, pydir, UseGESp, UseRRSp, config_L)
    if not FirstInstallFuncT:
        logging.info('Setup has been automatically canceled.')
        print('Setup has been automatically canceled.')
        messagebox.showinfo("Kuro_B787-8 Installer", "Setup has been automatically canceled.")
        close()
    isSetUpDone = FirstInstallFuncT[0]
    isFirstInstallT = FirstInstallFuncT[1]
    if not isSetUpDone:
        logging.info('Setup has been automatically canceled.')
        print('Setup has been automatically canceled.')
        messagebox.showinfo("Kuro_B787-8 Installer", "Setup has been automatically canceled.")
        close()










'''
#com written in cfg or not
if Community == "" or not os.path.exists(Community): 
    #message
    print("Select your MSFS Community folder in the next pop-up")
    messagebox.showinfo("Kuro_B787-8 Installer", "Select your MSFS Community folder in the next pop-up")
    #write config
    Community = AskCom()
    logging.info("Community Path = " + Community)
    print("Community Path = " + Community)
    with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
        config_L["CommunityPath"] = Community
        json.dump(config_L, config_json)
        logging.debug("set Community (1)")'''

#menu
def info():
    messagebox.showinfo("Kuro_B787-8 Installer " + version, "This program is the installer/updater of Kuro_B787-8 for Microsoft Flight Simulator.\n\nRequired Contents :\nMSFS Premium Delux Version (B787-10)\n\nCreator : Kurorin(@kuro_x#4595)\nhttps://flightsim.to/profile/Kurorin")
    logging.debug("Info")

def faq():
    webbrowser.open(faq_url)
    logging.debug("faq")

def chglog():
    webbrowser.open(chglog_url)
    logging.debug("chglog")

def sb():
    webbrowser.open(sb_url)
    logging.debug("sb")

def fsto():
    webbrowser.open(fsto_url)
    logging.debug("fsto")

def AskCom0(sub_set, pydir, entry1):
    sub_set.attributes("-topmost", False)
    Community = AskCom1(sub_set)
    if not Community =="":
        entry1.set(Community)
        logging.debug("Ask Community")
        with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
            config_L["CommunityPath"] = Community
            json.dump(config_L, config_json)
            logging.info("write Community to cfg")
        logging.info("Community Path = " + Community)
        print("Community Path = " + Community)
    sub_set.attributes("-topmost", True)


def logger(pydir, Community):
    if messagebox.askyesno("Kuro_B787-8 Installer", """The installer will list the contents inside your MSFS Community folder and compile them into a file.

Although the process may appear inactive at times, it is still running. Please wait until the window appears."""):
        if not Community or not os.path.exists(Community):
            while True:
                Community = AskCom()
                if Community and os.path.exists(Community):
                    break
        print("Loading Logger")
        logging.info('Loading Logger')

        #Community folders
        Files_dir = [
        f for f in os.listdir(Community) if os.path.isdir(os.path.join(Community, f))
        ]

        #exclude org Kuro_B788
        kuro_dirname= Community + "\Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8"
        #Check conflicts - cameras.cfg
        Conf_listC = []
        for filenameC in glob.glob(Community + '/**/Kuro_B787_8/cameras.cfg', recursive=True):
            dirnameC = os.path.dirname(filenameC)
            if not dirnameC == kuro_dirname:
                Conf_listC.append(dirnameC)
        
        #Check conflicts - flight_model.cfg
        Conf_listF = []
        for filenameF in glob.glob(Community + '/**/Kuro_B787_8/flight_model.cfg', recursive=True):
            dirnameF = os.path.dirname(filenameF)
            if not dirnameF == kuro_dirname:
                Conf_listF.append(dirnameF)
        
        #Check conflicts - systems.cfg
        Conf_listS = []
        for filenameS in glob.glob(Community + '/**/Kuro_B787_8/systems.cfg', recursive=True):
            dirnameS = os.path.dirname(filenameS)
            if not dirnameS == kuro_dirname:
                Conf_listS.append(dirnameS)
        
        #Check liveries
        files_code = {}
        Livery_dir = []
        black_dirname=["Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-AAL","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-ACA","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-ANA","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-ANAs","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-AVA","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-BAW","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-BOE","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-ETH","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-JAL","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-QTR","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-TUI","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-UAL"]
        for filenameA in glob.glob(Community + '/**/aircraft.cfg', recursive=True):
            with open(filenameA, 'rb') as f:
                b = f.read()
                files_code[filenameA] = detect(b)['encoding']
        for filenameA in glob.glob(Community + '/**/aircraft.cfg', recursive=True):
            with open(filenameA, encoding=files_code[filenameA]) as f1:
                s1 = f1.read()
            if 'Kuro_B787_8' in s1:
                tempdirname = os.path.dirname(filenameA)
                dirnameA = tempdirname.replace(Community + '\\' ,'')
                if not dirnameA in black_dirname:
                    Livery_dir.append(dirnameA)

        #Write logger.log
        txtpath = os.path.join(os.path.dirname(pydir), 'logger.log')
        with open(txtpath, 'w') as f:
            #Date
            f.write("--------Log Date----------------:\n")
            f.write("Date:"+datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')+"\n")
            #Path
            f.write("\n--------Community Path----------:\n")
            f.write("Path:"+Community+"\n")
            
            #cameras.cfg
            f.write("\n----------cameras.cfg-------------:\n")
            for d in Conf_listC:
                f.write("%s\n" % d)

            #flight_model.cfg
            f.write("\n--------flight_model.cfg--------:\n")
            for d in Conf_listF:
                f.write("%s\n" % d)
            
            #systems.cfg
            f.write("\n--------systems.cfg-------------:\n")
            for d in Conf_listS:
                f.write("%s\n" % d)
            
            #Liveries
            f.write("\n--------B788 Liveries-----------:\n")
            for d in Livery_dir:
                f.write("%s\n" % d)

            #Folders
            f.write("\n--------Community Folder--------:\n")
            for d in Files_dir:
                f.write("%s\n" % d)
        messagebox.showinfo("Kuro_B787-8 Installer", "Log file was succesfully exported to the following path.\nYou may be asked to submit the file for support.\n\n"+os.path.join(os.path.dirname(pydir), 'logger.log'))
        return
    else:
        return





def settings(com, Community, root, pydir, UseGESp, UseRRSp, GESpDate, RRSpDate):
    with open(os.path.join(pydir, 'settings.jsonc'), mode='r', encoding='utf-8') as config_json:
        config_L=json.load(config_json)
        Community = config_L["CommunityPath"]
        UseGESp = config_L["UseGESp"]
        GESpDate = config_L["GESpDate"]
        UseRRSp = config_L["UseRRSp"]
        RRSpDate = config_L["RRSpDate"]
        isFirstInstall = config_L["isFirstInstall"]
        logging.debug("read Community from cfg")
        print("Community Path = " + Community)
    logging.debug("Settings")
    sub_set = tk.Toplevel()
    lw1 = 300
    lh1 = 200
    sub_set.geometry(str(lw1)+"x"+str(lh1)+"+"+str(int(ww/2-lw1/2))+"+"+str(int(wh/2-lh1/2)) )
    sub_set.protocol('WM_DELETE_WINDOW', lambda:closesettings(sub_set, val_UseGESp, val_UseRRSp, entry1, Sp1, Sp2))
    sub_set.tk.call('wm', 'iconphoto', sub_set._w, tk.PhotoImage(data=data))
    sub_set.resizable(0,0)
    sub_set.transient(root)
    sub_set.attributes("-topmost", True)
    sub_set.lift()
    sub_set.focus_force()
    sub_set.grab_set()
    entry1 = tk.StringVar()
    entry1.set(Community)
    com.set(Community)
    Sp1 = tk.StringVar()
    Sp2 = tk.StringVar()
    Sp1.set(GESpDate)
    Sp2.set(RRSpDate)
    '''entrySp1 = tk.StringVar()
    entrySp1.set(Sp1.get())
    entrySp2 = tk.StringVar()
    entrySp2.set(Sp2.get())'''
    val_UseGESp = tk.BooleanVar()
    val_UseGESp.set(UseGESp)
    val_UseRRSp = tk.BooleanVar()
    val_UseRRSp.set(UseRRSp)

    label_sub0 = tk.Label(sub_set, text="Settings")
    label_sub0.place(relx = 0.5, rely = 0.075, relwidth = 0.9, anchor = tk.CENTER)
    label_sub = tk.Label(sub_set, text="Communty Path :")
    label_sub.place(relx = 0.5, rely = 0.175, relwidth = 0.9, anchor = tk.CENTER)
    IDirEntry = ttk.Entry(sub_set, textvariable=entry1)
    IDirEntry.place(relx = 0.4, rely = 0.275, relwidth = 0.7, anchor = tk.CENTER)
    IDirButton = ttk.Button(sub_set, text="Select", command=lambda:AskCom0(sub_set, pydir, entry1))
    IDirButton.place(relx = 0.85, rely = 0.275, relwidth = 0.2, anchor = tk.CENTER)

    label_sub1 = ttk.Label(sub_set, textvariable=Sp1)
    label_sub1.place(relx = 0.74, rely = 0.525, relwidth = 0.7, anchor = tk.CENTER)
    label_sub1_2 = ttk.Label(sub_set, text="GE Latest Loaded:")
    label_sub1_2.place(relx = 0.24, rely = 0.525, relwidth = 0.32, anchor = tk.CENTER)
    IDirButton1 = ttk.Button(sub_set, text="Select", command=lambda:AskGESp(sub_set, pydir, Sp1))
    IDirButton1.place(relx = 0.85, rely = 0.525, relwidth = 0.2, anchor = tk.CENTER)
    if not val_UseGESp.get():
        label_sub1.config(state='disabled')
        IDirButton1.config(state='disabled')
        label_sub1_2.config(state='disabled')
    def change_state(bool_check, button, date, label):
        if bool_check.get():
            date.config(state='normal')
            button.config(state='normal')
            label.config(state='normal')
        else:
            date.config(state='disabled')
            button.config(state='disabled')
            label.config(state='disabled')
    rdo1 = ttk.Checkbutton(sub_set, variable=val_UseGESp, text='Use GE SoundPack', command=lambda:[writeGESpsetting(val_UseGESp, pydir), change_state(val_UseGESp, IDirButton1, label_sub1, label_sub1_2)])
    rdo1.place(relx = 0.04, rely = 0.4, anchor = tk.W)

    label_sub2 = ttk.Label(sub_set, textvariable=Sp2)
    label_sub2.place(relx = 0.74, rely = 0.775, relwidth = 0.7, anchor = tk.CENTER)
    label_sub2_2 = ttk.Label(sub_set, text="RR Latest Loaded:")
    label_sub2_2.place(relx = 0.24, rely = 0.775, relwidth = 0.32, anchor = tk.CENTER)
    IDirButton2 = ttk.Button(sub_set, text="Select", command=lambda:AskRRSp(sub_set, pydir, Sp2))
    IDirButton2.place(relx = 0.85, rely = 0.775, relwidth = 0.2, anchor = tk.CENTER)
    if not val_UseRRSp.get():
        label_sub2.config(state='disabled')
        IDirButton2.config(state='disabled')
        label_sub2_2.config(state='disabled')
    rdo2 = ttk.Checkbutton(sub_set, variable=val_UseRRSp, text='Use RR SoundPack', command=lambda:[writeRRSpsetting(val_UseRRSp, pydir), change_state(val_UseRRSp, IDirButton2, label_sub2, label_sub2_2)])
    rdo2.place(relx = 0.04, rely = 0.65, anchor = tk.W)
    IDirButton3 = ttk.Button(sub_set, text="Close", command=lambda:closesettings(sub_set, val_UseGESp, val_UseRRSp, entry1, Sp1, Sp2))
    IDirButton3.place(relx = 0.85, rely = 0.9, relwidth = 0.2, anchor = tk.CENTER)
    label_sub3 = tk.Label(sub_set, text="Don't Forget to Update B787-8")
    label_sub3.place(relx = 0.4, rely = 0.9, relwidth = 0.7, anchor = tk.CENTER)
    sub_set.mainloop()


def install(com, UseGESp, UseRRSp, root):
    logging.debug("Install")
    root.withdraw()
    print("\n\n>>Although the process may appear inactive at times, it is still running. Please wait until the window appears.<<\n\n")
    with open(os.path.join(pydir, 'settings.jsonc'), mode='r', encoding='utf-8') as config_json:
        config_L=json.load(config_json)
        Community = config_L["CommunityPath"]
        if Community and os.path.exists(Community):
            com.set(Community)
        else:
            Community = AskCom()
            config_L["CommunityPath"] = Community
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                json.dump(config_L, config_json)
            com.set(Community)
            print("Community Path = " + Community)
    if not Community:
        root.deiconify()
        return
    KuroPath = os.path.join(Community, 'Kuro_B787-8')
    checker788 = check788exist(Community, zippath, KuroPath)
    willInstall = checker788[0]
    isUpdate = checker788[1]
    if not willInstall:
        logging.error("Installation canceled")
        print("Installation canceled")
        root.deiconify()
        return
    #install
    isInstallperformed = install788(Community, zippath, isUpdate, KuroPath, pydir)
    if not isInstallperformed:
        logging.error("Update canceled")
        print("Update canceled")
        root.deiconify()
        return
    #clear Temp folder v2.0.0-
    logging.debug("clear temp")
    TempF = os.path.join(pydir, 'Temp')
    shutil.rmtree(TempF, ignore_errors=True)
    os.mkdir(TempF)
    endI()
    root.deiconify()



def livery(com, root):
    root.withdraw()
    logging.debug("livery")
    with open(os.path.join(pydir, 'settings.jsonc'), mode='r', encoding='utf-8') as config_json:
        config_L=json.load(config_json)
        Community = config_L["CommunityPath"]
        if Community and os.path.exists(Community):
            com.set(Community)
        else:
            Community = AskCom()
            config_L["CommunityPath"] = Community
            with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
                json.dump(config_L, config_json)
            com.set(Community)
            print("Community Path = " + Community)
    if not Community:
        root.deiconify()
        return
    isConvertOnly = 1
    isUpdate = 0
    isConverted = liveryconv(Community, isUpdate, root)
    if not isConverted:
        root.deiconify()
        return
    else:
        endL()
    root.deiconify()

#clear Temp folder v2.0.0-
logging.debug("clear temp")
TempF = os.path.join(pydir, 'Temp')
shutil.rmtree(TempF, ignore_errors=True)
os.mkdir(TempF)

#check Sp exists  v2.0.0-
logging.debug("check Sp")
SpGEPath = os.path.join(pydir, 'Sp/GE/sound.xml')
SpRRPath = os.path.join(pydir, 'Sp/RR/sound.xml')

if UseGESp:
    if not os.path.isfile(SpGEPath):
        with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
            config_L["GESpDate"] = ""
            config_L["UseGESp"] = bool(0)
            json.dump(config_L, config_json)
        print("GE Sp not found. GE Sp setting is disabled.")

if UseRRSp:
    if not os.path.isfile(SpRRPath):
        with open(os.path.join(pydir, 'settings.jsonc'), mode='w', encoding='utf-8') as config_json:
            config_L["RRSpDate"] = ""
            config_L["UseRRSp"] = bool(0)
            json.dump(config_L, config_json)
        print("RR Sp not found. RR Sp setting is disabled.")


logging.debug("root")
root.title("Kuro_B787-8 Installer " + version)
root.update_idletasks()
ww = root.winfo_screenwidth()
wh = root.winfo_screenheight()
lw = 320
lh = 150
root.geometry(str(lw)+"x"+str(lh)+"+"+str(int(ww/2-lw/2))+"+"+str(int(wh/2-lh/2)) )
root.resizable(0,0)
com = tk.StringVar()
com.set(Community)
men = tk.Menu(root) 
root.config(menu=men)
root.deiconify()
menu_file1 = tk.Menu(root, tearoff=0)
menu_file2 = tk.Menu(root, tearoff=0)
menu_file3 = tk.Menu(root, tearoff=0)
menu_file4 = tk.Menu(root, tearoff=0)

men.add_cascade(label='Settings', menu=menu_file1) 
menu_file1.add_command(label='Settings', command=lambda:settings(com, Community, root, pydir, UseGESp, UseRRSp, GESpDate, RRSpDate)) 
menu_file1.add_separator() 
menu_file1.add_command(label='Close', command=close)

men.add_cascade(label='Links', menu=menu_file2)
menu_file2.add_command(label='FAQ Page', command=faq)
menu_file2.add_command(label='SimBrief Profile', command=sb)
menu_file2.add_command(label='Changelogs Page', command=chglog)

men.add_cascade(label='Info', menu=menu_file3) 
menu_file3.add_command(label='Info', command=info)
menu_file3.add_command(label='Flightsim.to Page', command=fsto)

men.add_cascade(label='Tools', menu=menu_file4)
menu_file4.add_command(label='Write Log for Support', command=lambda:logger(pydir, Community))

button1 = ttk.Button(root, text="Install/Update B787-8", command=lambda:install(com, UseGESp, UseRRSp, root))
button1.place(relx = 0.5, rely = 0.2, relwidth = 0.8, anchor = tk.CENTER)
button2 = ttk.Button(root, text="Convert Livery (From ~v1.1.6)", command=lambda:livery(com, root))
button2.place(relx = 0.5, rely = 0.4, relwidth = 0.8, anchor = tk.CENTER)
button3 = ttk.Button(root, text="Settings", command=lambda:settings(com, Community, root, pydir, UseGESp, UseRRSp, GESpDate, RRSpDate))
button3.place(relx = 0.3, rely = 0.6, relwidth = 0.4, anchor = tk.CENTER)
button4 = ttk.Button(root, text="FAQ", command=faq)
button4.place(relx = 0.7, rely = 0.6, relwidth = 0.4, anchor = tk.CENTER)
label1 = ttk.Label(root, text="Kurorin(@kuro_x#4595)")
label1.place(relx = 0.5, rely = 0.8, anchor = tk.CENTER)



def closelivconv(convroot):
    convroot.destroy()
    convroot.quit()
    return

def convroot(list_name, list_airline, list_creator, root, list_isv2):
    ww = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    convroot = tk.Toplevel()
    lw1 = 970
    lh1 = 400
    convroot.geometry(str(lw1)+"x"+str(lh1)+"+"+str(int(ww/2-lw1/2))+"+"+str(int(wh/2-lh1/2)) )
    convroot.tk.call('wm', 'iconphoto', convroot._w, tk.PhotoImage(data=data))
    convroot.resizable(0,0)
    #convroot.transient(root)
    convroot.attributes("-topmost", True)
    convroot.lift()
    convroot.focus_force()
    convroot.grab_set()
    convroot.title('Engine Variant Selector')
    convroot.geometry('970x400')
    convroot.protocol('WM_DELETE_WINDOW', lambda:closelivconv(convroot))
    num_list = len(list_name)
    canvas = tk.Canvas(convroot,width=930,height=350,bg='white')
    canvas.grid(row=1,rowspan=num_list,column=0,columnspan=5)
    vbar=tk.ttk.Scrollbar(convroot,orient=tk.VERTICAL)
    vbar.grid(row=1,rowspan=7,column=5,sticky='ns')
    vbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=vbar.set)
    sc_hgt=int(300/6*(num_list+1))
    canvas.config(scrollregion=(0,0,1000,sc_hgt))
    frame = tk.Frame(canvas,bg='white')
    canvas.create_window((0,0),window=frame,anchor=tk.NW,width=canvas.cget('width'))
    e0=tk.Label(frame,width=4,text='GE',background='white')
    e0.grid(row=1,column=0,padx=0,pady=0,ipadx=0,ipady=0)
    e01=tk.Label(frame,width=4,text='RR',background='white')
    e01.grid(row=1,column=1,padx=0,pady=0,ipadx=0,ipady=0)
    e4=tk.Label(frame,width=20,text='is Converted Before',background='white')
    e4.grid(row=1,column=2,padx=0,pady=0,ipadx=0,ipady=0)
    e1=tk.Label(frame,width=50,text='Name',background='white')
    e1.grid(row=1,column=3,padx=0,pady=0,ipadx=0,ipady=0)
    e2=tk.Label(frame,width=15,text='Airline',background='white')
    e2.grid(row=1,column=4,padx=0,pady=0,ipadx=0,ipady=0)
    e3=tk.Label(frame,width=35,text='Creator',background='white')
    e3.grid(row=1,column=5,padx=0,pady=0,ipadx=0,ipady=0)

    isGE =[]
    isGEv = tk.StringVar()
    def exit_list(convroot, frame):
        values = [x.get() for x in isGE]
        isGEv.set(','.join(map(str, values)))
        frame.destroy()
        convroot.destroy()
        convroot.quit()
        return
    allSelectButton = tk.Button(convroot,text=' Convert ',command=lambda:exit_list(convroot, frame))
    allSelectButton.grid(row=num_list+2,column=4)
    allSelectButton1 = tk.Button(convroot,text=' Cancel ', command=lambda:closelivconv(convroot))
    allSelectButton1.grid(row=num_list+2,column=3)

    n=0

    for i in list_name:
        if n%2==0:
            color='#e8fff7'
        else:
            color='white'
        isGE.append(tk.IntVar())
        #isGE[n].set(0)
        ##
        #read list
        with open(os.path.join(pydir, 'icao_ENG.jsonc'), "r", encoding="utf-8") as listfileT:
            list = listfileT.read()
        re_list = re.sub(r'/\*[\s\S]*?\*/|//.*', '', list)
        listB = json.loads(re_list)
        logging.debug("read icao list")
        if list_airline[n] in listB:
            icao = list_airline[n]
            isGE[n].set(listB[icao])
        else:
            isGE[n].set(0)
        ##
        c = tk.Radiobutton(frame, value=0, variable = isGE[n], width=2, text='',background='white')
        c.grid(row=n+2,column=0,padx=0,pady=0,ipadx=0,ipady=0)
        c1 = tk.Radiobutton(frame, value=1, variable = isGE[n], width=2, text='',background='white')
        c1.grid(row=n+2,column=1,padx=0,pady=0,ipadx=0,ipady=0)
        a4=str(bool(list_isv2[n]))
        b4=tk.Label(frame,width=20,text=a4,background=color)
        b4.grid(row=n+2,column=2,padx=0,pady=0,ipadx=0,ipady=0)
        a1=list_name[n]
        b1=tk.Label(frame,width=50,text=a1,background=color)
        b1.grid(row=n+2,column=3,padx=0,pady=0,ipadx=0,ipady=0)
        a2=list_airline[n]
        b2=tk.Label(frame,width=15,text=a2,background=color)
        b2.grid(row=n+2,column=4,padx=0,pady=0,ipadx=0,ipady=0)
        a3=list_creator[n]
        b3=tk.Label(frame,width=35,text=a3,background=color)
        b3.grid(row=n+2,column=5,padx=0,pady=0,ipadx=0,ipady=0)

        n=n+1
    convroot.mainloop()
    return isGEv.get()


#livery converter v1.1.2
def convert(Community, root):
    print("Loading Livery Converter")
    print("\n\n>>Although the process may appear inactive at times, it is still running. Please wait until the window appears.<<\n\n")
    logging.info('Loading Livery Converter')
    os.chdir(Community)
    files_code = {}
    #v2.0.0
    list_name = []
    list_airline = []
    list_creator = []
    list_dirname = []
    list_isv2 = []
    for filename1 in glob.glob('**/aircraft.cfg', recursive=True):
        with open(filename1, 'rb') as f:
            b = f.read()
            files_code[filename1] = detect(b)['encoding']
    for filename1 in glob.glob('**/aircraft.cfg', recursive=True):
        with open(filename1, encoding=files_code[filename1]) as f1:
            s1 = f1.read()
        if 'Kuro_B787_8' in s1:
            dirname1 = os.path.dirname(filename1)
            print("Scanning : " + dirname1 + ", Encoding=" + files_code[filename1])
            #v2.0.0
            black_dirname=["Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-AAL","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-ACA","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-ANA","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-ANAs","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-AVA","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-BAW","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-BOE","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-ETH","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-JAL","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-QTR","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-TUI","Kuro_B787-8\SimObjects\Airplanes\Kuro_B787_8-UAL"]
            if not dirname1 in black_dirname:
                air_ini = configparser.ConfigParser()
                air_ini.read(os.path.join(dirname1, 'aircraft.cfg'), encoding="utf-8")
                #v2.0.0 or not
                txt=air_ini["FLTSIM.0"]["sound"]
                txt=txt.split(';')[0]
                txt=txt.replace('"','')
                txt=txt.replace(' ','')

                txt1=air_ini["FLTSIM.0"]["title"]
                txt1=txt1.split(';')[0]
                txt1=txt1.replace('"','')
                '''txt1=txt1.replace(' ','')'''
                list_name.append(txt1)

                txt2=air_ini["FLTSIM.0"]["icao_airline"]
                txt2=txt2.split(';')[0]
                txt2=txt2.replace('"','')
                txt2=txt2.replace(' ','')
                list_airline.append(txt2)
                
                txt3=air_ini["FLTSIM.0"]["ui_createdby"]
                if txt3.split(';')[0].replace(' ','') == "\"Kuro_x\"" or txt3.split(';')[0].replace(' ','') == "\"Kuro_x,AsoboStudio\"":
                    list_creator.append("----")
                else:
                    list_creator.append(txt3.split(';')[0])
                list_dirname.append(dirname1)
                if txt == "":
                    list_isv2.append(0)
                else:
                    list_isv2.append(1)
            print("Scanned")
    #check if no list to show
    if list_dirname:
        isGEv = convroot(list_name, list_airline, list_creator, root, list_isv2).split(',')
        m=0
        for dirname1 in list_dirname:
            #if GE/RR Canceled
            if isGEv[0] == "":
                isConverted = False
                return isConverted
            if isGEv[m] == "0":
                #aircraft.cfg - GE
                air_ini = configparser.ConfigParser()
                air_ini.read(os.path.join(dirname1, 'aircraft.cfg'), encoding="utf-8")
                air_ini["FLTSIM.0"]["panel"] = "\"\..\..\Kuro_B787_8\panel.GE.W\""
                air_ini["FLTSIM.0"]["sound"] = "\"\..\..\Kuro_B787_8\soundGE\""
                f = open(os.path.join(dirname1, 'aircraft.cfg'), "w")
                air_ini.write(f)
                f.close()
                
                #texture.cfg - GE
                texCFG = glob.glob(os.path.join(dirname1, 'texture.*/texture.cfg'))
                if texCFG:
                    newtex = "[fltsim]\n\nfallback.1=..\..\..\..\\texture\nfallback.2=..\..\..\..\\texture\Interiors\nfallback.3=..\..\..\..\\texture\DetailMap\nfallback.4=..\..\..\..\\texture\Glass\nfallback.5=..\..\..\..\\texture\Livery\nfallback.6=..\..\Kuro_B787_8\\texture.GE\nfallback.7=..\..\Kuro_B787_8\\texture\nfallback.8=..\..\Asobo_B787_10\\texture\nfallback.9=..\..\..\..\\texture\Planes_Generic\nfallback.10=..\..\..\..\\texture\Extinguisher"
                    f1 = open(texCFG[0], "w")
                    f1.write(newtex)
                    f1.close()

            else:
                #aircraft.cfg - RR
                air_ini = configparser.ConfigParser()
                air_ini.read(os.path.join(dirname1, 'aircraft.cfg'), encoding="utf-8")
                air_ini["FLTSIM.0"]["panel"] = "\"\..\..\Kuro_B787_8\panel.RR.W\""
                air_ini["FLTSIM.0"]["sound"] = "\"\..\..\Kuro_B787_8\soundRR\""
                f = open(os.path.join(dirname1, 'aircraft.cfg'), "w")
                air_ini.write(f)
                f.close()

                #texture.cfg - RR
                texCFG = glob.glob(os.path.join(dirname1, 'texture.*/texture.cfg'))
                if texCFG:
                    newtex = "[fltsim]\n\nfallback.1=..\..\..\..\\texture\nfallback.2=..\..\..\..\\texture\Interiors\nfallback.3=..\..\..\..\\texture\DetailMap\nfallback.4=..\..\..\..\\texture\Glass\nfallback.5=..\..\..\..\\texture\Livery\nfallback.6=..\..\Kuro_B787_8\\texture.RR\nfallback.7=..\..\Kuro_B787_8\\texture\nfallback.8=..\..\Asobo_B787_10\\texture\nfallback.9=..\..\..\..\\texture\Planes_Generic\nfallback.10=..\..\..\..\\texture\Extinguisher"
                    f1 = open(texCFG[0], "w")
                    f1.write(newtex)
                    f1.close()
            
            #del Panel
            paneldir = glob.glob(os.path.join(dirname1, 'panel.*'))
            if paneldir:
                if os.path.isdir(paneldir[0]):
                    shutil.rmtree(paneldir[0], onerror=remove_readonly)

            #model.cfg
            mdlCFG = glob.glob(os.path.join(dirname1, 'model.*/model.cfg'))
            if mdlCFG:
                newmod = '; Reference LOD implementation, please keep these comments (for now).\n\n[model.options]\n; if true, when showing the exterior, also show the interior model (default false)\nwithExterior_showInterior=true\n; if true, when showing the interior with the exterior, exclude interior.lod.0 (default false); only has an effect when withExterior_showInterior is true\nwithExterior_showInterior_hideFirstLod=true\n; when showing the interior, force showing lod0 (default true)\nwithInterior_forceFirstLod=true\n; when showing the interior, also show the exterior model (default false)\nwithInterior_showExterior=true\n\n[models]\nexterior=B787.xml\ninterior=..\..\Asobo_B787_10\model\B787_10_interior.xml\n\n'
                f2 = open(mdlCFG[0], "w")
                f2.write(newmod)
                f2.close()
            
            #model.xml
            mdlXML = glob.glob(os.path.join(dirname1, 'model.*/*.xml'))
            if mdlXML:
                tree = ET.parse(mdlXML[0]) 
                root = tree.getroot()
                #delete Heavy
                for name in root.iter('Behaviors'):
                    for child in name:
                        for inc in child.iter('Include'):
                            if inc.attrib.get('ModelBehaviorFile') == "Heavy\\Engines\\Index.xml":
                                name.remove(child)
                            if inc.attrib.get('ModelBehaviorFile') == "Heavy\\Aircrafts\\Boeing\\787\\10\XH\\Index.xml":
                                name.remove(child)
                #delete Lights (Heavy)
                    for child in name:
                        for inc in child.iter('Component'):
                            #del GEARS
                            if inc.attrib.get('ID') == "GEARS":
                                name.remove(child)
                    for child in name:
                        for inc in child.iter('Component'):
                            if inc.attrib.get('ID') == "Lightning":
                                name.remove(child)
                            #del ENGINE
                            if inc.attrib.get('ID') == "ENGINE":
                                name.remove(child)
                new_tree = ET.ElementTree(root)
                new_tree.write(mdlXML[0], encoding='utf-8', xml_declaration=True)

                #add ENGINE/GEARS
                with open(mdlXML[0], mode="r", encoding="UTF-8") as xml1:
                    Conxml1 = xml1.read()
                    edit_old = "	</Behaviors>	\n</ModelInfo>"
                    #v2.0.0
                    #edit_new = "		<Component ID=\"GEARS\">\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>c_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:0, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:0, number) 100 * } els{ (A:GEAR ANIMATION POSITION:0, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n		<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Center_Template\">\n				<ANIM_NAME>c_gear</ANIM_NAME>\n			</UseTemplate>\n		-->\n		<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Template\">\n				<ANIM_NAME>l_gear</ANIM_NAME>\n			</UseTemplate>\n		-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>l_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:1, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:1, number) 100 * } els{ (A:GEAR ANIMATION POSITION:1, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>Door01_left_LIVERYDECALS</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:1, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:1, number) 100 * } els{ (A:GEAR ANIMATION POSITION:1, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n			</UseTemplate>\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Template\">\n				<ANIM_NAME>Door01_left_LIVERYDECALS</ANIM_NAME>\n			</UseTemplate>\n			-->\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Template\">\n				<ANIM_NAME>r_gear</ANIM_NAME>\n			-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>r_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:2, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:2, number) 100 * } els{ (A:GEAR ANIMATION POSITION:2, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n				<!-- ANIM EVENTS -->\n				<ANIM_EVENT_EFFECT_NAME>CAM_LANDINGGEARS</ANIM_EVENT_EFFECT_NAME>\n				<NORMALIZED_TIME>0.5</NORMALIZED_TIME>\n				<DIRECTION>Both</DIRECTION>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>Door01_right_LIVERYDECALS</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:2, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:2, number) 100 * } els{ (A:GEAR ANIMATION POSITION:2, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Template\">\n				<ANIM_NAME>Door01_right_LIVERYDECALS</ANIM_NAME>\n			</UseTemplate>\n			-->\n			<UseTemplate Name=\"ASOBO_GEAR_Center_Tire_Template\">\n				<ANIM_NAME>c_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>Wheel_Nose_center</NODE_ID_STILL>\n				<NODE_ID_BLURRED>Wheel_Nose_blurred</NODE_ID_BLURRED>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Tire_Template\">\n				<ANIM_NAME>l_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>LWHEEL_01_STILL</NODE_ID_STILL>\n				<NODE_ID_BLURRED>LWHEEL_01_BLURRED</NODE_ID_BLURRED>\n				<NODE_ID_STILL_2>LWHEEL_02_STILL</NODE_ID_STILL_2>\n				<NODE_ID_BLURRED_2>LWHEEL_02_BLURRED</NODE_ID_BLURRED_2>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Tire_Template\">\n				<ANIM_NAME>r_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>RWHEEL_01_STILL</NODE_ID_STILL>\n				<NODE_ID_BLURRED>RWHEEL_01_BLURRED</NODE_ID_BLURRED>\n				<NODE_ID_STILL_2>RWHEEL_02_STILL</NODE_ID_STILL_2>\n				<NODE_ID_BLURRED_2>RWHEEL_02_BLURRED</NODE_ID_BLURRED_2>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Steering_Template\">\n    			<ANIM_SIMVAR_SCALE>1</ANIM_SIMVAR_SCALE>\n				<ANIM_NAME>c_wheel</ANIM_NAME>\n			</UseTemplate>\n		</Component>\n		<Component ID=\"ENGINE\">\n			<UseTemplate Name=\"ASOBO_ENGINE_Turbine_Template\">\n				<ID>1</ID>\n				<MIN_RPM_FOR_SLOW>19000</MIN_RPM_FOR_SLOW>\n				<MIN_RPM_FOR_BLUR>19000</MIN_RPM_FOR_BLUR>\n				<STILL_NODE_ID>1_STILL_LEFT</STILL_NODE_ID>\n				<SLOW_NODE_ID>1_SLOW_LEFT</SLOW_NODE_ID>\n				<BLURRED_NODE_ID>1_BLURRED_LEFT</BLURRED_NODE_ID>\n				<ANIM_NODE_ID>B787:Reactor_Prop_Still_left</ANIM_NODE_ID>\n				<ANIM_NAME>N1_1_anim</ANIM_NAME>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_ENGINE_Turbine_Template\">\n				<ID>2</ID>\n				<MIN_RPM_FOR_SLOW>19000</MIN_RPM_FOR_SLOW>\n				<MIN_RPM_FOR_BLUR>19000</MIN_RPM_FOR_BLUR>\n				<STILL_NODE_ID>2_STILL_RIGHT</STILL_NODE_ID>\n				<SLOW_NODE_ID>2_SLOW_RIGHT</SLOW_NODE_ID>\n				<BLURRED_NODE_ID>2_BLURRED_RIGHT</BLURRED_NODE_ID>\n				<ANIM_NODE_ID>B787:Reactor_Prop_Still_right</ANIM_NODE_ID>\n				<ANIM_NAME>N1_2_anim</ANIM_NAME>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>thrust_rev_1</ANIM_NAME>\n				<ANIM_CODE>(A:GENERAL ENG THROTTLE LEVER POSITION:1, Percent) 0 &lt; 100 *</ANIM_CODE>\n				<ANIM_LAG>75</ANIM_LAG>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>thrust_rev_2</ANIM_NAME>\n				<ANIM_CODE>(A:GENERAL ENG THROTTLE LEVER POSITION:2, Percent) 0 &lt; 100 *</ANIM_CODE>\n				<ANIM_LAG>75</ANIM_LAG>\n			</UseTemplate>\n		</Component>\n	</Behaviors>	\n</ModelInfo>"
                    #-v2.1.0
                    #edit_new = "		<Component ID=\"GEARS\">\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>c_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:0, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:0, number) 100 * } els{ (A:GEAR ANIMATION POSITION:0, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n		<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Center_Template\">\n				<ANIM_NAME>c_gear</ANIM_NAME>\n			</UseTemplate>\n		-->\n		<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Template\">\n				<ANIM_NAME>l_gear</ANIM_NAME>\n			</UseTemplate>\n		-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>l_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:1, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:1, number) 100 * } els{ (A:GEAR ANIMATION POSITION:1, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>Door01_left_LIVERYDECALS</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:1, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:1, number) 100 * } els{ (A:GEAR ANIMATION POSITION:1, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n			</UseTemplate>\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Template\">\n				<ANIM_NAME>Door01_left_LIVERYDECALS</ANIM_NAME>\n			</UseTemplate>\n			-->\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Template\">\n				<ANIM_NAME>r_gear</ANIM_NAME>\n			-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>r_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:2, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:2, number) 100 * } els{ (A:GEAR ANIMATION POSITION:2, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n				<!-- ANIM EVENTS -->\n				<ANIM_EVENT_EFFECT_NAME>CAM_LANDINGGEARS</ANIM_EVENT_EFFECT_NAME>\n				<NORMALIZED_TIME>0.5</NORMALIZED_TIME>\n				<DIRECTION>Both</DIRECTION>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>Door01_right_LIVERYDECALS</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:2, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:2, number) 100 * } els{ (A:GEAR ANIMATION POSITION:2, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Template\">\n				<ANIM_NAME>Door01_right_LIVERYDECALS</ANIM_NAME>\n			</UseTemplate>\n			-->\n			<UseTemplate Name=\"ASOBO_GEAR_Center_Tire_Template\">\n				<ANIM_NAME>c_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>Wheel_Nose_center</NODE_ID_STILL>\n				<NODE_ID_BLURRED>Wheel_Nose_blurred</NODE_ID_BLURRED>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Tire_Template\">\n				<ANIM_NAME>l_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>LWHEEL_01_STILL</NODE_ID_STILL>\n				<NODE_ID_BLURRED>LWHEEL_01_BLURRED</NODE_ID_BLURRED>\n				<NODE_ID_STILL_2>LWHEEL_02_STILL</NODE_ID_STILL_2>\n				<NODE_ID_BLURRED_2>LWHEEL_02_BLURRED</NODE_ID_BLURRED_2>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Tire_Template\">\n				<ANIM_NAME>r_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>RWHEEL_01_STILL</NODE_ID_STILL>\n				<NODE_ID_BLURRED>RWHEEL_01_BLURRED</NODE_ID_BLURRED>\n				<NODE_ID_STILL_2>RWHEEL_02_STILL</NODE_ID_STILL_2>\n				<NODE_ID_BLURRED_2>RWHEEL_02_BLURRED</NODE_ID_BLURRED_2>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Steering_Template\">\n    			<ANIM_SIMVAR_SCALE>1</ANIM_SIMVAR_SCALE>\n				<ANIM_NAME>c_wheel</ANIM_NAME>\n			</UseTemplate>\n		</Component>\n		<Component ID=\"ENGINE\">\n			<Component ID=\"ENGINE_Turbine_1\" Node=\"N1_1_anim\">\n				<DefaultTemplateParameters>\n					<ID>1</ID>\n					<ANIM_NODE_ID>N1_1_anim</ANIM_NODE_ID>\n					<ANIM_NAME>N1_1_anim</ANIM_NAME>\n					<STILL_NODE_ID>PROP_1_STILL_LEFT</STILL_NODE_ID>\n					<SLOW_NODE_ID>PROP_1_SLOW_LEFT</SLOW_NODE_ID>\n					<BLURRED_NODE_ID>PROP_1_BLURRED_LEFT</BLURRED_NODE_ID>\n					<MIN_N1_PCT_FOR_SLOW>80</MIN_N1_PCT_FOR_SLOW>\n					<MIN_N1_PCT_FOR_BLUR>120</MIN_N1_PCT_FOR_BLUR>\n					<FROSTED>False</FROSTED>\n					<STILL_NODE_ID_COUNT>2</STILL_NODE_ID_COUNT>\n					<SLOW_NODE_ID_COUNT>1</SLOW_NODE_ID_COUNT>\n					<BLURRED_NODE_ID_COUNT>2</BLURRED_NODE_ID_COUNT>\n				</DefaultTemplateParameters>\n				<UseTemplate Name=\"ASOBO_GT_Anim\">\n					<!-- 2726 is the max rated N1 of the GEnx-1B64 -->\n					<ANIM_CODE>0.01 3 2726 (A:TURB ENG N1:1, Percent) (A:ANIMATION DELTA TIME, seconds) * * * *</ANIM_CODE>\n					<ANIM_LENGTH>360</ANIM_LENGTH>\n					<ANIM_WRAP>1</ANIM_WRAP>\n					<ANIM_DELTA>1</ANIM_DELTA>\n				</UseTemplate>\n			</Component>\n			<Component ID=\"ENGINE_Turbine_1_Visibility\">\n				<DefaultTemplateParameters>\n					<ID>1</ID>\n					<ANIM_NODE_ID>N1_1_anim</ANIM_NODE_ID>\n					<ANIM_NAME>N1_1_anim</ANIM_NAME>\n					<STILL_NODE_ID>PROP_1_STILL_LEFT</STILL_NODE_ID>\n					<SLOW_NODE_ID>PROP_1_SLOW_LEFT</SLOW_NODE_ID>\n					<BLURRED_NODE_ID>PROP_1_BLURRED_LEFT</BLURRED_NODE_ID>   \n					<MIN_N1_PCT_FOR_SLOW>80</MIN_N1_PCT_FOR_SLOW>\n					<MIN_N1_PCT_FOR_BLUR>120</MIN_N1_PCT_FOR_BLUR>\n					<FROSTED>False</FROSTED>\n					<STILL_NODE_ID_COUNT>2</STILL_NODE_ID_COUNT>\n					<SLOW_NODE_ID_COUNT>1</SLOW_NODE_ID_COUNT>\n					<BLURRED_NODE_ID_COUNT>2</BLURRED_NODE_ID_COUNT>\n				</DefaultTemplateParameters>\n				<OverrideTemplateParameters>\n					<PROCESS_PARAM1>True</PROCESS_PARAM1>\n					<PARAM1>NODE_ID</PARAM1>\n					<PARAM1_SUFFIX>_NODE_ID</PARAM1_SUFFIX>\n				</OverrideTemplateParameters>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>2</MAX_ID>\n					<STATE>Still</STATE>\n					<PARAM1_PREFIX>STILL_</PARAM1_PREFIX>\n				</UseTemplate>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>1</MAX_ID>\n					<STATE>Slow</STATE>\n					<PARAM1_PREFIX>SLOW_</PARAM1_PREFIX>\n				</UseTemplate>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>2</MAX_ID>\n					<STATE>Blurred</STATE>\n					<PARAM1_PREFIX>BLURRED_</PARAM1_PREFIX>\n				</UseTemplate>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Still\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>(A:TURB ENG N1:1, Percent) 80 &lt;</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Slow\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>\n								(A:TURB ENG N1:1, Percent) 80 &gt;\n								(A:TURB ENG N1:1, Percent) 120 &lt; and\n							</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Blurred\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>(A:TURB ENG N1:1, Percent) 120 &gt;</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n			</Component>\n			<Component ID=\"ENGINE_Turbine_2\" Node=\"N1_2_anim\">\n				<DefaultTemplateParameters>\n					<ID>2</ID>\n					<ANIM_NODE_ID>N1_2_anim</ANIM_NODE_ID>\n					<ANIM_NAME>N1_2_anim</ANIM_NAME>\n					<STILL_NODE_ID>PROP_2_STILL_LEFT</STILL_NODE_ID>\n					<SLOW_NODE_ID>PROP_2_SLOW_LEFT</SLOW_NODE_ID>\n					<BLURRED_NODE_ID>PROP_2_BLURRED_LEFT</BLURRED_NODE_ID>\n					<MIN_N1_PCT_FOR_SLOW>80</MIN_N1_PCT_FOR_SLOW>\n					<MIN_N1_PCT_FOR_BLUR>120</MIN_N1_PCT_FOR_BLUR>\n					<FROSTED>False</FROSTED>\n					<STILL_NODE_ID_COUNT>2</STILL_NODE_ID_COUNT>\n					<SLOW_NODE_ID_COUNT>1</SLOW_NODE_ID_COUNT>\n					<BLURRED_NODE_ID_COUNT>2</BLURRED_NODE_ID_COUNT>\n				</DefaultTemplateParameters>\n				<UseTemplate Name=\"ASOBO_GT_Anim\">\n					<!-- 2726 is the max rated N1 of the GEnx-1B64 -->\n					<ANIM_CODE>0.01 3 2726 (A:TURB ENG N1:2, Percent) (A:ANIMATION DELTA TIME, seconds) * * * *</ANIM_CODE>\n					<ANIM_LENGTH>360</ANIM_LENGTH>\n					<ANIM_WRAP>1</ANIM_WRAP>\n					<ANIM_DELTA>1</ANIM_DELTA>\n				</UseTemplate>\n			</Component>\n			<Component ID=\"ENGINE_Turbine_2_Visibility\">\n				<DefaultTemplateParameters>\n					<ID>2</ID>\n					<ANIM_NODE_ID>N1_2_anim</ANIM_NODE_ID>\n					<ANIM_NAME>N1_2_anim</ANIM_NAME>\n					<STILL_NODE_ID>PROP_2_STILL_LEFT</STILL_NODE_ID>\n					<SLOW_NODE_ID>PROP_2_SLOW_LEFT</SLOW_NODE_ID>\n					<BLURRED_NODE_ID>PROP_2_BLURRED_LEFT</BLURRED_NODE_ID>   \n					<MIN_N1_PCT_FOR_SLOW>80</MIN_N1_PCT_FOR_SLOW>\n					<MIN_N1_PCT_FOR_BLUR>120</MIN_N1_PCT_FOR_BLUR>\n					<FROSTED>False</FROSTED>\n					<STILL_NODE_ID_COUNT>2</STILL_NODE_ID_COUNT>\n					<SLOW_NODE_ID_COUNT>1</SLOW_NODE_ID_COUNT>\n					<BLURRED_NODE_ID_COUNT>2</BLURRED_NODE_ID_COUNT>\n				</DefaultTemplateParameters>\n				<OverrideTemplateParameters>\n					<PROCESS_PARAM1>True</PROCESS_PARAM1>\n					<PARAM1>NODE_ID</PARAM1>\n					<PARAM1_SUFFIX>_NODE_ID</PARAM1_SUFFIX>\n				</OverrideTemplateParameters>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>2</MAX_ID>\n					<STATE>Still</STATE>\n					<PARAM1_PREFIX>STILL_</PARAM1_PREFIX>\n				</UseTemplate>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>1</MAX_ID>\n					<STATE>Slow</STATE>\n					<PARAM1_PREFIX>SLOW_</PARAM1_PREFIX>\n				</UseTemplate>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>2</MAX_ID>\n					<STATE>Blurred</STATE>\n					<PARAM1_PREFIX>BLURRED_</PARAM1_PREFIX>\n				</UseTemplate>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Still\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>(A:TURB ENG N1:2, Percent) 80 &lt;</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Slow\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>\n								(A:TURB ENG N1:2, Percent) 80 &gt;\n								(A:TURB ENG N1:2, Percent) 120 &lt; and\n							</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Blurred\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>(A:TURB ENG N1:2, Percent) 120 &gt;</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n			</Component>\n			<!--<UseTemplate Name=\"ASOBO_ENGINE_Turbine_Template\">\n				<ID>1</ID>\n				<MIN_RPM_FOR_SLOW>19000</MIN_RPM_FOR_SLOW>\n				<MIN_RPM_FOR_BLUR>19000</MIN_RPM_FOR_BLUR>\n				<STILL_NODE_ID>1_STILL_LEFT</STILL_NODE_ID>\n				<SLOW_NODE_ID>1_SLOW_LEFT</SLOW_NODE_ID>\n				<BLURRED_NODE_ID>1_BLURRED_LEFT</BLURRED_NODE_ID>\n				<ANIM_NODE_ID>B787:Reactor_Prop_Still_left</ANIM_NODE_ID>\n				<ANIM_NAME>N1_1_anim</ANIM_NAME>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_ENGINE_Turbine_Template\">\n				<ID>2</ID>\n				<MIN_RPM_FOR_SLOW>19000</MIN_RPM_FOR_SLOW>\n				<MIN_RPM_FOR_BLUR>19000</MIN_RPM_FOR_BLUR>\n				<STILL_NODE_ID>2_STILL_RIGHT</STILL_NODE_ID>\n				<SLOW_NODE_ID>2_SLOW_RIGHT</SLOW_NODE_ID>\n				<BLURRED_NODE_ID>2_BLURRED_RIGHT</BLURRED_NODE_ID>\n				<ANIM_NODE_ID>B787:Reactor_Prop_Still_right</ANIM_NODE_ID>\n				<ANIM_NAME>N1_2_anim</ANIM_NAME>\n			</UseTemplate>-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>thrust_rev_1</ANIM_NAME>\n				<ANIM_CODE>(A:GENERAL ENG THROTTLE LEVER POSITION:1, Percent) 0 &lt; 100 *</ANIM_CODE>\n				<ANIM_LAG>75</ANIM_LAG>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>thrust_rev_2</ANIM_NAME>\n				<ANIM_CODE>(A:GENERAL ENG THROTTLE LEVER POSITION:2, Percent) 0 &lt; 100 *</ANIM_CODE>\n				<ANIM_LAG>75</ANIM_LAG>\n			</UseTemplate>\n		</Component>\n	</Behaviors>	\n</ModelInfo>"
                    #v2.1.0
                    edit_new = "		<Component ID=\"GEARS\">\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>c_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:0, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:0, number) 100 * } els{ (A:GEAR ANIMATION POSITION:0, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n            <!--v2.1.0-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>c_gear2</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:0, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:0, number) 100 * } els{ (A:GEAR ANIMATION POSITION:0, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n		<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Center_Template\">\n				<ANIM_NAME>c_gear</ANIM_NAME>\n			</UseTemplate>\n		-->\n		<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Template\">\n				<ANIM_NAME>l_gear</ANIM_NAME>\n			</UseTemplate>\n		-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>l_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:1, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:1, number) 100 * } els{ (A:GEAR ANIMATION POSITION:1, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>Door01_left_LIVERYDECALS</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:1, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:1, number) 100 * } els{ (A:GEAR ANIMATION POSITION:1, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n			</UseTemplate>\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Template\">\n				<ANIM_NAME>Door01_left_LIVERYDECALS</ANIM_NAME>\n			</UseTemplate>\n			-->\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Template\">\n				<ANIM_NAME>r_gear</ANIM_NAME>\n			-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n                <ANIM_NAME>r_gear</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:2, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:2, number) 100 * } els{ (A:GEAR ANIMATION POSITION:2, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n				<!-- ANIM EVENTS -->\n				<ANIM_EVENT_EFFECT_NAME>CAM_LANDINGGEARS</ANIM_EVENT_EFFECT_NAME>\n				<NORMALIZED_TIME>0.5</NORMALIZED_TIME>\n				<DIRECTION>Both</DIRECTION>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>Door01_right_LIVERYDECALS</ANIM_NAME>\n                <ANIM_CODE>(A:GEAR ANIMATION POSITION:2, number) 0.5 &lt; if{ (A:GEAR ANIMATION POSITION:2, number) 100 * } els{ (A:GEAR ANIMATION POSITION:2, number) 2 * 1 - sqrt 50 * 50 + }</ANIM_CODE>\n                <ANIM_LENGTH>100</ANIM_LENGTH>\n            </UseTemplate>\n			<!--\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Template\">\n				<ANIM_NAME>Door01_right_LIVERYDECALS</ANIM_NAME>\n			</UseTemplate>\n			-->\n			<UseTemplate Name=\"ASOBO_GEAR_Center_Tire_Template\">\n				<ANIM_NAME>c_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>Wheel_Nose_center</NODE_ID_STILL>\n				<NODE_ID_BLURRED>Wheel_Nose_blurred</NODE_ID_BLURRED>\n			</UseTemplate>\n            <!--v2.1.0-->\n			<UseTemplate Name=\"ASOBO_GEAR_Center_Tire_Template\">\n				<ANIM_NAME>c_tire_key2</ANIM_NAME>\n				<NODE_ID_STILL>Wheel_Nose_center</NODE_ID_STILL>\n				<NODE_ID_BLURRED>Wheel_Nose_blurred</NODE_ID_BLURRED>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Left_Tire_Template\">\n				<ANIM_NAME>l_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>LWHEEL_01_STILL</NODE_ID_STILL>\n				<NODE_ID_BLURRED>LWHEEL_01_BLURRED</NODE_ID_BLURRED>\n				<NODE_ID_STILL_2>LWHEEL_02_STILL</NODE_ID_STILL_2>\n				<NODE_ID_BLURRED_2>LWHEEL_02_BLURRED</NODE_ID_BLURRED_2>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Right_Tire_Template\">\n				<ANIM_NAME>r_tire_key</ANIM_NAME>\n				<NODE_ID_STILL>RWHEEL_01_STILL</NODE_ID_STILL>\n				<NODE_ID_BLURRED>RWHEEL_01_BLURRED</NODE_ID_BLURRED>\n				<NODE_ID_STILL_2>RWHEEL_02_STILL</NODE_ID_STILL_2>\n				<NODE_ID_BLURRED_2>RWHEEL_02_BLURRED</NODE_ID_BLURRED_2>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GEAR_Steering_Template\">\n    			<ANIM_SIMVAR_SCALE>1</ANIM_SIMVAR_SCALE>\n				<ANIM_NAME>c_wheel</ANIM_NAME>\n			</UseTemplate>\n            <!--v2.1.0-->\n			<UseTemplate Name=\"ASOBO_GEAR_Steering_Template\">\n    			<ANIM_SIMVAR_SCALE>1</ANIM_SIMVAR_SCALE>\n				<ANIM_NAME>c_wheel2</ANIM_NAME>\n			</UseTemplate>\n		</Component>\n		<Component ID=\"ENGINE\">\n			<Component ID=\"ENGINE_Turbine_1\" Node=\"N1_1_anim\">\n				<DefaultTemplateParameters>\n					<ID>1</ID>\n					<ANIM_NODE_ID>N1_1_anim</ANIM_NODE_ID>\n					<ANIM_NAME>N1_1_anim</ANIM_NAME>\n					<STILL_NODE_ID>PROP_1_STILL_LEFT</STILL_NODE_ID>\n					<SLOW_NODE_ID>PROP_1_SLOW_LEFT</SLOW_NODE_ID>\n					<BLURRED_NODE_ID>PROP_1_BLURRED_LEFT</BLURRED_NODE_ID>\n					<MIN_N1_PCT_FOR_SLOW>80</MIN_N1_PCT_FOR_SLOW>\n					<MIN_N1_PCT_FOR_BLUR>120</MIN_N1_PCT_FOR_BLUR>\n					<FROSTED>False</FROSTED>\n					<STILL_NODE_ID_COUNT>2</STILL_NODE_ID_COUNT>\n					<SLOW_NODE_ID_COUNT>1</SLOW_NODE_ID_COUNT>\n					<BLURRED_NODE_ID_COUNT>2</BLURRED_NODE_ID_COUNT>\n				</DefaultTemplateParameters>\n				<UseTemplate Name=\"ASOBO_GT_Anim\">\n					<!-- 2726 is the max rated N1 of the GEnx-1B64 -->\n					<ANIM_CODE>0.01 3 2726 (A:TURB ENG N1:1, Percent) (A:ANIMATION DELTA TIME, seconds) * * * *</ANIM_CODE>\n					<ANIM_LENGTH>360</ANIM_LENGTH>\n					<ANIM_WRAP>1</ANIM_WRAP>\n					<ANIM_DELTA>1</ANIM_DELTA>\n				</UseTemplate>\n			</Component>\n			<Component ID=\"ENGINE_Turbine_1_Visibility\">\n				<DefaultTemplateParameters>\n					<ID>1</ID>\n					<ANIM_NODE_ID>N1_1_anim</ANIM_NODE_ID>\n					<ANIM_NAME>N1_1_anim</ANIM_NAME>\n					<STILL_NODE_ID>PROP_1_STILL_LEFT</STILL_NODE_ID>\n					<SLOW_NODE_ID>PROP_1_SLOW_LEFT</SLOW_NODE_ID>\n					<BLURRED_NODE_ID>PROP_1_BLURRED_LEFT</BLURRED_NODE_ID>   \n					<MIN_N1_PCT_FOR_SLOW>80</MIN_N1_PCT_FOR_SLOW>\n					<MIN_N1_PCT_FOR_BLUR>120</MIN_N1_PCT_FOR_BLUR>\n					<FROSTED>False</FROSTED>\n					<STILL_NODE_ID_COUNT>2</STILL_NODE_ID_COUNT>\n					<SLOW_NODE_ID_COUNT>1</SLOW_NODE_ID_COUNT>\n					<BLURRED_NODE_ID_COUNT>2</BLURRED_NODE_ID_COUNT>\n				</DefaultTemplateParameters>\n				<OverrideTemplateParameters>\n					<PROCESS_PARAM1>True</PROCESS_PARAM1>\n					<PARAM1>NODE_ID</PARAM1>\n					<PARAM1_SUFFIX>_NODE_ID</PARAM1_SUFFIX>\n				</OverrideTemplateParameters>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>2</MAX_ID>\n					<STATE>Still</STATE>\n					<PARAM1_PREFIX>STILL_</PARAM1_PREFIX>\n				</UseTemplate>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>1</MAX_ID>\n					<STATE>Slow</STATE>\n					<PARAM1_PREFIX>SLOW_</PARAM1_PREFIX>\n				</UseTemplate>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>2</MAX_ID>\n					<STATE>Blurred</STATE>\n					<PARAM1_PREFIX>BLURRED_</PARAM1_PREFIX>\n				</UseTemplate>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Still\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>(A:TURB ENG N1:1, Percent) 80 &lt;</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Slow\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>\n								(A:TURB ENG N1:1, Percent) 80 &gt;\n								(A:TURB ENG N1:1, Percent) 120 &lt; and\n							</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Blurred\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>(A:TURB ENG N1:1, Percent) 120 &gt;</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n			</Component>\n			<Component ID=\"ENGINE_Turbine_2\" Node=\"N1_2_anim\">\n				<DefaultTemplateParameters>\n					<ID>2</ID>\n					<ANIM_NODE_ID>N1_2_anim</ANIM_NODE_ID>\n					<ANIM_NAME>N1_2_anim</ANIM_NAME>\n					<STILL_NODE_ID>PROP_2_STILL_LEFT</STILL_NODE_ID>\n					<SLOW_NODE_ID>PROP_2_SLOW_LEFT</SLOW_NODE_ID>\n					<BLURRED_NODE_ID>PROP_2_BLURRED_LEFT</BLURRED_NODE_ID>\n					<MIN_N1_PCT_FOR_SLOW>80</MIN_N1_PCT_FOR_SLOW>\n					<MIN_N1_PCT_FOR_BLUR>120</MIN_N1_PCT_FOR_BLUR>\n					<FROSTED>False</FROSTED>\n					<STILL_NODE_ID_COUNT>2</STILL_NODE_ID_COUNT>\n					<SLOW_NODE_ID_COUNT>1</SLOW_NODE_ID_COUNT>\n					<BLURRED_NODE_ID_COUNT>2</BLURRED_NODE_ID_COUNT>\n				</DefaultTemplateParameters>\n				<UseTemplate Name=\"ASOBO_GT_Anim\">\n					<!-- 2726 is the max rated N1 of the GEnx-1B64 -->\n					<ANIM_CODE>0.01 3 2726 (A:TURB ENG N1:2, Percent) (A:ANIMATION DELTA TIME, seconds) * * * *</ANIM_CODE>\n					<ANIM_LENGTH>360</ANIM_LENGTH>\n					<ANIM_WRAP>1</ANIM_WRAP>\n					<ANIM_DELTA>1</ANIM_DELTA>\n				</UseTemplate>\n			</Component>\n			<Component ID=\"ENGINE_Turbine_2_Visibility\">\n				<DefaultTemplateParameters>\n					<ID>2</ID>\n					<ANIM_NODE_ID>N1_2_anim</ANIM_NODE_ID>\n					<ANIM_NAME>N1_2_anim</ANIM_NAME>\n					<STILL_NODE_ID>PROP_2_STILL_LEFT</STILL_NODE_ID>\n					<SLOW_NODE_ID>PROP_2_SLOW_LEFT</SLOW_NODE_ID>\n					<BLURRED_NODE_ID>PROP_2_BLURRED_LEFT</BLURRED_NODE_ID>   \n					<MIN_N1_PCT_FOR_SLOW>80</MIN_N1_PCT_FOR_SLOW>\n					<MIN_N1_PCT_FOR_BLUR>120</MIN_N1_PCT_FOR_BLUR>\n					<FROSTED>False</FROSTED>\n					<STILL_NODE_ID_COUNT>2</STILL_NODE_ID_COUNT>\n					<SLOW_NODE_ID_COUNT>1</SLOW_NODE_ID_COUNT>\n					<BLURRED_NODE_ID_COUNT>2</BLURRED_NODE_ID_COUNT>\n				</DefaultTemplateParameters>\n				<OverrideTemplateParameters>\n					<PROCESS_PARAM1>True</PROCESS_PARAM1>\n					<PARAM1>NODE_ID</PARAM1>\n					<PARAM1_SUFFIX>_NODE_ID</PARAM1_SUFFIX>\n				</OverrideTemplateParameters>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>2</MAX_ID>\n					<STATE>Still</STATE>\n					<PARAM1_PREFIX>STILL_</PARAM1_PREFIX>\n				</UseTemplate>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>1</MAX_ID>\n					<STATE>Slow</STATE>\n					<PARAM1_PREFIX>SLOW_</PARAM1_PREFIX>\n				</UseTemplate>\n				<UseTemplate Name=\"ASOBO_GT_Helper_Recursive_ID\">\n					<MAX_ID>2</MAX_ID>\n					<STATE>Blurred</STATE>\n					<PARAM1_PREFIX>BLURRED_</PARAM1_PREFIX>\n				</UseTemplate>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Still\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>(A:TURB ENG N1:2, Percent) 80 &lt;</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Slow\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>\n								(A:TURB ENG N1:2, Percent) 80 &gt;\n								(A:TURB ENG N1:2, Percent) 120 &lt; and\n							</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n				<Condition NotEmpty=\"NODE_ID\" STATE=\"Blurred\">\n					<True>\n						<UseTemplate Name=\"ASOBO_GT_Visibility\">\n							<VISIBILITY_CODE>(A:TURB ENG N1:2, Percent) 120 &gt;</VISIBILITY_CODE>\n						</UseTemplate>\n					</True>\n				</Condition>\n			</Component>\n			<!--<UseTemplate Name=\"ASOBO_ENGINE_Turbine_Template\">\n				<ID>1</ID>\n				<MIN_RPM_FOR_SLOW>19000</MIN_RPM_FOR_SLOW>\n				<MIN_RPM_FOR_BLUR>19000</MIN_RPM_FOR_BLUR>\n				<STILL_NODE_ID>1_STILL_LEFT</STILL_NODE_ID>\n				<SLOW_NODE_ID>1_SLOW_LEFT</SLOW_NODE_ID>\n				<BLURRED_NODE_ID>1_BLURRED_LEFT</BLURRED_NODE_ID>\n				<ANIM_NODE_ID>B787:Reactor_Prop_Still_left</ANIM_NODE_ID>\n				<ANIM_NAME>N1_1_anim</ANIM_NAME>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_ENGINE_Turbine_Template\">\n				<ID>2</ID>\n				<MIN_RPM_FOR_SLOW>19000</MIN_RPM_FOR_SLOW>\n				<MIN_RPM_FOR_BLUR>19000</MIN_RPM_FOR_BLUR>\n				<STILL_NODE_ID>2_STILL_RIGHT</STILL_NODE_ID>\n				<SLOW_NODE_ID>2_SLOW_RIGHT</SLOW_NODE_ID>\n				<BLURRED_NODE_ID>2_BLURRED_RIGHT</BLURRED_NODE_ID>\n				<ANIM_NODE_ID>B787:Reactor_Prop_Still_right</ANIM_NODE_ID>\n				<ANIM_NAME>N1_2_anim</ANIM_NAME>\n			</UseTemplate>-->\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>thrust_rev_1</ANIM_NAME>\n				<ANIM_CODE>(A:GENERAL ENG THROTTLE LEVER POSITION:1, Percent) 0 &lt; 100 *</ANIM_CODE>\n				<ANIM_LAG>75</ANIM_LAG>\n			</UseTemplate>\n			<UseTemplate Name=\"ASOBO_GT_Anim\">\n				<ANIM_NAME>thrust_rev_2</ANIM_NAME>\n				<ANIM_CODE>(A:GENERAL ENG THROTTLE LEVER POSITION:2, Percent) 0 &lt; 100 *</ANIM_CODE>\n				<ANIM_LAG>75</ANIM_LAG>\n			</UseTemplate>\n		</Component>\n	</Behaviors>	\n</ModelInfo>"
                    Conxml1= Conxml1.replace(edit_old, edit_new)
                with open(mdlXML[0], mode="w", encoding="UTF-8") as Conxml2:
                    Conxml2.write(Conxml1)
            m=m+1
        isConverted = True
        return isConverted
    else:
        messagebox.showinfo("Kuro_B787-8 Installer", "There are no liveries to convert\n(= You haven't installed any third party liveries)")
        isConverted = False
        return isConverted



#livery updater v1.1.0
def liveryconv(Community, isUpdate, root):
    logging.debug("liveryconv")
    if messagebox.askyesno("Kuro_B787-8 Installer", """B787-8 liveries released before v2 are not compatible and cause CTD.
Do you want to convert all the liveries for the B787-8 installed in your Community folder?
(Including third party liveries created from the official Paint Kit)

Although the process may appear inactive at times, it is still running. Please wait until the window appears."""):
        isConverted = convert(Community, root)
    else:
        isConverted = 0
    os.chdir(pydir)
    return isConverted




def endI():
    logging.info('Installation/Update has been completed')
    print('Installation/Update has been completed')
    messagebox.showinfo("Kuro_B787-8 Installer", "Installation/Update has been completed.")
    os.chdir(pydir)

def endL():
    logging.info('Liveries have been updated.')
    print('Liveries have been updated.')
    messagebox.showinfo("Kuro_B787-8 Installer", "Liveries have been updated.")
    os.chdir(pydir)

def endC():
    logging.info('Installation/Update has been automatically canceled.')
    print('Installation/Update has been automatically canceled.')
    messagebox.showinfo("Kuro_B787-8 Installer", "Installation has been automatically canceled.")
    os.chdir(pydir)

#firstinstall step5,6
if isFirstInstallT:
    install(com, UseGESp, UseRRSp, root)
    livery(com, root)
root.mainloop()
