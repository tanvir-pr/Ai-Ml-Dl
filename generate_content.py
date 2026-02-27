"""
Content Generation Script for ML-DL Learning Path
This script helps generate placeholder files for the remaining weeks.
Run this to create the basic structure, then fill in content as you progress.
"""

import os
import json

# Week templates
WEEK_STRUCTURE = {
    "Week-2-NumPy-Pandas-Matplotlib": {
        "notebooks": [
            "01_numpy_fundamentals.ipynb",  # Already created
            "02_pandas_data_manipulation.ipynb",
            "03_data_visualization.ipynb"
        ],
        "files": ["exercises.md", "mini_project.md", "resources.md"]
    },
    "Week-3-Statistics-Probability": {
        "notebooks": [
            "01_descriptive_statistics.ipynb",
            "02_probability_theory.ipynb",
            "03_hypothesis_testing.ipynb"
        ],
        "files": ["exercises.md", "mini_project.md", "resources.md"]
    },
    "Week-4-Linear-Regression": {
        "notebooks": [
            "01_simple_linear_regression.ipynb",
            "02_multiple_regression.ipynb",
            "03_gradient_descent.ipynb",
            "04_regularization.ipynb"
        ],
        "files": ["exercises.md", "mini_project.md", "resources.md"]
    }
}

def create_placeholder_notebook(title, topics):
    """Create a basic Jupyter notebook structure."""
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\\n\\n"
                    f"## Topics Covered\\n" +
                    "\\n".join([f"- {topic}" for topic in topics]) +
                    "\\n\\n**Status:** Content to be added\\n"
                    "**Time estimate:** 3-4 hours"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["import numpy as np\\nimport pandas as pd\\nimport matplotlib.pyplot as plt"]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    return json.dumps(notebook, indent=1)

def create_placeholder_md(title, description):
    """Create a placeholder markdown file."""
    return f"""# {title}

## Overview
{description}

**Status:** Content to be added as you progress through the course.

## Instructions
1. Complete the corresponding notebooks first
2. Practice with the exercises
3. Apply knowledge in the mini project

## Resources
- Refer to the main resources folder
- Check week-specific resources.md file

---

*This file will be populated with detailed content as you work through the material.*
"""

print("Content generation script ready!")
print("This script provides templates for remaining weeks.")
print("\\nRecommendation: Focus on one week at a time, filling in content as you learn.")
