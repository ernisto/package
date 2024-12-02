import tomllib
import sys

def write_toml(file_path, data):
    new_content = []
    for section, values in data.items():
        new_content.append(f"[{section}]")
        for key, value in values.items():
            if isinstance(value, str):
                new_content.append(f'{key} = "{value}"')
            elif isinstance(value, (int, float, bool)):
                new_content.append(f"{key} = {value}")
            elif isinstance(value, list):
                formatted_list = ', '.join(f'"{v}"' if isinstance(v, str) else str(v) for v in value)
                new_content.append(f"{key} = [{formatted_list}]")
            elif value is None:
                new_content.append(f"{key} = null")
            else:
                raise ValueError(f"Unsupported value type for {key}: {type(value).__name__}")
        new_content.append("")  # Blank line between sections

    with open(file_path, 'w') as file:
        file.write("\n".join(new_content))

def update_version(file_path: str, new_version: str):
    with open(file_path, 'rb') as file:
        data = tomllib.load(file)

    if 'package' not in data or 'version' not in data['package']:
        raise KeyError("The TOML file must contain a 'package' section with a 'version' key.")

    data['package']['version'] = new_version
    write_toml(file_path, data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <wally_file_path> <new_version>")
        sys.exit(1)

    update_version(sys.argv[1], sys.argv[2])