import ssdeep


class SSDEEPByteAnalyser:

    def __init__(self):
        self.first_string = None
        self.second_string = None
        self.threshold = 5
        self.comparison_data = list()
        self.defined_data = list()
        self.undefined_data = list()

    def get_comparison_data(self):
        return self.comparison_data

    def get_defined_data(self):
        return self.defined_data

    def get_undefined_data(self):
        return self.undefined_data

    @staticmethod
    def to_byte_array(any_str):
        en_str = list()
        i = 0
        while i != len(any_str):
            en_str.append(ord(any_str[i]))
            i += 1
        byte_str = " ".join(str(x) for x in en_str)
        return byte_str

    def compare_bytes(self, byte_str1, byte_str2):
        print(byte_str1)
        print(byte_str2)
        self.first_string = ssdeep.hash(byte_str1)
        print(self.first_string)
        # '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'
        self.second_string = ssdeep.hash(byte_str2)
        print(self.second_string)
        # '3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C'
        return ssdeep.compare(self.first_string, self.second_string)

    def send_forward(self, signatory_index, threshold):
        if threshold > self.threshold:
            self.undefined_data = self.comparison_data[signatory_index]
        else:
            self.defined_data = self.comparison_data[signatory_index]


str1 = 'Also called fuzzy hashes, Ctph can match inputs that have homologies.'
str2 = 'Also called fuzzy hashes, CTPH can match inputs that have homologies.'

ssdeep_an1 = SSDEEPByteAnalyser()

byte_str1 = SSDEEPByteAnalyser.to_byte_array(str1)
byte_str2 = SSDEEPByteAnalyser.to_byte_array(str2)

i = 0
while len(ssdeep_an1.get_comparison_data()):
    ssdeep_an1.send_forward(i, ssdeep_an1.compare_bytes(byte_str1, byte_str2))
    i += 1






