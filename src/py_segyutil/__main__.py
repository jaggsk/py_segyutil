from .core import SegyUtil

def main() -> None:
    # Customize name or parse CLI args here
    segyrun = SegyUtil()
    segyrun.run()

if __name__ == "__main__":
    main()
