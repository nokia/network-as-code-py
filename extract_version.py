import toml

def get_version():
    with open("pyproject.toml", "r") as f:
        pyproject_data = toml.load(f)
        version = pyproject_data["tool"]["poetry"]["version"]
        return version

if __name__ == "__main__":
    print(get_version())
