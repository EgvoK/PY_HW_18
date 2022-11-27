#### TASK 03 ####
# Каждый год ваша компания предоставляет различным государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные.
# Используя механизм декораторов, решите вопрос отчетности для организаций.

from menu_task_03 import *


getReport("Quarterly report", {"Order quantity": 1000, "Customer count": 800, "Turnover amount": 1234567.9,
                               "Profit amount": 50000, "Tax amount": 20000, "Net profit amount": 30000},
          "Signature: J.H. Fray")
