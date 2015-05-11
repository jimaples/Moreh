# Run this in Python 3.3 for the unicode to work correctly
codec = 'utf-8'

fp = open('HebrewReference.csv','wb')

fp.write(codec.encode(codec)+b'\n')
#fp.write(csv([codec], 'codec'))

def csv(values=[], prefix=''):
    if prefix:
        prefix += ','
    prefix += ','.join(values)+'\n'
    return prefix.encode(codec)
    
######################################################################
alephbet = 'א,ב,ג,ד,ה,ו,ז,ח,ט,י,כ,ל,מ,נ,ס,ע,פ,צ,ק,ר,ש,ת'.split(',')
a_first  = 'א,בּ,גּ,דּ,ה,ו,ז,ח,ט,י,כּ,ל,מ,נ,ס,ע,פּ,צ,ק,ר,ש,תּ'.split(',')
a_final  = 'א,ב,ג,ד,ה,ו,ז,ח,ט,י,ך,ל,ם,ן,ס,ע,ף,ץ,ק,ר,ש,ת'.split(',')
a_name   = ('Aleph','Bet','Gimel','Dalet','Hey','Vav','Zayin','Chet','Tet','Yod','Kaf','Lamed','Mem',
            'Nun','Samech','Ayin','Peh','Tsadi','Kof','Resh','Shin','Tav')
#a_speak  = (u'\u00e1h-leph','beth',u'g\u00e9e-mel',u'd\u00e1h-leth','heh','vahv',u'z\u00e1h-yin',u'\u1e25eth','teht','yodh','kahf',u'l\u00e1h-med','mem',
#            'nun',u's\u00e1h-mekh',u'\u00e1h-yin','peh',u'ts\u00e1h-dee','kofh','rehsh','seen','taw')
a_english = ('›','b','g','d','h','v','z','h','t','y','k','l','m','n','s','‹','p','s','q','r','s','t')

fp.write(csv(alephbet,  'alephbet'))
fp.write(csv(a_first,   'a_first'))
fp.write(csv(a_final,   'a_final'))
fp.write(csv(a_name,    'a_name'))
fp.write(csv(a_english, 'a_english'))

######################################################################
vowels = 'בבַבֶבִבֻבָבֵבֵיבִיבוֿבוּ'
v_names = ('Patah','Seghol','Hiriq Qatan','Qubbus',
           'Qamats','Sereh','Sereh','Hiriq Gadol','Holam','Shuruq')
v_translit = ('a','e','i','u',
              'a','e','e','i','o','o','u')
v_word = ('card','pen','sit','pull',
          'card','prey','prey','marine','lore','lore','flute')

# Remove Bet to make vowels generic
def addO(s=b''):
    return b'\xd7\x91'+s
    # The '◌' character doesn't display correctly with the markings
    if b'\xd7\x95' in s:
        return s+'◌'.encode(codec)
    else:
        return s
    
vowels_en = tuple([ addO(s).decode(codec) for s in bytes(vowels.encode(codec)).split(b'\xd7\x91') if s ])

print('\nHebrew Vowels: ',vowels)
for i in zip(v_names, vowels_en, v_translit, v_word):
    #print('  {0:13s}{1:>3s}  {3:s} as in {4:7s} {2:s}'.format(i[0], i[1].decode(codec), i[1], i[2], i[3]))
    print('  {0:13s}{1:>3s}  {3:s} as in {4:7s} {2:s}'.format(i[0], i[1], i[1].encode(codec), i[2], i[3]))

fp.write(csv(vowels_en,  'vowels'))
fp.write(csv(v_names,    'v_names'))
fp.write(csv(v_translit, 'v_english'))
fp.write(csv(v_word,     'v_word'))
fp.write(csv(v_names,    'v_names'))

######################################################################

# TODO
# Add example words for transliteration... h as in hair
# See p19 for similar letters

fp.close()
