import sys
from pathlib import Path

DOC = '''
redirector.py generates HTML files for redirection.
Call as:
  python redirector.py  TARGET_URL           OUT_FILE_PATH
  python redirector.py  https://example.com  example.html
  python redirector.py  https://example.com  foo/example.html
'''

def main():
    args = [ x.strip() for x in sys.argv if x.strip() not in ["", '--output', '-o'] ]
    if len(args) == 2 and (args[1].endswith('help') or args[1] == '-h'):
        print_help()
        return
    if len(args) != 3:
        print_help()
        return
    
    # Write output
    target_url = args[1]
    outfp = args[2]
    html = template(target_url)
    write_file(html, outfp)


def print_help():
    global DOC
    print(DOC.strip())


def write_file(string, outfp):
    outfp = Path(outfp)
    if not outfp.parent.exists(): outfp.parent.mkdir(parents=True)
    with open(outfp, "w", encoding="utf-8") as f:
        f.write(string)
    print(f"HTML written to `{outfp}`.")


def template(target_url):
    html = '''
    <!doctype html>
    <html lang=en-us>

    <head>
        <title>{{ TARGET_URL }}</title>
        <meta name=robots content="noindex">
        <meta charset=utf-8>
        <meta http-equiv=refresh content="0; url={{ TARGET_URL }}">
    </head>
    <body>
        <p>
            Redirecting to <a href="{{ TARGET_URL }}">{{ TARGET_URL }}</a>
        </p>
    </body>
    </html>
    '''
    return html.replace("{{ TARGET_URL }}", target_url)


#%%
def template(target_url):
    html = '''
    <!doctype html>
    <html lang=en-us>

    <head>
        <title>{{ TARGET_URL }}</title>
        <meta name=robots content="noindex">
        <meta charset=utf-8>
        <meta http-equiv=refresh content="0; url={{ TARGET_URL }}">
    </head>
    <body>
        <p>
            Redirecting to <a href="{{ TARGET_URL }}">{{ TARGET_URL }}</a>
        </p>
    </body>
    </html>
    '''
    return html.replace("{{ TARGET_URL }}", target_url)

# %%


if __name__ == "__main__":
    main()
