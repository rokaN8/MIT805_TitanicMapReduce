# MIT805 MapReduce Example

Python example converted from Java for the MIT805 Titanic MapReduce program.
Works on Windows/Linux with Python > 3.x

## Requirements
* Python > 3.x
* Pip

## Install

mrjob required for MapReduce, found and issue with the newest version and file access issues on Windows10, working version is 0.5.10

* pip install mrjob==0.5.10

## Running

* make run

or

* python main.py input\titanic.csv -o output\

## Output

Two files:
part-00000
* boarded-female	314
* boarded-male	577

part-00001
* survived-female	233
* survived-male	109
