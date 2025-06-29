#data.py

import numpy as np

t_values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
					16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
					29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 
					42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 
					55, 56, 57, 58, 59, 60, 61, 62, 63, 64]) #номер потребителя по СП 30, таблица А2 приложения А

q_tot_hru_values = np.array([5.0, 8.1, 8.7, 8.2, 10.3, 11.6, 10.4, 12.5, 
            				10.2, 12.5, 19, 22.4, 28, 30, 8.4, 12, 14, 12.5, 12.5, 10, 
            				2.6, 9.5, 18, 10, 18, 75, 40, 4, 2.7, 43.2, 3.1, 3.1, 3.1, 
            				9, 4, 32, 12, 10, 37, 4, 9, 0.5, 0.9, 0.9, 3.4, 0.3, 4.5, 9, 
            				0, 0.3, 9, 180, 290, 360, 540, 500, 14.1, 9.4, 0, 0, 0, 0, 0, 0])

q_h_hru_values = np.array([0, 0, 0, 4.5, 5.7, 6.5, 5.4, 7.0, 6.38, 7.0, 10.2, 
            			8.8, 12.8, 13.6, 4.6, 6.55, 8.1, 7.0, 7.0, 4.2, 1.0, 3.8, 6.8, 
            			3.8, 6.8, 21.3, 12.8, 1.7, 1.0, 18.4, 0.85, 0.85, 0.85, 5.1, 1.7, 
            			7.0, 3.4, 2.6, 8.2, 1.7, 4.0, 0.17, 0.34, 0.26, 1.9, 0.09, 2.5, 4.3, 
            			0, 0.09, 4.3, 100, 160, 200, 300, 230, 7.1, 3.7, 0, 0, 0, 0, 0, 0])

q_c_hru_values = np.array([5, 8.1, 8.7, 3.7, 4.6, 5.1, 5, 5.5, 3.82, 5.5, 
						8.8, 13.6, 15.2, 16.4, 3.8, 5.45, 5.9, 5.5, 5.5, 5.8, 1.6, 5.7, 
						11.2, 6.2, 11.2, 53.7, 27.2, 2.3, 1.7, 24.8, 2.25, 2.25, 2.25, 
						3.9, 2.3, 25, 8.6, 7.4, 28.8, 2.3, 5, 0.33, 0.56, 0.64, 1.5, 0.21, 
						2, 4.7, 0, 0.21, 4.7, 80, 130, 160, 240, 270, 7, 5.7, 0, 0, 0, 0, 0, 0])

q_tot_values = np.array([70, 110, 120, 130, 160, 180, 85, 110, 120, 120, 230, 200, 
                         250, 300, 115, 200, 240, 130, 150, 200, 13, 22, 60, 40, 
                         90, 75, 40, 12, 17.2, 220, 10, 12, 9, 70, 12, 310, 12, 10, 
                         250, 12, 56, 4, 8.6, 10, 40, 3, 50, 100, 10, 3, 100, 180, 290, 
                         360, 540, 500, 45, 25, 3, 0.5, 1.5, 0.45, 4.5, 0.5])

q_h_values = np.array([0, 0, 0, 50, 65, 70, 45, 50, 70, 60, 120, 85, 130, 160, 65, 
                       75, 95, 55, 65, 100, 4.4, 10, 21, 20, 25, 21.3, 12.8, 4.5, 
                       5, 95, 2.5, 2.9, 2.7, 30, 4, 47, 3.4, 2.6, 55, 4, 28, 1.3, 
                       2.2, 4, 21, 0.85, 25, 51, 0, 0.85, 51, 100, 160, 200, 300, 
                       230, 20.4, 9.4, 0, 0, 0, 0, 0, 0])

q_c_values = np.array([70.0, 110.0, 120.0, 80.0, 95.0, 110.0, 40.0, 60.0, 50.0, 60.0,
                      110.0, 115.0, 120.0, 140.0, 50.0, 125.0, 145.0, 75.0, 85.0, 100.0,
                      8.6, 12.0, 39.0, 20.0, 65.0, 53.7, 27.2, 7.5, 12.2, 125.0,
                      7.5, 9.1, 6.3, 40.0, 8.0, 263.0, 8.6, 7.4, 195.0, 8.0,
                      28.0, 2.7, 6.4, 6.0, 19.0, 2.15, 25.0, 49.0, 10.0, 2.15,
                      49.0, 0.0, 20.0, 160.0, 60.0, 240.0, 270.0, 24.6, 15.6, 3.0,
                      0.5, 1.5, 0.45, 4.5, 0.5])

