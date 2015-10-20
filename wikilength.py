## get song length from wikipedia.
import wikipedia
import re


expr = re.compile('class="duration"><span class="min">(\d)*</span>:<span class="s">(\d)+</span></span>')
test = wikipedia.page("King Kunta")
s = test.html()
span = expr.search(s).span()
(x,y) = span
sub = s[x:y]


