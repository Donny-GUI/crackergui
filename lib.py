
ASCII = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
SUPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïð "
DIGITS = "0123456789"
LCHARS = 'abcdefghijklmnopqrstuvwxyz'
UCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LUCHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
COMMON_SYMBOLS = "!@#$%&+_-.?"
symbol_sets = [
    'Upper Lower Alphabet', 
    'Upper Lower Alphabet and Digits 0-9', 
    'Lower Alphabet digits 0-9', 
    'Upper Alphabet digits 0-9', 
    'All Ascii Characters'
    ]
digits_and_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
digits_and_lower = "0123456789abcdefghijklmnopqrstuvwxyz"
digits_upper_and_lower = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
base_character_set = {
    'ascii': ASCII, 
    'lower characters': LCHARS, 
    'upper characters':UCHARS, 
    'upper and lower alphabet':LUCHARS,
    'digits and upper':digits_and_upper,
    'digits and lower':digits_and_lower,
    'digits with upper and lower': digits_upper_and_lower,
    'custom': 'CUSTOM'}
character_set_names = list(base_character_set.keys())
character_sets = list(base_character_set.values())