q_tot_0_values = np.array([0.2, 0.3, 0.3, 0.2, 0.3, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 
                           0.3, 0.3, 0.3, 0.2, 0.3, 0.2, 0.2, 0.2, 0.3, 0.2, 0.14, 
                           0.2, 0.14, 0.2, 0.2, 0.3, 0.14, 0.14, 0.2, 0.14, 0.14, 
                           0.14, 0.14, 0.14, 0.2, 0.3, 0.3, 0.3, 0.14, 0.14, 0.14, 
                           0.14, 0.14, 0.14, 0.14, 0.2, 0.2, 0, 0.14, 0.2, 0.4, 0.4, 
                           0.2, 0.3, 0.2, 0.14, 0.14, 0, 0, 0, 0, 0, 0])

q_h_0_values = np.array([0.2, 0.3, 0.3, 0.14, 0.2, 0.2, 0.14, 0.14, 0.14, 
						0.2, 0.14, 0.2, 0.2, 0.2, 0.14, 0.2, 0.14, 0.14, 0.14, 0.2, 
						0.14, 0.1, 0.14, 0.1, 0.14, 0.2, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 
						0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 
						0.1, 0.1, 0.14, 0.14, 0, 0.1, 0.14, 0.4, 0.4, 0.14, 0.2, 0.14, 
						0.1, 0.1, 0, 0, 0, 0, 0])

q_c_0_values = np.array([0.2, 0.3, 0.3, 0.14, 0.2, 0.2, 0.14, 0.14, 0.14, 
						0.2, 0.14, 0.2, 0.2, 0.2, 0.14, 0.2, 0.14, 0.14, 0.14, 0.2, 
						0.14, 0.1, 0.14, 0.1, 0.14, 0.2, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 
						0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 
						0.1, 0.1, 0.14, 0.14, 0, 0.1, 0.14, 0.4, 0.4, 0.14, 0.2, 0.14, 
						0.1, 0.1, 0, 0, 0, 0, 0])

q_tot_0_hr_values = np.array([50, 300, 300, 100, 300, 300, 100, 100, 100, 300, 
                              115, 250, 280, 300, 100, 300, 200, 100, 100, 300, 
                              80, 100, 100, 100, 100, 300, 300, 80, 100, 200, 100, 100, 
                              100, 100, 60, 300, 300, 300, 300, 80, 60, 80, 80, 60, 
                              80, 60, 80, 80, 0, 60, 80, 180, 290, 360, 540, 500, 60, 
                              60, 0, 0, 0, 0, 0, 0])

q_h_0_hr_values = np.array([50, 300, 300, 60, 200, 200, 60, 60, 60, 200, 80, 180, 
                          190, 200, 60, 200, 120, 60, 60, 200, 60, 60, 60, 60, 
                          60, 200, 200, 60, 60, 200, 60, 60, 60, 60, 40, 200, 200, 
                          200, 200, 60, 40, 50, 50, 40, 50, 40, 50, 50, 0, 40, 
                          50, 120, 190, 240, 360, 270, 40, 40, 0, 0, 0, 0, 0, 0])

q_c_0_hr_values = np.array([50, 300, 300, 60, 200, 200, 60, 60, 60, 200, 80, 180, 
                          190, 200, 60, 200, 120, 60, 60, 200, 60, 60, 60, 60, 
                          60, 200, 200, 60, 60, 200, 60, 60, 60, 60, 40, 200, 200, 
                          200, 200, 60, 40, 50, 50, 40, 50, 40, 50, 50, 0, 40, 
                          50, 120, 190, 240, 360, 270, 40, 40, 0, 0, 0, 0, 0, 0])

