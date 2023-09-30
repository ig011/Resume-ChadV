![chad-face](https://s2.coinmarketcap.com/static/img/coins/200x200/24507.png)

<h1 align="center">ChadV Resume Generator</h1>

# Table of Contents

1. [Installation](#installation)
   1. Requirements
1. [Usage](#usage)
   1. Create your resume config
   1. Generate the HTML file
   1. Generate PDF file
1. [Exporting resume to PDF file](#exporting-resume-to-pdf-file)

# Installation

Coming soon...

# Usage

In order to generate the resume to PDF file by means of docker container image you need to run the command

Build the image:

```sh
docker build -t chadv .
```

Run the docker image with volumes added to the current working directory:

```sh
docker run --rm -it -v ${pwd}:/code chadv
```

# Exporting resume to PDF file

Coming soon...
