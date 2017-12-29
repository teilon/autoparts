from django.shortcuts import render

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
				'Peugeot', 'Porsche', 'Plymuth',
				'Renault', 'Rolls-Royce', 'Ram',
				'Subaru', 'Suzuki', 'SAAB', 'Scania', 'Skoda', 'Ssang Yong', 'Seat', 'Smart'
				'Toyota',
				'Volkswagen', 'Volvo', 'Vauxhall'
			]

	return render(request, 'app_auto/index.html', {'models' : models,})