t_num_values = np.array(["1", "1", "1", "1", "1", "1", "2", "2", "2", "3", "3", "3", 
            			"3", "3", "4", "4", "4", "5", "5", "5", "6", "7", "7", "7", "7", "8", "8", 
            			"9", "10", "11", "12", "12", "13", "13", "14", "14", "15", "15", "16", "16", 
            			"17", "18", "19", "20", "20", "21", "21", "21", "22", "22", "22", "23", "23", 
            			"23", "23", "24", "25", "25", "26", "26", "26", "26", "26", "27"])  #номер группы потребителя по СП 30, таблица А2 приложения А 

t_string_values = np.array(["1 Жилые дома квартирного типа с водопроводом и канализацией без ванн", 
            				"2 Жилые дома квартирного типа с водопроводом канализацией и ваннами с водонагревателями работающими на твердом топливе", 
           					"3 Жилые дома квартирного типа с водопроводом канализацией и ваннами с газовыми водонагревателями", 
            				"4 Жилые дома квартирного типа с централизованным горячим водоснабжением оборудованные умывальниками мойками и душами", 
            				"5 Жилые дома квартирного типа с сидячими ваннами оборудованными душами", 
            				"6 Жилые дома квартирного типа с ваннами длиной от 1500 мм оборудованными душами", 
            				"7 Общежития с общими душевыми", 
                            "8 Общежития с душами при всех жилых комнатах", 
            				"9 Общежития с общими кухнями и блоками душевых на этажах при жилых комнатах в каждой секции здания", 
            				"10 Гостиницы пансионаты и мотели с общими ваннами и душами", 
            				"11 Гостиницы пансионаты и мотели с душами во всех отдельных номерах", 
            				"12 Гостиницы пансионаты и мотели с ваннами в отдельных номерах процент общего числа номеров до 25", 
            				"13 Гостиницы пансионаты и мотели с ваннами в отдельных номерах процент общего числа номеров до 75", 
            				"14 Гостиницы пансионаты и мотели с ваннами в отдельных номерах процент общего числа номеров до 100", 
            				"15 Больницы с общими ваннами и душевыми", 
                            "16 Больницы с санузлами приближенными к палатам", 
                            "17 Больницы инфекционные", 
            				"18 Санатории и дома отдыха с общими душами", 
                            "19 Санатории и дома отдыха с душами при всех жилых комнатах", 
            				"20 Санатории и дома отдыха с ваннами при всех жилых комнатах", 
                            "21 Поликлиники и амбулатории", 
            				"22 Дошкольные образовательные организации с дневным пребыванием детей со столовыми работающими на полуфабрикатах", 
            				"23 Дошкольные образовательные организации с дневным пребыванием детей со столовыми работающими на сырье и прачечными оборудованными автоматическими стиральными", 
            				"24 Дошкольные образовательные организации с круглосуточным пребыванием детей со столовыми работающими на полуфабрикатах", 
            				"25 Дошкольные образовательные организации с круглосуточным пребыванием детей со столовыми работающими на сырье и прачечными оборудованными автоматическими стиральными",  
            				"26 Прачечные механизированные", 
                            "27 Прачечные немеханизированные", 
                            "28 Административные здания", 
            				"29 Образовательные организации профессионального и высшего образования с душевыми при гимнастических залах и буфетами реализующими готовую продукцию", 
            				"30 Лаборатории общеобразовательных организаций и организаций профессиональных и высшего образования", 
            				"31 Общеобразовательные организации с душевыми при гимнастических залах и столовыми работающими на полуфабрикатах", 
            				"32 Общеобразовательные организации с продленным днем", 
                            "33 Общеобразовательные организации интернаты с помещениями учебными с душевыми при гимнастических залах", 
            				"34 Общеобразовательные организации интернаты с помещениями спальными", 
                            "35 Аптеки торговый зал и подсобные помещения", 
            				"36 Аптеки лаборатория приготовления лекарств", 
                            "37 Предприятия общественного питания для приготовления пищи реализуемой в обеденном зале", 
            				"38 Предприятия общественного питания для приготовления пищи продаваемой на дом", 
                            "39 Магазины продовольственные", 
            				"40 Магазины промтоварные", 
                            "41 Парикмахерские", 
                            "42 Кинотеатры", 
                            "43 Клубы", 
                            "44 Театры для зрителей", 
                            "45 Театры для артистов", 
            				"46 Стадионы и спортзалы для зрителей", 
                            "47 Стадионы и спортзалы для физкультурников с учетом приема душа", 
           					"48 Стадионы и спортзалы для спортсменов с учетом приема душа", 
                            "49 Плавательные бассейны пополнение бассейна", 
            				"50 Плавательные бассейны для зрителей", 
                            "51 Плавательные бассейны для спортсменов с учетом приема душа", 
            				"52 Бани для мытья в мыльной с тазами на скамьях и ополаскиванием в душе", 
                            "53 Бани с приемом оздоровительных процедур и ополаскиванием в душе", 
            				"54 Бани душевая кабина", 
                            "55 Бани ванная кабина", 
                            "56 Душевые в бытовых помещениях промышленных предприятий", 
            				"57 Цеха с тепловыделениями свыше 84 кДж на 1 м куб в час", 
                            "58 Цеха остальные цеха", 
            				"59 Расход воды на поливку травяного покрова", 
                            "60 Расход воды на поливку футбольного поля", 
            				"61 Расход воды на поливку остальных спортивных сооружений", 
                            "62 Расход воды на поливку совершенствованных покрытий тротуаров площадей заводских проездов", 
            				"63 Расход воды на поливку зеленых насаждений газонов и цветников", 
                            "64 Заливка поверхности катка"])

