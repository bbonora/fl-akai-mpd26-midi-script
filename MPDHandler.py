"""
IMPORTANT:
 All event handling goes in this file.
 Pretty much all of your tweaks and changes can go here.
"""


import time

import arrangement
import channels
import mixer
import general
import patterns
import playlist
import screen
import transport
import ui

import device
import launchMapPages
import midi
import utils

import helpers
from lib.MPD26 import MPD26

class MPDHandler(MPD26):

    port = None
    init_time = None
    last_pad_press_time = None
    last_stop_press_time = None
    button_map = 0
    rewind = 0
    fast_forward = 0
    output = ""
    mode_change_unlocked = True
    selected_track = mixer.trackNumber()
    selected_channel = channels.channelNumber()
    octave = 4

    """
    Initialization
    """
    def set_port_number(self):
        self.port = self.get_port_number()

    def set_init_time(self):
        self.init_time = self.get_timestamp()

    """
    External accessors
    """

    def get_port_number(self):
        return device.getPortNumber()

    def get_timestamp(self):
        return time.perf_counter()

    """
    Utility methods
    """

    def set_hint_message(self, message):
        if isinstance(message, str):
            ui.setHintMsg(message)
        else:
            print("self.setHintMessage error:\n  " +
                  "Param 'message' must be of type str.")

    def check_buffer(self, button, time_pressed):
        if button.type == 'transport' and self.last_stop_press_time:
            return time_pressed - self.last_stop_press_time > self.STOP_BUFFER
        elif button.type == 'pad' and self.last_pad_press_time:
            return time_pressed - self.last_pad_press_time > self.PAD_BUFFER
        else:
            print(button.type.upper() + " " +
                  str(button.number) + " has no associated buffer.")

    def check_for_mode_change_unlock(self, slider):
        if all(lock.value == slider.value for lock in [
            self.slider_1, self.slider_2, self.slider_3, self.slider_4
        ]):
            self.mode_change_unlocked = True
            self.set_hint_message("Button remapping mode")
            print("Button remapping mode UNLOCKED.")

    def check_for_remap(self, pad, event):
        """ Change the button mapping if certain conditions are met. """
        if self.mode_change_unlocked:
            if self.pad_d_13.held and self.pad_d_16.held:
                if pad == self.pad_d_1:
                    self.change_button_mapping(-1)
                    event.handled = True
                elif pad == self.pad_d_4:
                    self.change_button_mapping(1)
                    event.handled = True

    def change_button_mapping(self, map=1):
        """ Update the global button mapping mode id. """
        if isinstance(map, str):
            if map in self.INPUT_MODES:
                map = self.INPUT_MODES.index(map)
        self.button_map = (
            self.button_map + map
        ) % len(self.INPUT_MODES)
        self.set_hint_message(
            self.INPUT_MODES[self.button_map] + " mode".upper()
        )

        print("Remapped to " +
              self.INPUT_MODES[self.button_map].upper() + " mode.")

    """
    Input handlers
    """

    def handle_pad_press(self, event, pad):
        """ Put pad press code here.
        """
        # CHANNEL RACK OMNI MODE
        if pad.bank == 'a':
            helpers.channelMidiNoteOn((pad.number - 1), 60, event)
            helpers.channelSelect(pad.number - 1)
            event.handled = True

        # FPC MODE
        elif pad.bank == 'b':
            # Check if there is an FPC instance
            pad_note = self.pads_fpc_note_map[pad.number]
            event.data1 = pad_note
            event.handled = False

        # Chromatic Mode
        elif pad.bank == 'c':
            if pad.number == 15:
                if self.octave >= 0:
                    self.octave -= 1
                    self.output = 'Octave Shift: ' + str(self.octave)
                event.handled = True
            elif pad.number == 16:
                if self.octave <= 8:
                    self.octave += 1
                    self.output = 'Octave Shift: ' + str(self.octave)
                event.handled = True
            else:
                pad_note = self.pads_chromatic_note_map[pad.number]
                pad_note_shifted_on = (12 * self.octave) + (12 + pad_note)
                event.data1 = pad_note_shifted_on
                event.handled = False

        # Function Mode (use pads to control the ui functions)
        elif pad.bank == 'd':
            if pad.number == 1:
                # enter button
                transport.globalTransport(midi.FPT_Enter, 80, event.pmeFlags-1)
                self.output = 'Enter'

            elif pad.number == 2:
                # escape button
                transport.globalTransport(midi.FPT_Escape, 81, event.pmeFlags-1)
                self.output = 'Escape'

            elif pad.number == 3:
                # cut button
                transport.globalTransport(midi.FPT_Cut, 2, event.pmeFlags-1)
                self.output = 'Cut'
            
            elif pad.number == 4:

                # Edison is focused
                if ui.getFocusedPluginName() == 'Edison':
                    transport.globalTransport(midi.FPT_AddMarker, 33, event.pmeFlags-1)
                    self.output = 'Set Marker'

                # Default 
                else:
                    self.output = 'unasigned'

            elif pad.number == 5:
                # song/pattern
                transport.globalTransport(midi.FPT_Loop, 15, event.pmeFlags-1)
                self.output = 'Toggle: Song/Pattern'

            elif pad.number == 6:
                # metronome
                transport.globalTransport(midi.FPT_Metronome, 112, event.pmeFlags-1)
                self.output = 'Toggle: Metronome'

            elif pad.number == 7:
                # overdub
                transport.globalTransport(midi.FPT_Overdub, 112, event.pmeFlags-1)
                self.output = 'Toggle: Overdub'

            elif pad.number == 8:
                # loop record
                transport.globalTransport(midi.FPT_LoopRecord, 113, event.pmeFlags-1)
                self.output = 'Toggle: Loop Record'

            elif pad.number == 9:
                # open mixer
                ui.showWindow(midi.widMixer)
                ui.setFocused(midi.widMixer)
                self.output = 'Open: Mixer'

            elif pad.number == 10:
                # plugin picker
                transport.globalTransport(midi.FPT_F8, 67, event.pmeFlags-1)

            elif pad.number == 11:
                # Browser - there is a bug and this doesn't work
                ui.setFocused(midi.widBrowser)
                self.output = 'Open: File Browser'

            elif pad.number == 12:
                # down
                ui.down()
                self.output = 'Down'

            elif pad.number == 13:
                # playlist view
                transport.globalTransport(midi.FPT_F5, 64, event.pmeFlags-1)
                self.output = 'Open: Playlist'

            elif pad.number == 14:
                # open piano roll
                transport.globalTransport(midi.FPT_F7, 66, event.pmeFlags-1)
                self.output = 'Open: Piano Roll'

            elif pad.number == 15:
                # open channel rack
                # transport.globalTransport(midi.FPT_F6, 65, event.pmeFlags-1)
                ui.showWindow(midi.widChannelRack)
                ui.setFocused(midi.widChannelRack)
                self.output = 'Open: Channel Rack'

            elif pad.number == 16:
                # up button
                ui.up()
                self.output = 'Up'
            
            event.handled = True

        print("Pressed pad " + str(pad.number) + ".")
        self.set_hint_message(self.output)

    def handle_pad_release(self, event, pad):
        """ Put pad release code here.
        """
        # Omni Mode
        if pad.bank == 'a':
            pass

        # FPC MODE
        elif pad.bank == 'b':
            # Check if there is an FPC instance
            pad_note = self.pads_fpc_note_map[pad.number]
            event.data1 = pad_note
            event.handled = False
        
        # Chromatic Mode
        elif pad.bank == 'c':
            if pad.number <= 13:
                pad_note = self.pads_chromatic_note_map[pad.number]
                pad_note_shifted_off = (12 * self.octave) + (12 + pad_note)
                event.data1 = pad_note_shifted_off
                event.handled = False
            else:
                event.handled = True
        
        # Function Mode
        elif pad.bank == 'd':
            pass
        self.set_hint_message(self.output)
        print("Released pad " + str(pad.number) + ".")


    def handle_pad_pressure_change(self, event, pad, value):
        """ Put pad pressure change code here.
        """
        print("Changed pad " + str(pad.number) +
              " pressure to " + str(value) + ".")

        event.handled = True

    def handle_knob_change(self, event, knob, value):
        """ Put knob change code here.
        """

        self.selected_channel = channels.selectedChannel()
        # Mixer Focused
        if(ui.getFocused(midi.widMixer) is 1):
            if knob.number is not 1:
                offset = knob.number - 2
                trackNum = helpers.getMixerTrackNum()
                helpers.mixerAdjustPan(trackNum + offset, event.data2)
            else:
                helpers.mixerAdjustPan(0, event.data2)
        # Everything else
        else:
            if knob.number == 1:
                helpers.channelAdjustPan(self.selected_channel, event.data2)

            elif knob.number == 2:
                helpers.channelAdjustVolume(self.selected_channel, event.data2)
        print(event.isIncrement)
        print("Changed knob " + str(knob.number) + " to " + str(value) + ".")

        event.handled = True

    def handle_slider_change(self, event, slider, value):
        """ Put slider change code here.
        """
        # Sliders 2-6
        ui.showWindow(midi.widMixer)
        ui.setFocused(midi.widMixer)
        if slider.number is not 1:
            offset = slider.number - 2
            trackNum = helpers.getMixerTrackNum()
            helpers.mixerAdjustFader(trackNum + offset, event.data2)
        # Slider 1 always controls the master mixer volume
        else:
            helpers.mixerAdjustFader(0, event.data2)
        
        print("Changed slider " + str(slider.number) +
              " to " + str(value) + ".")

        #self.set_hint_message(self.output)
        event.handled = True

    def handle_backward_press(self, event, backward):
        """ Put backward press code here.
        """
        # Mixer Mode
        if ui.getFocused(0) is 1:
            ui.previous()
            self.output = "Mixer: Selected next track: " + helpers.getMixerTrackName(self.selected_track - 1)
           
        
        # Edison is focused
        elif ui.getFocusedPluginName() == "Edison":
            ui.jog(-1)
            self.output = "Jog Back"
        
        # Default Mode
        else:
            self.output = "Previous"
            ui.previous()

        self.set_hint_message(self.output)
        print("Pressed backward button.")
        
        event.handled = True

    def handle_forward_press(self, event, forward):
        """ Put forward press code here.
        """

        # Mixer Mode
        if ui.getFocused(0) is 1:
            ui.next()
            self.output = "Mixer: Selected next track: " + helpers.getMixerTrackName(self.selected_track + 1)
        
        # Edison is focused
        elif ui.getFocusedPluginName() == "Edison":
            ui.jog(1)
            self.output = "Jog Forward"
        
        # Default Mode
        else:
            self.output = "Next"
            ui.next()
            self.set_hint_message(self.output)

        print("Pressed forward button." + str(forward.on))

        event.handled = True
        
    def handle_stop_press(self, event, stop):
        """ Put stop press code here.
        """
        print(ui.getFocusedPluginName())
        transport.stop()
        self.output = "Transport: Stop"
        self.set_hint_message(self.output)
        print("Pressed stop button.")

        event.handled = True

    def handle_play_press(self, event, play):
        """ Put play press code here.
        """
        transport.start()
        if transport.isPlaying() is 1: 
            self.output = "Transport: Play"
        else: 
            self.output = "Transport: Paused at " + transport.getSongPosHint()
        self.set_hint_message(self.output)
        print("Pressed play button.")
       
        event.handled = True

    def handle_rec_press(self, event, rec):
        """ Put rec press code here.
        """
        # Mixer Mode
        if ui.getFocused(0) is 1:
            selectedTrack = mixer.trackNumber()
            mixer.armTrack(selectedTrack)
            self.output = "Mixer: Armed track: " + helpers.getMixerTrackName(selectedTrack)

        # Default Mode
        else:
            transport.record()
            if transport.isRecording() is 1:
                self.output = "Transport: Recording Enabled"
            else:
                self.output = "Transport: Recording Disabled"
        
        self.set_hint_message(self.output)
        print("Pressed rec button.")

        event.handled = True

    """
    Other event handlers
    """
    def handle_beat(self, value):
        """ Respond to beat indicators. Value is 1 at bar, 2 at beat, 0 at off.
        """
        pass