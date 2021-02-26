A={0, "Nastya", "Alina", "Danil"}
B=[1, "ALina","Danya","Dima","Nikita"]
def group (A,B):
    for i in B:
        if i not in A:
            return False
    return True
print(group(A,B))