diam_values = np.array([20, 25, 32, 40, 50, 63, 75, 90, 110])  #диаметры ппрс SDR6 по каталогу Heisskraft

q_values = np.array([0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1, 2, 3, 
                    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
                    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
                    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])

v_20_values = np.array([1.02, 1.12, 1.22, 1.32, 1.42, 1.52, 1.62, 1.73, 1.83, 1.93, 2.03, 
                        4.06, 6.09, 8.12, 10.16, 12.19, 14.22, 16.25, 18.28, 20.31, 22.34, 
                        24.37, 26.4, 28.43, 30.47, 32.5, 34.53, 36.56, 38.59, 40.62, 42.65, 
                        44.68, 46.71, 48.75, 50.78, 52.81, 54.84, 56.87, 58.9, 60.93, 62.96, 
                        64.99, 67.02, 69.06, 71.09, 73.12, 75.15, 77.18, 79.21, 81.24, 83.27, 
                        85.3, 87.33, 89.37, 91.4, 93.43, 95.46, 97.49, 99.52, 101.55])

v_25_values = np.array([0.64, 0.71, 0.77, 0.83, 0.9, 0.96, 1.03, 1.09, 1.16, 1.22, 1.28, 
                        2.57, 3.85, 5.14, 6.42, 7.71, 8.99, 10.27, 11.56, 12.84, 14.13, 
                        15.41, 16.7, 17.98, 19.26, 20.55, 21.83, 23.12, 24.4, 25.69, 26.97, 
                        28.25, 29.54, 30.82, 32.11, 33.39, 34.67, 35.96, 37.24, 38.53, 39.81, 
                        41.1, 42.38, 43.66, 44.95, 46.23, 47.52, 48.8, 50.09, 51.37, 52.65, 
                        53.94, 55.22, 56.51, 57.79, 59.08, 60.36, 61.64, 62.93, 64.21])

v_32_values = np.array([0.39, 0.43, 0.47, 0.51, 0.55, 0.59, 0.63, 0.67, 0.71, 0.75, 0.79, 
                        1.57, 2.36, 3.15, 3.94, 4.72, 5.51, 6.3, 7.09, 7.87, 8.66, 9.45, 
                        10.24, 11.02, 11.81, 12.6, 13.39, 14.17, 14.96, 15.75, 16.54, 17.32, 
                        18.11, 18.9, 19.68, 20.47, 21.26, 22.05, 22.83, 23.62, 24.41, 25.2, 
                        25.98, 26.77, 27.56, 28.35, 29.13, 29.92, 30.71, 31.5, 32.28, 33.07, 
                        33.86, 34.65, 35.43, 36.22, 37.01, 37.8, 38.58, 39.37])

