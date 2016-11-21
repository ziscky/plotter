import plotly.plotly as py
import plotly.graph_objs as go

# Present data plots phase responses for a Second Order Passive High Pass Filter
uname = ""
api_key = ""

py.sign_in(uname,api_key)
x = [2.798173972,
3.099209843,
3.497149879,
3.798179868,
4.099209864,
4.497149873,
4.798179868,
5.099209864,
5.497149873,
5.798179868]
y0 = [
0,
0,
0,
0,
0,
-18.95,
-36.00,
-150.0,
-180.0,
-360.0]
y1 = [
-0.2139,
-0.4279,
-1.0706,
-2.1470,
-4.3412,
-11.7446,
-32.2484,
-130.2774,
-168.5357,
-177.64]
y2 = [
0,
0,
0,
0,
0,
-9.47,
-30,
-180,
-180,
-360]
y3 = [
-0.0792,
-0.1584,
-0.3964,
-0.7952,
-1.6099,
-4.4014,
-13.1474,
-156.4009,
-175.7061,
-178.0119]

# Create a trace
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'lines',
    name = 'Phase-a1',
    line=dict(
        color='black'
    )
)
trace1 = go.Scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'Phase-c1',
    line=dict(
        color='red'
    )
)
trace2 = go.Scatter(
    x = random_x,
    y = random_y2,
    mode = 'lines+markers',
    name = 'Phase-a2',
    line=dict(
        color='blue'
    )
)
trace3 = go.Scatter(
    x = random_x,
    y = random_y3,
    mode = 'lines+markers',
    name = 'Phase-c2',
    line=dict(
        color='green'
    )
)
data = [trace0, trace1, trace2,trace3]

# Plot and embed in ipython notebook!
py.plot(data, filename='biquad-phase')
