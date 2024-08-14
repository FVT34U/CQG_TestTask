import argparse
from utils.file_loader import FileLoader
from converter import Converter


parser = argparse.ArgumentParser()
parser.add_argument("config_file_path", type=str)
parser.add_argument("input_file_path", type=str)


def main():
    args = parser.parse_args()

    conf = FileLoader(args.config_file_path).get_content()
    inp = FileLoader(args.input_file_path).get_content()

    conv = Converter(conf, inp)

    result = conv.convert()

    print(result)


if __name__ == "__main__":
    main()