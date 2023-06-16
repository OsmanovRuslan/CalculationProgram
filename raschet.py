import math


class Calculation:
    def __init__(self, t_inner_int, t_ext, z_otopit_perioda, t_otopit_periuda_int):
        self.t_inner_int = t_inner_int  # Температура внутреннего воздуха, °C
        self.t_otopit_periuda_int = t_otopit_periuda_int  # Средняя расчетная температура отопительного периода, °C
        self.t_ext = t_ext  # Расчетная зимняя температура наружного воздуха, °C
        self.z_otopit_perioda = z_otopit_perioda

        self.n = 1  # коэффициент, принимаемый в зависимости от положения наружной поверхности ограждающих
        # конструкций по отношению к наружному воздуху
        self.alpha_int = 8.7  # Коэффициент теплоотдачи внутренней поверхности ограждающих конструкций, Вт/(м²·°C)]
        self.alpha_int_out = 23  # Вт/(м2 ∙ °С) коэффициент теплоотдачи наружной поверхности стена, Вт/(м2 ∙ °С)
        self.alpha_int_out_ch = 12  # Вт/(м2 ∙ °С) коэффициент теплоотдачи наружной поверхности чердак, Вт/(м2 ∙ °С)
        self.delta_t = 4  # Нормативный температурный перепад, °C

        self.R_min = 2.4  # минимальное требуемое сопротивление теплопередаче
        self.R_max = 2  # максимальное требуемое сопротивление теплопередаче
        self.T_min = 8000  # минимальное значение градусосуток
        self.T_max = 6000  # максимальное значение градусосуток

    def calculate_R_mp_0(self):
        # Расчет требуемого сопротивления теплопередаче конструкций стены
        R_mp_0 = round((self.t_inner_int - self.t_ext) * self.n / (self.alpha_int * self.delta_t), 2)

        # Определение требуемого термического сопротивления Стены
        gsop_wall = round((self.t_inner_int - self.t_otopit_periuda_int) * self.z_otopit_perioda,
                          2)  # градусосутки отопительного периода
        R_s_wall = round(0.00035 * gsop_wall + 1.4, 2)  # термическое сопротивление теплопередаче

        # Определение требуемого термического сопротивления Чердак
        gsop_cherdak = round((self.t_inner_int - self.t_otopit_periuda_int) * self.z_otopit_perioda,
                             2)  # градусосутки отопительного периода
        R_s_cherdak = round(0.00045 * gsop_cherdak + 1.9, 2)  # термическое сопротивление теплопередаче

        # Подбор толщины утеплителя стена
        Ro_wall = 1 / self.alpha_int + 0.630 + 1 / self.alpha_int_out
        h_wall = math.ceil((R_s_wall - Ro_wall) * 0.035 * 1000)
        h_rounded_wall = math.ceil(h_wall / 10) * 10

        # Толщина утеплителя чердак, мм
        Ro_cherdak = 1 / self.alpha_int + 1 / self.alpha_int_out_ch + 0.203
        h_cherdak = math.ceil((R_s_cherdak - Ro_cherdak) * 0.045 * 1000)
        h_rounded_cherdak = math.ceil(h_cherdak / 10) * 10

        return [R_mp_0, h_rounded_wall, h_rounded_cherdak]
