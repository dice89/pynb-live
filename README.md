# pynb-live

Jupyter Notebooks are great but they can also suck if,

* You want to develop a production-able data pipeline
* You want to structure your code according to software engineering principles (no code duplication, tdd)
* You want to run code from command-line and in a long running process
* You don't want to get stuck in a non-linear coding workflow

Anyhow Jupyter Notebooks are great for:

* Interactive and iterative fast feedback data exploration
* Sharing Results with Stakeholders and fellow Data Scientist


That is why @elehcimd came up with the great `pynb` tool, to bridge the gap between software development and data analysis worflow.

However the great feature of interactivity got lost in his effort. `pynb-live` is a small cli tool that uses `livereload` to enable a interactive *web-dev* like data analysis workflow


## Demo

TODO gif


`pynb-live` is watching your notebooks directory.

## Usage

```
pip install pynb-live
pynb-live --help
```

Install the livereload chrome plugin, fire up pynb-live activate the connection, add a new pynb file and start seeing the magic work.




