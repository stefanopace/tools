#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Unicode printer')

parser.add_argument('-c', '--category',
                    dest='category',
                    metavar='<category name>',
                    type=str, nargs=1, default='',
                    help='the category of characters to print')

parser.add_argument('-n', '--names',
                    dest='names',
                    action='store_true',
                    help='print all category names')

args = parser.parse_args()
category = args.category[0] if args.category else ''
print_names = args.names or False

row_len = 20

categories = [
	{"name":"Latin-1 Supplement", "range":(0x00A0, 0x00FF)},
	{"name":"Gurmukhi", "range":(0x0A00, 0x0A7F)},
	{"name":"Gujarati", "range":(0x0A80, 0x0AFF)},
	{"name":"Oriya", "range":(0x0B00, 0x0B7F)},
	{"name":"Tamil", "range":(0x0B80, 0x0BFF)},
	{"name":"Telugu", "range":(0x0C00, 0x0C7F)},
	{"name":"Kannada", "range":(0x0C80, 0x0CFF)},
	{"name":"Malayalam", "range":(0x0D00, 0x0D7F)},
	{"name":"Sinhala", "range":(0x0D80, 0x0DFF)},
	{"name":"Thai", "range":(0x0E00, 0x0E7F)},
	{"name":"Lao", "range":(0x0E80, 0x0EFF)},
	{"name":"Tibetan", "range":(0x0F00, 0x0FFF)},
	{"name":"Yi Syllables", "range":(0xA000, 0xA48F)},
	{"name":"Yi Radicals", "range":(0xA490, 0xA4CF)},
	{"name":"Hangul Syllables", "range":(0xAC00, 0xD7AF)},
	# {"name":"High Surrogates", "range":(0xD800, 0xDB7F)},
	# {"name":"High Private Use Surrogates", "range":(0xDB80, 0xDBFF)},
	# {"name":"Low Surrogates", "range":(0xDC00, 0xDFFF)},
	{"name":"Private Use Area", "range":(0xE000, 0xF8FF)},
	{"name":"CJK Compatibility Ideographs", "range":(0xF900, 0xFAFF)},
	{"name":"Alphabetic Presentation Forms", "range":(0xFB00, 0xFB4F)},
	{"name":"Arabic Presentation Forms-A", "range":(0xFB50, 0xFDFF)},
	{"name":"Variation Selectors", "range":(0xFE00, 0xFE0F)},
	{"name":"Combining Half Marks", "range":(0xFE20, 0xFE2F)},
	{"name":"CJK Compatibility Forms", "range":(0xFE30, 0xFE4F)},
	{"name":"Small Form Variants", "range":(0xFE50, 0xFE6F)},
	{"name":"Arabic Presentation Forms-B", "range":(0xFE70, 0xFEFF)},
	{"name":"Halfwidth and Fullwidth Forms", "range":(0xFF00, 0xFFEF)},
	{"name":"Specials", "range":(0xFFF0, 0xFFFF)},
	{"name":"Byzantine Musical Symbols", "range":(0x1D000, 0x1D0FF)},
	{"name":"Phonetic Extensions", "range":(0x1D00, 0x1D7F)},
	{"name":"Musical Symbols", "range":(0x1D100, 0x1D1FF)},
	{"name":"Tai Xuan Jing Symbols", "range":(0x1D300, 0x1D35F)},
	{"name":"Mathematical Alphanumeric Symbols", "range":(0x1D400, 0x1D7FF)},
	{"name":"Latin Extended Additional", "range":(0x1E00, 0x1EFF)},
	{"name":"Greek Extended", "range":(0x1F00, 0x1FFF)},
	{"name":"Spacing Modifier Letters", "range":(0x02B0, 0x02FF)},
	{"name":"Supplemental Mathematical Operators", "range":(0x2A00, 0x2AFF)},
	{"name":"Miscellaneous Symbols and Arrows", "range":(0x2B00, 0x2BFF)},
	{"name":"CJK Radicals Supplement", "range":(0x2E80, 0x2EFF)},
	{"name":"Kangxi Radicals", "range":(0x2F00, 0x2FDF)},
	{"name":"CJK Compatibility Ideographs Supplement", "range":(0x2F800, 0x2FA1F)},
	{"name":"Ideographic Description Characters", "range":(0x2FF0, 0x2FFF)},
	{"name":"Yijing Hexagram Symbols", "range":(0x4DC0, 0x4DFF)},
	{"name":"CJK Unified Ideographs", "range":(0x4E00, 0x9FFF)},
	{"name":"Georgian", "range":(0x10A0, 0x10FF)},
	{"name":"Cherokee", "range":(0x13A0, 0x13FF)},
	{"name":"Runic", "range":(0x16A0, 0x16FF)},
	{"name":"Khmer Symbols", "range":(0x19E0, 0x19FF)},
	{"name":"Basic Latin", "range":(0x0020, 0x007F)},
	{"name":"Currency Symbols", "range":(0x20A0, 0x20CF)},
	{"name":"Combining Diacritical Marks for Symbols", "range":(0x20D0, 0x20FF)},
	{"name":"Geometric Shapes", "range":(0x25A0, 0x25FF)},
	{"name":"Miscellaneous Mathematical Symbols-A", "range":(0x27C0, 0x27EF)},
	{"name":"Supplemental Arrows-A", "range":(0x27F0, 0x27FF)},
	{"name":"Katakana", "range":(0x30A0, 0x30FF)},
	{"name":"Bopomofo Extended", "range":(0x31A0, 0x31BF)},
	{"name":"Katakana Phonetic Extensions", "range":(0x31F0, 0x31FF)},
	{"name":"Latin Extended-A", "range":(0x0100, 0x017F)},
	{"name":"Latin Extended-B", "range":(0x0180, 0x024F)},
	{"name":"IPA Extensions", "range":(0x0250, 0x02AF)},
	{"name":"Combining Diacritical Marks", "range":(0x0300, 0x036F)},
	{"name":"Greek and Coptic", "range":(0x0370, 0x03FF)},
	{"name":"Cyrillic", "range":(0x0400, 0x04FF)},
	{"name":"Cyrillic Supplementary", "range":(0x0500, 0x052F)},
	{"name":"Armenian", "range":(0x0530, 0x058F)},
	{"name":"Hebrew", "range":(0x0590, 0x05FF)},
	{"name":"Arabic", "range":(0x0600, 0x06FF)},
	{"name":"Syriac", "range":(0x0700, 0x074F)},
	{"name":"Thaana", "range":(0x0780, 0x07BF)},
	{"name":"Devanagari", "range":(0x0900, 0x097F)},
	{"name":"Bengali", "range":(0x0980, 0x09FF)},
	{"name":"Myanmar", "range":(0x1000, 0x109F)},
	{"name":"Hangul Jamo", "range":(0x1100, 0x11FF)},
	{"name":"Ethiopic", "range":(0x1200, 0x137F)},
	{"name":"Unified Canadian Aboriginal Syllabics", "range":(0x1400, 0x167F)},
	{"name":"Ogham", "range":(0x1680, 0x169F)},
	{"name":"Tagalog", "range":(0x1700, 0x171F)},
	{"name":"Hanunoo", "range":(0x1720, 0x173F)},
	{"name":"Buhid", "range":(0x1740, 0x175F)},
	{"name":"Tagbanwa", "range":(0x1760, 0x177F)},
	{"name":"Khmer", "range":(0x1780, 0x17FF)},
	{"name":"Mongolian", "range":(0x1800, 0x18AF)},
	{"name":"Limbu", "range":(0x1900, 0x194F)},
	{"name":"Tai Le", "range":(0x1950, 0x197F)},
	{"name":"General Punctuation", "range":(0x2000, 0x206F)},
	{"name":"Superscripts and Subscripts", "range":(0x2070, 0x209F)},
	{"name":"Letterlike Symbols", "range":(0x2100, 0x214F)},
	{"name":"Number Forms", "range":(0x2150, 0x218F)},
	{"name":"Arrows", "range":(0x2190, 0x21FF)},
	{"name":"Mathematical Operators", "range":(0x2200, 0x22FF)},
	{"name":"Miscellaneous Technical", "range":(0x2300, 0x23FF)},
	{"name":"Control Pictures", "range":(0x2400, 0x243F)},
	{"name":"Optical Character Recognition", "range":(0x2440, 0x245F)},
	{"name":"Enclosed Alphanumerics", "range":(0x2460, 0x24FF)},
	{"name":"Box Drawing", "range":(0x2500, 0x257F)},
	{"name":"Block Elements", "range":(0x2580, 0x259F)},
	{"name":"Miscellaneous Symbols", "range":(0x2600, 0x26FF)},
	{"name":"Dingbats", "range":(0x2700, 0x27BF)},
	{"name":"Braille Patterns", "range":(0x2800, 0x28FF)},
	{"name":"Supplemental Arrows-B", "range":(0x2900, 0x297F)},
	{"name":"Miscellaneous Mathematical Symbols-B", "range":(0x2980, 0x29FF)},
	{"name":"CJK Symbols and Punctuation", "range":(0x3000, 0x303F)},
	{"name":"Hiragana", "range":(0x3040, 0x309F)},
	{"name":"Bopomofo", "range":(0x3100, 0x312F)},
	{"name":"Hangul Compatibility Jamo", "range":(0x3130, 0x318F)},
	{"name":"Kanbun", "range":(0x3190, 0x319F)},
	{"name":"Enclosed CJK Letters and Months", "range":(0x3200, 0x32FF)},
	{"name":"CJK Compatibility", "range":(0x3300, 0x33FF)},
	{"name":"CJK Unified Ideographs Extension A", "range":(0x3400, 0x4DBF)},
	{"name":"Linear B Syllabary", "range":(0x10000, 0x1007F)},
	{"name":"Linear B Ideograms", "range":(0x10080, 0x100FF)},
	{"name":"Aegean Numbers", "range":(0x10100, 0x1013F)},
	{"name":"Old Italic", "range":(0x10300, 0x1032F)},
	{"name":"Gothic", "range":(0x10330, 0x1034F)},
	{"name":"Ugaritic", "range":(0x10380, 0x1039F)},
	{"name":"Deseret", "range":(0x10400, 0x1044F)},
	{"name":"Shavian", "range":(0x10450, 0x1047F)},
	{"name":"Osmanya", "range":(0x10480, 0x104AF)},
	{"name":"Cypriot Syllabary", "range":(0x10800, 0x1083F)},
	{"name":"CJK Unified Ideographs Extension B", "range":(0x20000, 0x2A6DF)},
]

categories.sort(key=(lambda el: el["range"][0]))

def print_unicode_range(start, end):
	i = 0
	for u in range(start, end + 1):
		i, end = (0, "\n\n") if i == row_len - 1 else (i + 1, ' ')
		print(chr(u), end=end)
	print()

def print_category_names():
	print("\n".join([category["name"] for category in categories]))

def print_category(name):
	category = [category for category in categories if category["name"] == name]
	if not category:
		print(f"Categoria inesistente: {name}")
		exit(1)
	
	(start, end) = category[0]["range"]
	print(name + ":", end="\n\n")
	print_unicode_range(start, end)


if print_names:
	print_category_names()
	exit(0)

if category:
	print_category(category)
	exit(0)

for category in categories:
	print(category["name"])
	(start, end) = category["range"]
	print_unicode_range(start, end)
	print("-" * row_len * 2)

