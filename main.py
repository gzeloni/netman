from netman.parse_args import parser
from netman.connect import connect
from netman.exec_command import CommandExec


def main():
    args = parser()
    con = connect(args=args)
    executor = CommandExec(con)
    print("Type 'exit' to leave\n")
    while True:
        user_input = input("> ")
        if user_input.lower() == 'exit':
            break
        
        output = executor.exec_command(user_input)
        print(output)

if __name__ == "__main__":
    main()