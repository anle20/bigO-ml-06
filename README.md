# Introduction to Machine Learning - Course 06

This is your student repository template for the course.

## First-Time Setup

1. Open the course template repository:

```text
https://github.com/bigocoding-ai/intro-to-ml-template-06
```

2. Click **Use this template** and create your own private repository.

Use a clear repository name, for example:

```text
intro-to-ml-nguyen-van-a
```

3. Add the instructor GitHub account as a collaborator:

```text
htn274
```

4. Send your repository URL to the instructor.

Example:

```text
https://github.com/student-username/intro-to-ml-nguyen-van-a
```

5. Clone your own repository:

```bash
git clone https://github.com/<student-username>/<student-repo>.git
cd <student-repo>
```

6. Add the course template as `upstream` once:

```bash
git remote add upstream https://github.com/bigocoding-ai/intro-to-ml-template-06.git
```

## Course Materials

| Lecture | Example Notebook | Homework | Solution |
| --- | --- | --- | --- |
| Lecture 01: Data Preparation | [Lecture01.ipynb](Lecture01-Data-Preparation/Lecture01.ipynb) | [lecture01_hw.ipynb](Lecture01-Data-Preparation/homework/lecture01_hw.ipynb) | [lecture01_sol.ipynb](Lecture01-Data-Preparation/homework/lecture01_sol.ipynb) |
| Lecture 02: KNN | [Lecture02.ipynb](Lecture02-KNN/Lecture02.ipynb) | [Lecture02_hw.ipynb](Lecture02-KNN/homework/Lecture02_hw.ipynb) |  |

## Setup

```bash
uv sync
uv run python -m ipykernel install --user --name bigoai-uv --display-name "Python (bigoai-uv)"
```

## Get Weekly Updates

Each week, pull newly released lecture materials:

```bash
git pull upstream main
```

If this is your first time pulling from `upstream` and Git says the histories are unrelated, run:

```bash
git pull upstream main --allow-unrelated-histories
```

After that first successful merge, use the normal `git pull upstream main` command for later updates.

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
