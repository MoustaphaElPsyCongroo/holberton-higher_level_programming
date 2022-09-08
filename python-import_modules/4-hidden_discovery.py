#!/usr/bin/python3
import hidden_4

hidden_4_dirs = dir(hidden_4)

if __name__ == "__main__":
    for dir in hidden_4_dirs:
        if dir[0] == '_':
            continue
        print(dir)
