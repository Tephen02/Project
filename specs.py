"""Спецификации функций модуля оценки рентабельности скважины (Вариант А).
Практическое занятие № 1. Выполнено в одиночку.
"""
OIL_DENSITY: float = 850.0 # кг/м³
M_MIN_THRESHOLD: float = 9.0 # Изменено под вариант N = 22

def read_valid_param(prompt: str, min_val: float, max_val: float) -> float:
 """Запрашивает у пользователя число в цикле до попадания в диапазон [min_val; max_val].
 Бизнес-правило (BR-01): Система не должна пропускать отрицательные значения,
 пустые строки и текстовый мусор. Запятая автоматически приводится к точке.
 Args:
 prompt (str): Текст приглашения для оператора.
 min_val (float): Нижняя допустимая граница (включительно).
 max_val (float): Верхняя допустимая граница (включительно).
 Returns:
 float: Проверенное вещественное число в границах [min_val; max_val].
 """
 pass

def calc_oil_volume(q_liq: float, w_pct: float) -> float:
 """Вычисляет суточный объёмный дебит чистой нефти по дебиту жидкости и обводнённости.
 Формула: Q_н = Q_ж * (1 - W / 100).
 Args:
 q_liq (float): Дебит пластовой жидкости, м³/сут (0.0 <= q_liq <= 1000.0).
 w_pct (float): Обводнённость продукции в процентах (0.0 <= w_pct <= 100.0).
 Returns:
 float: Объёмный дебит нефти Q_н, м³/сут.
 """
 return q_liq * (1.0 - w_pct / 100.0)

def calc_oil_mass(q_oil: float, density: float = OIL_DENSITY) -> float:
 """Переводит объёмный дебит нефти (м³/сут) в массовый дебит (т/сут).
 Формула: M_н = Q_н * density / 1000.
 Args:
 q_oil (float): Объёмный дебит нефти, м³/сут.
 density (float, optional): Плотность нефти, кг/м³. По умолчанию 850.0.
 Returns:
 float: Массовый дебит нефти M_н, т/сут.
 """
 return q_oil * density / 1000.0

def evaluate_profitability(m_oil: float, m_min: float = M_MIN_THRESHOLD, w_pct: float = 0.0) -> str:
 """Определяет категорию рентабельности скважины по массовому дебиту нефти.
 Бизнес-правило (BR-02):
 - Если m_oil < m_min -> 'Убыточна (стоп)'
 - Если m_min <= m_oil < 3 * m_min -> 'Рентабельна (база)'
 - Если m_oil >= 3 * m_min -> 'Высокодебитная (приоритет)'
 Args:
 m_oil (float): Массовый дебит нефти, т/сут.
 m_min (float): Минимальный порог рентабельности для участка, т/сут.
 Returns:
 str: Строковый статус рентабельности скважины.
 """
 if w_pct == 100.0:
     return "Чистая вода (авария)"
 if m_oil < m_min:
     return "Убыточна (стоп)"
 elif m_oil < 3 * m_min:
     return "Рентабельна (база)"
 else:
     return "Высокодебитная (приоритет)"

if __name__ == "__main__":
 print("ПРОВЕРКА СПЕЦИФИКАЦИЙ МОДУЛЯ (Вариант А)")
 print("=" * 45)
 print(evaluate_profitability.__doc__)
 print("-" * 45)
 
 # Проверка Упражнения 2 и 3 для ваших чисел N = 22 (Qж=116, W=59)
 q_oil = calc_oil_volume(116.0, 59.0)
 m_oil = calc_oil_mass(q_oil)
 status = evaluate_profitability(m_oil, M_MIN_THRESHOLD, 59.0)
 print(f"При M_н = {m_oil:.3f} т/сут (порог {M_MIN_THRESHOLD}): -> {status}")
 
 # Проверка Упражнения 4 (Правка на 100% воды)
 status_avaria = evaluate_profitability(0.0, M_MIN_THRESHOLD, 100.0)
 print(f"При W = 100.00% -> {status_avaria}")
 print("-" * 45)
 
 help(evaluate_profitability)
