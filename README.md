# Apriori Algorithm Python Implementation

<p align=center>
    <a target="_blank" href="https://travis-ci.com/chonyy/apriori_python" title="Build Status"><img src="https://travis-ci.com/chonyy/apriori_python.svg?branch=master"></a>
    <a target="_blank" href="#" title="pip"><img src="https://img.shields.io/pypi/v/apriori_python?color=brightgreen"></a>
    <a target="_blank" href="#" title="language count"><img src="https://img.shields.io/github/languages/count/chonyy/apriori_python"></a>
    <a target="_blank" href="#" title="top language"><img src="https://img.shields.io/github/languages/top/chonyy/apriori_python?color=orange"></a>
    <a target="_blank" href="https://opensource.org/licenses/MIT" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
    <a target="_blank" href="#" title="repo size"><img src="https://img.shields.io/github/repo-size/chonyy/apriori_python"></a>
    <a target="_blank" href="http://makeapullrequest.com" title="PRs Welcome"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
</p>

## How to use

### Install the Pypi package using pip

```
pip install apriori_python
```

Then use it like 

```python
from apriori_python import apriori
itemSetList = [['eggs', 'bacon', 'soup'],
                ['eggs', 'bacon', 'apple'],
                ['soup', 'bacon', 'banana']]
freqItemSet, rules = apriori(itemSetList, minSup=0.5, minConf=0.5)
print(rules)  
# [[{'beer'}, {'rice'}, 0.6666666666666666], [{'rice'}, {'beer'}, 1.0]]
# rules[0] --> rules[1], confidence = rules[2]
```

### Clone the repo

To run the program with dataset provided and default values for *minSupport* = 0.5 and *minConfidence* = 0.5

```
python apriori.py -f dataset.csv
```

To run program with dataset and min support and min confidence  

```
python apriori.py -f dataset.csv -s 0.17 -c 0.68
```
