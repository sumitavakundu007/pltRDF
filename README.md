# pltRDF

# Radial Distribution Function (RDF)

pltRDF is a Python package to plot RDF by reading a GSD file.

If your input is a trajectory, then it will consider only last frame.

## Contributor
- [Sumitava Kundu](https://github.com/sumitavakundu007/), [IACS, Kolkata](http://www.iacs.res.in/).

## Installation
### Prerequisites
1. [python3 or higher](https://www.python.org/download/releases/3.0/)
2. [scikit-build](https://pypi.org/project/scikit-build/)
3. [freud-v2.0.0 or higher](https://freud.readthedocs.io/en/latest/index.html)
4. [tbb](https://pkgs.org/download/tbb) and [tbb-devel](https://pkgs.org/download/tbb-devel)

#### Using PyPI
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pltRDF.
You must install tbb and tbb-devel separately, though wheels for tbb and tbb-devel exist on [PyPi](https://pypi.org/) for specific operating systems.
For example, on ubuntu, you may use the following command.
```bash
sudo apt install libtbb-dev
```
Now you are ready to use pip
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
#### It will ask for few inputs to calculate RDF like number of bins (bins), maximum cutoff distance (r_max)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/
