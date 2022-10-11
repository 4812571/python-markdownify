#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from markdownify import markdownify as md

def testOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    in_str = fdp.ConsumeUnicodeNoSurrogates(64)
    md(in_str)
        
def main():
    atheris.Setup(sys.argv, testOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()