from matplotlib import pyplot as plt
import numpy as np
from typing import Callable, Union

__all__ = ["plot_gd_one_minimum", "plot_gd_two_minimums", "run_gd_one_minimum", "run_gd_two_minimums"]

X_MIN = -1.25
X_MAX = 1.25


class Function:
    def __init__(
        self,
        f: Callable[[Union[float, np.ndarray]], Union[float, np.ndarray]],
        df: Callable[[Union[float, np.ndarray]], Union[float, np.ndarray]],
    ) -> None:
        self.f = f
        self.df = df

    def __call__(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        return self.f(x)

    def derivative(self, x: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        return self.df(x)


def plot_gd(
    func: Function,
    x0: float,
    num_iters: int,
    alpha: float,
    func_name: str,
    plot_path: bool = True,
) -> None:
    xs = np.linspace(X_MIN, X_MAX, 100)
    plt.plot(xs, func(xs), "k", label=func_name)

    if plot_path:
        x_path = [x0]
        for _ in range(num_iters):
            x_path.append(x_path[-1] - alpha * func.derivative(x_path[-1]))
            if x_path[-1] < X_MIN or x_path[-1] > X_MAX:
                print("Gradient Descent Path Exceeded Bounds")
                break

        x_path = np.array(x_path)
        plt.plot(x_path, func(x_path), "ro--", label="Gradient Descent Path")

    plt.grid()
    plt.legend()
    plt.show()


one_minimum_cfg = {
    "func": Function(f=lambda x: 0.5 * x**2 - 2, df=lambda x: x),
    "x0": -1,
    "num_iters": 20,
    "func_name": "0.5x^2-2",
}

two_minimums_cfg = {
    "func": Function(
        f=lambda x: x**6
        - 3 / 16 * x**5
        + 23 / 16 * x**4
        - 5 / 16 * x**3
        - 79 / 16 * x**2
        + 1,
        df=lambda x: 6 * x**5
        - 15 / 16 * x**4
        + 23 / 4 * x**3
        - 15 / 16 * x**2
        - 79 / 8 * x,
    ),
    "alpha": 0.01,
    "num_iters": 20,
    "func_name": "x^6 - 3/16*x^5 + 23/16*x^4 - 5/16*x^3 - 79/16*x^2 + 1",
}


def plot_gd_one_minimum(alpha: float, **kwargs) -> None:
    plot_gd(**one_minimum_cfg, alpha=alpha, **kwargs)


def plot_gd_two_minimums(x0: float, **kwargs) -> None:
    assert -1 <= x0 <= 1, "x0 must be between -1 and 1"
    plot_gd(**two_minimums_cfg, x0=x0, **kwargs)

def run_gd_one_minimum(
    alpha: float, tolerance: float = 0.01, max_steps: int = 20
) -> dict:
    """Chạy bài 1.1 từ x0 = -1, dừng khi |x| < tolerance hoặc hết số bước."""
    if not np.isfinite(alpha) or alpha <= 0:
        raise ValueError("alpha phải là số hữu hạn lớn hơn 0")
    if not 0 < tolerance < 1:
        raise ValueError("tolerance phải nằm trong khoảng (0, 1)")
    if not isinstance(max_steps, int) or max_steps < 1:
        raise ValueError("max_steps phải là số nguyên dương")

    func = one_minimum_cfg["func"]
    x = float(one_minimum_cfg["x0"])
    path = [x]
    for _ in range(max_steps):
        x = x - alpha * func.derivative(x)
        path.append(x)
        if abs(x) < tolerance:
            break

    steps = len(path) - 1
    reached_target = abs(x) < tolerance
    result = {
        "reached_target": reached_target,
        "steps": steps,
        "x_final": x,
        "distance": abs(x),
        "path": path,
    }

    print(f"Alpha: {alpha:g}")
    print(f"Đạt |x| < {tolerance:g} trong tối đa {max_steps} bước: "
          f"{'Có' if reached_target else 'Không'}")
    print(f"Số bước đã chạy: {steps}")
    print(f"Giá trị x khi dừng: {x:.10g}")
    print(f"Khoảng cách đến nghiệm |x|: {abs(x):.10g}")

    # Chỉ giới hạn phần đường đi được vẽ; vẫn đo đủ số bước ở trên.
    visible_path = path
    for i, point in enumerate(path):
        if point < X_MIN or point > X_MAX:
            visible_path = path[:i + 1]
            print("Đường đi vượt miền hiển thị; kết quả bên trên vẫn tính đủ số bước đã chạy.")
            break

    xs = np.linspace(X_MIN, X_MAX, 200)
    points = np.asarray(visible_path)
    plt.figure()
    plt.plot(xs, func(xs), "k", label="f(x) = 0.5x² - 2")
    plt.plot(points, func(points), "ro--", label="Đường đi Gradient Descent")
    plt.axvline(0, color="gray", linestyle=":", label="Nghiệm x* = 0")
    plt.xlim(X_MIN, X_MAX)
    plt.ylim(-2.1, -1.1)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"alpha = {alpha:g}")
    plt.grid()
    plt.legend()
    plt.show()
    return result

def run_gd_two_minimums(x0: float) -> dict:
    """Chạy bài 1.2 với alpha = 0.01 và đúng 20 bước cho mỗi vị trí bắt đầu."""
    if not np.isfinite(x0) or not -1 <= x0 <= 1:
        raise ValueError("x0 phải là số hữu hạn trong đoạn [-1, 1]")
    func = two_minimums_cfg["func"]
    alpha = two_minimums_cfg["alpha"]
    num_steps = two_minimums_cfg["num_iters"]
    x = float(x0)
    path = [x]
    for _ in range(num_steps):
        x = x - alpha * func.derivative(x)
        path.append(x)

    result = {
        "x0": float(x0),
        "steps": num_steps,
        "x_final": x,
        "objective": float(func(x)),
        "gradient": float(func.derivative(x)),
        "path": path,
    }
    print(f"Vị trí bắt đầu x0: {x0:g}")
    print(f"Learning rate: {alpha:g}; số bước đã chạy: {num_steps}")
    print(f"Vị trí sau {num_steps} bước: {x:.8f}")
    print(f"Giá trị hàm mục tiêu khi dừng: {result['objective']:.8f}")
    print(f"Gradient tại vị trí cuối: {result['gradient']:.8f}")

    xs = np.linspace(X_MIN, X_MAX, 200)
    points = np.asarray(path)
    plt.figure()
    plt.plot(xs, func(xs), "k", label="f(x)")
    plt.plot(points, func(points), "ro--", label="Đường đi Gradient Descent")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"x0 = {x0:g}, alpha = {alpha:g}, {num_steps} bước")
    plt.grid()
    plt.legend()
    plt.show()
    return result