v_40_values = np.array([0.25, 0.28, 0.3, 0.33, 0.35, 0.38, 0.4, 0.43, 0.45, 0.48, 0.5, 1, 1.5, 
                        2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 
                        10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.51, 17.01, 
                        17.51, 18.01, 18.51, 19.01, 19.51, 20.01, 20.51, 21.01, 21.51, 22.01, 
                        22.51, 23.01, 23.51, 24.01, 24.51, 25.01])

v_50_values = np.array([0.16, 0.17, 0.19, 0.21, 0.22, 0.24, 0.25, 0.27, 0.29, 0.3, 0.32, 0.63, 
                        0.95, 1.27, 1.59, 1.9, 2.22, 2.54, 2.86, 3.17, 3.49, 3.81, 4.12, 4.44, 
                        4.76, 5.08, 5.39, 5.71, 6.03, 6.35, 6.66, 6.98, 7.3, 7.61, 7.93, 8.25, 
                        8.57, 8.88, 9.2, 9.52, 9.83, 10.15, 10.47, 10.79, 11.1, 11.42, 11.74, 
                        12.06, 12.37, 12.69, 13.01, 13.32, 13.64, 13.96, 14.28, 14.59, 14.91, 
                        15.23, 15.54, 15.86])

v_63_values = np.array([0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.4, 
                        0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.81, 2.01, 2.21, 2.41, 2.61, 2.81, 3.01, 
                        3.21, 3.41, 3.61, 3.81, 4.01, 4.21, 4.41, 4.61, 4.81, 5.02, 5.22, 5.42, 
                        5.62, 5.82, 6.02, 6.22, 6.42, 6.62, 6.82, 7.02, 7.22, 7.42, 7.62, 7.82, 
                        8.02, 8.23, 8.43, 8.63, 8.83, 9.03, 9.23, 9.43, 9.63, 9.83, 10.03])

v_75_values = np.array([0.07, 0.08, 0.08, 0.09, 0.1, 0.11, 0.11, 0.12, 0.13, 0.13, 0.14, 0.28, 
                        0.42, 0.57, 0.71, 0.85, 0.99, 1.13, 1.27, 1.42, 1.56, 1.7, 1.84, 1.98, 
                        2.12, 2.26, 2.41, 2.55, 2.69, 2.83, 2.97, 3.11, 3.26, 3.4, 3.54, 3.68, 
                        3.82, 3.96, 4.11, 4.25, 4.39, 4.53, 4.67, 4.81, 4.95, 5.1, 5.24, 5.38, 
                        5.52, 5.66, 5.8, 5.95, 6.09, 6.23, 6.37, 6.51, 6.65, 6.79, 6.94, 7.08])

v_90_values = np.array([0.05, 0.05, 0.06, 0.06, 0.07, 0.07, 0.08, 0.08, 0.09, 0.09, 0.1, 0.2, 
                        0.29, 0.39, 0.49, 0.59, 0.69, 0.79, 0.88, 0.98, 1.08, 1.18, 1.28, 1.38, 
                        1.47, 1.57, 1.67, 1.77, 1.87, 1.97, 2.06, 2.16, 2.26, 2.36, 2.46, 2.56, 
                        2.65, 2.75, 2.85, 2.95, 3.05, 3.15, 3.24, 3.34, 3.44, 3.54, 3.64, 3.74, 
                        3.83, 3.93, 4.03, 4.13, 4.23, 4.33, 4.42, 4.52, 4.62, 4.72, 4.82, 4.92])

v_110_values = np.array([0.03, 0.04, 0.04, 0.04, 0.05, 0.05, 0.05, 0.06, 0.06, 0.06, 0.07, 0.13, 
                        0.2, 0.26, 0.33, 0.39, 0.46, 0.53, 0.59, 0.66, 0.72, 0.79, 0.85, 0.92, 
                        0.99, 1.05, 1.12, 1.18, 1.25, 1.31, 1.38, 1.45, 1.51, 1.58, 1.64, 1.71, 
                        1.77, 1.84, 1.9, 1.97, 2.04, 2.1, 2.17, 2.23, 2.3, 2.36, 2.43, 2.5, 2.56, 
                        2.63, 2.69, 2.76, 2.82, 2.89, 2.96, 3.02, 3.09, 3.15, 3.22, 3.28])

