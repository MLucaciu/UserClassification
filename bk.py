# X = [[80., 70., 10., 80.], [10., 50., 80., 50.], [90., 60., 70., 90.], [0., 100., 0., 100.]]
# prediction = clf.predict([[0., 0., 0., 100., 0., 0., 0., 0.]])
# prediction2 = clf.predict_proba([[10., 10., 10., 100., 30., 20., 10., 30.]])
# c = prediction2.tolist()
# jj = pd.DataFrame(clf.predict_proba([[0., 0., 0., 100., 0., 0., 0., 0.]]), columns=clf.classes_)
# final_response = jj.to_json()
# Stereotypes
# y2 = ['siria', 'europa', 'africa', 'europa']
y = ['CityBreak',
     'CityBreak',
     'CityBreak',
     'EconomicCityBreak',
     'EconomicCityBreak',
     'EconomicCityBreak',
     'EconomicCityBreak',
     'EconomicCityBreak',
     'EconomicCityBreak',
     'Vacantion',
     'Vacantion',
     'Vacantion',
     'Vacantion',
     'Vacantion',
     'Vacantion',
     'SunnyVacantion',
     'CityBreak',
     'CityBreak',
     'CityBreak',
     'ExpensiveCityBreak',
     'ExpensiveCityBreak',
     'ExpensiveCityBreak']
