from os.path import sep

default_csv = 'HebrewReference.csv'

######################################################################
# Hebrew Language Reference
######################################################################
def readCSV(filename=default_csv, sep=','):
    d = {}
    try:
        fp = open(filename)
    except:
        print 'File',filename,'not found!'
        return {}
    
    codec = fp.readline()[:-1]
    for line in fp:
        s = line[:-1].split(sep,1)
        try:
            s[1].decode('ascii')
        except:
            s[1] = s[1].decode(codec)
        d[s[0]] = s[1].split(sep)

    fp.close()
    return d

class HebrewReference():
    # Class to use a Hebrew language reference
    def __init__(self):
        print 'Loading data from',default_csv
        # load data from pickle?
        self.__dict__.update(readCSV(default_csv, ','))        

        print 'Created HebrewReference instance at',id(self)
        repr(self)

    def __repr__(self):
        s = u''
        for i in zip(self.a_first, self.alephbet, self.a_final, self.a_name, self.a_english):
            s += u'{0:s} {1:s} {2:s}  {3:<10s} {4:s}\n'.format(*i)
        #print s
        # not sure how to return a string without breaking
        return 'HebrewReference('+','.join(self.__dict__.keys())+')'

    def lookup(self, field1='', field2='', s=''):
        # Helper function to find an entry s in field1 and return the corresponding entry in field2

        if type(s) not in (str, unicode): # Bad entry lookup
            raise TypeError
        elif (field1 not in dir(self)) or (field2 not in dir(self)): # Bad fields
            print 'HebrewReference class has fields:', self.__dict__.keys()
            raise KeyError
        elif len(self.__dict__[field1]) != len(self.__dict__[field2]):
            print 'These fields are not the same length!'
            raise KeyError

        # find the first match
        i = self.__dict__[field1].index(s)
        return self.__dict__[field2][i]

######################################################################
# Random Functions (temp)
# The following encodings support Hebrew
# cp424    , EBCDIC-CP-HE, IBM424
# cp856
# cp862    , 862, IBM862
# cp1255   , windows-1255
# iso8859_8, iso-8859-8, hebrew
# utf8, utf16 utf32
######################################################################

