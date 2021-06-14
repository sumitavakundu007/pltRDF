# pltRDF

# Radial Distribution Function (RDF)

pltRDF is a Python package to plot RDF by reading a GSD file.

If your input is a trajectory, then it will consider only last frame.

## Contributors
- [Sumitava Kundu](https://github.com/sumitavakundu007/), IACS, Kolkata.

## Installation
### Prerequisites
1. [python3 or higher](https://www.python.org/download/releases/3.0/)
2. [scikit-build](https://pypi.org/project/scikit-build/)
3. [freud](https://freud.readthedocs.io/en/latest/index.html)

#### Using PyPI
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pltRDF.

```bash
pip install pltRDF
```

#### Using source code
```bash
git clone https://github.com/sumitavakundu007/pltRDF.git
tar -xvf pltRDF-X.X.X
cd pltRDF-X.X.X
python3 setup.py install --user
```

## Usage

```python
import pltRDF
pltRDF.rdf("input_file.gsd", "output_file.pdf") # a PDF file for RDF
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/
