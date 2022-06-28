# Project Pythia Cookbook Contributor's Guide

Project Pythia Cookbooks are collections of more advanced and domain-specific example
workflows building on top of [Pythia Foundations](https://foundations.projectpythia.org/landing-page.html).
They are [geoscience](https://en.wikipedia.org/wiki/Earth_science)-focused
and should direct the reader towards the [Foundations material](https://foundations.projectpythia.org/landing-page.html) for any required
background knowledge.

The following is a step-by-step guide to getting your cookbook idea
hosted on the [Project Pythia Cookbooks gallery](https://cookbooks.projectpythia.org).

1. Use the template
    1. If you don't already have a GitHub account, create one by following the [Getting Started with GitHub guide](https://foundations.projectpythia.org/foundations/getting-started-github.html)
    1. On https://github.com/ProjectPythiaCookbooks/cookbook-template, click "Use this template"
    1. Choose "Include all branches"
    1. Create the repo under your account with a descriptive name, followed by `-cookbook` (e.g. `hydrology-cookbook`, `hpc-cookbook`, `cesm-cookbook`, etc.) by entering a name into the "Repository name" field and clicking on "Create repository from template"
    1. Your browser should be directed to the newly created repository under your GitHub account. Under Settings, enable GitHub Pages by changing the Source from "None" to `gh-pages` and clicking on "Save"
    1. [Clone the repo](https://foundations.projectpythia.org/foundations/github/github-cloning-forking.html) in your local workspace and `cd` into your cookbook directory
1. Create the environment
    1. Edit `environment.yml`: change the name to `<your-cookbook-name>-dev` (e.g. `cesm-cookbook-dev`) and add all required libraries and other dependencies under `dependencies:`. Commit the changes
    1. Create the Conda environment with `conda env create -f environment.yml`. If it crashes, try running `conda config --set channel_priority strict`
    1. Activate your environment with `conda activate <env-name>`
1. Add content
    1. After [creating a new git branch](https://foundations.projectpythia.org/foundations/github/git-branches.html), edit (and duplicate as necessary) the notebook template `notebooks/notebook-template.ipynb` to add your content. Add folders to organize notebooks into sections if applicable
    1. Add the notebooks to `_toc.yml`. See [`radar-cookbook/_toc.yml`](https://github.com/ProjectPythiaTutorials/radar-cookbook/blob/main/_toc.yml) for syntax
    1. Change `README.md` to include your cookbook title, various badges, a sentence or two describing the cookbook, and a link to the landing page. See the [Radar Cookbook](https://github.com/ProjectPythiaTutorials/radar-cookbook/blob/main/README.md) for an example
    2. Change `.gitignore` to include any pages from local site builds made during development. These will be in a `_build` directory (check if you moved the target directory from `notebooks/_build`).
    3. Commit your changes with git, and [open a Pull Request](https://foundations.projectpythia.org/foundations/github/github-pull-request.html) on your cookbook repo. When you open a PR there, the github-actions bot will comment a link to a preview of your cookbook
1. Transfer cookbook to the [ProjectPythiaCookbooks](https://github.com/ProjectPythiaCookbooks) organization
    1. Navigate to the settings of your repo, scroll down to the Danger Zone, and click "Transfer"
        1. For ProjectPythiaTutorials owners or members: type "ProjectPythiaTutorials", confirm, and transfer.
        1. For outside contributors:
            1. Contact an owner of ProjectPythiaTutorials to be added as an outside collaborator. Then transfer to ProjectPythiaTutorials; or
            1. Type the username of an owner or member. They will then transfer it to ProjectPythiaCookbooks and add you as an outside collaborator on that repo
    1. Open issues, PRs, and continue making edits as necessary
