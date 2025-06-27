import sys
from form_matcher import load_templates, find_template

def parse_args(args):
    result = {}
    for arg in args:
        if arg.startswith('--') and '=' in arg:
            key, value = arg[2:].split('=', 1)
            result[key] = value
    return result

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args or args[0] != 'get_tpl':
        print("Usage: app.py get_tpl --field=value ...")
        sys.exit(1)

    input_fields = parse_args(args[1:])
    templates = load_templates()
    result = find_template(input_fields, templates)
    print(result)
