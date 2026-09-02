"""Command line entry point for ppt2article MVP."""

import argparse

from workflow.pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser(description="Generate LaTeX paper project from PPT")
    parser.add_argument("input")
    parser.add_argument("--output", default="paper_project")
    args = parser.parse_args()

    run_pipeline(args.input, args.output)


if __name__ == "__main__":
    main()
