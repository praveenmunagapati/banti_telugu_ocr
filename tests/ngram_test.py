from banti.ngram import Ngram

logd = print
ngram_file = "library/mega.123.pkl"

txt = [['రా', 'మ', 'జో', 'గి', 'మ', 'ం', 'దు', ' ', 'కొ', 'న', 'రే',
        ' ', 'ఓ', 'జ', 'ను', 'లా', 'ర', ' ', 'రా', '.', '.'],
       ['అ', 'ను', '✓', 'ప', 'ల', '్ల', 'వి', ':'],
       ['రా', 'మ', 'జో', 'గి', 'మ', 'ం', 'దు', ' ', 'కొ', 'ని', ' ',
        'ే', 'ప', '్ర', 'మ', 'తో', ' ', 'భు', 'జి', 'యి', 'ం', 'చు', 'డ', 'న', '్న'],
       ['కా', 'మ', 'కో', '్ర', 'ధ', 'లో', 'భ', 'మో', '✓', 'హ', 'ఘ', 'న', 'మె', 'ై', 'న', ' ',
        'రో', 'గా', 'ల', 'కు', 'మ', 'ం', 'దు', 'రా', '.', '.'],
       ['చ', 'ర', 'ణ', 'ము', '(', 'లు', ')', ':'],
       ['కా', 'టు', 'క', 'కొ', 'ం', 'డ', 'ల', 'వ', 'ం', 'టి', ' ',
        'క', 'ర', '్మ', 'ము', 'లె', 'డ', 'బా', 'ే', 'ప', ' ', 'మ', 'ం', 'దు'],
       ['సా', 'టి', 'లే', 'ని', ' ', 'జ', 'గ', 'ము', 'న', 'ం', 'దు', ' ',
        'సా', '్వ', 'మి', 'రా', 'మ', 'జో', 'గి', 'మ', 'ం', 'దు', 'రా', '.', '.'],
       ['వా', 'దు', 'కు', ' ', 'చె', 'ి', 'ప', '్ప', 'న', 'గా', 'ని', ' ',
        'వా', 'రి', 'పా', '✓', 'ప', 'ము', 'లు', 'గొ', 'టి', '్ట'],
       ['ము', 'ద', 'ము', 'తో', 'నే', ' ', 'మో', 'క్ష', 'మి', 'చే', '్చ', ' ',
        'ము', 'దు', '్ద', ' ', 'రా', 'మ', 'జో', 'గి', 'మ', 'ం', 'దు', 'రా', '.', '.'],
       ['ము', 'ద', 'ము', 'తో', ' ', 'భ', 'దా', '్ర', 'ది', '్ర', 'య', 'ం', 'దు', ' ',
        'ము', 'కి', '్త', 'ని', ' ', 'పొ', 'ం', 'ది', 'ం', 'చే', 'మ', 'ం', 'దు'],
       ['స', 'ద', 'యు', 'డె', 'ై', 'న', ' ', 'రా', 'మ', 'దా', '✓', 'సు', ' ',
        'ము', 'ద', 'ము', 'తో', ' ', 'ే', 'స', 'వి', 'ం', 'చే', 'మ', 'ం', 'దు', 'రా']]

ngram = Ngram(ngram_file)
for text in txt:
    prior = 0
    for i in range(len(text)):
        prior += ngram(text[:i])

    print(prior, text)