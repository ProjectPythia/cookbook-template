# Cookbook Template

This is a template for creating [Project Pythia](https://projectpythia.org) Cookbooks.

This repository includes all the basic infrastructure to create your content and host it online. You can use this template by selecting the green "Use this Template" button at the top of the page.

You can use the `notebook-template` in `/notebooks` as your content template!

Once you have made your new content, add it to the table of contents (`notebooks/_toc.yml`) file, and push it to Github!

---

## Cookbook Contributor's Guide

Project Pythia Cookbooks are collections of more advanced and domain-specific example
workflows building on top of Pythia Foundations. 
They are [geoscience](https://en.wikipedia.org/wiki/Earth_science)-focused
and should point the reader towards the Foundations material for any required
background knowledge. 

The following is a step-by-step guide to getting your cookbook idea
published on the Project Pythia website.

1. Use the template
    1. On https://github.com/ProjectPythiaTutorials/cookbook-template, click "Use this template"
    1. Create the repo under your account with a descriptive name, followed by `-cookbook` (e.g. `hydrology-cookbook`, `hpc-cookbook`, `cesm-cookbook`, etc.)
    1. See the GitHub tutorial in Foundations for how to set up a clone
1. Create the environment
    1. Edit `environment.yml`: change the name to `<your-cookbook-name>-dev` and add all required libraries and other dependencies under `dependencies:`
    1. Create the Conda environment with `conda env create --file=environment.yml`
    1. Activate your environment with `conda activate <env-name>`
1. Additional infrastructure changes
    1. Add badges
1. Add notebooks
    1. Using the notebook template, add your content. Add folders to organize notebooks into sections
    1. Add notebooks to `_toc.yml`. See `radar-cookbook/notebooks/_toc.yml` for syntax