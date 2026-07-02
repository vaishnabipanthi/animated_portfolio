from html.parser import HTMLParser
from pathlib import Path
text = Path(r'c:\Users\lenovo\OneDrive\Desktop\portfolioNEW\index.html').read_text(encoding='utf-8')
void = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack=[]
        self.errors=[]
    def handle_starttag(self, tag, attrs):
        if tag not in void:
            self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0]==tag:
            self.stack.pop()
        else:
            self.errors.append((tag, self.getpos(), self.stack[-5:]))
parser = P()
parser.feed(text)
print('remaining_open', len(parser.stack))
if parser.stack:
    for tag,pos in parser.stack[-10:]:
        print('open', tag, pos)
print('errors', len(parser.errors))
for e in parser.errors[:20]:
    print('error', e)
