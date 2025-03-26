from phue import Bridge
from pprint import pprint
import json
import time
import toml
import requests


def phase(number, text):
    print("-----------------------------------------------")
    print("Phase", number)
    print(text)
    print("-----------------------------------------------")

phase(1, "Check Philips Hue Bridge connectivity.")
ip = input("Enter the private IP address of your Philips Hue Bridge")
bridge = Bridge(ip)
bridge.connect()
lights = []
for light in bridge.lights:
    try:
        bridge.get_light(light.name, 'colormode')
        print("Got light", light.name, ".")
    except KeyError:
        print("Didn't get light", light.name, ".")
    else: lights.append(light.name)
try:     
    title = 'Please use the spacebar to select at least one light from the choices below: '
    selectedLights = pick(lights, title, multiselect=True, min_selection_count=1, indicator='->')
except:
    print('Sorry, setup was unable to find any color capable hue lights connected to your bridge.')
else:
    goal_lights = {}
    goal_lights['Lights'] = []
    for light in selectedLights:
        goal_lights['Lights'].append(light[0])











