#!/usr/bin/python3

import os

def print_spacer():
    print(f"{'-'*10}\n")


def update_branch(branch):
    # refactor idea for OOP methodology
    # use factory to determine method
    # factory uses branch name to determine method
    # if branch name starts with * strip it use checkout method
    # if branch name does not start with * use fetch origin method
    formatted_branch = branch.replace('* ', '').strip()
    pull_cmd = f'git fetch origin {formatted_branch}:{formatted_branch}'
    pull_stream = os.popen(pull_cmd)

    for line in pull_stream.readlines():
        print(line)

    print_spacer()


def main():
    cmd = 'git branch'
    stream = os.popen(cmd)

    [update_branch(branch) for branch in stream.readlines()]


main()
