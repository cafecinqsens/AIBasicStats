# 문제를 풀고 해당 내용을 종이 또는 한글 파일에 작성하여 제출
# 제출처는 교수학습개발원(ctl.honam.ac.kr)의 AI기초통계 [학습활동]-[과제] 해당 게시물에 제출
# 종이에 작성한 내용은 스마트폰 카메라 앱 또는 스캔 앱을 이용하여 전체 내용이 나올 수 있도록 파일화
# 반드시 23일 오전 9시부터 3시간 이내에 작성해야 함 

# Q1. 명령문과 결과물을 확인하고 이를 설명하시오.
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(sum(10))

'''
결과값
55
'''

# Q2. 명령문과 결과물을 확인하고 이를 설명하시오.
def times2(k):
    k[0] = k[0] * 2
    k[1] = k[1] * 2
a = [1, 2]
b = [3, 4]

times2(a)
times2(b)
print('a=', a, 'b=', b)

'''
결과값
a = [2, 4] b = [6, 8]
'''

# Q3. 명령문을 확인하고 이를 설명하시오.
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

K = np.loadtxt('test1.csv', delimiter=',')
G = nx.to_networkx_graph(K)
nx.draw(G, with_labels=True, node_color='yellow', edge_color='red')

plt.show()


# Q4. 명령문과 결과값을 확인하고 이를 설명하시오.
import networkx as nx
import matplotlib.pyplot as plt
import numpy as  np
import zipfile 

zf = zipfile.ZipFile('football.zip')
# 만약 경로와 관련하여 유니코드 에러가 나올 때 대응 방법에 대해서 설명하면 가산점 

txt = zf.read('football.txt').decode()
gml = zf.read('football.gml').decode()
gml = gml.split('\n')[1:]
G = nx.parse_gml(gml)

print('No. of nodes: %d' % G.number_of_nodes())
print('No. of edges: %d' % G.number_of_edges())
print('Avg. of degrees: %.1f' % np.mean([d for n, d in G.degree()]))


'''
== 결과값 == 
No. of nodes: 115
No. of edges: 613
Avg. of degrees: 10.7
'''

# 수고하셨습니다.