import math
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QFormLayout, QWidget, QLabel, QSpinBox, QPushButton, \
    QTextEdit, QFrame


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class QEdit(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(22)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

class Application():
    def __init__(self):
        self.argv = sys.argv
        self.app = QApplication(self.argv)
        self.main_window = QMainWindow()
        self.main_window.setMinimumHeight(800)
        self.main_window.setMinimumWidth(600)
        self.main_window.setWindowTitle('Оценка ретроспективных профессиональных рисков')

        self.form_widget = QWidget()
        self.main_window.setCentralWidget(self.form_widget)

        self.layout = QFormLayout()
        self.form_widget.setLayout(self.layout)

        self.p_ns_label = QLabel('НС - число несчастных случаев за истекший период')
        self.p_ns_value = QSpinBox()
        self.p_ns_value.setMaximum(999999)
        self.layout.addRow(self.p_ns_label, self.p_ns_value)

        self.p_n_label = QLabel('N - cреднесписочная численность работников в рассматриваемом периоде')
        self.p_n_value = QSpinBox()
        self.p_n_value.setMinimum(1)
        self.p_n_value.setMaximum(999999999)
        self.layout.addRow(self.p_n_label, self.p_n_value)

        self.p_kf_button = QPushButton('Рассчитать Kf')
        self.p_kf_button.clicked.connect(self.calculate_kf)
        self.layout.addRow(self.p_kf_button)

        self.p_kf_label = QLabel('Кf - коэффициент частоты несчастных случаев')
        self.p_kf_value = QEdit()
        self.layout.addRow(self.p_kf_label, self.p_kf_value)

        self.layout.addRow(QHLine())

        self.p_sd_label = QLabel('сумма D - суммарное число дней временной нетрудоспособности, вызванной всеми несчастными случаями')
        self.p_sd_value = QSpinBox()
        self.p_sd_value.setMaximum(999999999)
        self.layout.addRow(self.p_sd_label, self.p_sd_value)

        self.p_kt_button = QPushButton('Рассчитать Kt')
        self.p_kt_button.clicked.connect(self.calculate_kt)
        self.layout.addRow(self.p_kt_button)

        self.p_kt_label = QLabel('Кt - коэффициент тяжести  несчастных случаев')
        self.p_kt_value = QEdit()
        self.layout.addRow(self.p_kt_label, self.p_kt_value)

        self.layout.addRow(QHLine())

        self.p_kp_button = QPushButton('Рассчитать Kп')
        self.p_kp_button.clicked.connect(self.calculate_kp)
        self.layout.addRow(self.p_kp_button)

        self.p_kp_label = QLabel('Кп - коэффициент потерь')
        self.p_kp_value = QEdit()
        self.layout.addRow(self.p_kp_label, self.p_kp_value)

        self.layout.addRow(QHLine())

        self.p_nssm_label = QLabel('НСсм - число несчастных случаев со смертельным исходом за истекший период')
        self.p_nssm_value = QSpinBox()
        self.p_nssm_value.setMaximum(999999)
        self.layout.addRow(self.p_nssm_label, self.p_nssm_value)

        self.p_ksm_button = QPushButton('Рассчитать Ксм')
        self.p_ksm_button.clicked.connect(self.calculate_ksm)
        self.layout.addRow(self.p_ksm_button)

        self.p_ksm_label = QLabel('Ксм - коэффициент частоты несчастных случаев со смертельным исходом')
        self.p_ksm_value = QEdit()
        self.layout.addRow(self.p_ksm_label, self.p_ksm_value)

        self.layout.addRow(QHLine())

        self.p_kob_button = QPushButton('Рассчитать Коб')
        self.p_kob_button.clicked.connect(self.calculate_kob)
        self.layout.addRow(self.p_kob_button)

        self.p_kob_label = QLabel('Коб - коэффициент обобщенных трудовых потерь')
        self.p_kob_value = QEdit()
        self.layout.addRow(self.p_kob_label, self.p_kob_value)

        self.layout.addRow(QHLine())

        self.p_t_label = QLabel('t - продолжительность работы, лет')
        self.p_t_value = QSpinBox()
        self.p_t_value.setMaximum(999999)
        self.layout.addRow(self.p_t_label, self.p_t_value)

        self.p_nq_label = QLabel('n - количество несчастных случаев')
        self.p_nq_value = QSpinBox()
        self.p_nq_value.setMaximum(999999)
        self.layout.addRow(self.p_nq_label, self.p_nq_value)

        self.p_pn_button = QPushButton('Рассчитать P(n)')
        self.p_pn_button.clicked.connect(self.calculate_pn)
        self.layout.addRow(self.p_pn_button)

        self.p_pn_label = QLabel('P(n) - Вероятность n-го количества несчастных случаев')
        self.p_pn_value = QEdit()
        self.layout.addRow(self.p_pn_label, self.p_pn_value)

        self.layout.addRow(QHLine())

        self.p_p0_button = QPushButton('Рассчитать P(0)')
        self.p_p0_button.clicked.connect(self.calculate_p0)
        self.layout.addRow(self.p_p0_button)

        self.p_p0_label = QLabel('P(0) - Вероятность безопасной работы для одного человека в течение года')
        self.p_p0_value = QEdit()
        self.layout.addRow(self.p_p0_label, self.p_p0_value)

        self.p_rt_button = QPushButton('Рассчитать Rтр')
        self.p_rt_button.clicked.connect(self.calculate_rt)
        self.layout.addRow(self.p_rt_button)

        self.p_rt_label = QLabel('Rтр - риск травмирования')
        self.p_rt_value = QEdit()
        self.layout.addRow(self.p_rt_label, self.p_rt_value)

        self.layout.addRow(QHLine())

        self.p_pz_label = QLabel('ПЗ - число впервые установленных профессиональных заболеваний')
        self.p_pz_value = QSpinBox()
        self.p_pz_value.setMaximum(999999)
        self.layout.addRow(self.p_pz_label, self.p_pz_value)

        self.p_kfp_button = QPushButton('Рассчитать Kfпроф')
        self.p_kfp_button.clicked.connect(self.calculate_kfp)
        self.layout.addRow(self.p_kfp_button)

        self.p_kfp_label = QLabel('Kfпроф - профессиональная и производственно обусловленная общая заболеваемость')
        self.p_kfp_value = QEdit()
        self.layout.addRow(self.p_kfp_label, self.p_kfp_value)

        self.layout.addRow(QHLine())

        self.p_oz_label = QLabel('ОЗ – число случаев общей заболеваемости')
        self.p_oz_value = QSpinBox()
        self.p_oz_value.setMaximum(999999)
        self.layout.addRow(self.p_oz_label, self.p_oz_value)

        self.p_a_label = QLabel('a = 0,25–0,3 – коэффициент, показывающий долю производственно обусловленной заболеваемости в общем, устанавливаемой по форме 16-ВН')
        self.p_a_value = QEdit()
        self.layout.addRow(self.p_a_label, self.p_a_value)

        self.p_kpz_button = QPushButton('Рассчитать Kfпр.з')
        self.p_kpz_button.clicked.connect(self.calculate_kpz)
        self.layout.addRow(self.p_kpz_button)

        self.p_kpz_label = QLabel('Kfпр.з - частота производственно обусловленной общей заболеваемости')
        self.p_kpz_value = QEdit()
        self.layout.addRow(self.p_kpz_label, self.p_kpz_value)

        self.set_values()

    def get_main_window(self):
        return self.main_window

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

    def set_values(self):
        self.p_n_value.setValue(150)
        self.p_ns_value.setValue(5)
        self.p_sd_value.setValue(20)
        self.p_ns_value.setValue(2)
        self.p_nq_value.setValue(5)
        self.p_t_value.setValue(1)
        self.p_oz_value.setValue(3)
        self.p_pz_value.setValue(4)
        self.p_a_value.setPlainText(str(0.25))


    def calculate_kf(self):
        ns = self.p_ns_value.value()
        n = self.p_n_value.value()
        kf = ns * 1000 / n

        self.p_kf_value.setText(str(kf))

    def calculate_kt(self):
        sd = self.p_sd_value.value()
        ns = self.p_ns_value.value()
        kt = sd / ns

        self.p_kt_value.setText(str(kt))

    def calculate_kp(self):
        kt = float(self.p_kt_value.toPlainText())
        kf = float(self.p_kf_value.toPlainText())

        kp = kt * kf

        self.p_kp_value.setText(str(kp))

    def calculate_ksm(self):
        nssm = self.p_nssm_value.value()
        n = self.p_n_value.value()
        ksm = nssm * 1000 / n

        self.p_ksm_value.setText(str(ksm))

    def calculate_kob(self):
        kf = float(self.p_kf_value.toPlainText())
        kt = float(self.p_kt_value.toPlainText())
        ksm = float(self.p_ksm_value.toPlainText())

        kob = kf * kt + ksm * 6000

        self.p_kob_value.setText(str(kob))

    def calculate_pn(self):
        kf = float(self.p_kf_value.toPlainText())
        n = self.p_n_value.value()
        nq = self.p_nq_value.value()
        t = self.p_t_value.value()

        pn = pow(kf / 1000 * n * t, nq) / nq * pow(math.e, (-1 * kf / 1000 * n * t))

        self.p_pn_value.setText(str(pn))

    def calculate_p0(self):
        kf = float(self.p_kf_value.toPlainText())
        n = self.p_n_value.value()
        t = self.p_t_value.value()

        p0 = pow(math.e, (-1 * kf / 1000 * n * t))

        self.p_p0_value.setText(str(p0))

    def calculate_rt(self):
        p0 = float(self.p_p0_value.toPlainText())

        rt = 1 - p0

        self.p_rt_value.setText(str(rt))

    def calculate_kfp(self):
        pz = self.p_pz_value.value()
        n = self.p_n_value.value()
        kfp = pz * pow(10, 4) / n

        self.p_kfp_value.setText(str(kfp))

    def calculate_kpz(self):
        oz = self.p_oz_value.value()
        n = self.p_n_value.value()
        a = float(self.p_a_value.toPlainText())

        kpz = a * oz * 100 / n

        self.p_kpz_value.setText(str(kpz))
