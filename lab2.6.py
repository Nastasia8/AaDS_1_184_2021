
A={0, "Nastya", "Kseni", "Igor"}
B=[1, "ALina","Danya","Kseni","Nikita"]
def group (A,B):
    for i in B:
        if i not in A:
            return False
    return True
print(group(A,B))