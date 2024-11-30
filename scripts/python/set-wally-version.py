import tomllib
import sys

def write_toml(file_path, data):
    new_content = []
    for section, values in data.items():
        new_content.append(f"[{section}]")
        for key, value in values.items():
            if isinstance(value, str):
                new_content.append(f"{key} = \"{value}\"")
            elif isinstance(value, (int, float, bool)):
                new_content.append(f"{key} = {value}")
            else:
                raise ValueError(f"not supported value {key}: {type(value)}")
        new_content.append("")

    with open(file_path, 'w') as file:
        file.write("\n".join(new_content))

def update_version(file_path: str, new_version: str):

    with open(file_path, 'rb') as file:
        data = tomllib.load(file)

    data['package']['version'] = new_version
    write_toml(file_path, data)

if __name__ == '__main__':
    update_version(sys.argv[1], sys.argv[2])