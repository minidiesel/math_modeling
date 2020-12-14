import matplotlib.pyplot as plt

# constants
dt = 1  # градусов по цельсию температура нагревания океана

C = 4150  # j/kg*dt

p = 1030000 # kg/m3 # плотность воды мирового океана

V_mirovogookeana = 1340_740_000_000_000_000 # m^3 объем

m_mirovogookeana = V_mirovogookeana * p # kg масса

A = 361_100_000 # площадь мирового океана km


Q_mirovogookeana = C * m_mirovogookeana * dt
Q_mirovogookeana_t = C * m_mirovogookeana * dt

tMID = 5  # world average temperature from https://www.meteoblue.com source
tMID_mirovogookeana = 4  #

# kipyatilnik мощностью 500вват и работающий 60 секунд
P = 1500  # power
t = 60  # seconds
timer = 0
x_0=0








## NEWTON'S LAW OF COOLING USING EULER METHOD #
import numpy as np
import matplotlib.pyplot as plt

plot_t=[]
plot_y=[]
y_analy=[]

def euler(f,y0,a,b,h):
    t,y=a,y0
    while t<=b:
        plot_t.append(t)
        plot_y.append(y)
        t=t+h
        y=y+h*f(y,t)

        
def cooling(temp,time):
    return -0.07*(temp-tMID)
euler(cooling,tMID_mirovogookeana,x_0,t,1)

for i in range(0,t,1):
    y_analy.append(tMID+(tMID_mirovogookeana-tMID)*np.exp(-0.07*i))
    
plt.plot(plot_t,plot_y,marker='.',label='euler')
plt.plot(y_analy,'r--',label='exact')
plt.title('Newton Law of Cooling')
plt.xlabel('Time(sec)')
plt.ylabel('Temperature(°C)')
plt.grid()
plt.legend(loc='best')
plt.show()
    





























kpd = 0.97
Q_1kipyatilnik = P * t * kpd  # 30_000 j
Q_1kipyatilnik_t = P * t * kpd  # 30_000 j


Q_accumulator = 0

temp = 0


# создание массивов графиков

X_graph1_t = []
Y_graph1_temp = []
Y_graph2_Qkip = []
Y_graph2_Qokean = []

# calculating
# the number of boilers required to heat the oceans by 1 degree Celsius without taking into account the law of cooling

value = Q_mirovogookeana / Q_1kipyatilnik

while (timer <= t):
    Q_1kipyatilnik_t = P * 1 * kpd * value

    Q_accumulator = Q_accumulator + Q_1kipyatilnik_t # количество теплоты выделенное кипятильниками до данного момента

    Q_mirovogookeana_t = Q_mirovogookeana - Q_accumulator # количество теплоты нужное для нагрева океана на 1 градус с данного момента

    temp = 5 + (Q_accumulator/(C*m_mirovogookeana))

    if (Q_mirovogookeana_t != 0):
        X_graph1_t.append(timer)
        Y_graph1_temp.append(temp)
        Y_graph2_Qkip.append(Q_accumulator)
        Y_graph2_Qokean.append(Q_mirovogookeana_t)


    print("температура =                                     ",temp)
    print("оставшееся количество теполоты                  : ", Q_mirovogookeana_t)
    print("количество теполоты выделенное до данной секунды: ", Q_accumulator)
    print("количество теполоты мирового океана             : ", Q_mirovogookeana)

    timer = timer + 1
    print()

print("Q_mirovogo_okeana = ", Q_mirovogookeana)
print("Q_1kipyatilnika = ", Q_1kipyatilnik)
print("number of boilers = ", value)

# GRAPH

plt.xlabel("время в секундах")
plt.ylabel("температура ℃")
strplt = 'Количество кипятильников мощностью 0.5КВт: ' + str(value)
plt.title(strplt)
plt.plot(X_graph1_t,Y_graph1_temp)

plt.show()

plt.xlabel("время необходимое для нагрева мирового океана на 1℃")
plt.ylabel("количество теплоты выделяемое "+str(value)+ " кипятильниками Дж/кг (5.73099313e27 Дж/кг)")
strplt = 'Количество кипятильников мощностью 0.5КВт: ' + str(value)
plt.title(strplt)
plt.plot(X_graph1_t,Y_graph2_Qkip)

plt.show()


plt.xlabel("время необходимое для нагрева мирового океана на 1℃")

str3 = "количество теплоты необходимое для нагрева океана на 1℃ = 5730993130000000000000000000 Дж/кг (5.73099313e27)"
plt.ylabel(str3)

plt.plot(X_graph1_t,Y_graph2_Qokean)

plt.show()
