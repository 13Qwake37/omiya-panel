import os
import blessed
import random
import time

term = blessed.Terminal()
underline = term.underline()
bold = term.bold()
reset = term.reset()

rozoviy = term.color_rgb(218, 112, 214)
rozoviyy = term.color_rgb(186, 85, 211)
rozoviyyy = term.color_rgb(147, 112, 219)
rozoviyyyy = term.color_rgb(238, 130, 238)
cyan = term.color_rgb(0, 255, 255)
aquamarine = term.color_rgb(127, 255, 212)
cyann = term.color_rgb(0, 206, 209)
cyannn = term.color_rgb(65, 105, 225)
green = term.color_rgb(0, 255, 127)
white = term.color_rgb(255, 255, 255)

help = f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ help - Посмотреть помощь			┃
┃ ./http-omiya - запустить атаку		┃
┃ clear - очистить консоль			┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
logo = f"""{green}
 █████╗ ███╗   ███╗██╗██╗   ██╗ █████╗       ██████╗  █████╗ ███╗  ██╗███████╗██╗
██╔══██╗████╗ ████║██║╚██╗ ██╔╝██╔══██╗      ██╔══██╗██╔══██╗████╗ ██║██╔════╝██║
██║  ██║██╔████╔██║██║ ╚████╔╝ ███████║█████╗██████╔╝███████║██╔██╗██║█████╗  ██║
██║  ██║██║╚██╔╝██║██║  ╚██╔╝  ██╔══██║╚════╝██╔═══╝ ██╔══██║██║╚████║██╔══╝  ██║
╚█████╔╝██║ ╚═╝ ██║██║   ██║   ██║  ██║      ██║     ██║  ██║██║ ╚███║███████╗███████╗
 ╚════╝ ╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝      ╚═╝     ╚═╝  ╚═╝╚═╝  ╚══╝╚══════╝╚══════╝{white}
 """

os.system("clear")
print(f"""{white}[!] Добро пожаловать в
{logo}
[!] Удачного использования""")
print(help)

def panel():
	cmd = input(f"""[{cyan}OMIYA~PANEL{white}] {rozoviy}={rozoviyy}={rozoviyyy}={rozoviyyyy}➤{white} """)
	if cmd == "help":
		print(help)
	if cmd == "clear":
		os.system("clear")
		print(logo)
		print(help)
	if cmd == "./http-omiya":
		os.system("node HTTP-OMIYA.js")

while True:
	panel()