x_values = np.array([0.015, 0.016, 0.017, 0.018, 0.019, 0.02, 0.021, 0.022, 0.023, 0.024, 0.025, 
                     0.026, 0.027, 0.028, 0.029, 0.03, 0.031, 0.032, 0.033, 0.034, 0.035, 0.036, 
                     0.037, 0.038, 0.039, 0.04, 0.041, 0.042, 0.043, 0.044, 0.045, 0.046, 0.047, 
                     0.048, 0.049, 0.05, 0.052, 0.054, 0.056, 0.058, 0.06, 0.062, 0.064, 0.065, 
                     0.068, 0.07, 0.072, 0.074, 0.076, 0.078, 0.08, 0.082, 0.084, 0.086, 0.088, 
                     0.09, 0.092, 0.094, 0.096, 0.098, 0.1, 0.105, 0.11, 0.115, 0.12, 0.125, 0.13, 
                     0.135, 0.14, 0.145, 0.15, 0.155, 0.16, 0.165, 0.17, 0.175, 0.18, 0.185, 0.19, 
                     0.195, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 
                     0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 
                     0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.52, 0.54, 0.56, 0.58, 0.6, 0.62, 0.64, 
                     0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 
                     0.92, 0.94, 0.96, 0.98, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 
                     1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.1, 2.2, 2.3, 2.4, 
                     2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.1, 
                     4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 
                     5.9, 6, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7, 7.1, 7.2, 7.3, 7.4, 7.5, 
                     7.6, 7.7, 7.8, 7.9, 8, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9, 9.1, 9.2, 
                     9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10, 10.2, 10.4, 10.6, 10.8, 11, 11.2, 11.4, 
                     11.6, 11.8, 12, 12.2, 12.4, 12.6, 12.8, 13, 13.2, 13.4, 13.6, 13.8, 14, 14.2, 
                     14.4, 14.6, 14.8, 15, 15.2, 15.4, 15.6, 15.8, 16, 16.2, 16.4, 16.6, 16.8, 17, 
                     17.2, 17.4, 17.6, 17.8, 18, 18.2, 18.4, 18.6, 18.8, 19, 19.2, 19.4, 19.6, 19.8, 
                     20, 21, 21.5, 22, 22.5, 23, 23.5, 24, 24.5, 25, 25.5, 26, 26.5, 27, 27.5, 28, 
                     28.5, 29, 29.5, 30, 30.5, 31, 31.5, 32, 32.5, 33, 33.5, 34, 34.5, 35, 35.5, 36, 
                     36.5, 37.5, 38, 38.5, 39, 39.5, 40, 40.5, 41, 41.5, 42, 42.5, 43, 43.5, 44, 44.5, 
                     45, 45.5, 46, 46.5, 47, 47.5, 48, 48.5, 49, 49.5, 50, 51, 52, 53, 54, 55, 56, 57, 
                     58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 
                     79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 
                     102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 
                     134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 158, 160, 162, 164, 166, 
                     168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 
                     200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 
                     280, 285, 290, 295, 300, 305, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 
                     365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 
                     445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 505, 510, 515, 520, 
                     525, 535, 540, 545, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600, 605, 
                     610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670, 675, 685, 690, 
                     695, 700, 705, 710, 715, 720, 725, 730, 735, 740, 745, 755, 760, 765, 770, 775, 
                     780, 785, 790, 795, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 
                     920, 930, 940, 950, 960, 970, 980, 990, 1000, 1250, 1600, 2000])

