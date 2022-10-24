from importlib.metadata import entry_points

def main():
    for ep in entry_points().get("mygroup", []):
        print(ep)
        func = ep.load()
        func()

if __name__ == "__main__":
    main()
