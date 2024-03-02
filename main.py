from netman.parse_args import parse_args
from netman.connect import connect
from netman.exec_command import CommandExec

def main():
    try:
        args = parse_args()
        connection = connect(args=args)
        executor = CommandExec(connection)
        print("Type 'exit' to leave\n")
        while True:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                break
            
            output = executor.exec_command(user_input)
            print(output)
    except KeyboardInterrupt:
        print("\nCtrl+C detected. Exiting gracefully.")

if __name__ == "__main__":
    main()
