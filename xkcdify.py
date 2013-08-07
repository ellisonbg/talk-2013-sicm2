def xkcdify(borders=True, code=True, html=True, prompts=True, output=True):
    """Turn on xkcd mode for the notebook.
    
    Run this in your notebook and it will enable the xkcd inspired font
    Humor Sans from http://antiyawn.com/uploads/Humor-Sans.ttf. Your browser
    will load this font from the internet so this only works if you are online.

    This mode can be used with Matplotlib's new xkcd mode to great effect. However,
    you will have to enable that separately by calling matplotlibs xkcd function.
    """
    from IPython.display import display, HTML
    s = """
    <style>
    @font-face {
        font-family: "xkcd";
        src: url('http://antiyawn.com/uploads/Humor-Sans.ttf');
    }
    """
    if borders:
        s += """
        div.cell {
            border: 2px solid black;
            margin-top: 10px;
            margin-bottom: 10 px;
        }
        """
    if code:
        s += """
        .CodeMirror {font-family: xkcd; font-size: 120%}
        """
    if html:
        s += """
        .rendered_html {font-family: xkcd; font-size: 120%}
        pre, code {font-family: xkcd; font-size: 120%}
        .rendered_html table {border: 2px solid black;}
        .rendered_html tr {border: 2px solid black;}
        .rendered_html th {border: 2px solid black; padding: 0.45em 1em;}
        .rendered_html td {border: 2px solid black; padding: 0.45em 1em;}
        """
    if prompts:
        s += """
        div.prompt {font-family: xkcd; font-size: 120%}
        """
    if output:
        s += """
        div.output_area pre {font-family: xkcd; font-size: 120%}
        """
    s += """</style>"""
    display(HTML(s))

