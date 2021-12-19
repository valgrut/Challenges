#! /usr/bin/env python3

# https://www.youtube.com/watch?v=ybkkiGtJmkM

wheel_1_tooth = 0 #turn every char
wheel_1_wiring = [
        (1, 9),
        (2, 18),
        (3, 8),
        (4, 17),
        (5, 3),
        (6, 22),
        (7, 11),
        (8, 23),
        (9, 19),
        (10, 4),
        (11, 10),
        (12, 16),
        (13, 21),
        (14, 5),
        (15, 20),
        (16, 1),
        (17, 26),
        (18, 12),
        (19, 25),
        (20, 7),
        (21, 14),
        (22, 15),
        (23, 2),
        (24, 6),
        (25, 24),
        (26, 13)
        ]

wheel_2_tooth = 8
wheel_2_wiring = [
        (1, 18),
        (2, 5),
        (3, 17),
        (4, 16),
        (5, 12),
        (6, 22),
        (7, 26),
        (8, 13),
        (9, 21),
        (10, 2),
        (11, 20),
        (12, 6),
        (13, 1),
        (14, 19),
        (15, 7),
        (16, 10),
        (17, 11),
        (18, 14),
        (19, 3),
        (20, 25),
        (21, 15),
        (22, 4),
        (23, 24),
        (24, 8),
        (25, 23),
        (26, 9)
        ]

wheel_3_tooth = 21
wheel_3_wiring = [
        (1, 9),
        (2, 10),
        (3, 11),
        (4, 19),
        (5, 4),
        (6, 20),
        (7, 21),
        (8, 1),
        (9, 18),
        (10, 7),
        (11, 8),
        (12, 17),
        (13, 16),
        (14, 26),
        (15, 12),
        (16, 5),
        (17, 13),
        (18, 25),
        (19, 22),
        (20, 3),
        (21, 23),
        (22, 6),
        (23, 24),
        (24, 14),
        (25, 2),
        (26, 15)
        ]

wheel_reflector_wiring = [
        (1, 11),
        (2, 4),
        (3, 10),
        (4, 9),
        (5, 5),
        (6, 26),
        (7, 15),
        (8, 16),
        (9, 1),
        (10, 22),
        (11, 23),
        (12, 21),
        (13, 25),
        (14, 6),
        (15, 12),
        (16, 24),
        (17, 7),
        (18, 20),
        (19, 18),
        (20, 13),
        (21, 17),
        (22, 2),
        (23, 14),
        (24, 3),
        (25, 19),
        (26, 8)
        ]

class Wheel:
    def __init__(self, wheel_wiring, wheel_tooth, initial_shift):
        self.wiring = wheel_wiring
        if wheel_tooth > 26 or wheel_tooth < 0:
            print("Error: Tooth must be placed value between 1 and 26. Or on 0, which means it will turn every click.")
            return -5
        self.tooth = wheel_tooth
        if initial_shift > 26 or initial_shift < 0:
            print("Error: Shift must be between 0 and 26")
            return -5
        self.init_shift = initial_shift
        
        self.current_shift = self.init_shift
        self.used_counter = 0


    def encode_input_char(self, in_char):
        self.used_counter += 1           
        int_char = ord(in_char.lower()) - 96
        # print("check:", in_char, "->", int_char)

        # get char according to setup and current shift
        shifted_index = self.current_shift 
        # shifted_index = (int_char - 1) + self.current_shift 
        wired = self.wiring[shifted_index][1]
        # print(wire)
        # print("initial shift and current shift", self.init_shift, self.current_shift)

        self.move_wheel()
        return chr(wired + 96).upper()
        # return wired


    def move_wheel(self):
        # move wheel after each encoded char.
        if self.tooth == 0:
            self.current_shift = (self.current_shift + 1) % 26
        else:
            if self.used_counter == self.tooth:
                self.used_counter = 0
                self.current_shift = (self.current_shift + 1) % 26

 
class Reflector:
    def __init__(self, reflector_wiring):
        self.wiring = reflector_wiring

    def encode_input_char(self, in_char):
        int_char = ord(in_char.lower()) - 96
        wired = self.wiring[int_char - 1][1]
        return chr(wired + 96).upper()


 
class Plugboard:
    def __init__(self, plugboard):
        self.plugboard = plugboard

    def process_input(self, inp):
        for plug in self.plugboard:
            if inp.upper() == plug[0].upper():
                return plug[1].lower()
        return inp.lower()


class Enigma:
    def __init__(self, wheel1, wheel2, wheel3, reflector, plugboard):
        self.wheel1 = wheel1
        self.wheel2 = wheel2
        self.wheel3 = wheel3
        self.reflector = reflector
        self.plugboard = plugboard

    def encode_char(self, char):
        char = char.lower()
        plugged = self.plugboard.process_input(char)
        enc1 = self.wheel1.encode_input_char(plugged)
        enc2 = self.wheel2.encode_input_char(enc1)
        enc3 = self.wheel3.encode_input_char(enc2)
        ref = self.reflector.encode_input_char(enc3)
        aenc3 = self.wheel3.encode_input_char(ref)
        aenc2 = self.wheel2.encode_input_char(aenc3)
        aenc1 = self.wheel1.encode_input_char(aenc2)
        aplugged = self.plugboard.process_input(aenc1)
        return aplugged

    def encode_string(self, string):
        encripted = ""
        for c in string:
            encripted += self.encode_char(c)
        
        return encripted


# 1=A, 2=B, 3=C, ...
# 1. Battery
# 2. Key Switch
# 3. Plugboard
# 4. Rotors
# 5. Plugboard
# 6. Key Switch
# 7. Light Bulb
# 8. Battery

if __name__ == "__main__":
    print("This is Enigma.")
    wheel_1_offset = 0
    wheel_2_offset = 13
    wheel_3_offset = 24
    wheel1 = Wheel(wheel_1_wiring, wheel_1_tooth, wheel_1_offset)
    wheel2 = Wheel(wheel_2_wiring, wheel_2_tooth, wheel_2_offset)
    wheel3 = Wheel(wheel_3_wiring, wheel_3_tooth, wheel_3_offset)
    reflector = Reflector(wheel_reflector_wiring)

    plugboard_setting = [('A', 'G'), ('F', 'Y')]
    plugboard = Plugboard(plugboard_setting)
    
    enigma = Enigma(wheel1, wheel2, wheel3, reflector, plugboard)
    
    encripted = enigma.encode_string("hello")
    print(encripted)

    decripted = enigma.encode_string(encripted)
    print(decripted)
