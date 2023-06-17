"""A class or function to parse the config file and return the values as a dictionary.

The config file itself can be any of the following formats:

- ryo: means 'roll your own' and is a simple text file with key-value pairs separated by an equals sign. For example:
```
location = "Moondalup City Square Parking"
number_of_spaces = 192
```
**you** read the file and parse it into a dictionary.
- json: a json file with key-value pairs. For example:
```json
{location: "Moondalup City Square Parking", number_of_spaces: 192}
```
json is built in to python, so you can use the json module to parse it into a dictionary.
- toml: a toml file with key-value pairs. For example:
```toml
[location]
name = "Moondalup City Square Parking"
spaces = 192
```
toml is part of the standard library in python 3.11, otherwise you need to install tomli to parse it into a dictionary.
```bash

python3 -m pip install paho-mqtt
python3 -m pip install sense-hat
python3 -m pip install tkinter
python3 -m pip install tomli
"paho-mqtt",
        "sense-hat",
        "tkinter",
        "toml"
```
see [realpython.com](https://realpython.com/python-toml/) for more info.

Finally, you can use `yaml` if you prefer.

"""
import json

class ConfigParser:

    @staticmethod
    def parse_config(config: dict) -> dict:
        with open(config, "r") as f:
            config = json.load(f) #load make a dict
            return config