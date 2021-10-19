# name=Akai MPD26
# author=Ben Bonora
# version=1.0


from MPDHandler import MPDHandler

class DeviceInstance(MPDHandler):

    def OnInit(self):
        self.set_port_number()
        self.set_init_time()
        self.last_pad_press_time = self.init_time
        self.last_transport_press_time = self.init_time
        print("Initialized MPD26 on port " + str(self.port) + ".")

    def OnMidiMsg(self, event):
        event.handled = False
        self.delegate_event(event)

    def OnDeInit(self):
        pass

    def OnMidiIn(self, event):
        pass

    def OnMidiOutMsg(self, event):
        pass

    def OnIdle(self):
        pass

    def OnRefresh(self, flags):
        pass

    def OnUpdateBeatIndicator(self, value):
        self.handle_beat(value)

    def delegate_event(self, event):
        status = event.status
        try:
            if self.events[status] == "Note On":
                self.delegate_note_on(event)
            elif self.events[status] == "Note Off":
                self.delegate_note_off(event)
            elif self.events[status] == "Control Change":
                self.delegate_control_change(event)
            elif self.events[status] == "Channel Aftertouch (Poly)":
                self.delegate_channel_aftertouch(event)
            elif self.events[status] == "Channel Aftertouch (Channel)":
                print("IMPORTANT: Change pad channel "
                      "aftertouch settings to poly.")
                event.handled = True
            else:
                print("Event status " + status + " not found in self.events.")
                event.handled = True
        except KeyError:
            print("self.delegate_event error:\n  "
                  "Event status {status} does not exist.")

    def delegate_note_on(self, event):
        pad = self.get_pad(event.controlNum)
        if pad:
            self.handle_pad_press(event, pad)

    def delegate_note_off(self, event):
        pad = self.get_pad(event.controlNum)
        if pad:
            self.handle_pad_release(event, pad)
            

    def delegate_channel_aftertouch(self, event):
        pad = self.get_pad(event.controlNum)
        if pad:
            self.handle_pad_pressure_change(event, pad, event.controlVal)
            if pad.bank == 'c':
                event.handled = False
            else:
                event.handled = True
            

    def delegate_control_change(self, event):
        id = event.controlNum
        if any([knob.id == id for knob in [
            self.knob_1, 
            self.knob_2, 
            # self.knob_3, 
            # self.knob_4,
            # self.knob_5,
            # self.knob_6
        ]]):
            knob = self.get_knob(id)
            self.handle_knob_change(event, knob, event.controlVal)
        elif any([slider.id == id for slider in [
            self.slider_1, 
            self.slider_2, 
            self.slider_3, 
            self.slider_4,
            self.slider_5,
            self.slider_6
        ]]):
            slider = self.get_slider(id)
            slider.value = event.controlVal
            if slider.value == self.MODE_CHANGE_UNLOCK_VALUE:
                self.check_for_mode_change_unlock(slider)
            else:
                if self.mode_change_unlocked:
                    self.set_hint_message("Button remapping mode locked")
                    print("Button remapping mode LOCKED.")
                self.mode_change_unlocked = False
            self.handle_slider_change(event, slider, event.controlVal)
        elif any([switch.id == id for switch in [
            self.switch_1, self.switch_2, self.switch_3, self.switch_4
        ]]):
            switch = self.get_switch(id)
            switch.on = not switch.on
            self.handle_switch_press(event, switch)
        elif any([transport.id == id for transport in [
            self.backward,
            self.forward,
            self.stop, 
            self.play, 
            self.rec
        ]]):
            self.delegate_transport_press(event, self.get_transport(id))
        else:
            print("Input not found for event.controlNum " + str(id) + ".")
            event.handled = True

    def delegate_transport_press(self, event, transport):
        if transport.number == 1:
            self.backward.on = not self.backward.on
            self.handle_backward_press(event, transport)
        elif transport.number == 2:
            self.forward.on = not self.forward.on
            self.handle_forward_press(event, transport)
        elif transport.number == 3:
            self.stop.on = not self.stop.on
            self.handle_stop_press(event, transport)
        elif transport.number == 4:
            self.play.on = not self.play.on
            self.handle_play_press(event, transport)
        elif transport.number == 5:
            self.rec.on = not self.rec.on
            self.handle_rec_press(event, transport)
        else:
            event.handled = True


mpd_device = DeviceInstance()

class NRPN_Message:
    id = 0
    id_set = 0
    value = 0

    def appendId(self, event):
        
        self.id =+ (event.data2 << 7)

    def appendValue(self, event):
        pass
    
    def OnNRPN(event):
        pass



def OnInit():
    mpd_device.OnInit()


def OnDeInit():
    pass


def OnMidiIn(event):
    pass


def OnMidiOutMsg(event):
    pass

def OnMidiMsg(event):
     mpd_device.OnMidiMsg(event)

def OnControlChange(event):
    if event.data1 == 0x63:
        print("Non-Registered Parameter Number MSB")


    elif event.data1 == 0x62:
        print("Non-Registered Parameter Number LSB")


    elif event.data1 == 0x06:
        print("IS NRPN: MSB")
    elif 0x20 <= event.data1 <= 0x3F:
        print("IS NRPN: LSB")

def OnIdle():
    pass


def OnRefresh(flags):
    pass


def OnUpdateBeatIndicator(value):
    mpd_device.OnUpdateBeatIndicator(value)
