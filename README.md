# json_keys
## Overview

A simple helper that provides easy ways to access keys from a json data structure. This is work in progress and currently only works with json data that is a dictionary.


## Motivation

Often times while working with large JSON datas, I have needed to access just all the keys or keys from a portion of the data and never found a library that did that. 

## Installation and Usage

```python
workon venv
git clone https://github.com/madhurimapoddar/json_keys.git
cd json_keys
python setup.py install

# once you have the package installed
import json_keys
data = open('path/to/test.json')
all_keys = get_all_keys(data)
```

## Tests
```
python setup.py test
```

