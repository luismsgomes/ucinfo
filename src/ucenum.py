import sys, unicodedata


CATEGORIES = '''
L  - Letter
Lu - Letter, Uppercase
Ll - Letter, Lowercase
Lt - Letter, Titlecase
Lm - Letter, Modifier
Lo - Letter, Other
M  - Mark
Mn - Mark, Nonspacing
Mc - Mark, Spacing Combining
Me - Mark, Enclosing
N  - Number
Nd - Number, Decimal Digit
Nl - Number, Letter
No - Number, Other
P  - Punctuation
Pc - Punctuation, Connector
Pd - Punctuation, Dash
Ps - Punctuation, Open
Pe - Punctuation, Close
Pi - Punctuation, Initial quote (may behave like Ps or Pe depending on usage)
Pf - Punctuation, Final quote (may behave like Ps or Pe depending on usage)
Po - Punctuation, Other
S  - Symbol
Sm - Symbol, Math
Sc - Symbol, Currency
Sk - Symbol, Modifier
So - Symbol, Other
Z  - Separator
Zs - Separator, Space
Zl - Separator, Line
Zp - Separator, Paragraph
C  - Other
Cc - Other, Control
Cf - Other, Format
Cs - Other, Surrogate
Co - Other, Private Use
Cn - Other, Not Assigned
'''

usage = '''
usage: {prog} CATEGORY

CATEGORY is one of the following abbreviations:

{categories}
'''

CATS = set(line.split(' ', 1)[0].lower() for line in CATEGORIES.splitlines())

def main():
    if 2 != len(sys.argv) or sys.argv[1] not in CATS:
        sys.exit(usage.format(prog=sys.argv[0], categories=CATEGORIES))

    cat = sys.argv[1].lower()
    chars = (c for c in map(chr, range(65536)) if unicodedata.category(c).lower().startswith(cat))
    sys.stdout.write(''.join(chars))


if __name__ == "__main__":
    main()
