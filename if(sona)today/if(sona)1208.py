import openpyxl
import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# print(fm.findSystemFonts(fontpaths=None, fontext='ttf'))
plt.rc('font', family='Malgun Gothic')
fpath=r'C:\Users\akmris00\Downloads\코로나바이러스감염증-19_확진환자_발생현황_211208.xlsx'


# 엑셀은 2020.01.20부터 매일 기록한 것이니, 
# 내가 원하는 범위인 2021.11.04 ~ 2021.12.08까지
# 주 단위로 그래프를 그릴 예정이다.

wb = openpyxl.load_workbook(fpath)
ws = wb.active

# 2021.11.04 국내발생(C661셀) 2021.12.08 국내발생(C695셀)
weeks= []
for i in range(1,7):
    days=ws.cell(row=661+i,column=3).value
    weeks.append(days)
    
x=[]
y=[]    
for i in range(0,6):    
    x.append(str(i)+'주후')
    y.append(weeks[i])

plt.plot(x,y,color='#ff8e7f',linestyle='--',linewidth=3,marker='o')
plt.title('도대체 얼마나 코로나 발생이 늘어났길래-!')
plt.xlabel('기존 시작일로부터')
plt.ylabel('코로나 발생자')

for i,j in enumerate(x):
    plt.text(j,y[i],y[i],
        horizontalalignment='center',  
        verticalalignment='bottom')

plt.show()