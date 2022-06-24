# Project Pythia Cookbook Contributor's Guide

Project Pythia Cookbooks are collections of more advanced and domain-specific example
workflows building on top of [Pythia Foundations](https://foundations.projectpythia.org/landing-page.html). 
They are [geoscience](https://en.wikipedia.org/wiki/Earth_science)-focused
and should direct the reader towards the [Foundations material](https://foundations.projectpythia.org/landing-page.html) for any required
background knowledge. 

The following is a step-by-step guide to getting your cookbook idea
hosted on the [Project Pythia Cookbooks gallery](https://projectpythia.org/cookbook-gallery.html).

1. Use the template
    1. On https://github.com/ProjectPythiaTutorials/cookbook-template, click "Use this template"
    1. Create the repo under your account with a descriptive name, followed by `-cookbook` (e.g. `hydrology-cookbook`, `hpc-cookbook`, `cesm-cookbook`, etc.)
    1. See the [GitHub tutorial in Foundations](https://foundations.projectpythia.org/foundations/getting-started-github.html) for how to set up a clone
1. Create the environment
    1. Edit `environment.yml`: change the name to `<your-cookbook-name>-dev` (e.g. `cesm-cookbook-dev`) and add all required libraries and other dependencies under `dependencies:`. Commit the changes
    1. Create the Conda environment with `conda env create -f environment.yml`. If it crashes, try running `conda config --set channel_priority strict`
    1. Activate your environment with `conda activate <env-name>`
1. Add content
    1. Using the notebook template, add your content. Add folders to organize notebooks into sections if applicable
    1. Add the notebooks to `_toc.yml`. See `radar-cookbook/notebooks/_toc.yml` for syntax
    1. Change `README.md` to include your cookbook title, various badges, a sentence or two describing the cookbook, and a link to the landing page. See the [Radar Cookbook](https://github.com/ProjectPythiaTutorials/radar-cookbook/blob/main/README.md) for an example
1. Transfer cookbook to the [ProjectPythiaTutorials](https://github.com/ProjectPythiaTutorials) organization
    1. Navigate to the settings of your repo, scroll down to the Danger Zone, and click "Transfer"
        1. For ProjectPythiaTutorials owners or members: type "ProjectPythiaTutorials", confirm, and transfer.
        1. For outside contributors: 
            1. Contact an owner of ProjectPythiaTutorials to be added as an outside collaborator. Then transfer to ProjectPythiaTutorials; or
            1. Type the username of an owner or member. They will then tranfer it to ProjectPythiaTutorials and add you as an outside collaborator on that repo
    1. Open issues, PRs, and continue making edits as necessary