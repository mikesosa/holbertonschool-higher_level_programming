#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        dumb = fct(*args)
        return dumb
    except Exception as en:
        print("Exception: {:s}".format(str(en)), file=sys.stderr)
        return None
