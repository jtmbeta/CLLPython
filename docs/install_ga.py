import re
import glob


ga_tag = """<head><!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-C8D7Q02SML"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-C8D7Q02SML');
</script>
"""


files = glob.glob('/Users/jtm545/Projects/CLLPython-sphinx-docs/html/*.html')

for f in files:
    html_fh = open(f, 'r')
    content = html_fh.readlines()
    content = [re.sub('<head>', ga_tag, s) for s in content]
    html_fh.close()
    html_fh = open(f, 'w')
    html_fh.writelines(content)
    html_fh.close()


