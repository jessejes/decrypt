import typer

app = typer.Typer()


@app.command()
def add(name: str):
    print(f"Hello {name}")

@app.command()
def bye(name: str):
    print(f"Bye {name}")

if __name__ == '__main__':
    app()