def specialCharacters(codec='cp1255'):
    print '\\x00: \x00  NULL'.decode(codec)
    print '\\x01: \x01  START OF HEADING'.decode(codec)
    print '\\x02: \x02  START OF TEXT'.decode(codec)
    print '\\x03: \x03  END OF TEXT'.decode(codec)
    print '\\x04: \x04  END OF TRANSMISSION'.decode(codec)
    print '\\x05: \x05  ENQUIRY'.decode(codec)
    print '\\x06: \x06  ACKNOWLEDGE'.decode(codec)
    print '\\x07: \x07  BELL'.decode(codec)
    print '\\x08: \x08  BACKSPACE'.decode(codec)
    print '\\x09: \x09  HORIZONTAL TABULATION'.decode(codec)
    print '\\x0A: \x0A  LINE FEED'.decode(codec)
    print '\\x0B: \x0B  VERTICAL TABULATION'.decode(codec)
    print '\\x0C: \x0C  FORM FEED'.decode(codec)
    print '\\x0D: \x0D  CARRIAGE RETURN'.decode(codec)
    print '\\x0E: \x0E  SHIFT OUT'.decode(codec)
    print '\\x0F: \x0F  SHIFT IN'.decode(codec)
    print '\\x10: \x10  DATA LINK ESCAPE'.decode(codec)
    print '\\x11: \x11  DEVICE CONTROL ONE'.decode(codec)
    print '\\x12: \x12  DEVICE CONTROL TWO'.decode(codec)
    print '\\x13: \x13  DEVICE CONTROL THREE'.decode(codec)
    print '\\x14: \x14  DEVICE CONTROL FOUR'.decode(codec)
    print '\\x15: \x15  NEGATIVE ACKNOWLEDGE'.decode(codec)
    print '\\x16: \x16  SYNCHRONOUS IDLE'.decode(codec)
    print '\\x17: \x17  END OF TRANSMISSION BLOCK'.decode(codec)
    print '\\x18: \x18  CANCEL'.decode(codec)
    print '\\x19: \x19  END OF MEDIUM'.decode(codec)
    print '\\x1A: \x1A  SUBSTITUTE'.decode(codec)
    print '\\x1B: \x1B  ESCAPE'.decode(codec)
    print '\\x1C: \x1C  FILE SEPARATOR'.decode(codec)
    print '\\x1D: \x1D  GROUP SEPARATOR'.decode(codec)
    print '\\x1E: \x1E  RECORD SEPARATOR'.decode(codec)
    print '\\x1F: \x1F  UNIT SEPARATOR'.decode(codec)
    print '\\x20: \x20  SPACE'.decode(codec)
    print '\\x21: \x21  EXCLAMATION MARK'.decode(codec)
    print '\\x22: \x22  QUOTATION MARK'.decode(codec)
    print '\\x23: \x23  NUMBER SIGN'.decode(codec)
    print '\\x24: \x24  DOLLAR SIGN'.decode(codec)
    print '\\x25: \x25  PERCENT SIGN'.decode(codec)
    print '\\x26: \x26  AMPERSAND'.decode(codec)
    print '\\x27: \x27  APOSTROPHE'.decode(codec)
    print '\\x28: \x28  LEFT PARENTHESIS'.decode(codec)
    print '\\x29: \x29  RIGHT PARENTHESIS'.decode(codec)
    print '\\x2A: \x2A  ASTERISK'.decode(codec)
    print '\\x2B: \x2B  PLUS SIGN'.decode(codec)
    print '\\x2C: \x2C  COMMA'.decode(codec)
    print '\\x2D: \x2D  HYPHEN-MINUS'.decode(codec)
    print '\\x2E: \x2E  FULL STOP'.decode(codec)
    print '\\x2F: \x2F  SOLIDUS'.decode(codec)
    print '\\x3A: \x3A  COLON'.decode(codec)
    print '\\x3B: \x3B  SEMICOLON'.decode(codec)
    print '\\x3C: \x3C  LESS-THAN SIGN'.decode(codec)
    print '\\x3D: \x3D  EQUALS SIGN'.decode(codec)
    print '\\x3E: \x3E  GREATER-THAN SIGN'.decode(codec)
    print '\\x3F: \x3F  QUESTION MARK'.decode(codec)
    print '\\x40: \x40  COMMERCIAL AT'.decode(codec)
    print '\\x5B: \x5B  LEFT SQUARE BRACKET'.decode(codec)
    print '\\x5C: \x5C  REVERSE SOLIDUS'.decode(codec)
    print '\\x5D: \x5D  RIGHT SQUARE BRACKET'.decode(codec)
    print '\\x5E: \x5E  CIRCUMFLEX ACCENT'.decode(codec)
    print '\\x5F: \x5F  LOW LINE'.decode(codec)
    print '\\x60: \x60  GRAVE ACCENT'.decode(codec)
    print '\\x7B: \x7B  LEFT CURLY BRACKET'.decode(codec)
    print '\\x7C: \x7C  VERTICAL LINE'.decode(codec)
    print '\\x7D: \x7D  RIGHT CURLY BRACKET'.decode(codec)
    print '\\x7E: \x7E  TILDE'.decode(codec)
    print '\\x7F: \x7F  DELETE'.decode(codec)
    print '\\x80: \x80  EURO SIGN'.decode(codec)
    print '\\x82: \x82  SINGLE LOW-9 QUOTATION MARK'.decode(codec)
    print '\\x83: \x83  LATIN SMALL LETTER F WITH HOOK'.decode(codec)
    print '\\x84: \x84  DOUBLE LOW-9 QUOTATION MARK'.decode(codec)
    print '\\x85: \x85  HORIZONTAL ELLIPSIS'.decode(codec)
    print '\\x86: \x86  DAGGER'.decode(codec)
    print '\\x87: \x87  DOUBLE DAGGER'.decode(codec)
    print '\\x88: \x88  MODIFIER LETTER CIRCUMFLEX ACCENT'.decode(codec)
    print '\\x89: \x89  PER MILLE SIGN'.decode(codec)
    print '\\x8B: \x8B  SINGLE LEFT-POINTING ANGLE QUOTATION MARK'.decode(codec)
    print '\\x91: \x91  LEFT SINGLE QUOTATION MARK'.decode(codec)
    print '\\x92: \x92  RIGHT SINGLE QUOTATION MARK'.decode(codec)
    print '\\x93: \x93  LEFT DOUBLE QUOTATION MARK'.decode(codec)
    print '\\x94: \x94  RIGHT DOUBLE QUOTATION MARK'.decode(codec)
    print '\\x95: \x95  BULLET'.decode(codec)
    print '\\x96: \x96  EN DASH'.decode(codec)
    print '\\x97: \x97  EM DASH'.decode(codec)
    print '\\x98: \x98  SMALL TILDE'.decode(codec)
    print '\\x99: \x99  TRADE MARK SIGN'.decode(codec)
    print '\\x9B: \x9B  SINGLE RIGHT-POINTING ANGLE QUOTATION MARK'.decode(codec)
    print '\\xA0: \xA0  NO-BREAK SPACE'.decode(codec)
    print '\\xA1: \xA1  INVERTED EXCLAMATION MARK'.decode(codec)
    print '\\xA2: \xA2  CENT SIGN'.decode(codec)
    print '\\xA3: \xA3  POUND SIGN'.decode(codec)
    print '\\xA4: \xA4  NEW SHEQEL SIGN'.decode(codec)
    print '\\xA5: \xA5  YEN SIGN'.decode(codec)
    print '\\xA6: \xA6  BROKEN BAR'.decode(codec)
    print '\\xA7: \xA7  SECTION SIGN'.decode(codec)
    print '\\xA8: \xA8  DIAERESIS'.decode(codec)
    print '\\xA9: \xA9  COPYRIGHT SIGN'.decode(codec)
    print '\\xAA: \xAA  MULTIPLICATION SIGN'.decode(codec)
    print '\\xAB: \xAB  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK'.decode(codec)
    print '\\xAC: \xAC  NOT SIGN'.decode(codec)
    print '\\xAD: \xAD  SOFT HYPHEN'.decode(codec)
    print '\\xAE: \xAE  REGISTERED SIGN'.decode(codec)
    print '\\xAF: \xAF  MACRON'.decode(codec)
    print '\\xB0: \xB0  DEGREE SIGN'.decode(codec)
    print '\\xB1: \xB1  PLUS-MINUS SIGN'.decode(codec)
    print '\\xB2: \xB2  SUPERSCRIPT TWO'.decode(codec)
    print '\\xB3: \xB3  SUPERSCRIPT THREE'.decode(codec)
    print '\\xB4: \xB4  ACUTE ACCENT'.decode(codec)
    print '\\xB5: \xB5  MICRO SIGN'.decode(codec)
    print '\\xB6: \xB6  PILCROW SIGN'.decode(codec)
    print '\\xB7: \xB7  MIDDLE DOT'.decode(codec)
    print '\\xB8: \xB8  CEDILLA'.decode(codec)
    print '\\xB9: \xB9  SUPERSCRIPT ONE'.decode(codec)
    print '\\xBA: \xBA  DIVISION SIGN'.decode(codec)
    print '\\xBB: \xBB  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK'.decode(codec)
    print '\\xBC: \xBC  VULGAR FRACTION ONE QUARTER'.decode(codec)
    print '\\xBD: \xBD  VULGAR FRACTION ONE HALF'.decode(codec)
    print '\\xBE: \xBE  VULGAR FRACTION THREE QUARTERS'.decode(codec)
    print '\\xBF: \xBF  INVERTED QUESTION MARK'.decode(codec)
    print '\\xC0: \xC0  HEBREW POINT SHEVA'.decode(codec)
    print '\\xC1: \xC1  HEBREW POINT HATAF SEGOL'.decode(codec)
    print '\\xC2: \xC2  HEBREW POINT HATAF PATAH'.decode(codec)
    print '\\xC3: \xC3  HEBREW POINT HATAF QAMATS'.decode(codec)
    print '\\xC4: \xC4  HEBREW POINT HIRIQ'.decode(codec)
    print '\\xC5: \xC5  HEBREW POINT TSERE'.decode(codec)
    print '\\xC6: \xC6  HEBREW POINT SEGOL'.decode(codec)
    print '\\xC7: \xC7  HEBREW POINT PATAH'.decode(codec)
    print '\\xC8: \xC8  HEBREW POINT QAMATS'.decode(codec)
    print '\\xC9: \xC9  HEBREW POINT HOLAM'.decode(codec)
    print '\\xCB: \xCB  HEBREW POINT QUBUTS'.decode(codec)
    print '\\xCC: \xCC  HEBREW POINT DAGESH OR MAPIQ'.decode(codec)
    print '\\xCD: \xCD  HEBREW POINT METEG'.decode(codec)
    print '\\xCE: \xCE  HEBREW PUNCTUATION MAQAF'.decode(codec)
    print '\\xCF: \xCF  HEBREW POINT RAFE'.decode(codec)
    print '\\xD0: \xD0  HEBREW PUNCTUATION PASEQ'.decode(codec)
    print '\\xD1: \xD1  HEBREW POINT SHIN DOT'.decode(codec)
    print '\\xD2: \xD2  HEBREW POINT SIN DOT'.decode(codec)
    print '\\xD3: \xD3  HEBREW PUNCTUATION SOF PASUQ'.decode(codec)
    print '\\xD4: \xD4  HEBREW LIGATURE YIDDISH DOUBLE VAV'.decode(codec)
    print '\\xD5: \xD5  HEBREW LIGATURE YIDDISH VAV YOD'.decode(codec)
    print '\\xD6: \xD6  HEBREW LIGATURE YIDDISH DOUBLE YOD'.decode(codec)
    print '\\xD7: \xD7  HEBREW PUNCTUATION GERESH'.decode(codec)
    print '\\xD8: \xD8  HEBREW PUNCTUATION GERSHAYIM'.decode(codec)
    print '\\xE0: \xE0  HEBREW LETTER ALEF'.decode(codec)
    print '\\xE1: \xE1  HEBREW LETTER BET'.decode(codec)
    print '\\xE2: \xE2  HEBREW LETTER GIMEL'.decode(codec)
    print '\\xE3: \xE3  HEBREW LETTER DALET'.decode(codec)
    print '\\xE4: \xE4  HEBREW LETTER HE'.decode(codec)
    print '\\xE5: \xE5  HEBREW LETTER VAV'.decode(codec)
    print '\\xE6: \xE6  HEBREW LETTER ZAYIN'.decode(codec)
    print '\\xE7: \xE7  HEBREW LETTER HET'.decode(codec)
    print '\\xE8: \xE8  HEBREW LETTER TET'.decode(codec)
    print '\\xE9: \xE9  HEBREW LETTER YOD'.decode(codec)
    print '\\xEA: \xEA  HEBREW LETTER FINAL KAF'.decode(codec)
    print '\\xEB: \xEB  HEBREW LETTER KAF'.decode(codec)
    print '\\xEC: \xEC  HEBREW LETTER LAMED'.decode(codec)
    print '\\xED: \xED  HEBREW LETTER FINAL MEM'.decode(codec)
    print '\\xEE: \xEE  HEBREW LETTER MEM'.decode(codec)
    print '\\xEF: \xEF  HEBREW LETTER FINAL NUN'.decode(codec)
    print '\\xF0: \xF0  HEBREW LETTER NUN'.decode(codec)
    print '\\xF1: \xF1  HEBREW LETTER SAMEKH'.decode(codec)
    print '\\xF2: \xF2  HEBREW LETTER AYIN'.decode(codec)
    print '\\xF3: \xF3  HEBREW LETTER FINAL PE'.decode(codec)
    print '\\xF4: \xF4  HEBREW LETTER PE'.decode(codec)
    print '\\xF5: \xF5  HEBREW LETTER FINAL TSADI'.decode(codec)
    print '\\xF6: \xF6  HEBREW LETTER TSADI'.decode(codec)
    print '\\xF7: \xF7  HEBREW LETTER QOF'.decode(codec)
    print '\\xF8: \xF8  HEBREW LETTER RESH'.decode(codec)
    print '\\xF9: \xF9  HEBREW LETTER SHIN'.decode(codec)
    print '\\xFA: \xFA  HEBREW LETTER TAV'.decode(codec)
    print '\\xFD: \xFD  LEFT-TO-RIGHT MARK'.decode(codec)
    print '\\xFE: \xFE  RIGHT-TO-LEFT MARK'.decode(codec)


def printRange(start, stop, codec='cp1255'):
    alephbet = ''
    for i in range(start, stop):
        try:
                alephbet += '  {0:3d}: {1}\n'.format(c*8+r, chr(c*8+r))
        except:
                alephbet += '  {0:3d}:  \n'.format(c*8+r)
    print alephbet.decode(codec)

######################################################################
if __name__ == '__main__':
    h = HebrewReference()
elif sep in __file__:
    # By default, use the *.csv file in this file's directory (may be
    # different from the current working directory)
    cwd = __file__.rsplit(sep,1)[0]+sep
    default_csv = cwd+'HebrewReference.csv'

