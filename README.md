# Introduction to Machine Learning - Course 06

This is your student repository template for the course.

## Course Materials

| Lecture | Example Notebook | Homework | Solution |
| --- | --- | --- | --- |
| Lecture 01: Data Preparation | [Lecture01.ipynb](Lecture01-Data-Preparation/Lecture01.ipynb) | [lecture01_hw.ipynb](Lecture01-Data-Preparation/homework/lecture01_hw.ipynb) | To be released |

## Setup

```bash
uv sync
uv run python -m ipykernel install --user --name bigoai-uv --display-name "Python (bigoai-uv)"
```

## Get Weekly Updates

After creating your own repository from this template, add the course template as `upstream` once:

```bash
git remote add upstream https://github.com/bigocoding-ai/intro-to-ml-template-06.git
```

Each week, pull newly released lecture materials:

```bash
git pull upstream main
```

## Submission Guideline

For each lecture, commit your completed homework and create a lecture-specific submission tag.

Example for Lecture 01:

```bash
git add .
git commit -m "Submit Lecture 01"
git tag submit-lecture01
git push origin main
git push origin submit-lecture01
```

For later lectures, replace `01` with the lecture number, for example `submit-lecture02`.
