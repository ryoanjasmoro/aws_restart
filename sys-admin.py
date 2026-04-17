#!/usr/bin/env python3
# coding: utf-8

import os
import subprocess

print("=== OS SYSTEM ===")
os.system("ls")

print("\n=== SUBPROCESS LS ===")
subprocess.run(["ls"])

print("\n=== SUBPROCESS LS -L ===")
subprocess.run(["ls", "-l"])

print("\n=== SUBPROCESS SPECIFIC FILE ===")
subprocess.run(["ls", "-l", "README.md"])

print("\n=== SYSTEM INFO ===")
command = "uname"
arg = "-a"
print(f"Running: {command} {arg}")
subprocess.run([command, arg])

print("\n=== ACTIVE PROCESSES ===")
command = "ps"
arg = "-x"
print(f"Running: {command} {arg}")
subprocess.run([command, arg])