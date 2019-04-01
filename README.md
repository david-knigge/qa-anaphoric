# a probabilistic approach to resolving anaphoric relations in short factoid narrations using Wikipedia

We propose a method for anaphoric resolution based on a combination of the three historical approaches; syntactic, semantic and morphological. Our system assigns probabilities to possible anaphoric relations on basis of rules, semantic content and distance in discourse between anaphor and entity. Our current best configuration obtains an F1-Score of 0.46 on our hand-annotated silver standard, proving that our combinational approach is promising.

### Prerequisites

See requirements.txt

### Installing

To be able to run our implementation, clone this git and run:

```
pip install requirements.txt
```

## Usage

```
python main.py
```

### Optional parameters:

To set the context similarity weighting use:
```
--wsim [float]
```

To set the inverse distance weighting use:
```
--widist [float]
```

The program will then ask for input, and start resolving anaphoric relations in that input.

## Authors

* **David Knigge**
* **Pepijn Sibbes**
* **Laurence Bont**
* **Marthijn den Hartog**
