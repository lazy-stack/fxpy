from utils.period_util import calc_period_info
from classes.Present_Value import PresentValue


class PriceBondRegular:
    def __init__(self, coupon, period, period_type, interest_rate, par_value):
        self.coupon = coupon
        self.period = period
        self.period_type = period_type
        self.interest_rate = interest_rate
        self.par_value = par_value

    def calculate(self):
        if self.coupon != 0:
            coupon_period_cal = calc_period_info(self.period, self.period_type, self.coupon / 100)
            coupon_period = coupon_period_cal['interest_rate'] * self.par_value

            coupon_pv = PresentValue(coupon_period, self.interest_rate, self.period, self.period_type, True)
            par_pv = PresentValue(self.par_value, self.interest_rate, self.period, self.period_type, False)

            return round(coupon_pv.calculate()) + round(par_pv.calculate())
        else:
            par_pv = PresentValue(self.par_value, self.interest_rate, self.period, self.period_type, False)
            return round(par_pv.calculate())

