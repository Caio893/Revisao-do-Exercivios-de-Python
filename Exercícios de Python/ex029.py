speed = float(input('Enter with speed car: '))
if speed >= 81:
    multa = (speed-80)*7
    print(f'You are over speed limit of 80km/h'
          f'\nYou may pay a multa of $7 for each 7km/h above of limit, and total is ${multa}')
print('Thank you!')
