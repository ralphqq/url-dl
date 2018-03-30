# url-dl

This command line tool lets users download files from the Internet by simply providing the target URLs on a terminal.

## Requirements and Installation

This tool runs on Python 3.6 and uses requests and click. To install the full list of dependencies and to  run url-dl as a command line tool, follow the below instructions:

1. Clone this repo into your local machine.
2. Create a fresh virtual environment.
3. cd to the project directory and enter:

```
$ pip install --editable .
```

**Note:** Make sure to activate the virtual environment you created for this project each time you run the script.

## Usage

The basic syntax goes something like this:

```
$ dl url1 url2 url3 ...
```

You need to provide at least 1 valid URL. If you enter more than 1 link, you must separate each URL with a space. This tool lets you specify as many URLs as you want.

## Output

This tool saves the downloaded files in the `downloads` directory.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributing

Please feel free to use or build this project further.