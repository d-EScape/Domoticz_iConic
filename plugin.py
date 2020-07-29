# Domoticz Python Plugin to monitor tracker for presence/absence of wifi devices without pinging them (pinging can drain your phone battery).
#
# Author: ESCape
#
"""
<plugin key="iConic" name="iConic - Upload custom icons into domoticz (work-around because it is broken in domoticz gui)" author="ESCape" version="0.1">
	<description>
		<h2>Work-around to upload custom icon sets into Domoticz. Without any support or guarantees.</h2>
		The plugin uses the python plugin frameworks methods to add any custom icons. Icon zip files must meet the Domoticz custom icon specs.
		Just put he icon zip files in the plugin directory (like: /home/pi/domoticz/plugins/iconic), (re)start the iconic hardware and the import will start.
		Let it run once and disable the plugin (hardware) immediately after the import has finished. Remove the zip files.
	</description>
</plugin>
"""

import Domoticz

class BasePlugin:

	def __init__(self):
		return

	def onStart(self):
		import os
		sourcepath = Parameters["HomeFolder"]
		if not os.path.isdir(sourcepath):
			Domoticz.Error(sourcepath + " not found")
		else:
			Domoticz.Status("Will import all zipfiles from " + sourcepath + ". Make sure they are all icon files!")
			allfiles = os.listdir(sourcepath)
			for thisfile in allfiles:
				if thisfile.endswith('.zip'):
					Domoticz.Status("Found " + thisfile)
					thisname = thisfile[:-4]
					if thisname in Images:
						Domoticz.Error("Iconset " + thisname + " already exists")
					else:
						fullpath = thisfile
						Domoticz.Status("Adding iconset " + thisname + " from " + fullpath)
						newimage = Domoticz.Image(Filename=fullpath)
						Domoticz.Status("Newimage data=" + str(newimage))
						newimage.Create()
						if thisname in Images:
							Domoticz.Status("iconset " + thisname + " created")
						else:
							Domoticz.Error("iconset " + thisname + " was NOT created!")
				else:
					Domoticz.Status(thisfile + " is not a (zip) icon-file")
					
		Domoticz.Status("Done importing icons.. disable this plugin!!")

			
#	def onDataReceive(self, source):

	def onHeartbeat(self):
		Domoticz.Error("Icon import is already done at startup. Disable this plugin immediately after!")

#	def onCommand(self, Unit, Command, Level, Hue):
		
	def onStop(self):
		Domoticz.Satus('IConic stopped')

global _plugin
_plugin = BasePlugin()

def onStart():
	global _plugin
	_plugin.onStart()
	
def onStop():
	global _plugin
	_plugin.onStop()

def onHeartbeat():
	global _plugin
	_plugin.onHeartbeat()

def onCommand(Unit, Command, Level, Hue):
	global _plugin
	_plugin.onCommand(Unit, Command, Level, Hue)

# Generic helper functions
def DumpConfigToLog():
	for x in Parameters:
		if Parameters[x] != "":
			Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
	Domoticz.Debug("Device count: " + str(len(Devices)))
	for x in Devices:
		Domoticz.Debug("Device:			  " + str(x) + " - " + str(Devices[x]))
		Domoticz.Debug("Device ID:		 '" + str(Devices[x].ID) + "'")
		Domoticz.Debug("Device Name:	 '" + Devices[x].Name + "'")
		Domoticz.Debug("Device nValue:	  " + str(Devices[x].nValue))
		Domoticz.Debug("Device sValue:	 '" + Devices[x].sValue + "'")
		Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
	return
