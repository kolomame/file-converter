
import sys
import markdown
if sys.argv[1] == 'markdown' and len(sys.argv) == 4:
    with open(sys.argv[2], 'r') as f:
        mark = f.read()

    html = markdown.markdown(mark)

    with open(sys.argv[3], 'w') as f:
        f.write(html)