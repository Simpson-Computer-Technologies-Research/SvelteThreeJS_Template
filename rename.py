new_name: str = input("New Project Name: ")
for f in ["package-lock.json", "package.json"]:
    n: str = (open(f, "r").read().replace("\"sveltejs_threejs_template\"", f"\"{new_name}\""))
    open(f, "w").write(n)
