from netman.parse_args import parser
from netman.connect import connect
def main():
    args = parser()
    connect(args=args)


if __name__ == "__main__":
    main()