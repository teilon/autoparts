from django.shortcuts import render
import re

def index(request):

	models = [	'Audi', 'Abarth', 'Alfa Romero',
				'BMW', 
				'Chevrolet', 'Citroen', 'Chrysler',
				'Daewoo', 'Dodge', 'Dacia',
				'Fiat', 'Ford',
				'Honda', 'Hyundai',
				'Isuzu', 'Infiniti',
				'Jeep', 'Jaguar',
				'Kia',
				'Lexus', 'Land Rover', 'Lancia',
				'Mitsubishi', 'Mazda', 'Man', 'Mercedes', 'Mini',
				'Nissan',
				'Opel',
				'Peugeot', 'Porsche', 'Plymouth',
				'Renault', 'Rolls-Royce', 'Ram',
				'Subaru', 'Suzuki', 'SAAB', 'Scania', 'Skoda', 'Ssang Yong', 'Seat', 'Smart',
				'Toyota',
				'Volkswagen', 'Volvo', 'Vauxhall'
			]

	output = []
	for m in models:
		model_name = m.replace(' ', '_').lower()
		# static_file = "{} static 'app_auto/images/auto_logos/logo_{}.png' {}".format('{%', model_name, '%}')
		# static_file = 'app_auto/images/auto_logos/logo_{}.png'.format(model_name)


		output.append('logo_' + model_name + '50x50.png')
		# output.append(static_file)


	return render(request, 'app_auto/index.html', {'models' : output,})