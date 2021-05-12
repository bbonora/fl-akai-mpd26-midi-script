from .MPD26Input import *

class MPD26:

    # bank a
    pad_a_1 = Pad(1, 'pad', 1, 'a')  # C3
    pad_a_2 = Pad(2, 'pad', 2, 'a')  # D3
    pad_a_3 = Pad(3, 'pad', 3, 'a')  # E3
    pad_a_4 = Pad(4, 'pad', 4, 'a')  # F3
    pad_a_5 = Pad(5, 'pad', 5, 'a')  # G3
    pad_a_6 = Pad(6, 'pad', 6, 'a')  # A3
    pad_a_7 = Pad(7, 'pad', 7, 'a')  # B3
    pad_a_8 = Pad(8, 'pad', 8, 'a')  # C4
    pad_a_9 = Pad(9, 'pad', 9, 'a')  # D4
    pad_a_10 = Pad(10, 'pad', 10, 'a')  # E4
    pad_a_11 = Pad(11, 'pad', 11, 'a')  # F4
    pad_a_12 = Pad(12, 'pad', 12, 'a')  # G4
    pad_a_13 = Pad(13, 'pad', 13, 'a')  # A4
    pad_a_14 = Pad(14, 'pad', 14, 'a')  # B4
    pad_a_15 = Pad(15, 'pad', 15, 'a')  # C5
    pad_a_16 = Pad(16, 'pad', 16, 'a')  # D5

    # bank b
    pad_b_1 = Pad(1, 'pad', 17, 'b')
    pad_b_2 = Pad(2, 'pad', 18,'b')
    pad_b_3 = Pad(3, 'pad', 19, 'b')
    pad_b_4 = Pad(4, 'pad', 20,'b')
    pad_b_5 = Pad(5, 'pad', 21, 'b')
    pad_b_6 = Pad(6, 'pad', 22, 'b')
    pad_b_7 = Pad(7, 'pad', 23, 'b')
    pad_b_8 = Pad(8, 'pad', 24, 'b')
    pad_b_9 = Pad(9, 'pad', 25, 'b')
    pad_b_10 = Pad(10, 'pad', 26, 'b')
    pad_b_11 = Pad(11, 'pad', 27, 'b')
    pad_b_12 = Pad(12, 'pad', 28, 'b')
    pad_b_13 = Pad(13, 'pad', 29, 'b')
    pad_b_14 = Pad(14, 'pad', 30, 'b')
    pad_b_15 = Pad(15, 'pad', 31, 'b')
    pad_b_16 = Pad(16, 'pad', 32, 'b')

    # bank c
    pad_c_1 = Pad(1, 'pad', 33, 'c')
    pad_c_2 = Pad(2, 'pad', 34,'c')
    pad_c_3 = Pad(3, 'pad', 35, 'c')
    pad_c_4 = Pad(4, 'pad', 36,'c')
    pad_c_5 = Pad(5, 'pad', 37, 'c')
    pad_c_6 = Pad(6, 'pad', 38, 'c')
    pad_c_7 = Pad(7, 'pad', 39, 'c')
    pad_c_8 = Pad(8, 'pad', 40, 'c')
    pad_c_9 = Pad(9, 'pad', 41, 'c')
    pad_c_10 = Pad(10, 'pad', 42, 'c')
    pad_c_11 = Pad(11, 'pad', 43, 'c')
    pad_c_12 = Pad(12, 'pad', 44, 'c')
    pad_c_13 = Pad(13, 'pad', 45, 'c')
    pad_c_14 = Pad(14, 'pad', 46, 'c')
    pad_c_15 = Pad(15, 'pad', 47, 'c')
    pad_c_16 = Pad(16, 'pad', 48, 'c')

    # bank d
    pad_d_1 = Pad(1, 'pad', 49, 'd')
    pad_d_2 = Pad(2, 'pad', 50,'d')
    pad_d_3 = Pad(3, 'pad', 51, 'd')
    pad_d_4 = Pad(4, 'pad', 52,'d')
    pad_d_5 = Pad(5, 'pad', 53, 'd')
    pad_d_6 = Pad(6, 'pad', 54, 'd')
    pad_d_7 = Pad(7, 'pad', 55, 'd')
    pad_d_8 = Pad(8, 'pad', 56, 'd')
    pad_d_9 = Pad(9, 'pad', 57, 'd')
    pad_d_10 = Pad(10, 'pad', 58, 'd')
    pad_d_11 = Pad(11, 'pad', 59, 'd')
    pad_d_12 = Pad(12, 'pad', 60, 'd')
    pad_d_13 = Pad(13, 'pad', 61, 'd')
    pad_d_14 = Pad(14, 'pad', 62, 'd')
    pad_d_15 = Pad(15, 'pad', 63, 'd')
    pad_d_16 = Pad(16, 'pad', 64, 'd')

    # knobs
    knob_1 = Knob(1, 'knob', 12)
    knob_2 = Knob(2, 'knob', 13)
    knob_3 = Knob(3, 'knob', 14)
    knob_4 = Knob(4, 'knob', 15)
    knob_5 = Knob(5, 'knob', 16)
    knob_6 = Knob(6, 'knob', 17)

    # faders
    slider_1 = Slider(1, 'slider', 20)
    slider_2 = Slider(2, 'slider', 21)
    slider_3 = Slider(3, 'slider', 22)
    slider_4 = Slider(4, 'slider', 23)
    slider_5 = Slider(5, 'slider', 24)
    slider_6 = Slider(6, 'slider', 25)
    
    # switches @todo: remove these
    switch_1 = Switch(1, 'switch', 28)
    switch_2 = Switch(2, 'switch', 29)
    switch_3 = Switch(3, 'switch', 30)
    switch_4 = Switch(4, 'switch', 31)

    #transport controls
    backward = Transport(1, 'transport', 115)
    forward = Transport(2, 'transport', 116)
    stop = Transport(3, 'transport', 117)
    play = Transport(4, 'transport', 118)
    rec = Transport(5, 'transport', 119)

    PAD_BUFFER = 0.1
    STOP_BUFFER = 2

    INPUT_MODES = ['default', 'ui', 'transport']
    MODE_CHANGE_UNLOCK_VALUE = 127

    def __init__(self):
        self.events = {
            153: 'Note On',
            144: 'Note On',
            137: 'Note Off',
            128: 'Note Off',  # custom preset value
            176: 'Control Change',
            185: 'Control Change',  # custom preset value
            169: 'Channel Aftertouch (Poly)',
            160: 'Channel Aftertouch (Poly)',  # custom preset value
            217: 'Channel Aftertouch (Channel)',
            208: 'Channel Aftertouch (Channel)'  # custom preset value
        }
        self.pads_by_id = {
            1: self.pad_a_1,
            2: self.pad_a_2,
            3: self.pad_a_3,
            4: self.pad_a_4,
            5: self.pad_a_5,
            6: self.pad_a_6,
            7: self.pad_a_7,
            8: self.pad_a_8,
            9: self.pad_a_9,
            10: self.pad_a_10,
            11: self.pad_a_11,
            12: self.pad_a_12,
            13: self.pad_a_13,
            14: self.pad_a_14,
            15: self.pad_a_15,
            16: self.pad_a_16,
            17: self.pad_b_1,
            18: self.pad_b_2,
            19: self.pad_b_3,
            20: self.pad_b_4,
            21: self.pad_b_5,
            22: self.pad_b_6,
            23: self.pad_b_7,
            24: self.pad_b_8,
            25: self.pad_b_9,
            26: self.pad_b_10,
            27: self.pad_b_11,
            28: self.pad_b_12,
            29: self.pad_b_13,
            30: self.pad_b_14,
            31: self.pad_b_15,
            32: self.pad_b_16,
            33: self.pad_c_1,
            34: self.pad_c_2,
            35: self.pad_c_3,
            36: self.pad_c_4,
            37: self.pad_c_5,
            38: self.pad_c_6,
            39: self.pad_c_7,
            40: self.pad_c_8,
            41: self.pad_c_9,
            42: self.pad_c_10,
            43: self.pad_c_11,
            44: self.pad_c_12,
            45: self.pad_c_13,
            46: self.pad_c_14,
            47: self.pad_c_15,
            48: self.pad_c_16,
            49: self.pad_d_1,
            50: self.pad_d_2,
            51: self.pad_d_3,
            52: self.pad_d_4,
            53: self.pad_d_5,
            54: self.pad_d_6,
            55: self.pad_d_7,
            56: self.pad_d_8,
            57: self.pad_d_9,
            58: self.pad_d_10,
            59: self.pad_d_11,
            60: self.pad_d_12,
            61: self.pad_d_13,
            62: self.pad_d_14,
            63: self.pad_d_15,
            64: self.pad_d_16
        }
        self.pads_omni_note_map = {
            1: 48,
            2: 50,
            3: 52,
            4: 53,
            5: 55,
            6: 57,
            7: 59,
            8: 60,
            9: 62,
            10: 64,
            11: 65,
            12: 67,
            13: 69,
            14: 71,
            15: 72,
            16: 74
        }
        self.pads_fpc_note_map = {
            1:37,
            2:36,
            3:42,
            4:54,
            5:40,
            6:38,
            7:46,
            8:44,
            9:48,
            10:47,
            11:45,
            12:43,
            13:49,
            14:55,
            15:51,
            16:53
        }
        self.pads_chromatic_note_map = {
            1:0,
            2:1,
            3:2,
            4:3,
            5:4,
            6:5,
            7:6,
            8:7,
            9:8,
            10:9,
            11:10,
            12:11,
            13:12,
            14:13
        }
        self.knobs_by_id = {
            12: self.knob_1,
            13: self.knob_2,
            14: self.knob_3,
            15: self.knob_4,
            16: self.knob_5,
            17: self.knob_6
        }
        self.sliders_by_id = {
            20: self.slider_1,
            21: self.slider_2,
            22: self.slider_3,
            23: self.slider_4,
            24: self.slider_5,
            25: self.slider_6
        }
        self.switches_by_id = {
            28: self.switch_1,
            29: self.switch_2,
            30: self.switch_3,
            31: self.switch_4
        }
        self.transports_by_id = {
            115: self.backward,
            116: self.forward,
            117: self.stop,
            118: self.play,
            119: self.rec
        }

    def get_pad(self, pad_id):
        try:
            return self.pads_by_id[pad_id]
        except KeyError:
            print("self.get_pad error:\n  No pad with id " + str(pad_id) + ".")

    def get_knob(self, knob_id):
        try:
            return self.knobs_by_id[knob_id]
        except KeyError:
            print("self.get_knob error:\n  No knob with id " + str(knob_id) + ".")

    def get_slider(self, slider_id):
        try:
            return self.sliders_by_id[slider_id]
        except KeyError:
            print("self.get_slider error:\n  No slider with id " + str(slider_id) + ".")

    def get_switch(self, switch_id):
        try:
            return self.switches_by_id[switch_id]
        except:
            print("self.get_switch error:\n  No switch with id " + str(switch_id) + ".")

    def get_transport(self, transport_id):
        try:
            return self.transports_by_id[transport_id]
        except:
            print("self.get_transport error:\n  No transport with id " + str(transport_id) + ".")