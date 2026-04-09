import marimo

__generated_with = "0.23.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Stabilnost sustava
    """)
    return


@app.cell
def _():
    import scipy as sc
    import numpy as np
    from scipy.integrate import odeint
    import matplotlib.pyplot as plt

    return np, odeint, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Fazni portret gibanja njihala
    """)
    return


@app.cell
def _(np, odeint):
    def njihalo(x, t):
        dxdt = [-x[1], -10 * np.sin(x[0])]
        return dxdt
    _x0 = np.linspace(-8, 2, 50)
    _x1 = np.linspace(-8, 8, 50)
    X0, X1 = np.meshgrid(_x0, _x1)
    dX0 = np.zeros(X0.shape)
    dX1 = np.zeros(X1.shape)
    _shape1, _shape2 = X1.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = njihalo([X0[_indexShape1, _indexShape2], X1[_indexShape1, _indexShape2]], 0)
            dX0[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1[_indexShape1, _indexShape2] = _dxdtAtX[1]
    _početnoStanje = np.array([-1, -1])
    _vrijeme = np.linspace(0, 5, 50)
    rješenje = odeint(njihalo, _početnoStanje, _vrijeme)
    return X0, X1, dX0, dX1, rješenje


@app.cell
def _(X0, X1, dX0, dX1, plt, rješenje):
    plt.figure(figsize=(7, 7))
    plt.quiver(X0,X1,dX0,dX1,color='b')

    plt.xlim(-8,2)
    plt.ylim(-8,8)

    plt.plot(rješenje[:,0], rješenje[:,1], color='r',linewidth=3)

    plt.title('Fazni portret', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [-x[0], -2 * x[1]]
        return dxdt
    _x0 = np.linspace(-2, 2, 20)
    _x1 = np.linspace(-2, 2, 20)
    X0_1, X1_1 = np.meshgrid(_x0, _x1)
    dX0_1 = np.zeros(X0_1.shape)
    dX1_1 = np.zeros(X1_1.shape)
    _shape1, _shape2 = X1_1.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([X0_1[_indexShape1, _indexShape2], X1_1[_indexShape1, _indexShape2]], 0)
            dX0_1[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_1[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_1, X1_1, dX0_1, dX1_1, color='b')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [x[0], 2 * x[1]]
        return dxdt
    _x0 = np.linspace(-2, 2, 20)
    _x1 = np.linspace(-2, 2, 20)
    X0_2, X1_2 = np.meshgrid(_x0, _x1)
    dX0_2 = np.zeros(X0_2.shape)
    dX1_2 = np.zeros(X1_2.shape)
    _shape1, _shape2 = X1_2.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([X0_2[_indexShape1, _indexShape2], X1_2[_indexShape1, _indexShape2]], 0)
            dX0_2[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_2[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_2, X1_2, dX0_2, dX1_2, color='b')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [x[0], -2 * x[1]]
        return dxdt
    _x0 = np.linspace(-2, 2, 20)
    _x1 = np.linspace(-2, 2, 20)
    X0_3, X1_3 = np.meshgrid(_x0, _x1)
    dX0_3 = np.zeros(X0_3.shape)
    dX1_3 = np.zeros(X1_3.shape)
    _shape1, _shape2 = X1_3.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([X0_3[_indexShape1, _indexShape2], X1_3[_indexShape1, _indexShape2]], 0)
            dX0_3[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_3[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_3, X1_3, dX0_3, dX1_3, color='b')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [2 * x[0], 2 * x[1]]
        return dxdt
    _x0 = np.linspace(-4, 4, 20)
    _x1 = np.linspace(-4, 4, 20)
    X0_4, X1_4 = np.meshgrid(_x0, _x1)
    dX0_4 = np.zeros(X0_4.shape)
    dX1_4 = np.zeros(X1_4.shape)
    _shape1, _shape2 = X1_4.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([X0_4[_indexShape1, _indexShape2], X1_4[_indexShape1, _indexShape2]], 0)
            dX0_4[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_4[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_4, X1_4, dX0_4, dX1_4, color='b')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [2 * x[0] + x[1], 2 * x[1]]
        return dxdt
    _x0 = np.linspace(-4, 4, 20)
    _x1 = np.linspace(-4, 4, 20)
    X0_5, X1_5 = np.meshgrid(_x0, _x1)
    dX0_5 = np.zeros(X0_5.shape)
    dX1_5 = np.zeros(X1_5.shape)
    _shape1, _shape2 = X1_5.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([X0_5[_indexShape1, _indexShape2], X1_5[_indexShape1, _indexShape2]], 0)
            dX0_5[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_5[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_5, X1_5, dX0_5, dX1_5, color='b')
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [2 * x[0], 1]
        return dxdt
    _r = np.linspace(0, 1, 5)
    _theta = np.linspace(0, 2 * np.pi, 20)
    _R, _Theta = np.meshgrid(_r, _theta)
    _dR = np.zeros(_R.shape)
    _dTheta = np.zeros(_Theta.shape)
    _shape1, _shape2 = _Theta.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([_R[_indexShape1, _indexShape2], _Theta[_indexShape1, _indexShape2]], 0)
            _dR[_indexShape1, _indexShape2] = _dxdtAtX[0]
            _dTheta[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(_R * np.cos(_Theta), _R * np.sin(_Theta), _dR * np.cos(_dTheta), _dR * np.sin(_dTheta), color='b')
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [-2 * x[0], 1]
        return dxdt
    _r = np.linspace(0, 1, 5)
    _theta = np.linspace(0, 2 * np.pi, 20)
    _R, _Theta = np.meshgrid(_r, _theta)
    _dR = np.zeros(_R.shape)
    _dTheta = np.zeros(_Theta.shape)
    _shape1, _shape2 = _Theta.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([_R[_indexShape1, _indexShape2], _Theta[_indexShape1, _indexShape2]], 0)
            _dR[_indexShape1, _indexShape2] = _dxdtAtX[0]
            _dTheta[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(_R * np.cos(_Theta), _R * np.sin(_Theta), _dR * np.cos(_dTheta), _dR * np.sin(_dTheta), color='b')
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [0, -2 * x[1]]
        return dxdt
    _x0 = np.linspace(-2, 2, 20)
    _x1 = np.linspace(-2, 2, 20)
    X0_6, X1_6 = np.meshgrid(_x0, _x1)
    dX0_6 = np.zeros(X0_6.shape)
    dX1_6 = np.zeros(X1_6.shape)
    _shape1, _shape2 = X1_6.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([X0_6[_indexShape1, _indexShape2], X1_6[_indexShape1, _indexShape2]], 0)
            dX0_6[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_6[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_6, X1_6, dX0_6, dX1_6, color='b')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    return


@app.cell
def _(np, plt):
    def _sustav(x, t):
        dxdt = [0, 2 * x[1]]
        return dxdt
    _x0 = np.linspace(-2, 2, 20)
    _x1 = np.linspace(-2, 2, 20)
    X0_7, X1_7 = np.meshgrid(_x0, _x1)
    dX0_7 = np.zeros(X0_7.shape)
    dX1_7 = np.zeros(X1_7.shape)
    _shape1, _shape2 = X1_7.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = _sustav([X0_7[_indexShape1, _indexShape2], X1_7[_indexShape1, _indexShape2]], 0)
            dX0_7[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_7[_indexShape1, _indexShape2] = _dxdtAtX[1]
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_7, X1_7, dX0_7, dX1_7, color='b')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Van der Polov oscilator
    """)
    return


@app.cell
def _(np, odeint, plt):
    def vanderPol(x, t, eps):
        dxdt = [x[1], -x[0] + _eps * (1 - x[0] ** 2) * x[1]]
        return dxdt
    _eps = 1
    _x0 = np.linspace(-3, 3, 50)
    _x1 = np.linspace(-3, 3, 50)
    X0_8, X1_8 = np.meshgrid(_x0, _x1)
    dX0_8 = np.zeros(X0_8.shape)
    dX1_8 = np.zeros(X1_8.shape)
    _shape1, _shape2 = X1_8.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = vanderPol([X0_8[_indexShape1, _indexShape2], X1_8[_indexShape1, _indexShape2]], 0, _eps)
            dX0_8[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_8[_indexShape1, _indexShape2] = _dxdtAtX[1]
    _početnoStanje = np.array([-1, -1])
    _vrijeme = np.linspace(0, 20, 200)
    rješenje_1 = odeint(vanderPol, _početnoStanje, _vrijeme, args=(_eps,))
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_8, X1_8, dX0_8, dX1_8, color='b')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.plot(rješenje_1[:, 0], rješenje_1[:, 1], color='r', linewidth=3)
    plt.title('Fazni portret', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()
    return (vanderPol,)


@app.cell
def _(np, odeint, plt, vanderPol):
    _eps = 0
    _x0 = np.linspace(-3, 3, 50)
    _x1 = np.linspace(-3, 3, 50)
    X0_9, X1_9 = np.meshgrid(_x0, _x1)
    dX0_9 = np.zeros(X0_9.shape)
    dX1_9 = np.zeros(X1_9.shape)
    _shape1, _shape2 = X1_9.shape
    for _indexShape1 in range(_shape1):
        for _indexShape2 in range(_shape2):
            _dxdtAtX = vanderPol([X0_9[_indexShape1, _indexShape2], X1_9[_indexShape1, _indexShape2]], 0, _eps)
            dX0_9[_indexShape1, _indexShape2] = _dxdtAtX[0]
            dX1_9[_indexShape1, _indexShape2] = _dxdtAtX[1]
    _početnoStanje = np.array([-1, -1])
    _vrijeme = np.linspace(0, 20, 200)
    rješenje_2 = odeint(vanderPol, _početnoStanje, _vrijeme, args=(_eps,))
    plt.figure(figsize=(7, 7))
    plt.quiver(X0_9, X1_9, dX0_9, dX1_9, color='b')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.plot(rješenje_2[:, 0], rješenje_2[:, 1], color='r', linewidth=3)
    plt.title('Fazni portret', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
