Array = [] #������ ������ ������
length = int(input()) #���� ���-�� �����, ������� �� ����� �������
for i in range(length): #���� for, ������� ��� �� ������� lenght
    Array.append(input()) #����� ����� � ��������� �� � ������
print("Initial array:") #������� �� ����� Initial array:
print(', '.join(Array)) #��������� ���� ����� ����� �������
Count = len(Array[0]) #������ ������� ��������
Phase=0 #
Rang=10 #���-�� Busket
for i in range(Count-1,-1,-1): #���� for, ������� ��� � �������� ����������� �� Count-1 �� -1 � ����� -1
    Phase+=1 # ���������� � ���� 1
    print('**********') #������� **********
    print(f'Phase {Phase}') #������� Phase � ����� ����
    bucket = [[] for _ in range(Rang)] #������ ������ �������� 10 ���������
    for j in range(len(Array)): #���� for �� ����� �������
        bucket[ord(Array[j][i]) - ord('0')].append(Array[j]) #��������� ������ � ������� ������� ord � ���������� � ���� j-�� �������
    for j in range(Rang): #���� for �� 10
        if len(bucket[j])==0: #������� ��� ������� ����� ������� ����� 0
            print(f'Bucket {j}: empty') #������� Bucket (�����): empty
        else: #�����
            print("Bucket "+str(j)+": ", end='') #������� Bucket (�����): 
            for now in range(len(bucket[j])): #���� for �� ����� ������� ������
                print(bucket[j][now],end=', ') #������� �����,������� ��������� � �������
            print() #������� �� ����� ������
    p = 0 #������ ����������
    for j in range(Rang): #���� for �� 10
        for k in range(len(bucket[j])): #���� �� ����� �������
          Array[p] = bucket[j][k] #� ������� ���������� p ������������� ����� �� ������� � �������� j
          p += 1 #����������� ���������� p �� �������
 
print('**********') #������� �� ����� **********
print("Sorted array:") #������� �� ����� Sorted array:
print(', '.join(Array)) #������� ���������� ���������