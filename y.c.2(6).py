Goods = int(input()) #������ ���-�� ��������� �������
a = list(map(int,input().split(maxsplit=Goods))) #����� ������ ������ ���������� ������ �������� ������ ��������� �������, �� �������� ��� ���� �������� "Goods"
Buying = int(input()) #������ ���-�� ������� ��������
b = list(map(int,input().split(maxsplit=Buying))) #����� ������ ������ ���������� ������� � ������������ �������, �� �������� ��� ���� �������� "Buying"
for i in range(0, Buying): #�������� ���-�� ������� �� ���-�� �������
    a[b[i]-1] -= 1

for i in range(0, Goods): #��������� ������� �� � ��� �� ������ ������ ��� ���
    if (a[i] < 0):
        print("yes")
    else:
        print("no")