y_values = np.array([0.202, 0.205, 0.207, 0.21, 0.212, 0.215, 0.217, 0.219, 0.222, 0.224,  
					 0.226, 0.228, 0.23, 0.233, 0.235, 0.237, 0.239, 0.241, 0.243, 0.245,  
					 0.247, 0.249, 0.25, 0.252, 0.254, 0.256, 0.258, 0.259, 0.261, 0.263,  
					 0.265, 0.266, 0.268, 0.27, 0.271, 0.273, 0.276, 0.28, 0.283, 0.286,  
					 0.289, 0.292, 0.295, 0.298, 0.301, 0.304, 0.307, 0.309, 0.312, 0.315,  
					 0.318, 0.32, 0.323, 0.326, 0.328, 0.331, 0.333, 0.336, 0.338, 0.341,  
					 0.343, 0.349, 0.355, 0.361, 0.367, 0.373, 0.378, 0.384, 0.389, 0.394,  
					 0.399, 0.405, 0.41, 0.415, 0.42, 0.425, 0.43, 0.435, 0.439, 0.444,  
					 0.449, 0.458, 0.467, 0.476, 0.485, 0.493, 0.502, 0.51, 0.518, 0.526,  
					 0.534, 0.542, 0.55, 0.558, 0.565, 0.573, 0.58, 0.588, 0.595, 0.602,  
					 0.61, 0.617, 0.624, 0.631, 0.638, 0.645, 0.652, 0.658, 0.665, 0.672,  
					 0.678, 0.692, 0.704, 0.717, 0.73, 0.742, 0.755, 0.767, 0.779, 0.791,  
					 0.803, 0.815, 0.826, 0.838, 0.849, 0.86, 0.872, 0.883, 0.894, 0.905,  
					 0.916, 0.927, 0.937, 0.948, 0.959, 0.969, 0.995, 1.021, 1.046, 1.071,  
					 1.096, 1.12, 1.144, 1.168, 1.191, 1.215, 1.238, 1.261, 1.283, 1.306,  
					 1.328, 1.35, 1.372, 1.394, 1.416, 1.437, 1.479, 1.521, 1.563, 1.604,  
					 1.644, 1.684, 1.724, 1.763, 1.802, 1.84, 1.879, 1.917, 1.954, 1.991,  
					 2.029, 2.065, 2.102, 2.138, 2.174, 2.21, 2.246, 2.281, 2.317, 2.352,  
					 2.386, 2.421, 2.456, 2.49, 2.524, 2.558, 2.592, 2.626, 2.66, 2.693,  
					 2.726, 2.76, 2.793, 2.826, 2.858, 2.891, 2.924, 2.956, 2.989, 3.021,  
					 3.053, 3.085, 3.117, 3.149, 3.181, 3.212, 3.244, 3.275, 3.307, 3.338,  
					 3.369, 3.4, 3.431, 3.462, 3.493, 3.524, 3.555, 3.585, 3.616, 3.646,  
					 3.677, 3.707, 3.738, 3.768, 3.798, 3.828, 3.858, 3.888, 3.918, 3.948,  
					 3.978, 4.008, 4.037, 4.067, 4.097, 4.126, 4.185, 4.244, 4.302, 4.361,  
					 4.419, 4.477, 4.534, 4.592, 4.649, 4.707, 4.764, 4.82, 4.877, 4.934,  
					 4.99, 5.047, 5.103, 5.159, 5.215, 5.27, 5.326, 5.382, 5.437, 5.492,  
					 5.547, 5.602, 5.657, 5.712, 5.767, 5.821, 5.876, 5.93, 5.984, 6.039,  
					 6.093, 6.147, 6.201, 6.254, 6.308, 6.362, 6.415, 6.469, 6.522, 6.575,  
					 6.629, 6.682, 6.734, 6.788, 6.84, 6.893, 7.156, 7.287, 7.417, 7.547,  
					 7.677, 7.806, 7.935, 8.064, 8.192, 8.32, 8.447, 8.575, 8.701, 8.828,  
					 8.955, 9.081, 9.207, 9.332, 9.457, 9.583, 9.707, 9.832, 9.957, 10.08,  
					 10.2, 10.33, 10.45, 10.58, 10.7, 10.82, 10.94, 11.07, 11.31, 11.43,  
					 11.56, 11.68, 11.8, 11.92, 12.04, 12.16, 12.28, 12.41, 12.53, 12.65,  
					 12.77, 12.89, 13.01, 13.13, 13.25, 13.37, 13.49, 13.61, 13.73, 13.85,  
					 13.97, 14.09, 14.2, 14.32, 14.56, 14.8, 15.04, 15.27, 15.51, 15.74,  
					 15.98, 16.22, 16.45, 16.69, 16.92, 17.15, 17.39, 17.62, 17.85, 18.09,  
					 18.32, 18.55, 18.79, 19.02, 19.25, 19.48, 19.71, 19.94, 20.18, 20.41,  
					 20.64, 20.87, 21.1, 21.33, 21.56, 21.69, 22.02, 22.48, 22.71, 22.94,  
					 23.17, 23.39, 23.62, 23.85, 24.08, 24.31, 24.54, 24.77, 24.99, 25.22,  
					 25.45, 25.68, 25.91, 26.36, 26.82, 27.27, 27.72, 28.18, 28.63, 29.09,  
					 29.54, 29.89, 30.44, 30.9, 31.35, 31.8, 32.25, 32.7, 33.15, 33.6,  
					 34.06, 34.51, 34.96, 35.41, 35.86, 36.31, 36.76, 37.21, 37.66, 38.11,  
					 39.01, 39.46, 39.91, 40.35, 40.8, 41.25, 41.7, 42.15, 42.6, 43.05,  
					 43.5, 43.95, 44.4, 44.84, 45.29, 45.74, 46.19, 46.64, 47.09, 47.54,  
					 47.99, 48.43, 49.49, 50.59, 51.7, 52.8, 53.9, 55, 56.1, 57.19,  
					 58.29, 59.38, 60.48, 61.57, 62.66, 63.75, 64.85, 65.94, 67.03, 68.12,  
					 69.2, 70.29, 71.38, 73.55, 74.63, 75.72, 76.8, 77.88, 78.96, 80.04,  
					 81.12, 82.2, 83.28, 84.36, 85.44, 86.52, 87.6, 88.67, 89.75, 90.82,  
					 91.9, 92.97, 94.05, 95.12, 96.2, 97.27, 98.34, 99.41, 100.49, 101.56,  
					 102.63, 103.7, 104.77, 105.84, 106.91, 107.98, 109.05, 110.11, 111.18, 112.25,  
					 113.32, 114.38, 115.45, 116.52, 117.58, 118.65, 120.78, 121.84, 122.91, 123.97,  
					 125.04, 126.1, 127.16, 128.22, 129.29, 130.35, 131.41, 132.47, 133.54, 134.6,  
					 135.66, 136.72, 137.78, 138.84, 139.9, 140.96, 142.02, 143.08, 144.14, 145.2,  
					 146.25, 147.31, 148.37, 149.43, 150.49, 152.6, 153.66, 154.72, 155.77, 156.83,  
					 157.89, 158.94, 160, 161.06, 162.11, 163.17, 164.22, 165.28, 167.39, 168.44,  
					 169.5, 170.55, 171.6, 172.66, 173.71, 174.76, 175.82, 176.87, 178.98, 181.08,  
					 183.19, 185.29, 187.39, 189.49, 191.6, 193.7, 195.7, 197.9, 200, 202.1,  
					 204.2, 206.3, 208.39, 210.49, 212.59, 214.68, 216.78, 218.87, 271.14, 343.9,  
					 426.8])

v_dict = {
    20: v_20_values,
    25: v_25_values,
    32: v_32_values,
    40: v_40_values,
    50: v_50_values,
    63: v_63_values,
    75: v_75_values,
    90: v_90_values,
    110: v_110_values
}

__all__ = ['t_values', 
           'q_tot_hru_values', 'q_h_hru_values', 'q_c_hru_values', 
           'q_tot_values', 'q_h_values', 'q_c_values', 
		   'q_tot_0_values', 'q_h_0_values', 'q_c_0_values',
           'q_tot_0_hr_values', 'q_h_0_hr_values', 'q_c_0_hr_values',
           't_num_values', 't_string_values',
           'diam_values', 'q_values', 'v_16_values', 'v_20_values', 
           'v_25_values', 'v_32_values', 'v_40_values', 'v_50_values', 'v_63_values', 
           'v_75_values', 'v_90_values', 'v_110_values', 'x_values', 'y_values', 'q_dict', 'v_dict']