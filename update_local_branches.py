#!/usr/bin/python3

import os

def print_spacer():
    print(f"{'-'*10}\n")


def update_branch(branch):
    formatted_branch = branch.replace('* ', '').strip()
    pull_cmd = f'git checkout {formatted_branch} && git pull'
    pull_stream = os.popen(pull_cmd)

    for line in pull_stream.readlines():
        print(line)

    print_spacer()


def main():
    cmd = 'git branch'
    stream = os.popen(cmd)

    [update_branch(branch) for branch in stream.readlines()]


main()
