import typer

app = typer.Typer()

@app.command()
def show():
    print("Hi")

@app.command()
def add(id: int):
    print(f"Hello {id}")

@app.command()
def delete(id: int):
    print(id)

if __name__ == '__main__':
    app()
