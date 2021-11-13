data=[10, 20, 30, 40, 50]
 
#방법1 총합 나누기 개수
방법1 = sum(data) / len(data)
 
#방법2 numpy 모듈
import numpy
방법2=numpy.mean(data)
 
#방법3 statistcics 라이브러리
import statistics
방법3 = statistics.mean(data)
 
print(방법1)    # 30.0
print(방법2)    # 30.0
print(방법3)    # 30