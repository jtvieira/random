import subprocess


def generate(city, url):
    result = subprocess.run(["curl", url], capture_output=True, text=True)
    res = result.stdout

    # Output to a file
    with open(f"{city}_output.txt", "w") as file:
        file.write(res)
