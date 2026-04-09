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
    # Primjer: Geostacionarni satelit
    """)
    return


@app.cell
def _():
    from astropy.constants import G
    from astropy.constants import M_earth
    from astropy.constants import R_earth
    import scipy as sc
    import numpy as np
    from astropy import units
    from scipy.integrate import odeint
    from scipy import constants as sconst
    import matplotlib.pyplot as plt

    return G, M_earth, R_earth, np, odeint, plt, sconst, units


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Kutna brzina zemlje \(u radijanima\)
    """)
    return


@app.cell
def _(sconst, units):
    Omega = 2*sconst.pi/(86400*units.second)
    Omega
    return (Omega,)


@app.cell
def _(G, M_earth, Omega, np, units):
    R_0 = np.cbrt(G*M_earth/Omega**2)
    R_0.to(units.km)
    return (R_0,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Visina na kojoj se nalazi satelit
    """)
    return


@app.cell
def _(R_0, R_earth, units):
    (R_0 - R_earth).to(units.km)
    return


@app.cell
def _(G, M_earth, Omega, R_0):
    Om = Omega.value 
    R0 = R_0.value
    Gr = G.value
    Mz = M_earth.value
    Ms = 100
    return Gr, Ms, Mz, Om, R0


@app.function
def satellite(x,t,Om,R0,Gr,Mz,Ms,u):
    x1,x2,x3,x4 = x 
    Fr, Ftheta = u
    dxdt = [x2, (x1+R0)*(x4+Om)**2 - Gr*Mz/(x1+R0)**2 + Fr/Ms, x4, -2*x2*(x4+Om)/(x1+R0) + Ftheta/(Ms*(x1+R0))]
    return dxdt


@app.cell
def _(np):
    x0 = [0.02, 0.01, 0.01, 0.02]
    t = np.linspace(0, 10, 101)
    u = [0,0]
    return t, u, x0


@app.cell
def _(Gr, Ms, Mz, Om, R0, odeint, t, u, x0):
    sol = odeint(satellite, x0, t, args=(Om,R0,Gr,Mz,Ms,u))
    return (sol,)


@app.cell
def _(plt, sol, t):
    plt.plot(t, sol[:, 0], 'b', label='x1(t)')
    plt.plot(t, sol[:, 2], 'g', label='x3(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


@app.cell
def _(plt, sol, t):
    plt.plot(t, sol[:, 0], 'b', label='x1(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


@app.cell
def _(plt, sol, t):
    plt.plot(t, sol[:, 2], 'g', label='x3(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


@app.cell
def _(Gr, Ms, Mz, Om, R0, np, odeint, plt, u):
    x0_1 = [0.0, 0.0, 0.0, 0.0]
    t_1 = np.linspace(0, 1000, 10001)
    sol_1 = odeint(satellite, x0_1, t_1, args=(Om, R0, Gr, Mz, Ms, u))
    plt.plot(t_1, sol_1[:, 0], 'b', label='x1(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return sol_1, t_1


@app.cell
def _(plt, sol_1, t_1):
    plt.plot(t_1, sol_1[:, 2], 'g', label='x3(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


@app.cell
def _(Om, R0, np):
    A = np.array([[0., 1., 0., 0.], [3*Om**2, 0., 0., 2*Om*R0], [0.,0.,0.,1.],[0., -2*Om/R0, 0., 0.]])
    return (A,)


@app.cell
def _(A):
    A
    return


@app.cell
def _(Ms, R0, np):
    B = np.array([[0.,0.],[1./Ms, 0.],[0., 0.],[0., 1/(Ms*R0)]])
    return (B,)


@app.cell
def _(B):
    B
    return


@app.cell
def _(np):
    C = np.array([0., 0., 1., 0.])
    return


@app.function
def lin_satellite(x, t, A, B, u):
    dxdt = A@x+B@u
    return dxdt


@app.cell
def _(A, B, np, odeint):
    x0_2 = np.array([0.02, 0.01, 0.01, 0.02]).T
    t_2 = np.linspace(0, 10, 101)
    u_1 = np.array([0.0, 0.0]).T
    sol_2 = odeint(lin_satellite, x0_2, t_2, args=(A, B, u_1))
    return sol_2, t_2, u_1


@app.cell
def _(plt, sol_2, t_2):
    plt.plot(t_2, sol_2[:, 0], 'b', label='x1(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


@app.cell
def _(plt, sol_2, t_2):
    plt.plot(t_2, sol_2[:, 2], 'g', label='x3(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


@app.cell
def _(A, B, np, odeint, plt, u_1):
    x0_3 = [0.0, 0.0, 0.0, 0.0]
    t_3 = np.linspace(0, 1000, 10001)
    sol_3 = odeint(lin_satellite, x0_3, t_3, args=(A, B, u_1))
    plt.plot(t_3, sol_3[:, 0], 'b', label='x1(t)')
    plt.plot(t_3, sol_3[:, 2], 'g', label='x3(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


@app.cell
def _(A, np):
    np.linalg.eigvals(A)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Da bi mogli nešto suvislo napraviti, prvo bi trebalo promijeniti jedinice da bi brojevi postali "normalni"\.
    """)
    return


@app.cell
def _(Omega, R_0):
    Om2 = Omega.value*1e5 
    R02 = R_0.value*1e-7
    Ms2 = 1.
    return Ms2, Om2, R02


@app.cell
def _(Om2, R02, np):
    A2 = np.array([[0., 1., 0., 0.], [3*Om2**2, 0., 0., 2*Om2*R02], [0.,0.,0.,1.],[0., -2*Om2/R02, 0., 0.]])
    A2
    return (A2,)


@app.cell
def _(Ms2, R02, np):
    B2 = np.array([[0.,0.],[1./Ms2, 0.],[0., 0.],[0., 1/(Ms2*R02)]])
    B2
    return (B2,)


@app.cell
def _(A2, B2, np, odeint):
    x0_4 = np.array([0.02, 0.01, 0.01, 0.02]).T
    t_4 = np.linspace(0, 10, 101)
    u_2 = np.array([0.0, 0.0]).T
    sol_4 = odeint(lin_satellite, x0_4, t_4, args=(A2, B2, u_2))
    return sol_4, t_4


@app.cell
def _(plt, sol_4, t_4):
    plt.plot(t_4, sol_4[:, 0], 'b', label='x1(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


@app.cell
def _(plt, sol_4, t_4):
    plt.plot(t_4, sol_4[:, 2], 'g', label='x3(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
