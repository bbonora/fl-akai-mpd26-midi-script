"""
Helper functions for mixer and channel operations.

"""

import channels
import mixer
import ui
import transport
import midi

# Snapping constants
################################
LONG_PRESS_TIME = 0.5 # Change how long a long press needs to be held for

ENABLE_SNAPPING = False # Change to False to prevent faders and knobs from snapping to default values
SNAP_RANGE = 0.03 # Will snap if within this disatnce of snap value

# Mixer snap values
MIXER_VOLUME_SNAP_TO = 0.8 # Snap mixer track volumes to 100%
MIXER_PAN_SNAP_TO = 0.0 # Snap mixer track pannings to Centred
MIXER_STEREO_SEP_SNAP_TO = 0.0 # Snap mixer track stereo separation to Original

# Channel rack snap values
CHANNEL_VOLUME_SNAP_TO = 0.78125 # Snap channel volumes to ~= 78% (FL Default)
CHANNEL_PAN_SNAP_TO = 0.0 # Snap channel pans to Centred

# Functions for mixer

# Gets the selected mixer track
def getMixerTrackNum():
	trackNum = mixer.trackNumber()
	if(trackNum is 0):
		trackNum = 1
		return trackNum
	else:
		return trackNum

# Returns name of mixer track
def getMixerTrackName(trackNum):
	if trackNum < 0: trackNum = 126
	if trackNum > 126: trackNum = 0
	return mixer.getTrackName(trackNum)  + " (" + str(trackNum) + ")"

# Toggles solo on mixer track
def mixerToggleSolo(selectedTrackNum):
	mixer.soloTrack(selectedTrackNum)
	if mixer.isTrackSolo(selectedTrackNum) is 1: return "Mixer: Solo track: " + getMixerTrackName(selectedTrackNum)
	else: return "Mixer: Unsolo track: " + getMixerTrackName(selectedTrackNum)

# Toggles mute on mixer track
def mixerToggleMute(selectedTrackNum):
	mixer.muteTrack(selectedTrackNum)
	if mixer.isTrackMuted(selectedTrackNum) is 1: return "Mixer: Mute track: " + getMixerTrackName(selectedTrackNum)
	else: return "Mixer: Unmute track: " + getMixerTrackName(selectedTrackNum)

# Adjusts fader on mixer track
def mixerAdjustFader(selectedTrackNum, data):
	parameter = float(data)/127.0
	hasSnapped = False
	if ENABLE_SNAPPING is True:
		if parameter >= (MIXER_VOLUME_SNAP_TO - SNAP_RANGE) and parameter <= (MIXER_VOLUME_SNAP_TO + SNAP_RANGE):
			parameter = MIXER_VOLUME_SNAP_TO
			hasSnapped = True
	mixer.setTrackVolume(selectedTrackNum, parameter)
	ret = "Mixer: Adjust " + getMixerTrackName(selectedTrackNum) + " volume to " + str(round(parameter / 0.8 * 100, 0)) + "%"
	if hasSnapped is True: ret += " [Snapped]"
	return ret

# Adjusts panning on mixer track
def mixerAdjustPan(selectedTrackNum, data):
	parameter = float(data - 63.5)/63.5
	hasSnapped = False
	if ENABLE_SNAPPING is True:
		if parameter >= (MIXER_PAN_SNAP_TO - SNAP_RANGE) and parameter <= (MIXER_PAN_SNAP_TO + SNAP_RANGE):
			parameter = MIXER_PAN_SNAP_TO
			hasSnapped = True
	mixer.setTrackPan(selectedTrackNum, parameter)
	ret ="Mixer: Adjust " + getMixerTrackName(selectedTrackNum) + " panning to "
	if parameter < 0: ret += str(-round(parameter * 100, 0)) + "% Left"
	elif parameter > 0: ret += str(round(parameter * 100, 0)) + "% Right"
	else: ret += "Centred"

	if hasSnapped is True: ret += " [Snapped]"
	return ret

