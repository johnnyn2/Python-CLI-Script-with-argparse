# Cylinder Calculator

Cylinder Calculator is a Python CLI tool for calculating cylinder volume and surface

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the zip file.

```bash
pip install https://github.com/johnnyn2/Python-CLI-Script-with-argparse/blob/master/cycal.zip?raw=true
```

## Usage

```bash
# calculate cylinder total surface area
cycal surface --radius=5 --height=2 --verbose

# calculate cylinder volume
cycal volume --radius=5 --height=2 --verbose

# get help for surface command
cycal surface -h

# get help for volume command
cycal volume -h
```

## Development

```bash
# To install and test the CLI tool in local environment
pip install -e .
```

## Build distribution
```bash
# build .zip distribution
python build.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)