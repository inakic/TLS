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
    ## Privlačan i nestabilan sustav
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $$ \dot{x}_1 = \frac{x_1^2 (x_2 - x_1)+ x_2^5}{(x_1^2 + x_2^2)(1+(x_1^2 + x_2^2)^2 )} $$
    $$ \dot{x}_2 = \frac{x_2^2 (x_2 - 2 x_1)}{(x_1^2 + x_2^2)(1+(x_1^2 + x_2^2)^2 )} $$
    """)
    return


@app.function
def odeVinograd(t, x):
    """
    t = vrijeme (ne koristi se eksplicitno)
    x = [x1, x2]
    """
    x1, x2 = x
    denom = x1**2 + x2**2
    # Izbjegavanje dijeljenja s nulom u ishodištu
    if denom == 0:
        return [0.0, 0.0]
    factor = denom * (1 + denom**2)
    dx1 = (x1**2 * (x2 - x1) + x2**5) / factor
    dx2 = (x2**2 * (x2 - 2*x1)) / factor
    return [dx1, dx2]


@app.cell
def _():
    import numpy as np
    from scipy.integrate import solve_ivp
    import matplotlib.pyplot as plt

    # Definicija početnih vrijednosti za koje želimo riješiti sustav
    initial_values = [
        [0.5, 0.0],
        [0.0, 0.5],
        [1.0, 1.0],
        [2.0, -1.0],
        [-1.0, 2.0],
    ]

    t_eval = np.linspace(0, 20, 1000)

    plt.figure(figsize=(8, 6))
    for x0 in initial_values:
        sol = solve_ivp(odeVinograd, (0, 20), x0, t_eval=t_eval, rtol=1e-9, atol=1e-12)
        plt.plot(sol.y[0], sol.y[1], label=f"x0={x0}")
        plt.scatter([x0[0]], [x0[1]], s=40)

    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title('Trajektorije sustava odeVinograd za različite početne vrijednosti')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
    return np, plt, solve_ivp, x0


@app.cell
def _(mo):
    x1 = mo.ui.slider(-2.0,2.0,step=0.1)
    x2 = mo.ui.slider(-2.0,2.0,step=0.1)
    return x1, x2


@app.cell
def _(x1, x2):
    x1, x2
    return


@app.cell
def _(np, plt, solve_ivp, x1, x2):
    T =250
    t_eval2 = np.linspace(0, T, 1000)
    plt.figure(figsize=(8, 6))
    sol2 = solve_ivp(odeVinograd, (0, T), [x1.value,x2.value], t_eval=t_eval2, rtol=1e-9, atol=1e-12)
    plt.plot(sol2.y[0], sol2.y[1], label=f"x0={[x1.value,x2.value]}")
    plt.scatter([x1.value], [x2.value], s=40)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title('Trajektorije sustava odeVinograd za odabrane početne vrijednosti')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
    return


@app.cell
def _(np, plt, solve_ivp, x0):
    # Prikaz faznog portreta u okolici ishodišta
    fig, ax = plt.subplots(figsize=(10, 10))

    # Kreiraj mrežu točaka za vektorsko polje
    x1_range = np.linspace(-0.5, 0.5, 20)
    x2_range = np.linspace(-0.5, 0.5, 20)
    X1, X2 = np.meshgrid(x1_range, x2_range)

    # Izračunaj vektore polja
    U = np.zeros_like(X1)
    V = np.zeros_like(X2)
    for i in range(X1.shape[0]):
        for j in range(X1.shape[1]):
            x = [X1[i, j], X2[i, j]]
            dx = odeVinograd(0, x)
            U[i, j] = dx[0]
            V[i, j] = dx[1]

    # Prikaži vektorsko polje
    ax.quiver(X1, X2, U, V, alpha=0.6, scale=50)

    # Dodaj nekoliko trajektorija iz točaka na mreži
    initial_points = [
        [0.3, 0.0],
        [0.0, 0.3],
        [0.3, 0.3],
        [-0.3, 0.3],
        [0.3, -0.3],
        [-0.3, -0.3],
        [0.1, 0.2],
        [-0.2, 0.1],
    ]

    t_eval_local = np.linspace(0, 5, 500)
    for x_0 in initial_points:
        sol3 = solve_ivp(odeVinograd, (0, 5), x_0, t_eval=t_eval_local, rtol=1e-10, atol=1e-12)
        ax.plot(sol3.y[0], sol3.y[1], 'b-', alpha=0.5, linewidth=1)
        ax.scatter([x0[0]], [x0[1]], s=30, c='red', zorder=5)

    # Označi ishodište
    ax.scatter([0], [0], s=100, c='black', marker='o', zorder=10, label='Ishodište')

    ax.set_xlabel('$x_1$', fontsize=12)
    ax.set_ylabel('$x_2$', fontsize=12)
    ax.set_title('Fazni portret sustava odeVinograd oko ishodišta', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    ax.legend()
    plt.show()
    return X1, X2, fig





if __name__ == "__main__":
    app.run()
