from BSM import *
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

#mkt_prc = 0.31
#option_type = 1
#S = 268.55      #기초자산 가격
#K = 275.0       #행사가
#T = 9           #만기일


#Prarmeters
K = 100         #행사가

r = 0.01        #이자율
q = 0.00        #배당율
sigma = 0.25    #변동성

n1 = 100
n2 = 50
start_t = 0.000001      #만기 시작
end_t = 1               #만기 끝
start_s = 0.000001      #기초자산 시작
end_s = 200             #기초자산끝


#Variables
T = np.linspace(start_t, end_t, n1)
S = np.linspace(start_s, end_s, n1)
T, S = np.meshgrid(T, S)

'''
#옵션가격
call_value = BSM.option_value(S, K, T, r, sigma, 1)

trace = go.Surface(x=T, y=S, z=call_value)
data = [trace]
layout = go.Layout(title='call option', scene={'xaxis':{'title':'만기'}, 'yaxis':{'title':'기초자산'}})
fig = go.Figure(data=data, layout=layout)
iplot(fig)
'''
#델타
call_dalta = BSM.delta(S, K, T, r, sigma, 1)

trace = go.Surface(x=T, y=S, z=call_dalta, colorscale='Jet', opacity=0.8,
                    contours_x=dict(show=True, color="black", start=start_t, end=end_t, size=(end_t-start_t)/n2, project_x=True),
                    contours_y=dict(show=True, color="black", start=start_s, end=end_s, size=(end_s-start_s)/n2, project_y=True)
                    )
data = [trace]
layout = go.Layout(title='call_dalta', 
                    scene={'xaxis':{'title':'만기'}, 'yaxis':{'title':'기초자산' }, 'zaxis':{'title':'델타' }},
                    width=800, height=800, autosize=True
                    )
fig = go.Figure(data=data, layout=layout)
iplot(fig)

#감마
call_gamma = BSM.gamma(S, K, T, r, sigma, 1)

trace = go.Surface(x=T, y=S, z=call_gamma, colorscale='Jet', opacity=0.8,
                    contours_x=dict(show=True, color="black", start=start_t, end=end_t, size=(end_t-start_t)/n2, project_x=True),
                    contours_y=dict(show=True, color="black", start=start_s, end=end_s, size=(end_s-start_s)/n2, project_y=True)
                    )
data = [trace]
layout = go.Layout(title='call_gamma', 
                    scene={'xaxis':{'title':'만기'}, 'yaxis':{'title':'기초자산' }, 'zaxis':{'title':'감마' }},
                    width=800, height=800, autosize=False,
                    margin=dict(pad=0)
                    )
fig = go.Figure(data=data, layout=layout)
iplot(fig)

#세타
call_theta = BSM.theta(S, K, T, r, sigma, 1)

trace = go.Surface(x=T, y=S, z=call_theta, colorscale='Jet', opacity=0.8,
                    contours_x=dict(show=True, color="black", start=start_t, end=end_t, size=(end_t-start_t)/n2, project_x=True),
                    contours_y=dict(show=True, color="black", start=start_s, end=end_s, size=(end_s-start_s)/n2, project_y=True)
                    )
data = [trace]
layout = go.Layout(title='call_theta', 
                    scene={'xaxis':{'title':'만기'}, 'yaxis':{'title':'기초자산' }, 'zaxis':{'title':'세타' }},
                    width=800, height=800, autosize=False,
                    margin=dict(pad=0)
                    )
fig = go.Figure(data=data, layout=layout)
iplot(fig)

#베가
call_vega = BSM.vega(S, K, T, r, sigma, 1)

trace = go.Surface(x=T, y=S, z=call_vega, colorscale='Jet', opacity=0.8,
                    contours_x=dict(show=True, color="black", start=start_t, end=end_t, size=(end_t-start_t)/n2, project_x=True),
                    contours_y=dict(show=True, color="black", start=start_s, end=end_s, size=(end_s-start_s)/n2, project_y=True)
                    )
data = [trace]
layout = go.Layout(title='call_vega', 
                    scene={'xaxis':{'title':'만기'}, 'yaxis':{'title':'기초자산' }, 'zaxis':{'title':'베가' }},
                    width=800, height=800, autosize=False,
                    margin=dict(pad=0)
                    )
fig = go.Figure(data=data, layout=layout)
iplot(fig)
