import ast

import black

with open('setup.py') as f:
    parsed_setup = ast.parse(f.read())
    for element in parsed_setup.body:
        if isinstance(element, ast.Expr) and element.value.func.id == 'setup':
            for keyword in element.value.keywords:
                if keyword.arg == 'version':
                    original_version = keyword.value.value
                    # TODO use a proper version lib later
                    x, y, z = keyword.value.value.split('.')
                    z = str(int(z) + 1)
                    bumped_version = keyword.value.value = f'{x}.{y}.{z}'
    bumped_setup = black.format_str(ast.unparse(parsed_setup), mode=black.FileMode())
    print(bumped_version)

with open('setup.py', 'w') as w:
    w.write(bumped_setup)