# Adjusts stereo separation on mixer track - Currently doesn't work
def mixerAdjustStereoSep(selectedTrackNum, data):
	parameter = float(data - 63.5)/63.5
	hasSnapped = False
	if ENABLE_SNAPPING is True:
		if parameter >= (MIXER_STEREO_SEP_SNAP_TO - SNAP_RANGE) and parameter <= (MIXER_STEREO_SEP_SNAP_TO + SNAP_RANGE):
			parameter = MIXER_STEREO_SEP_SNAP_TO
			hasSnapped = True
	mixer.setTrackStereoSeparation(selectedTrackNum, parameter)
	ret ="Mixer: Adjust " + getMixerTrackName(selectedTrackNum) + " stereo separation to "
	if parameter < 0: ret += str(-round(parameter * 100, 0)) + "% Separated"
	elif parameter > 0: ret += str(round(parameter * 100, 0)) + "% Merged"
	else: ret += "Original"

	if hasSnapped is True: ret += " [Snapped]"
	return ret

# Select mixer track given channel
def mixerTrackSelect(channelNum):
	mixer.deselectAll()
	mixer.selectTrack(channels.getTargetFxTrack(channelNum))

# Functions for channel rack

# Returns name of channel
def getChannelName(channelNum):
	return channels.getChannelName(channelNum)
	
def channelMidiNoteOn(channelNum, note, event):
	if channelNum < channels.channelCount():
		channels.midiNoteOn(channelNum, note, event.data2, -1)

def channelSelect(channelNum):
	if channelNum < channels.channelCount():
		channels.selectOneChannel(channelNum)
		
# Toggles solo on channel
def channelToggleSolo(selectedChannelNum):
	channels.soloChannel(selectedChannelNum)
	if(channels.isChannelSolo(selectedChannelNum) is 1): 
		return "Channel rack: Solo channel: " + getChannelName(selectedChannelNum)
	else: 
		return "Channel rack: Unsolo channel: " + getChannelName(selectedChannelNum)

# Toggles mute on channel
def channelToggleMute(selectedChannelNum):
	channels.muteChannel(selectedChannelNum)
	if(channels.isChannelMuted(selectedChannelNum) is 1): 
		return "Channel rack: Mute track: " + getChannelName(selectedChannelNum)
	else: 
		return "Channel rack: Unmute track: " + getChannelName(selectedChannelNum)

# Adjusts volume on channel
def channelAdjustVolume(selectedChannelNum, data):
	parameter = float(data)/127.0
	hasSnapped = False
	if(ENABLE_SNAPPING is True):
		if(parameter >= (CHANNEL_VOLUME_SNAP_TO - SNAP_RANGE) and parameter <= (CHANNEL_VOLUME_SNAP_TO + SNAP_RANGE)):
			parameter = CHANNEL_VOLUME_SNAP_TO
			hasSnapped = True
	channels.setChannelVolume(selectedChannelNum, parameter)
	ret = "Channel rack: Adjust " + getChannelName(selectedChannelNum) + " volume to " + str(round(parameter * 100, 0)) + "%"
	if(hasSnapped is True): 
		ret += " [Snapped]"
	return ret

# Adjusts panning on mixer track
def channelAdjustPan(selectedChannelNum, data):
	parameter = float(data - 63.5)/63.5
	hasSnapped = False
	if(ENABLE_SNAPPING is True):
		if(parameter >= (CHANNEL_PAN_SNAP_TO - SNAP_RANGE) and parameter <= (CHANNEL_PAN_SNAP_TO + SNAP_RANGE)):
			parameter = CHANNEL_PAN_SNAP_TO
			hasSnapped = True
	channels.setChannelPan(selectedChannelNum, parameter)
	ret ="Channel rack: Adjust " + getChannelName(selectedChannelNum) + " panning to "
	if(parameter < 0): 
		ret += str(-round(parameter * 100, 0)) + "% Left"
	elif(parameter > 0): 
		ret += str(round(parameter * 100, 0)) + "% Right"
	else: 
		ret += "Centred"

	if(hasSnapped is True): 
		ret += " [Snapped]"
	return ret
