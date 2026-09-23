import numpy as np
import matplotlib.pyplot as plt

def plot_varying_parameter(func, x_range, param_name, param_values, fixed_params, title="", xlabel="x", ylabel="f(x)", saving_path=None):
    """
    Plots a function for multiple values of a single parameter.
    """
    x = np.linspace(x_range[0], x_range[1], 500)
    
    plt.figure(figsize=(10, 6))
    
    for val in param_values:
        params = {**fixed_params}
        params[param_name] = val
        y = func(x, **params)
        plt.plot(x, y, label=f"{param_name} = {val}", linewidth=2)
    
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5, alpha=0.3)
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.5, alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    if saving_path: plt.savefig(saving_path)
    plt.show()
    
def raw_svi(k, a, b, rho, m, sigma):
    """Raw SVI: w(k) = a + b * (rho * (k - m) + sqrt((k - m)^2 + sigma^2))"""
    return a + b * (rho * (k - m) + np.sqrt((k - m)**2 + sigma**2))

if __name__ == "__main__":

    # varying 'a' (Minimum variance / vertical level)
    plot_varying_parameter(
        func=raw_svi,
        x_range=(-1.0, 1.0),
        param_name="a",
        param_values=[0.01, 0.04, 0.08, 0.12],
        fixed_params={"a": 0.04, "b": 0.25, "rho": -0.5, "m": 0.05, "sigma": 0.2},
        title="Raw SVI - Varying Level (a)",
        xlabel="log-moneyness k = ln(K/F)",
        ylabel="Total Implied Variance w(k)",
        saving_path="./svi_a_plot.png"
    )

    # varying 'b' (Overall slope / amplitude of the smile)
    plot_varying_parameter(
        func=raw_svi,
        x_range=(-1.0, 1.0),
        param_name="b",
        param_values=[0.1, 0.3, 0.6, 1.0],
        fixed_params={"a": 0.04, "b": 0.25, "rho": -0.5, "m": 0.05, "sigma": 0.2},
        title="Raw SVI - Varying Slope (b)",
        xlabel="log-moneyness k = ln(K/F)",
        ylabel="Total Implied Variance w(k)",
        saving_path="./svi_b_plot.png"
    )

    # varying 'rho' (Skew / left-right asymmetry)
    plot_varying_parameter(
        func=raw_svi,
        x_range=(-1.0, 1.0),
        param_name="rho",
        param_values=[-0.8, -0.4, 0.0, 0.4, 0.8],
        fixed_params={"a": 0.04, "b": 0.25, "rho": 0.0, "m": 0.05, "sigma": 0.2},
        title="Raw SVI - Varying Skew (ρ)",
        xlabel="log-moneyness k = ln(K/F)",
        ylabel="Total Implied Variance w(k)",
        saving_path="./svi_rho_plot.png"
    )

    # varying 'm' (Horizontal shift / location of the minimum)
    plot_varying_parameter(
        func=raw_svi,
        x_range=(-1.0, 1.0),
        param_name="m",
        param_values=[-0.3, -0.1, 0.0, 0.1, 0.3],
        fixed_params={"a": 0.04, "b": 0.25, "rho": -0.5, "m": 0.05, "sigma": 0.2},
        title="Raw SVI - Varying Asymmetry Shift (m)",
        xlabel="log-moneyness k = ln(K/F)",
        ylabel="Total Implied Variance w(k)",
        saving_path="./svi_m_plot.png"
    )

    # varying 'sigma' (Smoothness / curvature of the wings)
    plot_varying_parameter(
        func=raw_svi,
        x_range=(-1.0, 1.0),
        param_name="sigma",
        param_values=[0.05, 0.2, 0.5, 1.0],
        fixed_params={"a": 0.04, "b": 0.25, "rho": -0.5, "m": 0.05, "sigma": 0.2},
        title="Raw SVI - Varying Wing Smoothness (σ)",
        xlabel="log-moneyness k = ln(K/F)",
        ylabel="Total Implied Variance w(k)",
        saving_path="./svi_sigma_plot.png"
    )