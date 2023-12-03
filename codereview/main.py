import sys
import os


def main():
    print("Open Source Zero AI Review!")
    print(os.environ['OPENAI_API_KEY'])
    print(os.environ['GITHUB_TOKEN'])

if __name__ == "__main__":
    main()